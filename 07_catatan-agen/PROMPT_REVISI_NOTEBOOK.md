# Prompt Revisi Notebook: skin_color_recommendation.ipynb

Gunakan prompt ini langsung di Claude baru (atau ChatGPT) dengan melampirkan file
`skin_color_recommendation.py` (kode asli). Prompt ini akan menghasilkan notebook
`.ipynb` yang sudah direvisi sesuai catatan Seminar Proposal.

---

## PROMPT

Kamu adalah asisten penelitian skripsi yang membantu merevisi kode Python menjadi
Jupyter Notebook `.ipynb` yang siap digunakan di Google Colab.

Saya melampirkan file `skin_color_recommendation.py` (kode asli). Tolong buat ulang
seluruh kode ini menjadi sebuah file `.ipynb` dengan menerapkan semua revisi berikut.
Jangan hanya menambahkan komentar — implementasikan perubahannya secara nyata di kode.

---

### REVISI 1 — Tambahkan Deteksi Wajah Haar Cascade (SEBELUM segmentasi kulit)

**Masalah di kode asli:** Tidak ada deteksi wajah. Gambar langsung diproses ke segmentasi
kulit tanpa crop wajah terlebih dahulu.

**Yang harus dibuat:**
- Muat Haar Cascade dari `cv2.data.haarcascades + "haarcascade_frontalface_default.xml"`
- Buat fungsi `detect_and_crop_face(img_bgr)` dengan parameter:
  - `scaleFactor=1.1`
  - `minNeighbors=5`
  - `minSize=(60, 60)`
  - `padding=0.15` — perluas crop 15% ke setiap sisi agar pipi dan dahi ikut
  - Jika lebih dari satu wajah terdeteksi, ambil yang terbesar (area terbesar)
  - Kembalikan `(face_crop, bbox)` atau `(None, None)` jika tidak terdeteksi
- Buat fungsi `detect_faces_dataset(preprocessed_dataset)` yang:
  - Menjalankan deteksi ke semua gambar
  - Men-skip gambar yang wajahnya tidak terdeteksi
  - Melaporkan jumlah berhasil dan jumlah di-skip
- Tambahkan fallback: jika lebih dari 50% gambar di-skip (misal dataset sintetis),
  gunakan `preprocessed_dataset` langsung tanpa face detection
- Sisipkan cell ini sesudah Bagian 3 (Preprocessing) dan sebelum Bagian segmentasi
- Sertakan visualisasi: tampilkan contoh hasil crop wajah untuk 3 gambar pertama

**Alasan yang harus ditulis di markdown cell:**
Haar Cascade dipilih karena ringan, tidak memerlukan GPU, sudah tersedia di OpenCV
tanpa instalasi tambahan, dan cukup untuk citra wajah frontal dengan ekspresi natural
sesuai batasan masalah penelitian.

---

### REVISI 2 — Ubah Klasifikasi Skintone dari HSV Brightness ke ITA (CIELAB)

**Masalah di kode asli:** Fungsi `classify_skin_tone()` menggunakan nilai brightness
dari HSV (`v` dari `rgb_to_hsv_single`). Ini tidak sesuai metodologi skripsi.

**Yang harus dihapus:**
- Fungsi `classify_skin_tone(rgb)` yang memakai HSV brightness
- Dictionary `SKIN_TONE_STRATEGY` dengan kategori Very Fair/Fair/Medium/Olive/Brown/Dark
- Semua pemanggilan `classify_skin_tone()` di seluruh notebook

**Yang harus dibuat sebagai penggantinya:**

Fungsi `rgb_to_cielab_std(rgb_tuple)`:
```
Konversi RGB (0-255) ke CIELAB skala standar menggunakan OpenCV.
Denormalisasi:
  L* = (L_opencv / 255.0) * 100.0       → range 0–100
  a* = float(a_opencv) - 128.0           → range -128 to 127
  b* = float(b_opencv) - 128.0           → range -128 to 127
Return: (L_star, a_star, b_star)
```

