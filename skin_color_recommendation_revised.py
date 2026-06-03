# -*- coding: utf-8 -*-
"""
skin_color_recommendation_revised.ipynb

Versi Revisi — sesuai catatan Seminar Proposal

Perubahan dari versi sebelumnya:
  1. Ditambahkan deteksi wajah menggunakan Haar Cascade (OpenCV)
  2. Klasifikasi skintone diubah dari HSV brightness ke ITA (Individual
     Typology Angle) dari CIELAB
  3. Fungsi CIEDE2000 diubah: dari evaluasi diversitas palet menjadi
     validasi centroid vs referensi warna kulit standar
  4. Dataset Kaggle diintegrasikan sebagai sumber data utama
     (dengan fallback sintetis jika folder kosong)

Kompatibel: Google Colab
"""

# ============================================================
# 1. INSTALL & IMPORT LIBRARY
# ============================================================

# !pip install colormath scikit-image -q   # uncomment di Colab

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

from sklearn.cluster import KMeans
from sklearn.metrics import (silhouette_score, davies_bouldin_score,
                              calinski_harabasz_score)

from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

import pandas as pd

# Patch numpy untuk kompatibilitas colormath
if not hasattr(np, 'asscalar'):
    np.asscalar = lambda x: x.item()

print("Semua library berhasil diimport!")
print(f"   OpenCV  : {cv2.__version__}")
print(f"   NumPy   : {np.__version__}")
print(f"   sklearn : {__import__('sklearn').__version__}")


# ============================================================
# KONFIGURASI GLOBAL
# ============================================================

# Ganti dengan path folder dataset Kaggle kamu.
# Cara: Mount Google Drive -> arahkan DATASET_PATH ke folder dataset.
# Contoh: DATASET_PATH = "/content/drive/MyDrive/dataset_wajah"
DATASET_PATH  = "/content/dataset"

TARGET_SIZE   = (256, 256)
SUPPORTED_EXT = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

# Nilai K yang dievaluasi.
# K tetap dipilih setelah Elbow Method pada sampel representatif.
# K_RANGE adalah rentang pengujian Elbow; K_VALUES adalah kandidat final.
K_RANGE  = range(2, 10)
K_VALUES = [3, 5, 7]

# Path Haar Cascade bawaan OpenCV
HAAR_CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"


# ============================================================
# 2. LOAD DATASET
#
# Dataset yang digunakan:
#   Sumber    : Dataset wajah dari Kaggle (misal: UTKFace, FairFace,
#               atau dataset wajah multi-etnis lainnya)
#   Jumlah    : minimal 120 citra wajah
#   Variasi   : mencakup skintone dari very light hingga dark
#   Tipe      : indoor dan outdoor
#   Format    : JPG / PNG
#
# Cara menggunakan dataset Kaggle di Colab:
#   1. Upload dataset ke Google Drive
#   2. from google.colab import drive; drive.mount('/content/drive')
#   3. Ubah DATASET_PATH ke path folder dataset
#
# Jika folder kosong atau tidak ditemukan, notebook otomatis membuat
# gambar sintetis sebagai fallback agar pipeline tetap bisa diuji.
# ============================================================

def load_dataset(folder_path, target_size=(256, 256)):
    """
    Load semua gambar dari folder dataset dan resize ke ukuran seragam.

    Args:
        folder_path : path ke folder citra wajah
        target_size : (width, height) ukuran target resize
    Returns:
        images : list of (filename, img_bgr numpy array)
    """
    images = []
    if not os.path.exists(folder_path):
        print(f"Folder tidak ditemukan: {folder_path}")
        return images

    for fname in sorted(os.listdir(folder_path)):
        if fname.lower().endswith(SUPPORTED_EXT):
            fpath = os.path.join(folder_path, fname)
            img   = cv2.imread(fpath)
            if img is None:
                print(f"  Gagal baca: {fname}")
                continue
            img_resized = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)
            images.append((fname, img_resized))

    print(f"Berhasil load {len(images)} gambar dari '{folder_path}'")
    return images


def generate_synthetic_fallback(n=12):
    """
    Buat gambar wajah sintetis sebagai fallback jika dataset tidak tersedia.
    HANYA untuk tujuan demo teknis -- bukan untuk eksperimen utama.
    """
    skin_tones = [
        ((255, 224, 189), "fair_1.png"),
        ((241, 194, 125), "light_2.png"),
        ((224, 172, 105), "medium_3.png"),
        ((198, 134,  66), "tan_4.png"),
        ((141,  85,  36), "brown_5.png"),
        ((80,   40,  20), "dark_6.png"),
        ((255, 205, 170), "fair_var_7.png"),
        ((210, 150,  90), "medium_var_8.png"),
        ((230, 190, 140), "light_warm_9.png"),
        ((170, 110,  60), "olive_10.png"),
        ((110,  65,  30), "brown_deep_11.png"),
        ((60,   35,  15), "dark_deep_12.png"),
    ]
    os.makedirs(DATASET_PATH, exist_ok=True)
    result = []
    for rgb, fname in skin_tones[:n]:
        img = np.ones((256, 256, 3), dtype=np.uint8) * 200
        cv2.ellipse(img, (128, 128), (80, 100), 0, 0, 360, rgb[::-1], -1)
        noise = np.random.randint(-10, 10, img.shape, dtype=np.int16)
        img   = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
        cv2.circle(img, (100, 108), 14, (30, 20, 15), -1)
        cv2.circle(img, (156, 108), 14, (30, 20, 15), -1)
        cv2.ellipse(img, (128, 163), (22, 10), 0, 0, 180,
                    tuple(max(0, c - 35) for c in rgb[::-1]), -1)
        path = os.path.join(DATASET_PATH, fname)
        cv2.imwrite(path, img)
        result.append((fname, img))
    print(f"PERINGATAN: Dataset tidak ditemukan. {n} gambar sintetis dibuat sebagai fallback.")
    print("  Untuk eksperimen nyata, arahkan DATASET_PATH ke dataset Kaggle.")
    return result


dataset = load_dataset(DATASET_PATH, target_size=TARGET_SIZE)

if len(dataset) == 0:
    dataset = generate_synthetic_fallback(n=12)

print(f"\nTotal gambar yang akan diproses : {len(dataset)}")
print(f"Resolusi standar                : {TARGET_SIZE[0]}x{TARGET_SIZE[1]} piksel")


# ============================================================
# 3. PREPROCESSING
#
# Tahapan:
#   a. Gaussian Blur      : reduksi noise piksel (kernel 5x5)
#   b. CLAHE pada L (LAB) : normalisasi pencahayaan/shadow
#      - clipLimit=2.0 mencegah over-amplification noise
#      - tileGridSize=(8,8) cocok untuk gambar 256x256
# ============================================================

def preprocess_image(img_bgr, apply_blur=True, normalize_lighting=True):
    """
    Preprocessing: Gaussian Blur + CLAHE illumination normalization.

    Normalisasi dilakukan pada channel L* di CIELAB agar variasi
    pencahayaan (indoor/outdoor, shadow) dapat dikurangi sebelum
    segmentasi dan clustering.

    Args:
        img_bgr           : gambar input (BGR numpy array)
        apply_blur        : aktifkan Gaussian Blur
        normalize_lighting: aktifkan CLAHE pada L*
    Returns:
        img               : gambar setelah preprocessing (BGR numpy array)
    """
    img = img_bgr.copy()

    if apply_blur:
        img = cv2.GaussianBlur(img, (5, 5), 0)

    if normalize_lighting:
        lab   = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        lab[:, :, 0] = clahe.apply(lab[:, :, 0])
        img   = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    return img


