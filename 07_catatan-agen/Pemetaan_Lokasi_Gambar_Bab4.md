# Pemetaan Lokasi Penyisipan Gambar — BAB IV Hasil dan Pembahasan

Urutan di bawah ini mengikuti urutan sub-bab di file `Skripsi_bab_1-5_M_Raihan_latest.md`, dari awal Bab IV sampai akhir. Tinggal scroll dokumen Word Anda dari atas ke bawah dan tempel gambar satu per satu sesuai urutan ini.

---

### 📍 Sub-bab 4.1 — Gambaran Umum Implementasi Sistem

**Gambar 4.1** — Lingkungan Pengembangan Sistem Komputasi pada Google Colaboratory
> ❌ **Tidak tersedia di paket ZIP.** Ambil screenshot manual dari sesi Colab Anda sendiri (tampilan import library / eksekusi kode).

**Gambar 4.2** — Sampel Dataset Citra Wajah dengan Variasi *Skintone* dan Kondisi Pencahayaan
> ✅ `Gambar4.2_Sampel_Dataset_Wajah.png`

---

### 📍 Sub-bab 4.2.1 — Hasil Deteksi dan Cropping Wajah

**Gambar 4.1** — Hasil Deteksi dan *Cropping* Wajah Menggunakan *Haar Cascade Classifier*
> ✅ `Gambar4.1_Hasil_Deteksi_Cropping_Wajah.png`

---

### 📍 Sub-bab 4.2.2 — Hasil Preprocessing dan Normalisasi Citra

**Gambar 4.1** — Perbandingan Kualitatif Visual Citra Wajah Asli dan Hasil Prapemrosesan (*Gaussian Blur* dan CLAHE)
> ✅ `Gambar4.x_Preprocessing_CLAHE_Gaussian.png`

**Gambar 4.x** — Perbandingan Visual *Skin Mask* Independen, *Mask* Gabungan (*Majority Voting*), dan Hasil *Overlay* Segmentasi Kulit Wajah
> ✅ Pilih salah satu (atau tampilkan ketiganya berurutan sebagai Gambar 4.x, 4.x+1, 4.x+2):
> - `Gambar4.x_Segmentasi_Mask_Sampel1.png`
> - `Gambar4.x_Segmentasi_Mask_Sampel2.png`
> - `Gambar4.x_Segmentasi_Mask_Sampel3.png`

**Gambar 4.x** — Diagram Alur Perbedaan Arsitektur Penanganan Kegagalan Deteksi Wajah pada Level Dataset dan Prediksi Individual
> ✅ `Gambar4.x_Diagram_Alur_Fallback_Dataset_vs_Individual.png`

---

### 📍 Sub-bab 4.3 — Hasil Penentuan Jumlah Cluster (K) Optimal

**Gambar 4.x** — Grafik *Elbow Method* pada Ruang Warna RGB untuk Penentuan Estimasi Awal Nilai *K*
> ✅ `Gambar4.x_Elbow_Method_RGB.png`

---

### 📍 Sub-bab 4.4.1 — Hasil Skenario S1 (Ruang Warna RGB)

**Gambar 4.1** — Visualisasi Klaster dan Palet *Centroid* Kulit Wajah pada Ruang Warna RGB (Skenario S1)
> ✅ `Gambar4.1_Palet_Centroid_RGB_K357.png`
> ⚠️ Catatan: file ini menampilkan palet centroid untuk K=3, K=5, **dan** K=7 sekaligus dalam satu gambar. Jika ingin fokus K=3 saja sesuai skenario S1, Anda bisa crop bagian "RGB K=3" saja saat menempel ke Word.

---

### 📍 Sub-bab 4.4.2 — Hasil Skenario S2 (Ruang Warna HSV)

**Gambar 4.2** — Visualisasi Klaster dan Palet *Centroid* Kulit Wajah pada Ruang Warna HSV (Skenario S2)
> ✅ `Gambar4.2_Palet_Centroid_HSV_K357.png` (sama, ambil bagian "HSV K=3" jika ingin spesifik)

---

### 📍 Sub-bab 4.4.3 — Hasil Skenario S3 (Ruang Warna CIELAB)

**Gambar 4.3** — Visualisasi Klaster dan Palet *Centroid* Kulit Wajah pada Ruang Warna CIELAB (Skenario S3)
> ✅ `Gambar4.3_Palet_Centroid_LAB_K357.png` (ambil bagian "LAB K=3" jika ingin spesifik)

---

### 📍 Sub-bab 4.5.1 — (bagian sebelum 4.5.2, tren metrik clustering)

**Gambar 4.x** — Grafik Perbandingan Tren Kualitas *Clustering* (Silhouette, DBI, CHI) terhadap Kenaikan Nilai *K* Lintas *Color Space*
> ✅ `Gambar4.x_Tren_Silhouette_DBI_CHI_vs_K.png`

---

### 📍 Sub-bab 4.5.2 — Hasil Analisis Stabilitas Klaster

**Gambar 4.x** — Perbandingan Visual Tingkat *Stability Score* Lintas Ruang Warna Berdasarkan Nilai Konfigurasi *K*
> ✅ `Gambar4.x_Stability_Score_per_ColorSpace_K.png`

---

### 📍 Sub-bab 4.5.3 — Skor Komposit dan Ranking Color Space Terbaik