Fungsi `compute_ita(L_star, b_star)`:
```
Formula: ITA = arctan((L* - 50) / b*) * (180 / pi)
Catatan: jika b* == 0, gunakan b* = 1e-6 untuk menghindari pembagian nol
```

Fungsi `classify_skintone_ita(rgb_tuple)`:
```
Kategori ITA (Chardon et al.):
  Very Light   : ITA > 55°
  Light        : 41° < ITA <= 55°
  Intermediate : 28° < ITA <= 41°
  Tan          : 10° < ITA <= 28°
  Brown        : -30° < ITA <= 10°
  Dark         : ITA <= -30°
Return: (category, ita_value, L_star, b_star)
```

Fungsi `classify_undertone_lab(rgb_tuple)`:
```
Tentukan undertone dari a* dan b* di CIELAB:
  Warm    : b* > 5 dan a* < 10
  Cool    : b* < -2 atau a* > 12
  Neutral : selainnya
Return: 'Warm' | 'Cool' | 'Neutral'
```

**Tabel rekomendasi yang harus digunakan** (ganti `SKIN_TONE_STRATEGY`):

```python
RECOMMENDATION_TABLE = {
    'Very Light': {
        'undertone_map': {
            'Cool'   : ['Royal Blue', 'Emerald', 'Lavender', 'Silver'],
            'Neutral': ['Soft Pink', 'Ice Blue', 'Mint', 'Pearl White'],
            'Warm'   : ['Blush Pink', 'Peach', 'Champagne', 'Warm Ivory'],
        },
        'avoid'  : 'Warna sangat pucat (putih murni, cream sangat terang) yang membuat tampilan kusam',
        'harmony': 'Complementary',
        'reason' : 'Kulit sangat terang memerlukan warna jewel tone untuk menciptakan kontras visual yang sehat',
    },
    'Light': {
        'undertone_map': {
            'Cool'   : ['Dusty Pink', 'Periwinkle', 'Soft Lavender', 'Slate Blue'],
            'Neutral': ['Jade Green', 'Off-White', 'Taupe', 'Grey'],
            'Warm'   : ['Warm Peach', 'Coral', 'Dusty Rose', 'Sand'],
        },
        'avoid'  : 'Warna neon terlalu terang dan orange yang terlalu jenuh',
        'harmony': 'Analogous',
        'reason' : 'Skintone light cocok dengan warna berdekatan (analogous) untuk tampilan harmonis',
    },
    'Intermediate': {
        'undertone_map': {
            'Cool'   : ['Mauve', 'Dusty Purple', 'Teal', 'Charcoal'],
            'Neutral': ['Olive Green', 'Khaki', 'Caramel', 'Rust'],
            'Warm'   : ['Mustard', 'Terracotta', 'Coral', 'Burnt Orange'],
        },
        'avoid'  : 'Warna neon dan kuning-hijau yang terlalu terang',
        'harmony': 'Triadic',
        'reason' : 'Earth tones dan warna hangat melengkapi undertone medium dengan baik',
    },
    'Tan': {
        'undertone_map': {
            'Cool'   : ['Cobalt Blue', 'Fuchsia', 'Forest Green', 'Burgundy'],
            'Neutral': ['Warm Brown', 'Copper', 'Amber', 'Olive'],
            'Warm'   : ['Golden Yellow', 'Deep Orange', 'Saffron', 'Rust'],
        },
        'avoid'  : 'Warna coklat muda yang terlalu mirip warna kulit sehingga kontras hilang',
        'harmony': 'Monochromatic',
        'reason' : 'Warna hangat dan cerah menonjolkan kehangatan skintone tan secara alami',
    },
    'Brown': {
        'undertone_map': {
            'Cool'   : ['Cream', 'Lilac', 'Soft Turquoise', 'Powder Blue'],
            'Neutral': ['Beige', 'Ivory', 'Forest Green', 'Burgundy'],
            'Warm'   : ['Orange', 'Bright Yellow', 'Warm Red', 'Royal Blue'],
        },
        'avoid'  : 'Warna coklat gelap yang menyatu dengan warna kulit',
        'harmony': 'Analogous',
        'reason' : 'Warna cerah dan terang menciptakan kontras yang menonjolkan skintone brown',
    },
    'Dark': {
        'undertone_map': {
            'Cool'   : ['Cobalt Blue', 'Magenta', 'Turquoise', 'Silver'],
            'Neutral': ['Maroon', 'Forest Green', 'Warm White', 'Emerald'],
            'Warm'   : ['Bright Red', 'Lime Green', 'Hot Pink', 'Electric Blue'],
        },
        'avoid'  : 'Warna gelap (hitam, navy gelap, coklat tua) yang mengurangi visibilitas warna kulit',
        'harmony': 'Complementary',
        'reason' : 'Warna vivid dan cerah memberikan kontras kuat yang menonjolkan keindahan skintone dark',
    },
}
```