preprocessed_dataset = []
for fname, img in dataset:
    preprocessed_dataset.append((fname, preprocess_image(img)))

print(f"Preprocessing selesai untuk {len(preprocessed_dataset)} gambar")

# Visualisasi Before vs After Preprocessing
n_show = min(4, len(dataset))
fig, axes = plt.subplots(2, n_show, figsize=(16, 6))
fig.suptitle("Before vs After Preprocessing (CLAHE)", fontsize=13, fontweight='bold')
for i in range(n_show):
    fname, orig   = dataset[i]
    _, processed  = preprocessed_dataset[i]
    axes[0, i].imshow(cv2.cvtColor(orig,      cv2.COLOR_BGR2RGB))
    axes[0, i].set_title(f"Original\n{fname}", fontsize=8)
    axes[0, i].axis('off')
    axes[1, i].imshow(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
    axes[1, i].set_title("After CLAHE", fontsize=8)
    axes[1, i].axis('off')
plt.tight_layout(); plt.show()


# ============================================================
# 4. DETEKSI WAJAH — HAAR CASCADE (OpenCV)
#
# Alasan pemilihan Haar Cascade:
#   - Ringan secara komputasi, tidak memerlukan GPU
#   - Sudah tersedia di OpenCV tanpa instalasi tambahan
#   - Cukup untuk citra wajah frontal dengan ekspresi natural
#     sesuai batasan masalah penelitian
#
# Batasan yang disepakati (sesuai Bab 1):
#   - Sistem hanya memproses wajah tampak depan (frontal)
#   - Ekspresi natural (bukan ekspresi ekstrem)
#   - Gambar yang wajahnya tidak terdeteksi di-skip dari analisis
#
# Parameter:
#   scaleFactor=1.1  : pyramid scaling (standar)
#   minNeighbors=5   : mencegah false positive
#   minSize=(60,60)  : ukuran minimum bounding box wajah
#   padding=0.15     : perluas crop 15% ke setiap sisi agar
#                      pipi dan dahi ikut tercakup
# ============================================================

face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
if face_cascade.empty():
    raise IOError(f"Haar Cascade tidak ditemukan: {HAAR_CASCADE_PATH}")
print(f"Haar Cascade berhasil dimuat.")


def detect_and_crop_face(img_bgr, scale_factor=1.1, min_neighbors=5,
                          min_size=(60, 60), padding=0.15):
    """
    Deteksi wajah menggunakan Haar Cascade lalu crop area wajah.

    Jika lebih dari satu wajah terdeteksi, ambil yang terbesar.
    Crop diperluas sebesar `padding` ke setiap sisi untuk memastikan
    area pipi dan dahi masuk tanpa mengikutkan terlalu banyak background.

    Args:
        img_bgr      : gambar input (BGR numpy array)
        scale_factor : faktor skala pyramid
        min_neighbors: jumlah tetangga minimum
        min_size     : ukuran minimum bounding box (px)
        padding      : fraksi padding di luar bounding box
    Returns:
        face_crop : cropped face (BGR), atau None jika tidak terdeteksi
        bbox      : (x, y, w, h) bounding box, atau None
    """
    gray  = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=min_size
    )

    if len(faces) == 0:
        return None, None

    # Pilih wajah terbesar
    faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
    x, y, w, h = faces[0]

    H_img, W_img = img_bgr.shape[:2]
    pad_x = int(w * padding)
    pad_y = int(h * padding)
    x1 = max(0, x - pad_x);  y1 = max(0, y - pad_y)
    x2 = min(W_img, x + w + pad_x); y2 = min(H_img, y + h + pad_y)

    return img_bgr[y1:y2, x1:x2], (x, y, w, h)


def detect_faces_dataset(preprocessed_dataset):
    """
    Terapkan deteksi wajah ke seluruh dataset.
    Gambar yang wajahnya tidak terdeteksi di-skip dan dilaporkan.
    """
    face_dataset = []
    n_skipped    = 0

    for fname, img in preprocessed_dataset:
        face_crop, bbox = detect_and_crop_face(img)
        if face_crop is None:
            print(f"  Wajah tidak terdeteksi, di-skip: {fname}")
            n_skipped += 1
            continue
        face_resized = cv2.resize(face_crop, TARGET_SIZE, interpolation=cv2.INTER_AREA)
        face_dataset.append((fname, face_resized))

    print(f"\nDeteksi wajah selesai.")
    print(f"  Berhasil : {len(face_dataset)} gambar")
    print(f"  Di-skip  : {n_skipped} gambar (wajah tidak terdeteksi)")
    return face_dataset, n_skipped


face_dataset, n_skipped = detect_faces_dataset(preprocessed_dataset)

# Fallback: jika mayoritas gambar di-skip (kemungkinan dataset sintetis
# atau kondisi gambar tidak ideal), gunakan preprocessed_dataset langsung
if len(face_dataset) < max(3, len(preprocessed_dataset) // 2):
    print("\nTerlalu banyak gambar di-skip. Menggunakan seluruh dataset tanpa face detection.")
    print("(Kemungkinan dataset berisi gambar sintetis atau non-frontal)")
    face_dataset = preprocessed_dataset

print(f"\nDataset siap untuk segmentasi: {len(face_dataset)} gambar")


# ============================================================
# 5. SEGMENTASI KULIT — RULE-BASED VOTING 3 COLOR SPACE
#
# Metode: Voting majority (RGB + HSV + YCrCb)
#   Pixel dianggap kulit jika minimal 2 dari 3 metode setuju.
#
# Threshold yang digunakan:
#   RGB  : R>95, G>40, B>20, R>G, R>B, |R-G|>15, max-min>15
#          (Kolkur et al., 2016)
#   HSV  : H in [0,25] or [160,179], S in [25,173], V in [90,255]
#          (OpenCV scale; setara H in [0°,25°]|[320°,360°] standard)
#   YCrCb: Cr in [133,173], Cb in [77,127]
#          (Moumene et al., 2022)
#
# Post-processing morfologi:
#   MORPH_CLOSE (7x7 ellipse) : mengisi lubang kecil pada mask
#   MORPH_OPEN  (7x7 ellipse) : menghilangkan noise/speckle
#
# K-Means hanya dijalankan pada pixel kulit yang sudah diisolasi
# via masking ini -- bukan seluruh pixel gambar.
# Ini memastikan centroid merepresentasikan warna kulit,
# bukan warna background atau pakaian.
# ============================================================

def segment_skin_rgb(img_bgr):
    """Segmentasi kulit dengan threshold di color space RGB."""
    img = img_bgr.astype(np.float32)
    R, G, B = img[:,:,2], img[:,:,1], img[:,:,0]
    mask = (
        (R > 95) & (G > 40) & (B > 20) &
        (R > G)  & (R > B)  &
        (np.abs(R.astype(int) - G.astype(int)) > 15) &
        (np.max(img, axis=2) - np.min(img, axis=2) > 15)
    ).astype(np.uint8) * 255
    return mask


def segment_skin_hsv(img_bgr):
    """Segmentasi kulit dengan threshold di color space HSV."""
    img_hsv    = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    mask_lower = cv2.inRange(img_hsv, (0,   25,  90), (25,  173, 255))
    mask_upper = cv2.inRange(img_hsv, (160, 25,  90), (179, 173, 255))
    return cv2.bitwise_or(mask_lower, mask_upper)


def segment_skin_ycrcb(img_bgr):
    """Segmentasi kulit dengan threshold di color space YCrCb."""
    img_ycrcb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)
    return cv2.inRange(img_ycrcb, (0, 133, 77), (255, 173, 127))


