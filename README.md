# Skripsi M. Raihan — Sistem Rekomendasi Fashion Berbasis Skin Tone

**Judul:** Sistem Rekomendasi Warna Fashion Berbasis Analisis Warna Kulit Menggunakan K-Means Clustering  
**Penulis:** M. Raihan  
**Program Studi:** Sistem Informasi  
**Tahun:** 2026

---

## Navigasi Cepat

| Folder | Isi | Frekuensi Akses |
|--------|-----|-----------------|
| [01_dokumen-skripsi/](./01_dokumen-skripsi/) | Draft & dokumen resmi skripsi | ⭐⭐⭐ Sering |
| [02_kode-program/](./02_kode-program/) | Notebook Jupyter & skrip Python | ⭐⭐⭐ Sering |
| [03_dataset/](./03_dataset/) | Dataset wajah, fashion, skin tone | ⭐⭐ Sedang |
| [04_gambar-skripsi/](./04_gambar-skripsi/) | Gambar & ilustrasi untuk BAB 4 | ⭐⭐ Sedang |
| [05_referensi/](./05_referensi/) | Jurnal & paper ilmiah | ⭐⭐ Sedang |
| [06_presentasi/](./06_presentasi/) | File PowerPoint presentasi | ⭐ Jarang |
| [07_catatan-agen/](./07_catatan-agen/) | Catatan & prompt dari sesi AI | ⭐ Jarang |

---

## Detail Setiap Folder

### 📄 01_dokumen-skripsi/ — (16 file)
Berisi semua dokumen tulisan skripsi dalam format Word (.docx) dan PDF.

```
01_dokumen-skripsi/
├── draft/          ← Semua versi draft BAB 1-5 (.docx) — 11 file
├── final/          ← PDF final yang sudah dikumpulkan — 1 file
└── _arsip/         ← File backup, AutoRecovered, & panduan — 4 file
```

**File terpenting:**
- `draft/Skripsi bab 1-5 M.Raihan latest revisi banget.docx` — **versi terbaru & terlengkap**
- `draft/Skripsi bab 1-5 M.Raihan latest.docx` — versi stabil terakhir
- `draft/Ringkasan_Hasil_Notebook_Skripsi.docx` — ringkasan hasil eksperimen
- `final/Skripsi bab 1-3 M.Raihan.pdf` — PDF yang sudah dikumpulkan
- `_arsip/Panduan Skripsi - SI - 2026.pdf` — panduan resmi dari kampus

---

### 💻 02_kode-program/ — (8 file)
Berisi semua kode implementasi sistem rekomendasi.

```
02_kode-program/
├── notebook/   ← File .ipynb (Google Colab / Jupyter) — 6 file
└── python/     ← File .py (skrip Python terstruktur) — 2 file
```

**File terpenting:**
- `notebook/skin_color_recommendation_(newest).ipynb` — **notebook utama terbaru**
- `notebook/skin_color_recommendation_revised_structured.ipynb` — versi terstruktur final
- `notebook/skin_color_recommendation (newest).ipynb - Colab.pdf` — versi PDF untuk lampiran
- `python/skin_color_recommendation_revised.py` — skrip Python versi revisi
- `python/skin_color_recommendation.py` — skrip Python versi awal

---

### 🗂️ 03_dataset/ — (39,560 file)
Berisi semua data mentah dan terproses yang digunakan dalam penelitian.

```
03_dataset/
├── wajah/                  ← Foto wajah untuk deteksi skin tone (UTKFace)
│   ├── [160 file .jpg]     ← Dataset wajah utama
│   └── part3/              ← Bagian tambahan dataset wajah
├── fashion/                ← Dataset gambar pakaian fashion
│   ├── berlabel/           ← Fashion dengan label kategori skin tone
│   │   ├── dark/
│   │   ├── light/
│   │   ├── mid-dark/
│   │   └── mid-light/
│   └── tidak-berlabel/     ← Fashion tanpa label (untuk augmentasi)
│       ├── dark/
│       ├── light/
│       ├── mid-dark/
│       └── mid-light/
└── skintone/               ← Dataset referensi warna kulit
    ├── dark/
    ├── light/
    ├── mid-dark/
    └── mid-light/
```

> **Catatan:** Dataset ini berukuran besar (~39 ribu file). Jangan dipindah atau diganti nama tanpa memperbarui path di notebook.