**Referensi HEX** untuk nama warna di atas:
```python
COLOR_HEX_REFERENCE = {
    'Royal Blue':'#4169E1', 'Emerald':'#50C878', 'Lavender':'#E6E6FA', 'Silver':'#C0C0C0',
    'Soft Pink':'#FFB6C1', 'Ice Blue':'#99C5C4', 'Mint':'#98FF98', 'Pearl White':'#F8F8FF',
    'Blush Pink':'#FF6B8A', 'Peach':'#FFCBA4', 'Champagne':'#F7E7CE', 'Warm Ivory':'#FFFFF0',
    'Dusty Pink':'#DCAE96', 'Periwinkle':'#CCCCFF', 'Soft Lavender':'#DCD0FF',
    'Slate Blue':'#6A5ACD', 'Jade Green':'#00A86B', 'Off-White':'#FAF9F6',
    'Taupe':'#483C32', 'Grey':'#808080', 'Warm Peach':'#FFCBA4', 'Coral':'#FF7F50',
    'Dusty Rose':'#DCAE96', 'Sand':'#C2B280', 'Mauve':'#E0B0FF', 'Dusty Purple':'#B57EDC',
    'Teal':'#008080', 'Charcoal':'#36454F', 'Olive Green':'#808000', 'Khaki':'#C3B091',
    'Caramel':'#C68642', 'Rust':'#B7410E', 'Mustard':'#FFDB58', 'Terracotta':'#E2725B',
    'Burnt Orange':'#CC5500', 'Cobalt Blue':'#0047AB', 'Fuchsia':'#FF00FF',
    'Forest Green':'#228B22', 'Burgundy':'#800020', 'Warm Brown':'#964B00',
    'Copper':'#B87333', 'Amber':'#FFBF00', 'Olive':'#808000', 'Golden Yellow':'#FFDF00',
    'Deep Orange':'#FF4500', 'Saffron':'#F4C430', 'Cream':'#FFFDD0', 'Lilac':'#C8A2C8',
    'Soft Turquoise':'#40E0D0', 'Powder Blue':'#B0E0E6', 'Beige':'#F5F5DC',
    'Ivory':'#FFFFF0', 'Orange':'#FF7F00', 'Bright Yellow':'#FFFF33', 'Warm Red':'#FF4500',
    'Magenta':'#FF00FF', 'Turquoise':'#30D5C8', 'Maroon':'#800000', 'Warm White':'#FEFEFA',
    'Bright Red':'#FF0000', 'Lime Green':'#32CD32', 'Hot Pink':'#FF69B4',
    'Electric Blue':'#7DF9FF',
}
```

**Ubah fungsi `get_clothing_recommendations()`** menjadi:
```
1. Konversi centroid ke tuple (R, G, B)
2. Panggil classify_skintone_ita() → dapatkan skintone_cat, ita_val, L_star, b_star
3. Panggil classify_undertone_lab() → dapatkan undertone
4. Lookup RECOMMENDATION_TABLE[skintone_cat]['undertone_map'][undertone]
5. Untuk setiap nama warna, ambil hex dari COLOR_HEX_REFERENCE, konversi ke RGB
6. Return dict berisi:
   - skin_rgb, skin_hex
   - skintone (dari ITA), undertone
   - ita_value, L_star, b_star
   - harmony (dari tabel)
   - recommended: list of {'name', 'hex', 'rgb'}
   - avoid (dari tabel)
   - reason (dari tabel)
```