def segment_skin_combined(img_bgr, use_morphology=True):
    """
    Gabungkan 3 metode segmentasi dengan voting majority.

    Args:
        img_bgr        : gambar input (BGR)
        use_morphology : terapkan post-processing morfologi
    Returns:
        mask_combined : binary mask (0/255)
        masks_dict    : dict mask per metode untuk analisis
    """
    mask_rgb   = segment_skin_rgb(img_bgr)
    mask_hsv   = segment_skin_hsv(img_bgr)
    mask_ycrcb = segment_skin_ycrcb(img_bgr)

    vote = (mask_rgb.astype(np.uint16)   // 255 +
            mask_hsv.astype(np.uint16)   // 255 +
            mask_ycrcb.astype(np.uint16) // 255)
    mask_combined = (vote >= 2).astype(np.uint8) * 255

    if use_morphology:
        kernel        = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask_combined = cv2.morphologyEx(mask_combined, cv2.MORPH_CLOSE, kernel)
        mask_combined = cv2.morphologyEx(mask_combined, cv2.MORPH_OPEN,  kernel)

    return mask_combined, {
        'RGB': mask_rgb, 'HSV': mask_hsv,
        'YCrCb': mask_ycrcb, 'Combined': mask_combined
    }


def visualize_segmentation(img_bgr, fname=""):
    """Tampilkan hasil segmentasi semua metode pada satu gambar."""
    mask_combined, masks = segment_skin_combined(img_bgr)
    img_rgb  = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    skin_only = img_rgb.copy()
    skin_only[mask_combined == 0] = [220, 220, 220]

    fig, axes = plt.subplots(1, 6, figsize=(20, 4))
    fig.suptitle(f"Hasil Segmentasi Kulit: {fname}", fontsize=12, fontweight='bold')
    titles = ["Original", "Mask RGB", "Mask HSV", "Mask YCrCb",
              f"Combined\n({(mask_combined>0).mean()*100:.1f}% kulit)", "Skin Region"]
    imgs   = [img_rgb, masks['RGB'], masks['HSV'], masks['YCrCb'],
              mask_combined, skin_only]
    for ax, im, title in zip(axes, imgs, titles):
        ax.imshow(im, cmap='gray' if im.ndim == 2 else None)
        ax.set_title(title, fontsize=8); ax.axis('off')
    plt.tight_layout(); plt.show()


for fname, img in face_dataset[:3]:
    visualize_segmentation(img, fname)


# ============================================================
# 6. EKSTRAKSI PIXEL KULIT
# ============================================================

def extract_skin_pixels(img_bgr, color_space='RGB', min_pixels=50):
    """
    Ekstrak pixel kulit dari citra dan konversi ke color space target.

    Args:
        img_bgr     : gambar input (BGR)
        color_space : 'RGB', 'HSV', atau 'LAB'
        min_pixels  : minimum pixel kulit yang diperlukan
    Returns:
        pixels : array (N, 3) pixel kulit, atau None
        mask   : binary mask hasil segmentasi
    """
    mask, _ = segment_skin_combined(img_bgr)

    if color_space == 'RGB':
        img_cs = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    elif color_space == 'HSV':
        img_cs = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    elif color_space == 'LAB':
        img_cs = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
    else:
        raise ValueError(f"Color space tidak dikenal: {color_space}")

    pixels = img_cs[mask > 0].reshape(-1, 3).astype(np.float32)
    return (None, mask) if len(pixels) < min_pixels else (pixels, mask)


def collect_all_skin_pixels(dataset, color_space='RGB'):
    """Kumpulkan semua pixel kulit dari seluruh dataset."""
    all_pixels = []
    n_success  = 0
    for fname, img in dataset:
        pixels, _ = extract_skin_pixels(img, color_space)
        if pixels is not None:
            all_pixels.append(pixels)
            n_success += 1
    print(f"  [{color_space}] Ekstraksi dari {n_success}/{len(dataset)} gambar")
    return np.vstack(all_pixels) if all_pixels else np.array([])


print("Mengekstrak pixel kulit untuk setiap color space...")
pixels_rgb = collect_all_skin_pixels(face_dataset, 'RGB')
pixels_hsv = collect_all_skin_pixels(face_dataset, 'HSV')
pixels_lab = collect_all_skin_pixels(face_dataset, 'LAB')

print(f"\nJumlah pixel kulit terkumpul:")
print(f"  RGB : {len(pixels_rgb):,} pixel")
print(f"  HSV : {len(pixels_hsv):,} pixel")
print(f"  LAB : {len(pixels_lab):,} pixel")


# ============================================================
# 7. ELBOW METHOD + K-MEANS CLUSTERING
#
# Penentuan nilai K (tetap):
#   1. Elbow Method (WCSS) dijalankan pada K=2..9 menggunakan
#      subsample pixel kulit dari dataset.
#   2. Knee point dideteksi via second derivative dari inertia.
#   3. Berdasarkan hasil Elbow dan pertimbangan representasi
#      skintone (light/medium/dark), K_VALUES = [3, 5, 7].
#   4. K final dipilih via composite score (Silhouette+DBI+CHI+Stability).
#
# K bersifat TETAP (bukan dinamis per gambar).
# Justifikasi:
#   - Konsistensi perbandingan antar color space
#   - Elbow Method sudah memvalidasi nilai K pada sampel representatif
#   - Efisiensi komputasi terjaga
# ============================================================

def run_kmeans(pixels, k, random_state=42):
    """Jalankan K-Means dengan inisialisasi k-means++."""
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10,
                    max_iter=300, random_state=random_state)
    labels = kmeans.fit_predict(pixels)
    return kmeans, labels, kmeans.cluster_centers_, kmeans.inertia_


def sample_pixels(pixels, n=5000, seed=42):
    """Subsample pixel untuk efisiensi komputasi."""
    if len(pixels) > n:
        rng = np.random.default_rng(seed)
        return pixels[rng.choice(len(pixels), n, replace=False)]
    return pixels