---

### 🖼️ 04_gambar-skripsi/ — (30 file)
Berisi gambar-gambar yang digunakan sebagai ilustrasi dalam dokumen skripsi.

```
04_gambar-skripsi/
├── bab4/       ← Gambar hasil eksperimen & analisis BAB 4 — 24 file
│   └── _arsip/ ← ZIP backup gambar BAB 4
└── aset-ai/    ← Gambar yang di-generate dengan AI Gemini — 5 file
```

**Gambar BAB 4 yang sudah bernomor:**
- `Gambar4.1_Hasil_Deteksi_Cropping_Wajah.png`
- `Gambar4.1_Palet_Centroid_RGB_K357.png`
- `Gambar4.2_Palet_Centroid_HSV_K357.png`
- `Gambar4.2_Sampel_Dataset_Wajah.png`
- `Gambar4.x_Preprocessing_CLAHE_Gaussian.png`
- `Gambar4.x_Matriks_Palet_Skintone_Undertone.png`
- `Gambar4.x_Dashboard_Komprehensif_RM1-RM4.png`
- Dan 17 gambar lainnya...

---

### 📚 05_referensi/ — (26 file)
Berisi jurnal ilmiah dan paper yang dijadikan referensi penelitian.

```
05_referensi/
├── utama/      ← 16 jurnal referensi utama (dari folder referensi/)
└── tambahan/   ← 10 jurnal referensi tambahan (dari referensi/new/)
```

**Referensi utama kunci:**
- `Real_Time_Skin_Color_Detection_Based_on_Adaptive_HSV_Thresholding.pdf`
- `Unsupervised_K_Means_Clustering_Algorithm.pdf`
- `Color_Feature_Based_Dominant_Color_Extraction.pdf`
- `Three-Way_Clustering_Based_on_Digital_Image_Processing.pdf`
- `Skin Research and Technology - 2024 - Jung - Skin Tone Analysis...pdf`

---

### 🎤 06_presentasi/ — (1 file)
Berisi file PowerPoint untuk presentasi sidang skripsi.

- `Skin_Tone_Fashion_Recommendation_System_(2).pptx`

---

### 📝 07_catatan-agen/ — (6 file)
Berisi file Markdown yang merupakan catatan & hasil kerja sesi AI Agent.

| File | Keterangan |
|------|------------|
| `Agent_Dosen_Pembimbing_Raihan.md` | Catatan sesi simulasi dosen pembimbing |
| `Kerangka_BAB_IV_Revisi.md` | Kerangka BAB IV hasil revisi |
| `Pemetaan_Lokasi_Gambar_Bab4.md` | Pemetaan posisi gambar di BAB 4 |
| `PROMPT_REVISI_NOTEBOOK.md` | Prompt yang digunakan untuk revisi notebook |
| `Skripsi bab 1-3 M.Raihan.md` | Versi Markdown dari skripsi BAB 1-3 |
| `hasil revisi dosen pembimbing skripsi 1-3.md` | Hasil revisi format MD |

---

## Teknologi yang Digunakan

| Komponen | Teknologi |
|----------|-----------|
| Bahasa Pemrograman | Python 3.x |
| Lingkungan | Google Colab / Jupyter Notebook |
| Library Utama | OpenCV, scikit-learn, NumPy, Matplotlib |
| Algoritma | K-Means Clustering, CLAHE, HSV Thresholding |
| Dataset Wajah | UTKFace Dataset |
| Ruang Warna | RGB, HSV, LAB (dibandingkan) |

---

## Alur Sistem (Ringkas)

```
Input Foto Wajah
      |
      v
Deteksi & Cropping Wajah (Haar Cascade / MediaPipe)
      |
      v
Preprocessing (CLAHE + Gaussian Blur)
      |
      v
Segmentasi Kulit (HSV Masking)
      |
      v
Ekstraksi Warna Dominan (K-Means, K=3/5/7)
      |
      v
Evaluasi: Silhouette Score, DBI, CHI
      |
      v
Klasifikasi Skin Tone (dark / mid-dark / mid-light / light)
      |
      v
Output: Rekomendasi Warna Pakaian Fashion
```

---

*Folder ini dirapihkan secara otomatis pada 2026-06-27 menggunakan Antigravity AI Agent.*  
*Total: 39,647 file teroganisasi dalam 7 folder utama.*