**Alasan yang harus ditulis di markdown cell:**
ITA (Individual Typology Angle) adalah standar industri kosmetik dan dermatologi.
Dihitung dari L* (kecerahan) dan b* (yellow-blue) di CIELAB. Lebih presisi dari HSV
brightness karena memperhitungkan komponen undertone (b*), bukan hanya kecerahan.

---

### REVISI 3 — Ubah Fungsi CIEDE2000 dari Evaluasi Diversitas Palet ke Validasi Centroid

**Masalah di kode asli:** Fungsi `evaluate_recommendation_diversity()` mengukur jarak
CIEDE2000 antar warna *rekomendasi* satu sama lain. Ini bukan validasi centroid.

**Yang harus dihapus:**
- Fungsi `evaluate_recommendation_diversity(rec)`
- Semua pemanggilan fungsi tersebut

**Yang harus dibuat sebagai penggantinya:**

Definisikan 6 referensi warna kulit standar:
```python
SKIN_REFERENCE_COLORS = {
    'Very Light (ITA>55)'     : (255, 224, 189),
    'Light (ITA 41-55)'       : (241, 194, 125),
    'Intermediate (ITA 28-41)': (210, 160,  90),
    'Tan (ITA 10-28)'         : (180, 120,  60),
    'Brown (ITA -30 to 10)'   : (130,  80,  35),
    'Dark (ITA<-30)'          : ( 70,  35,  15),
}
```

Buat fungsi `validate_centroids_ciede2000(centroids_rgb, color_space_name='')`:
```
Untuk setiap centroid:
  1. Hitung jarak CIEDE2000 ke semua 6 referensi
  2. Temukan referensi terdekat (min distance)
  3. Tentukan interpretasi berdasarkan nilai:
     < 2   → 'Sangat dekat — tidak terlihat berbeda'
     2–10  → 'Dekat — merepresentasikan warna kulit'
     10–20 → 'Sedang — masih dalam toleransi'
     > 20  → 'JAUH — kemungkinan noise/background'
  4. Klasifikasikan juga via ITA dan undertone
Return: DataFrame dengan kolom:
  Color Space | Cluster | Centroid Hex | ITA (deg) | Skintone (ITA) |
  Undertone | Nearest Reference | CIEDE2000 Distance | Interpretasi
```

Jalankan validasi untuk:
1. Model terbaik saja (tampilkan tabel dan bar chart)
2. Semua color space dan K (tampilkan tabel ringkasan avg CIEDE2000)

Tambahkan tabel interpretasi di markdown:
```
| Nilai CIEDE2000 | Interpretasi                          |
|:---:|---|
| < 2  | Tidak terlihat berbeda oleh mata manusia |
| 2–10 | Perbedaan kecil — centroid valid         |
| 10–20| Perbedaan sedang — masih dalam toleransi |
| > 20 | Kemungkinan noise — perbaiki segmentasi  |
```

Tambahkan peringatan penting di markdown cell:
```
CATATAN: Silhouette/DBI/CHI hanya mengukur struktur cluster, bukan membuktikan
bahwa centroid = warna kulit yang benar secara visual. Validasi CIEDE2000 di cell
ini mengisi celah tersebut dengan membandingkan centroid ke referensi standar.
```

---

### REVISI 4 — Integrasi Dataset Kaggle (Ganti Mode Sintetis)

**Masalah di kode asli:** `USE_SYNTHETIC = False` ada di kode tapi logikanya
hanya mencetak pesan "Mode Manual - pastikan gambar sudah ada". Tidak ada integrasi
nyata dengan dataset.