def elbow_method(pixels, k_range=range(2, 10), color_space='RGB', n_sample=3000):
    """
    Hitung WCSS untuk berbagai K dan deteksi knee point.
    Knee point = argmax dari second derivative inertia.

    Returns:
        best_k   : K rekomendasi Elbow
        inertias : list nilai WCSS per K
    """
    sample   = sample_pixels(pixels, n_sample)
    k_list   = list(k_range)
    inertias = []

    for k in k_list:
        _, _, _, inertia = run_kmeans(sample, k)
        inertias.append(inertia)

    deltas  = np.diff(inertias)
    deltas2 = np.diff(deltas)
    best_k  = k_list[np.argmax(deltas2) + 2] if len(deltas2) > 0 else k_list[1]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(f"Elbow Method — {color_space}", fontsize=13, fontweight='bold')
    axes[0].plot(k_list, inertias, 'bo-', linewidth=2, markersize=8)
    axes[0].axvline(x=best_k, color='red', linestyle='--',
                    label=f'Knee point K={best_k}')
    axes[0].set_xlabel('K'); axes[0].set_ylabel('Inertia (WCSS)')
    axes[0].set_title('Elbow Curve — semakin landai semakin baik')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)
    axes[1].plot(k_list[1:], -deltas, 'go-', linewidth=2, markersize=8)
    axes[1].set_xlabel('K'); axes[1].set_ylabel('Delta Inertia')
    axes[1].set_title('Rate of Improvement per K')
    axes[1].grid(True, alpha=0.3)
    plt.tight_layout(); plt.show()

    print(f"  Knee point K (auto-detect) = {best_k}")
    return best_k, inertias


print("Menjalankan Elbow Method pada color space RGB...")
best_k_rgb, inertias_rgb = elbow_method(pixels_rgb, k_range=K_RANGE, color_space='RGB')
print(f"  K rekomendasi Elbow (RGB) : {best_k_rgb}")
print(f"  K yang dievaluasi penuh   : {K_VALUES}")


def fit_kmeans_multiple_k(pixels, k_values, color_space='RGB'):
    """Latih K-Means untuk semua nilai K pada subsample pixels."""
    sample  = sample_pixels(pixels, 5000)
    results = {}
    for k in k_values:
        model, labels, centroids, inertia = run_kmeans(sample, k)
        results[k] = {'model': model, 'labels': labels,
                      'centroids': centroids, 'inertia': inertia, 'pixels': sample}
        print(f"  [{color_space}] K={k} | Inertia={inertia:.1f}")
    return results


print("\nTraining K-Means untuk semua K candidates...")
print("[RGB]") ; results_rgb = fit_kmeans_multiple_k(pixels_rgb, K_VALUES, 'RGB')
print("[HSV]") ; results_hsv = fit_kmeans_multiple_k(pixels_hsv, K_VALUES, 'HSV')
print("[LAB]") ; results_lab = fit_kmeans_multiple_k(pixels_lab, K_VALUES, 'LAB')
print("Training selesai!")


# ============================================================
# 8. EVALUASI CLUSTERING
#
# Tiga metrik internal:
#
#   Silhouette Score     : kohesi dan separasi cluster
#                          Range -1 s.d. 1. SEMAKIN TINGGI semakin baik.
#
#   Davies-Bouldin Index : rasio scatter intra vs jarak antar centroid
#                          Range >= 0. SEMAKIN RENDAH semakin baik.
#
#   Calinski-Harabasz    : rasio varians antar vs intra cluster
#   Index (CHI)          : Range > 0. SEMAKIN TINGGI semakin baik.
#
# PERINGATAN PENTING:
#   Ketiga metrik ini hanya mengukur kualitas STRUKTUR cluster.
#   Metrik ini TIDAK membuktikan bahwa centroid yang dihasilkan
#   merepresentasikan warna kulit dengan benar secara visual.
#   Oleh karena itu, validasi tambahan menggunakan CIEDE2000
#   diperlukan (lihat Bagian 10).
# ============================================================

def evaluate_clustering(pixels, labels):
    """Hitung Silhouette, DBI, dan CHI untuk satu konfigurasi."""
    if len(np.unique(labels)) < 2:
        return {'silhouette': 0, 'davies_bouldin': 999, 'calinski_harabasz': 0}
    idx = np.random.choice(len(pixels), min(3000, len(pixels)), replace=False)
    px, lb = pixels[idx], labels[idx]
    return {
        'silhouette'       : round(silhouette_score(px, lb), 4),
        'davies_bouldin'   : round(davies_bouldin_score(px, lb), 4),
        'calinski_harabasz': round(calinski_harabasz_score(px, lb), 2),
    }


def evaluate_all(results_dict, color_space):
    """Evaluasi semua K untuk satu color space."""
    rows = []
    for k, res in results_dict.items():
        m = evaluate_clustering(res['pixels'], res['labels'])
        rows.append({'Color Space': color_space, 'K': k,
                     **m, 'Inertia': round(res['inertia'], 2)})
    return rows


print("Menghitung metrik evaluasi clustering...")
eval_rows  = evaluate_all(results_rgb, 'RGB')
eval_rows += evaluate_all(results_hsv, 'HSV')
eval_rows += evaluate_all(results_lab, 'LAB')
df_eval = pd.DataFrame(eval_rows)

print("\nTabel Evaluasi Clustering:")
print(df_eval.to_string(index=False))
print("\n  Silhouette     : semakin TINGGI semakin baik (range -1 s.d. 1)")
print("  Davies-Bouldin : semakin RENDAH semakin baik (range 0 ke atas)")
print("  Calinski-Harab : semakin TINGGI semakin baik (range 0 ke atas)")

# Plot perbandingan metrik
cs_colors = {'RGB': '#E74C3C', 'HSV': '#2ECC71', 'LAB': '#3498DB'}
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Perbandingan Metrik Evaluasi Clustering — RGB vs HSV vs LAB",
             fontsize=13, fontweight='bold')
for ax, metric, title in zip(axes,
    ['silhouette', 'davies_bouldin', 'calinski_harabasz'],
    ['Silhouette Score (semakin tinggi semakin baik)',
     'Davies-Bouldin Index (semakin rendah semakin baik)',
     'Calinski-Harabasz Index (semakin tinggi semakin baik)']):
    for cs, grp in df_eval.groupby('Color Space'):
        ax.plot(grp['K'], grp[metric], 'o-', color=cs_colors[cs],
                label=cs, linewidth=2, markersize=8)
    ax.set_xlabel('K'); ax.set_ylabel(metric.replace('_',' ').title())
    ax.set_title(title); ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.show()


# ============================================================
# 9. ANALISIS STABILITAS + PEMILIHAN MODEL TERBAIK
# ============================================================

def compute_cluster_stability(pixels, k, n_runs=5):
    """
    Ukur stabilitas cluster: jalankan K-Means n_runs kali,
    hitung std centroid antar run. Semakin kecil = semakin stabil.
    """
    sample        = sample_pixels(pixels, 3000)
    all_centroids = []
    for seed in range(n_runs):
        _, _, centroids, _ = run_kmeans(sample, k, random_state=seed * 10)
        all_centroids.append(centroids[np.argsort(centroids.mean(axis=1))])
    return np.array(all_centroids).std(axis=0).mean()


print("Menghitung stabilitas cluster...")
stability_results = []
for cs, pixels in [('RGB', pixels_rgb), ('HSV', pixels_hsv), ('LAB', pixels_lab)]:
    for k in K_VALUES:
        stab = compute_cluster_stability(pixels, k)
        stability_results.append({'Color Space': cs, 'K': k,
                                   'Stability Score': round(stab, 4)})
        print(f"  [{cs}] K={k} | Stability={stab:.4f} (semakin kecil semakin stabil)")

df_stability = pd.DataFrame(stability_results)