**Gambar 4.x** — Grafik Batang Perbandingan *Composite Score* pada 9 Kombinasi *Color Space* dan Konfigurasi *K*
> ✅ `Gambar4.x_Ranking_Composite_Score_9Kombinasi.png`

---

### 📍 Sub-bab 4.6 — Hasil Klasifikasi Skintone dan Undertone

**Gambar 4.x** — Visualisasi Palet Warna *Centroid* Dominan Beserta Hasil Klasifikasi Kategori ITA dan *Undertone*
> ✅ `Gambar4.x_Dashboard_Komprehensif_RM1-RM4.png` → ambil **panel paling bawah saja** ("Palet Rekomendasi per Cluster dengan Label ITA") jika ingin gambar fokus, atau gunakan `Gambar4.x_Validasi_CIEDE2000.png` sebagai pelengkap pembahasan ITA+validasi.
> ⚠️ Tidak ada gambar berdiri sendiri persis untuk ini di notebook — panel ini adalah bagian dari dashboard komprehensif. Anda bisa crop bagian bawah dashboard saat menempel.

---

### 📍 Sub-bab 4.7.1 — Pemetaan Skintone–Undertone ke Palet Warna

**Gambar 4.x** — Visualisasi Matriks Pemetaan Palet Warna Pakaian Berdasarkan Klasifikasi Kategori *Skintone* dan *Undertone*
> ✅ `Gambar4.x_Matriks_Palet_Skintone_Undertone.png`

**Gambar 4.x** — Visualisasi Luaran Antarmuka Sistem yang Menampilkan Ketiga Klaster Sentroid Dataset Beserta Rekomendasi Palet Warnanya
> ✅ Tiga cluster, tempel berurutan (atau gabung jadi 1 figure 3-panel):
> - `Gambar4.x_Rekomendasi_Cluster1.png`
> - `Gambar4.x_Rekomendasi_Cluster2.png`
> - `Gambar4.x_Rekomendasi_Cluster3.png`

**Gambar 4.y** — Luaran Prediksi dan Rekomendasi Sistem pada Skenario Pengujian Gambar Pengguna Individual
> ✅ Tiga gambar berurutan menunjukkan satu alur testing end-to-end:
> 1. `Gambar4.y_Testing_User_Pipeline.png` (input → deteksi → crop → segmentasi)
> 2. `Gambar4.y_Testing_User_WarnaKulitTerdeteksi.png` (palet warna kulit terdeteksi + ITA)
> 3. `Gambar4.y_Testing_User_HasilRekomendasi.png` (hasil rekomendasi pakaian akhir)

---

### 📍 Sub-bab 4.8.4 — Validasi Jarak Perseptual CIEDE2000 dan Trade-off Akurasi

**Gambar 4.x** — Diagram Sintesis Evaluasi Pipeline dan Multi-Color Space (diagram ringkasan keterkaitan RM1–RM4)
> ✅ `Gambar4.x_Dashboard_Komprehensif_RM1-RM4.png` (gunakan gambar **utuh/lengkap** di sini, sebagai gambar penutup pembahasan)
> 💡 Anda juga bisa sisipkan `Gambar4.x_Validasi_CIEDE2000.png` sebagai pendukung khusus pembahasan CIEDE2000 di sub-bab ini, sebelum diagram sintesis.

---

## Ringkasan Urutan Penempelan (top → bottom)

| No | Sub-bab | File |
|---|---|---|
| 1 | 4.1 | *(screenshot manual Colab)* |
| 2 | 4.1 | Gambar4.2_Sampel_Dataset_Wajah.png |
| 3 | 4.2.1 | Gambar4.1_Hasil_Deteksi_Cropping_Wajah.png |
| 4 | 4.2.2 | Gambar4.x_Preprocessing_CLAHE_Gaussian.png |
| 5 | 4.2.2 | Gambar4.x_Segmentasi_Mask_Sampel1/2/3.png |
| 6 | 4.2.2 | Gambar4.x_Diagram_Alur_Fallback_Dataset_vs_Individual.png |
| 7 | 4.3 | Gambar4.x_Elbow_Method_RGB.png |
| 8 | 4.4.1 | Gambar4.1_Palet_Centroid_RGB_K357.png |
| 9 | 4.4.2 | Gambar4.2_Palet_Centroid_HSV_K357.png |
| 10 | 4.4.3 | Gambar4.3_Palet_Centroid_LAB_K357.png |
| 11 | 4.5.1 | Gambar4.x_Tren_Silhouette_DBI_CHI_vs_K.png |
| 12 | 4.5.2 | Gambar4.x_Stability_Score_per_ColorSpace_K.png |
| 13 | 4.5.3 | Gambar4.x_Ranking_Composite_Score_9Kombinasi.png |
| 14 | 4.6 | Gambar4.x_Dashboard_Komprehensif_RM1-RM4.png (crop panel bawah) atau Gambar4.x_Validasi_CIEDE2000.png |
| 15 | 4.7.1 | Gambar4.x_Matriks_Palet_Skintone_Undertone.png |
| 16 | 4.7.1 | Gambar4.x_Rekomendasi_Cluster1/2/3.png |
| 17 | 4.7.1 | Gambar4.y_Testing_User_Pipeline/WarnaKulitTerdeteksi/HasilRekomendasi.png |
| 18 | 4.8.4 | Gambar4.x_Dashboard_Komprehensif_RM1-RM4.png (gambar utuh) |

**Total: 21 gambar dari ZIP digunakan di 17 titik penyisipan + 1 yang harus Anda screenshot manual.**