**Yang harus diubah:**
- Hapus variabel `USE_SYNTHETIC`
- Ubah logika load dataset menjadi:
  1. Coba load dari `DATASET_PATH` terlebih dahulu
  2. Jika folder kosong atau tidak ada → otomatis buat gambar sintetis sebagai fallback
  3. Tampilkan peringatan eksplisit jika fallback diaktifkan:
     `"PERINGATAN: Dataset tidak ditemukan. N gambar sintetis dibuat sebagai fallback."`
     `"Untuk eksperimen nyata, ganti DATASET_PATH dengan dataset Kaggle kamu."`

- Tambahkan markdown cell dengan instruksi cara menggunakan dataset Kaggle:
```markdown
## Cara Menggunakan Dataset Kaggle

1. Mount Google Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
2. Ubah `DATASET_PATH` ke path folder dataset di Drive
3. Dataset yang disarankan:
   - UTKFace (Kaggle) — 20,000+ citra wajah, variasi usia, etnis, gender
   - FairFace (Kaggle) — dirancang untuk keseimbangan ras
   - Dataset wajah multi-etnis lainnya

Spesifikasi minimum dataset untuk penelitian ini:
- Jumlah    : minimal 120 citra wajah
- Variasi   : mencakup skintone very light hingga dark
- Tipe      : indoor dan outdoor
- Format    : JPG atau PNG
- Resolusi  : minimal 100×100 piksel (akan di-resize ke 256×256)
```

---

### REVISI 5 — Struktur Notebook (Markdown Cells & Urutan Section)

Susun notebook dengan urutan cell berikut:

```
[MD]  Title & deskripsi revisi
[MD]  ## 1. Install & Import Library
[CODE] install + import
[MD]  ## 2. Load Dataset
       + instruksi Kaggle
[CODE] load_dataset() + fallback sintetis
[MD]  ## 3. Preprocessing
       + penjelasan CLAHE
[CODE] preprocess_image() + visualisasi before/after
[MD]  ## 4. Deteksi Wajah — Haar Cascade        ← BARU
       + alasan pemilihan, batasan, parameter
[CODE] detect_and_crop_face() + detect_faces_dataset() + visualisasi
[MD]  ## 5. Segmentasi Kulit — Voting 3 Color Space
       + threshold yang digunakan
       + CATATAN: K-Means hanya pada pixel kulit
[CODE] segment_skin_rgb/hsv/ycrcb/combined() + visualisasi
[MD]  ## 6. Ekstraksi Pixel Kulit
[CODE] extract_skin_pixels() + collect_all_skin_pixels() + distribusi plot
[MD]  ## 7. Elbow Method + K-Means Clustering
       + penjelasan penentuan K tetap
[CODE] elbow_method() + fit_kmeans_multiple_k() + visualisasi centroid
[MD]  ## 8. Evaluasi Clustering
       + tabel metrik (arah, keterangan)
       + PERINGATAN: metrik ≠ bukti kebenaran warna
[CODE] evaluate_clustering() + evaluate_all() + plot perbandingan
[MD]  ## 9. Analisis Stabilitas + Pemilihan Model Terbaik
       + rumus composite score
[CODE] compute_cluster_stability() + select_best_model() + ranking chart
[MD]  ## 10. Klasifikasi Skintone — ITA (CIELAB)   ← DIUBAH
        + tabel 6 kategori ITA
        + alasan ITA vs HSV brightness
[CODE] rgb_to_cielab_std() + compute_ita() + classify_skintone_ita()
       + classify_undertone_lab() + demo untuk 3 warna referensi
[MD]  ## 11. Engine Rekomendasi Warna Pakaian       ← DIUBAH
        + RECOMMENDATION_TABLE + COLOR_HEX_REFERENCE
        + CATATAN: tidak menggunakan riwayat pengguna (rule-based)
[CODE] get_clothing_recommendations() + visualize_recommendations()
       + jalankan rekomendasi untuk model terbaik
[MD]  ## 12. Validasi Centroid — CIEDE2000          ← DIUBAH
        + tabel interpretasi nilai CIEDE2000
        + CATATAN: ini berbeda dari evaluasi diversitas palet
[CODE] SKIN_REFERENCE_COLORS + validate_centroids_ciede2000()
       + jalankan validasi model terbaik + ringkasan semua konfigurasi
[MD]  ## 13. Visualisasi Dashboard Komprehensif
[CODE] plot_summary_dashboard() yang menggabungkan:
       - Ranking composite score
       - Elbow curve
       - Silhouette & DBI chart
       - CIEDE2000 validation bar chart  ← BARU di dashboard
       - Palet rekomendasi per cluster (dengan ITA label)
[MD]  ## 14. Testing dengan Gambar User          ← DIPERBARUI (Revisi 6)
       + penjelasan alur pipeline yang digunakan
       + catatan cara upload & format gambar
       + best_cs dan best_k yang digunakan tercantum di markdown
[CODE] predict_skin_and_recommend() yang sudah diperbarui:
       - Haar Cascade di dalam pipeline (dengan fallback)
       - Klasifikasi ITA (bukan classify_skin_tone lama)
       - Validasi CIEDE2000 per gambar user
       - Visualisasi 3 baris: analisis gambar | clustering | rekomendasi dominan
       - Output console ringkasan lengkap
[CODE] files.upload() + loop eksekusi menggunakan best_cs dan best_k
[MD]  Tabel cara membaca hasil (setelah upload cell)
[MD]  ## 15. Kesimpulan
[CODE] print kesimpulan — update agar mencantumkan:
       - Color space terbaik + metrik
       - K terbaik + cara penentuan (Elbow)
       - Peringatan bahwa Silhouette/DBI/CHI hanya ukur struktur cluster
       - Validasi CIEDE2000 sebagai bukti kebenaran centroid
       - Pipeline lengkap dari awal ke akhir
```