def select_best_model(df_eval, df_stability):
    """
    Pilih model terbaik berdasarkan composite score.
    Bobot: Silhouette(35%) + DBI(25%) + CHI(20%) + Stability(20%)
    """
    df   = df_eval.merge(df_stability, on=['Color Space', 'K'])
    norm = lambda x: (x - x.min()) / (x.max() - x.min() + 1e-9)
    df['score_sil']  = norm(df['silhouette'])
    df['score_db']   = 1 - norm(df['davies_bouldin'])
    df['score_ch']   = norm(df['calinski_harabasz'])
    df['score_stab'] = 1 - norm(df['Stability Score'])
    df['composite']  = (0.35 * df['score_sil']  + 0.25 * df['score_db'] +
                        0.20 * df['score_ch']   + 0.20 * df['score_stab'])
    df_sorted = df.sort_values('composite', ascending=False)
    best      = df_sorted.iloc[0]

    cols = ['Color Space', 'K', 'silhouette', 'davies_bouldin',
            'calinski_harabasz', 'Stability Score', 'composite']
    print("\nRanking Model (Top 5 Composite Score):")
    print(df_sorted[cols].head(5).to_string(index=False))
    print(f"\nCOLOR SPACE TERBAIK : {best['Color Space']}")
    print(f"K optimal           : {int(best['K'])}")
    print(f"Composite Score     : {best['composite']:.4f}")
    return best['Color Space'], int(best['K']), df_sorted


best_cs, best_k, df_ranked = select_best_model(df_eval, df_stability)


# ============================================================
# 10. KLASIFIKASI SKINTONE — ITA (Individual Typology Angle)
#
# Alur klasifikasi (sesuai metodologi Bab 3):
#   1. Ambil centroid warna kulit (hasil K-Means)
#   2. Konversi centroid ke RGB (jika dari HSV/LAB)
#   3. Konversi RGB ke CIELAB
#   4. Hitung ITA:
#        ITA = arctan((L* - 50) / b*) * (180 / pi)
#   5. Klasifikasikan ke 6 kategori berdasarkan nilai ITA
#
# Kategori ITA (Chardon et al., diperkuat Jung et al., 2024):
#   Very Light   : ITA > 55°
#   Light        : 41° < ITA <= 55°
#   Intermediate : 28° < ITA <= 41°
#   Tan          : 10° < ITA <= 28°
#   Brown        : -30° < ITA <= 10°
#   Dark         : ITA <= -30°
#
# Alasan menggunakan ITA (bukan HSV brightness):
#   - ITA adalah standar industri kosmetik dan dermatologi
#   - Dihitung dari L* (kecerahan) dan b* (kuning-biru) di CIELAB
#   - Lebih presisi karena memperhitungkan komponen undertone (b*)
#   - HSV brightness hanya memperhitungkan kecerahan, bukan undertone
# ============================================================

def rgb_to_cielab_std(rgb_tuple):
    """
    Konversi RGB (0-255) ke CIELAB skala standar menggunakan OpenCV.
    Returns: (L* in [0,100], a* in [-128,127], b* in [-128,127])
    """
    px  = np.uint8([[list(rgb_tuple)]])
    bgr = cv2.cvtColor(px, cv2.COLOR_RGB2BGR)
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    L, a, b = lab[0][0]
    return (L / 255.0) * 100.0, float(a) - 128.0, float(b) - 128.0


def compute_ita(L_star, b_star):
    """
    Hitung Individual Typology Angle (ITA).
    ITA = arctan((L* - 50) / b*) * (180 / pi)
    Nilai besar positif = kulit sangat terang.
    Nilai besar negatif = kulit sangat gelap.
    """
    if b_star == 0:
        b_star = 1e-6
    return np.arctan((L_star - 50.0) / b_star) * (180.0 / np.pi)


def classify_skintone_ita(rgb_tuple):
    """
    Klasifikasikan warna kulit ke 6 kategori berdasarkan nilai ITA.

    Returns:
        category : nama kategori skintone
        ita_val  : nilai ITA numerik (derajat)
        L_star   : nilai L* dari CIELAB
        b_star   : nilai b* dari CIELAB
    """
    L_star, _, b_star = rgb_to_cielab_std(rgb_tuple)
    ita = compute_ita(L_star, b_star)

    if   ita > 55 : category = 'Very Light'
    elif ita > 41 : category = 'Light'
    elif ita > 28 : category = 'Intermediate'
    elif ita > 10 : category = 'Tan'
    elif ita > -30: category = 'Brown'
    else          : category = 'Dark'

    return category, round(ita, 2), round(L_star, 2), round(b_star, 2)


def classify_undertone_lab(rgb_tuple):
    """
    Tentukan undertone (Cool / Neutral / Warm) dari distribusi
    a* dan b* di CIELAB.
      b* > 5  dan a* < 10  = Warm
      b* < -2 atau a* > 12 = Cool
      Selainnya             = Neutral
    """
    _, a_star, b_star = rgb_to_cielab_std(rgb_tuple)
    if   b_star > 5 and a_star < 10 : return 'Warm'
    elif b_star < -2 or a_star > 12  : return 'Cool'
    else                              : return 'Neutral'


# Demo klasifikasi ITA
print("\nDemo klasifikasi ITA untuk warna referensi:")
for rgb, label in [((255,224,189),"Fair reference"),
                    ((198,134, 66),"Medium reference"),
                    (( 80, 40, 20),"Dark reference")]:
    cat, ita, L, b = classify_skintone_ita(rgb)
    und = classify_undertone_lab(rgb)
    print(f"  {label}: ITA={ita:+.1f}° -> {cat} | Undertone: {und} | L*={L:.1f}, b*={b:.1f}")


# ============================================================
# 11. ENGINE REKOMENDASI WARNA PAKAIAN
#
# Alur rekomendasi:
#   1. Centroid RGB -> klasifikasi ITA -> skintone + undertone
#   2. Lookup tabel rekomendasi (rule-based, bukan filtering)
#      Tabel memetakan kombinasi (skintone, undertone) ke
#      daftar warna pakaian yang sesuai
#   3. Output: nama warna, kode HEX, warna yang dihindari, alasan
#
# Catatan: Sistem ini TIDAK menggunakan riwayat pengguna.
# Rekomendasi murni berbasis aturan warna (color theory).
# ============================================================

# Tabel rekomendasi berdasarkan ITA category + undertone
RECOMMENDATION_TABLE = {
    'Very Light': {
        'undertone_map': {
            'Cool'   : ['Royal Blue','Emerald','Lavender','Silver'],
            'Neutral': ['Soft Pink','Ice Blue','Mint','Pearl White'],
            'Warm'   : ['Blush Pink','Peach','Champagne','Warm Ivory'],
        },
        'avoid' : 'Warna sangat pucat (putih murni, cream sangat terang) yang membuat tampilan kusam',
        'harmony': 'Complementary',
        'reason' : 'Kulit sangat terang memerlukan warna jewel tone untuk menciptakan kontras visual yang sehat',
    },
    'Light': {
        'undertone_map': {
            'Cool'   : ['Dusty Pink','Periwinkle','Soft Lavender','Slate Blue'],
            'Neutral': ['Jade Green','Off-White','Taupe','Grey'],
            'Warm'   : ['Warm Peach','Coral','Dusty Rose','Sand'],
        },
        'avoid' : 'Warna neon terlalu terang dan orange yang terlalu jenuh',
        'harmony': 'Analogous',
        'reason' : 'Skintone light cocok dengan warna berdekatan (analogous) untuk tampilan harmonis',
    },
    'Intermediate': {
        'undertone_map': {
            'Cool'   : ['Mauve','Dusty Purple','Teal','Charcoal'],
            'Neutral': ['Olive Green','Khaki','Caramel','Rust'],
            'Warm'   : ['Mustard','Terracotta','Coral','Burnt Orange'],
        },
        'avoid' : 'Warna neon dan kuning-hijau yang terlalu terang',
        'harmony': 'Triadic',
        'reason' : 'Earth tones dan warna hangat melengkapi undertone medium dengan baik',
    },
    'Tan': {
        'undertone_map': {
            'Cool'   : ['Cobalt Blue','Fuchsia','Forest Green','Burgundy'],
            'Neutral': ['Warm Brown','Copper','Amber','Olive'],
            'Warm'   : ['Golden Yellow','Deep Orange','Saffron','Rust'],
        },
        'avoid' : 'Warna coklat muda yang terlalu mirip warna kulit sehingga kontras hilang',
        'harmony': 'Monochromatic',
        'reason' : 'Warna hangat dan cerah menonjolkan kehangatan skintone tan secara alami',
    },
    'Brown': {
        'undertone_map': {
            'Cool'   : ['Cream','Lilac','Soft Turquoise','Powder Blue'],
            'Neutral': ['Beige','Ivory','Forest Green','Burgundy'],
            'Warm'   : ['Orange','Bright Yellow','Warm Red','Royal Blue'],
        },
        'avoid' : 'Warna coklat gelap yang menyatu dengan warna kulit',
        'harmony': 'Analogous',
        'reason' : 'Warna cerah dan terang menciptakan kontras yang menonjolkan skintone brown',
    },
    'Dark': {
        'undertone_map': {
            'Cool'   : ['Cobalt Blue','Magenta','Turquoise','Silver'],
            'Neutral': ['Maroon','Forest Green','Warm White','Emerald'],
            'Warm'   : ['Bright Red','Lime Green','Hot Pink','Electric Blue'],
        },
        'avoid' : 'Warna gelap (hitam, navy gelap, coklat tua) yang mengurangi visibilitas warna kulit',
        'harmony': 'Complementary',
        'reason' : 'Warna vivid dan cerah memberikan kontras kuat yang menonjolkan keindahan skintone dark',
    },
}

COLOR_HEX_REFERENCE = {
    'Royal Blue':'#4169E1','Emerald':'#50C878','Lavender':'#E6E6FA','Silver':'#C0C0C0',
    'Soft Pink':'#FFB6C1','Ice Blue':'#99C5C4','Mint':'#98FF98','Pearl White':'#F8F8FF',
    'Blush Pink':'#FF6B8A','Peach':'#FFCBA4','Champagne':'#F7E7CE','Warm Ivory':'#FFFFF0',
    'Dusty Pink':'#DCAE96','Periwinkle':'#CCCCFF','Soft Lavender':'#DCD0FF',
    'Slate Blue':'#6A5ACD','Jade Green':'#00A86B','Off-White':'#FAF9F6',
    'Taupe':'#483C32','Grey':'#808080','Warm Peach':'#FFCBA4','Coral':'#FF7F50',
    'Dusty Rose':'#DCAE96','Sand':'#C2B280','Mauve':'#E0B0FF','Dusty Purple':'#B57EDC',
    'Teal':'#008080','Charcoal':'#36454F','Olive Green':'#808000','Khaki':'#C3B091',
    'Caramel':'#C68642','Rust':'#B7410E','Mustard':'#FFDB58','Terracotta':'#E2725B',
    'Burnt Orange':'#CC5500','Cobalt Blue':'#0047AB','Fuchsia':'#FF00FF',
    'Forest Green':'#228B22','Burgundy':'#800020','Warm Brown':'#964B00',
    'Copper':'#B87333','Amber':'#FFBF00','Olive':'#808000','Golden Yellow':'#FFDF00',
    'Deep Orange':'#FF4500','Saffron':'#F4C430','Cream':'#FFFDD0','Lilac':'#C8A2C8',
    'Soft Turquoise':'#40E0D0','Powder Blue':'#B0E0E6','Beige':'#F5F5DC',
    'Ivory':'#FFFFF0','Orange':'#FF7F00','Bright Yellow':'#FFFF33','Warm Red':'#FF4500',
    'Magenta':'#FF00FF','Turquoise':'#30D5C8','Maroon':'#800000','Warm White':'#FEFEFA',
    'Bright Red':'#FF0000','Lime Green':'#32CD32','Hot Pink':'#FF69B4',
    'Electric Blue':'#7DF9FF',
}


def hex_to_rgb(hex_str):
    h = hex_str.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def get_clothing_recommendations(skin_centroid_rgb):
    """
    Hasilkan rekomendasi warna pakaian berdasarkan centroid warna kulit.

    Args:
        skin_centroid_rgb : tuple (R, G, B) centroid warna kulit
    Returns:
        dict hasil rekomendasi lengkap
    """
    skin_rgb = tuple(int(x) for x in skin_centroid_rgb)
    skin_hex = '#{:02X}{:02X}{:02X}'.format(*skin_rgb)

    skintone_cat, ita_val, L_star, b_star = classify_skintone_ita(skin_rgb)
    undertone    = classify_undertone_lab(skin_rgb)
    table        = RECOMMENDATION_TABLE.get(skintone_cat,
                       RECOMMENDATION_TABLE['Intermediate'])
    color_names  = table['undertone_map'].get(undertone,
                       table['undertone_map']['Neutral'])

    recommended_colors = [{
        'name': name,
        'hex' : COLOR_HEX_REFERENCE.get(name, '#808080'),
        'rgb' : hex_to_rgb(COLOR_HEX_REFERENCE.get(name, '#808080'))
    } for name in color_names]

    return {
        'skin_rgb'   : skin_rgb,
        'skin_hex'   : skin_hex,
        'skintone'   : skintone_cat,
        'undertone'  : undertone,
        'ita_value'  : ita_val,
        'L_star'     : L_star,
        'b_star'     : b_star,
        'harmony'    : table['harmony'],
        'recommended': recommended_colors,
        'avoid'      : table['avoid'],
        'reason'     : table['reason'],
    }


print("Engine rekomendasi warna siap.")


# ============================================================
# 12. VALIDASI CENTROID MENGGUNAKAN CIEDE2000
#
# Tujuan:
#   Mengukur seberapa jauh centroid hasil K-Means dari
#   referensi warna kulit manusia yang sudah diketahui.
#   Ini adalah validasi bahwa centroid benar-benar merepresentasikan
#   warna kulit, bukan noise atau background.
#
# Metode:
#   - 6 titik referensi warna kulit standar (Very Light s.d. Dark)
#   - Jarak diukur dengan CIEDE2000 di CIELAB
#     (memperhitungkan persepsi manusia, bukan Euclidean biasa)
#   - Centroid dengan jarak CIEDE2000 < 10 dianggap valid
#
# Interpretasi nilai CIEDE2000:
#   < 1   : tidak terlihat berbeda oleh mata manusia
#   1-2   : perbedaan sangat kecil (ambang persepsi)
#   2-10  : perbedaan kecil-sedang, masih merepresentasikan kulit
#   10-20 : perbedaan sedang, masih dalam toleransi wajar
#   > 20  : centroid mungkin mengandung noise atau non-skin pixel
#            -> pertimbangkan perbaikan tahap segmentasi
#
# CATATAN:
#   Berbeda dari versi sebelumnya yang mengukur diversitas palet,
#   fungsi CIEDE2000 di sini mengukur validitas centroid terhadap
#   referensi warna kulit yang diketahui.
# ============================================================