---

### REVISI 6 — Perbarui & Perluas Section Testing Gambar User di Akhir Notebook

**Masalah di kode asli:** Fungsi `predict_skin_and_recommend()` masih memanggil
`classify_skin_tone()` (HSV brightness, sudah dihapus), tidak ada Haar Cascade di
pipeline-nya, dan output visualisasinya minim — hanya 3 panel sederhana tanpa
detail ITA, undertone, hex code, atau warna yang dihindari.

**Yang harus diubah pada fungsi `predict_skin_and_recommend()`:**

Perbarui pipeline di dalam fungsi menjadi urutan berikut:
```
1. Load gambar (dari path string atau numpy array)
2. Resize ke TARGET_SIZE
3. Preprocessing: preprocess_image() — CLAHE + Gaussian Blur
4. Deteksi wajah: detect_and_crop_face()
   - Jika wajah terdeteksi → gunakan face_crop sebagai input selanjutnya
   - Jika tidak terdeteksi → gunakan gambar hasil preprocessing langsung
     (fallback) + tampilkan peringatan teks di output
5. Segmentasi kulit: segment_skin_combined()
6. Ekstraksi pixel: extract_skin_pixels() dengan color_space = best_cs
   - Jika pixel < 50 → print pesan error dan return []
7. K-Means clustering: run_kmeans() dengan k = best_k
8. Konversi centroid ke RGB: centroids_rgb_from_space()
9. Untuk setiap centroid → classify_skintone_ita() + classify_undertone_lab()
10. Untuk setiap centroid → get_clothing_recommendations()
11. Tentukan cluster dominan: np.bincount(labels).argmax()
12. Hitung CIEDE2000 centroid dominan vs SKIN_REFERENCE_COLORS
    → ambil min distance dan nearest reference
```

**Output visualisasi yang harus ditampilkan jika verbose=True:**

**Panel Baris 1 — Analisis Gambar (4 panel, 1 baris):**
```
Panel 1: Gambar original (RGB)
         Judul: "Input Gambar"

Panel 2: Gambar dengan bounding box wajah (rect merah) jika terdeteksi,
         atau gambar original dengan teks "Face not detected (fallback)"
         Judul: "Deteksi Wajah (Haar Cascade)"

Panel 3: Gambar hasil crop wajah yang diproses
         (face_crop setelah resize, atau gambar fallback)
         Judul: "Face Crop"

Panel 4: Overlay segmentasi kulit — area non-kulit jadi abu-abu [220,220,220]
         Judul: f"Segmentasi Kulit\n({pct:.1f}% pixel kulit)"
```