SKIN_REFERENCE_COLORS = {
    'Very Light (ITA>55)'    : (255, 224, 189),
    'Light (ITA 41-55)'      : (241, 194, 125),
    'Intermediate (ITA 28-41)': (210, 160,  90),
    'Tan (ITA 10-28)'        : (180, 120,  60),
    'Brown (ITA -30 to 10)'  : (130,  80,  35),
    'Dark (ITA<-30)'         : ( 70,  35,  15),
}


def rgb_to_lab_colormath(rgb_tuple):
    """Konversi RGB ke LabColor (colormath) untuk CIEDE2000."""
    srgb = sRGBColor(rgb_tuple[0]/255.0, rgb_tuple[1]/255.0, rgb_tuple[2]/255.0)
    return convert_color(srgb, LabColor)


def compute_ciede2000_distance(rgb1, rgb2):
    """Hitung jarak perceptual CIEDE2000 antara dua warna RGB."""
    return float(delta_e_cie2000(rgb_to_lab_colormath(rgb1),
                                  rgb_to_lab_colormath(rgb2)))


def validate_centroids_ciede2000(centroids_rgb, color_space_name=''):
    """
    Validasi centroid vs referensi warna kulit standar menggunakan CIEDE2000.

    Untuk setiap centroid: hitung jarak ke semua 6 referensi,
    laporkan referensi terdekat dan interpretasinya.

    Returns:
        df_validation : DataFrame hasil validasi
    """
    ref_names  = list(SKIN_REFERENCE_COLORS.keys())
    ref_colors = list(SKIN_REFERENCE_COLORS.values())
    rows = []

    for i, c_rgb in enumerate(centroids_rgb):
        c_rgb_tuple = tuple(int(x) for x in c_rgb)
        c_hex       = '#{:02X}{:02X}{:02X}'.format(*c_rgb_tuple)
        skintone_cat, ita_val, L_star, b_star = classify_skintone_ita(c_rgb_tuple)
        undertone = classify_undertone_lab(c_rgb_tuple)

        distances = [compute_ciede2000_distance(c_rgb_tuple, r) for r in ref_colors]
        min_dist  = min(distances)
        nearest   = ref_names[np.argmin(distances)]

        if   min_dist <  2 : interp = 'Sangat dekat — tidak terlihat berbeda'
        elif min_dist < 10 : interp = 'Dekat — merepresentasikan warna kulit'
        elif min_dist < 20 : interp = 'Sedang — masih dalam toleransi'
        else               : interp = 'JAUH — kemungkinan noise/background'

        rows.append({
            'Color Space'       : color_space_name,
            'Cluster'           : i + 1,
            'Centroid Hex'      : c_hex,
            'ITA (deg)'         : ita_val,
            'Skintone (ITA)'    : skintone_cat,
            'Undertone'         : undertone,
            'Nearest Reference' : nearest,
            'CIEDE2000 Distance': round(min_dist, 2),
            'Interpretasi'      : interp,
        })

    return pd.DataFrame(rows)


def centroids_rgb_from_space(centroids, color_space):
    """Konversi centroid dari color space tertentu ke RGB."""
    if color_space == 'RGB':
        return centroids.astype(np.uint8)
    elif color_space == 'HSV':
        return np.array([cv2.cvtColor(np.uint8([[c]]),
                         cv2.COLOR_HSV2RGB)[0][0] for c in centroids], dtype=np.uint8)
    elif color_space == 'LAB':
        return np.array([cv2.cvtColor(np.uint8([[c]]),
                         cv2.COLOR_LAB2RGB)[0][0] for c in centroids], dtype=np.uint8)


# Ambil model terbaik
BEST_RESULTS_MAP   = {'RGB': results_rgb, 'HSV': results_hsv, 'LAB': results_lab}
best_model_results = BEST_RESULTS_MAP[best_cs]
if best_k not in best_model_results:
    best_k = K_VALUES[0]

best_centroids_raw = best_model_results[best_k]['centroids']
best_centroids_rgb = centroids_rgb_from_space(best_centroids_raw, best_cs)

print(f"\nValidasi CIEDE2000 — Model Terbaik: {best_cs} | K={best_k}")
df_validation = validate_centroids_ciede2000(best_centroids_rgb, best_cs)
print(df_validation.to_string(index=False))

print("""
Interpretasi CIEDE2000:
  < 2  : Tidak terlihat berbeda oleh mata manusia
  2-10 : Perbedaan kecil, centroid valid merepresentasikan warna kulit
  10-20: Perbedaan sedang, masih dalam toleransi
  > 20 : Centroid kemungkinan noise/non-skin -> perbaiki segmentasi
""")

# Validasi untuk semua color space dan K
print("Validasi CIEDE2000 untuk semua konfigurasi...")
ciede_rows = []
for cs, results_dict in [('RGB', results_rgb), ('HSV', results_hsv), ('LAB', results_lab)]:
    for k, res in results_dict.items():
        c_rgb = centroids_rgb_from_space(res['centroids'], cs)
        df_v  = validate_centroids_ciede2000(c_rgb, cs)
        ciede_rows.append({'Color Space': cs, 'K': k,
                           'Avg CIEDE2000': round(df_v['CIEDE2000 Distance'].mean(), 2)})

df_ciede_summary = pd.DataFrame(ciede_rows)
print("\nRingkasan Rata-rata CIEDE2000 per Konfigurasi:")
print(df_ciede_summary.to_string(index=False))
print("  (Semakin rendah = centroid lebih dekat ke referensi warna kulit standar)")


# ============================================================
# 13. JALANKAN REKOMENDASI UNTUK MODEL TERBAIK
# ============================================================

print(f"\nRekomendasi dengan model terbaik: {best_cs} | K={best_k}")
print("=" * 65)

for i, centroid_rgb in enumerate(best_centroids_rgb):
    rec = get_clothing_recommendations(centroid_rgb)
    print(f"\n--- Cluster {i+1} ---")
    print(f"  Warna Kulit   : {rec['skin_hex']}")
    print(f"  Skintone (ITA): {rec['skintone']} (ITA = {rec['ita_value']:+.1f} derajat)")
    print(f"  Undertone     : {rec['undertone']}")
    print(f"  Harmoni       : {rec['harmony']}")
    print(f"  Rekomendasi   :")
    for cr in rec['recommended']:
        print(f"    OK  {cr['name']:<22} {cr['hex']}")
    print(f"  Hindari       : {rec['avoid']}")
    print(f"  Alasan        : {rec['reason']}")


# ============================================================
# 14. VISUALISASI DASHBOARD KOMPREHENSIF
# ============================================================