**Panel Baris 2 — Hasil Clustering (1 panel lebar):**
```
Tampilkan semua centroid sebagai strip warna (masing-masing 80px lebar)
Di bawah setiap strip, tampilkan teks:
  - Hex code centroid
  - Skintone category (dari ITA)
  - Nilai ITA (misal: ITA=+32.1°)
  - Undertone
  - Label "★ DOMINAN" dengan warna merah untuk cluster dominan
Judul: f"Warna Kulit Terdeteksi — {best_cs}, K={actual_k}"
```

**Panel Baris 3 — Hasil Rekomendasi Cluster Dominan (1 panel lebar):**
```
Tampilkan palet warna dalam satu strip horizontal:
  - Kotak pertama (lebih lebar, 100px): warna kulit dominan
    Label: "KULIT\n{hex}\n{skintone}\nITA={ita}°"
  - Divider visual (garis vertikal putih 4px)
  - Kotak berikutnya (60px tiap warna): setiap warna rekomendasi
    Label di bawah: nama warna (maks 10 karakter) + hex code

Di bawah strip warna, tampilkan teks:
  "Undertone  : {undertone}"
  "Harmoni    : {harmony}"
  "Rekomendasi: {nama_warna_1} · {nama_warna_2} · {nama_warna_3} · {nama_warna_4}"
  "Hindari    : {avoid}"
  "Alasan     : {reason}"

Judul panel: f"Rekomendasi Warna Pakaian — {skintone}, {undertone}"
```

**Setelah semua panel, tampilkan teks ringkasan ke console:**
```
============================================================
   HASIL ANALISIS — [nama file]
============================================================
Color Space    : {best_cs}
K              : {best_k}
Cluster Dominan: {dominant_idx + 1} dari {best_k}

Warna Kulit    : {skin_hex}
Skintone (ITA) : {skintone} (ITA = {ita_value:+.1f}°)
Undertone      : {undertone}
L*             : {L_star:.1f}  |  b* : {b_star:.1f}

Validasi CIEDE2000:
  Referensi terdekat : {nearest_ref}
  Jarak CIEDE2000    : {min_dist:.2f}
  Interpretasi       : {interpretasi}

Rekomendasi Warna Pakaian:
  1. {nama_1}  {hex_1}
  2. {nama_2}  {hex_2}
  3. {nama_3}  {hex_3}
  4. {nama_4}  {hex_4}

Warna yang Dihindari:
  {avoid}

Alasan Rekomendasi:
  {reason}
============================================================
```

**Bagian upload dan eksekusi testing** — ganti kode lama dengan ini:

```python
# ── Upload dan jalankan testing ──────────────────────────────
print("Unggah gambar wajah kamu dari komputer untuk dianalisis:")
print("(Format: JPG, PNG — pastikan wajah terlihat jelas dan frontal)\n")

uploaded = files.upload()

for fn in uploaded.keys():
    print(f'\nMemproses: "{fn}"')
    recs = predict_skin_and_recommend(
        fn,
        color_space=best_cs,   # gunakan color space terbaik dari eksperimen
        k=best_k,              # gunakan K terbaik dari eksperimen
        verbose=True
    )
    if not recs:
        print("Tidak ada rekomendasi yang dihasilkan. Pastikan gambar menampilkan wajah frontal.")
```

**Tambahkan markdown cell sebelum cell upload** dengan konten berikut:
```markdown
## 🧪 Testing dengan Gambar User

Bagian ini menjalankan pipeline lengkap pada gambar wajah yang diunggah langsung
oleh pengguna, menggunakan **color space dan nilai K terbaik** yang ditemukan
dari eksperimen pada dataset.

**Alur proses:**
Input Gambar → CLAHE Preprocessing → Haar Cascade (face detection)
→ Skin Masking (voting RGB+HSV+YCrCb) → K-Means ({best_cs}, K={best_k})
→ Klasifikasi ITA (CIELAB) → Rekomendasi Warna (rule-based)
→ Validasi CIEDE2000

**Catatan penggunaan:**
- Unggah foto wajah tampak depan (frontal) dengan pencahayaan cukup
- Ekspresi natural (bukan ekspresi ekstrem)
- Format: JPG atau PNG
- Jika wajah tidak terdeteksi oleh Haar Cascade, sistem akan tetap berjalan
  menggunakan seluruh gambar sebagai fallback dengan peringatan
- Hasil menggunakan model terbaik: color space **{best_cs}**, K = **{best_k}**
```

**Tambahkan markdown cell SESUDAH cell upload** untuk menjelaskan output:
```markdown
### Cara Membaca Hasil

| Elemen Output | Penjelasan |
|---|---|
| Deteksi Wajah | Bounding box merah menandai area wajah yang dideteksi Haar Cascade |
| Segmentasi Kulit | Area abu-abu = bukan kulit. Area berwarna = pixel yang dianalisis |
| Strip Centroid | Setiap kotak = satu cluster warna kulit. Bintang (★) = cluster dominan |
| ITA (°) | Nilai positif besar = kulit sangat terang. Nilai negatif = kulit gelap |
| Palet Rekomendasi | Kotak pertama = warna kulit kamu. Kotak berikutnya = rekomendasi pakaian |
| CIEDE2000 | Jarak ke referensi standar. < 10 = centroid valid merepresentasikan warna kulit |
| Hindari | Warna pakaian yang sebaiknya dihindari untuk skintone ini |
```

---

### CATATAN TEKNIS PENTING

1. **Numpy patch untuk colormath** — pastikan ada di awal kode setelah import:
   ```python
   if not hasattr(np, 'asscalar'):
       np.asscalar = lambda x: x.item()
   ```

2. **Konversi centroid ke RGB** — fungsi `centroids_rgb_from_space()` yang sudah ada
   di kode asli tetap digunakan, tidak perlu diubah.

3. **Dataset variable** — setelah deteksi wajah (Revisi 1), gunakan `face_dataset`
   sebagai input ke segmentasi (bukan `preprocessed_dataset`).

4. **Temperature output** — semua output klasifikasi harus konsisten menggunakan
   kategori ITA (Very Light/Light/Intermediate/Tan/Brown/Dark), bukan kategori
   Fitzpatrick lama (Very Fair/Fair/Medium/Olive/Brown/Dark).

5. **File output** — simpan hasil sebagai file `.ipynb` yang bisa langsung dibuka
   di Google Colab.

6. **Testing section** — fungsi `predict_skin_and_recommend()` harus menggunakan
   `best_cs` dan `best_k` yang sudah ditentukan dari eksperimen dataset di atas.
   Ini penting: user mendapat rekomendasi dari model yang sudah divalidasi,
   bukan dari model dengan parameter arbitrary. Jangan hardcode nilai K atau
   color space di dalam fungsi ini — selalu ambil dari `best_cs` dan `best_k`.

7. **Fallback face detection di testing** — berbeda dari pipeline dataset (yang
   men-skip gambar jika wajah tidak terdeteksi), pipeline testing untuk user
   TIDAK boleh men-skip. Jika wajah tidak terdeteksi, tetap lanjutkan dengan
   gambar hasil preprocessing dan tampilkan peringatan, karena user sudah
   menunggu hasil.

---

### FORMAT OUTPUT YANG DIHARAPKAN

- File: `skin_color_recommendation_revised.ipynb`
- Setiap section dipisahkan dengan markdown cell yang jelas
- Setiap fungsi baru dilengkapi docstring
- Komentar inline di bagian yang direvisi menjelaskan apa yang berubah
- Notebook harus bisa dijalankan dari atas ke bawah tanpa error (Run All)