def visualize_full_results(best_cs, best_k, best_centroids_rgb,
                            df_eval, df_ranked, df_validation,
                            inertias_rgb, best_k_rgb):
    """Dashboard ringkasan seluruh hasil analisis."""
    fig = plt.figure(figsize=(22, 16))
    fig.suptitle(
        f"Dashboard — Sistem Rekomendasi Warna Pakaian\n"
        f"Model Terbaik: {best_cs} | K={best_k}",
        fontsize=14, fontweight='bold', y=0.99
    )
    gs = fig.add_gridspec(3, 3, hspace=0.5, wspace=0.35)

    # Panel 1: Ranking Composite Score
    ax1 = fig.add_subplot(gs[0, :])
    bc  = [cs_colors[r['Color Space']] for _, r in df_ranked.iterrows()]
    lb  = [f"{r['Color Space']}-K{int(r['K'])}" for _, r in df_ranked.iterrows()]
    bars = ax1.bar(lb, df_ranked['composite'], color=bc, alpha=0.85,
                   edgecolor='black', linewidth=0.5)
    ax1.bar_label(bars, fmt='%.3f', padding=2, fontsize=8)
    ax1.set_title(f'Ranking Composite Score | Best: {best_cs}-K{best_k}')
    ax1.set_ylabel('Composite Score (semakin tinggi semakin baik)')
    ax1.tick_params(axis='x', rotation=45); ax1.grid(True, alpha=0.3, axis='y')
    patches = [mpatches.Patch(color=v, label=k) for k, v in cs_colors.items()]
    ax1.legend(handles=patches, loc='upper right')

    # Panel 2: Elbow Curve RGB
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.plot(list(K_RANGE), inertias_rgb, 'bo-', linewidth=2, markersize=7)
    ax2.axvline(x=best_k_rgb, color='red', linestyle='--', label=f'K={best_k_rgb}')
    ax2.set_title('Elbow Curve (RGB)'); ax2.set_xlabel('K'); ax2.set_ylabel('Inertia (WCSS)')
    ax2.legend(); ax2.grid(True, alpha=0.3)

    # Panel 3: Silhouette per K
    ax3 = fig.add_subplot(gs[1, 1])
    for cs, grp in df_eval.groupby('Color Space'):
        ax3.plot(grp['K'], grp['silhouette'], 'o-',
                 color=cs_colors[cs], label=cs, linewidth=2)
    ax3.set_title('Silhouette Score per K (semakin tinggi semakin baik)')
    ax3.set_xlabel('K'); ax3.legend(); ax3.grid(True, alpha=0.3)

    # Panel 4: CIEDE2000 Validation
    ax4 = fig.add_subplot(gs[1, 2])
    clrs = ['#27AE60' if d < 10 else '#E74C3C' for d in df_validation['CIEDE2000 Distance']]
    ax4.bar([f"C{r['Cluster']}" for _, r in df_validation.iterrows()],
            df_validation['CIEDE2000 Distance'], color=clrs, edgecolor='black', linewidth=0.5)
    ax4.axhline(y=10, color='orange', linestyle='--', linewidth=1.5, label='Threshold 10')
    ax4.axhline(y=2,  color='green',  linestyle='--', linewidth=1.5, label='Threshold 2')
    ax4.set_title(f'Validasi CIEDE2000 ({best_cs}, K={best_k})\n(semakin rendah = lebih valid)')
    ax4.set_xlabel('Cluster'); ax4.legend(fontsize=7); ax4.grid(True, alpha=0.3, axis='y')

    # Panel 5-7: Palet rekomendasi per cluster
    for i in range(min(3, len(best_centroids_rgb))):
        ax = fig.add_subplot(gs[2, i])
        skin_rgb = tuple(int(x) for x in best_centroids_rgb[i])
        rec = get_clothing_recommendations(skin_rgb)
        palette_colors = [skin_rgb] + [cr['rgb'] for cr in rec['recommended'][:4]]
        palette_names  = ['KULIT'] + [cr['name'][:9] for cr in rec['recommended'][:4]]
        palette_hex    = [rec['skin_hex']] + [cr['hex'] for cr in rec['recommended'][:4]]

        pal_img = np.zeros((80, len(palette_colors) * 50, 3), dtype=np.uint8)
        for j, c in enumerate(palette_colors):
            pal_img[:, j*50:(j+1)*50, :] = np.array(c[:3], dtype=np.uint8)
        ax.imshow(pal_img)
        ax.set_title(
            f"Cluster {i+1}: {rec['skintone']}\n"
            f"ITA={rec['ita_value']:+.0f} | {rec['undertone']} | {rec['skin_hex']}",
            fontsize=8
        )
        for j, (name, hx) in enumerate(zip(palette_names, palette_hex)):
            ax.text(j*50+25, 90, f"{name}\n{hx}", ha='center', va='top',
                    fontsize=5.5, linespacing=1.4)
        ax.axis('off')

    plt.savefig('/content/dashboard_results.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Dashboard disimpan ke: /content/dashboard_results.png")


visualize_full_results(best_cs, best_k, best_centroids_rgb,
                       df_eval, df_ranked, df_validation,
                       inertias_rgb, best_k_rgb)


# ============================================================
# 15. KESIMPULAN
# ============================================================

best_row = df_ranked.iloc[0]
print("=" * 65)
print("   KESIMPULAN PENELITIAN")
print("=" * 65)
print(f"""
1. COLOR SPACE TERBAIK: {best_cs}
   Silhouette Score     : {best_row['silhouette']:.4f}  (semakin tinggi semakin baik)
   Davies-Bouldin Index : {best_row['davies_bouldin']:.4f}  (semakin rendah semakin baik)
   Calinski-Harabasz    : {best_row['calinski_harabasz']:.2f} (semakin tinggi semakin baik)
   Stability Score      : {best_row['Stability Score']:.4f}  (semakin kecil semakin stabil)
   Composite Score      : {best_row['composite']:.4f}

2. K TERBAIK: {best_k}
   Penentuan:  Elbow Method (knee point K={best_k_rgb} pada RGB)
               + evaluasi penuh Silhouette/DBI/CHI/Stability pada K=[3,5,7]
   Sifat K  :  TETAP — divalidasi pada sampel representatif dataset
   Cakupan  :  K-Means hanya pada pixel KULIT (setelah skin masking)
               bukan seluruh pixel gambar

3. VALIDASI CIEDE2000:
   Silhouette/DBI/CHI hanya mengukur struktur cluster.
   Validasi CIEDE2000 mengonfirmasi kedekatan centroid ke referensi
   warna kulit standar (nilai lebih rendah = centroid lebih valid).

4. KLASIFIKASI SKINTONE (ITA):
   ITA = arctan((L* - 50) / b*) * (180/pi)
   6 kategori: Very Light > Light > Intermediate > Tan > Brown > Dark

5. PIPELINE LENGKAP:
   Input Citra Wajah
   -> Haar Cascade (face detection + crop)
   -> CLAHE Preprocessing (normalisasi pencahayaan)
   -> Skin Masking Voting (RGB + HSV + YCrCb, majority >= 2/3)
   -> Ekstraksi Pixel Kulit
   -> K-Means Clustering (RGB, HSV, LAB; K=[3,5,7])
   -> Elbow Method (penentuan K) + Evaluasi (Silhouette/DBI/CHI)
   -> Pilih Color Space Terbaik via Composite Score
   -> Klasifikasi ITA (skintone + undertone)
   -> Rule-based Rekomendasi Warna Pakaian
   -> Validasi CIEDE2000 (centroid vs referensi standar)
""")
print("=" * 65)
print("   Pipeline selesai!")
print("=" * 65)
