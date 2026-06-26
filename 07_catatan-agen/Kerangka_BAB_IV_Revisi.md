# KERANGKA BAB IV (REVISI SESUAI DATA AKTUAL NOTEBOOK)

## Catatan Perbaikan Sebelum Kerangka

Dibanding kerangka sebelumnya, ada beberapa perubahan struktural penting karena dicocokkan langsung dengan kode dan output `skin_color_recommendation__newest_.ipynb`:

| # | Masalah pada kerangka lama | Perbaikan |
|---|---|---|
| 1 | Menyebut "Hasil Evaluasi Waktu Komputasi" (4.5.2) | **Dihapus total** — tidak ada satu baris kode pun yang mengukur waktu eksekusi di notebook. Sesuai arahan Anda, ini ditangani terpisah di Tabel 3.5 BAB III, bukan di BAB IV. |
| 2 | Composite score digambarkan hanya dari Silhouette+DBI+CHI+Waktu | Komposisi sebenarnya: **Silhouette (35%) + DBI (25%) + CHI (20%) + Stability Score (20%)**. Stability Score disebut sebagai bagian dari formula tanpa diuraikan detail teknisnya. |
| 3 | K diuji pada rentang luas (mengisyaratkan elbow penuh K=2..10 untuk ketiga color space) | Faktanya: Elbow Method penuh (`range(2,11)`) **hanya dijalankan untuk RGB**, menghasilkan rekomendasi K=4. Tiga color space lalu dibandingkan langsung pada **K kandidat [3, 5, 7]** saja — bukan hasil elbow tiap color space. |
| 4 | minNeighbors Haar Cascade ditulis 6 | Kode aktual: **minNeighbors=5**. |
| 5 | CIEDE2000 digambarkan ada kasus "out of tolerance" pada rata-rata model terbaik | Faktanya: rata-rata CIEDE2000 dataset untuk RGB K=3 (model terbaik) = **10,530**, kategori "Sedang – masih dalam toleransi" untuk ketiga cluster. Yang "JAUH" (24,066) hanya terjadi pada **satu sampel uji gambar pengguna tunggal** di luar dataset, bukan rata-rata model. |
| 6 | Tidak ada pembahasan bahwa HSV punya Stability Score = 0 (anomali) | Ditambahkan sebagai temuan yang perlu dibahas — Stability Score 0,0 untuk HSV K=3 dan K=5 kemungkinan artefak konversi warna, bukan stabilitas sempurna. |
| 7 | 4.6–4.9 (klasifikasi skintone detail, output lengkap, Streamlit, pembahasan RM1-RM4) belum ada di draf | Ditambahkan kembali sebagai sub-bab, kali ini dengan slot data yang cocok dengan struktur notebook (Section 10-14). |

---

## KERANGKA BAB IV YANG DISARANKAN

### 4.1 Gambaran Umum Implementasi Sistem
*(tidak banyak berubah dari draf — sudah cocok dengan data: OpenCV 4.13.0, NumPy 2.0.2, 120 sampel, sumber Kaggle "Dataset Skin Tone")*

- Lingkungan: Google Colab, Python, OpenCV 4.13.0, NumPy 2.0.2, Scikit-Learn, colormath, Streamlit
- Dataset: 120 citra wajah, ukuran standar 256×256, sumber Kaggle "Dataset Skin Tone" [26]
- Variasi skintone: very light–dark (kategori ITA), variasi indoor/outdoor

### 4.2 Hasil Preprocessing dan Segmentasi Kulit

#### 4.2.1 Hasil Deteksi dan Cropping Wajah
- Parameter Haar Cascade: scaleFactor=1.1, **minNeighbors=5** (koreksi dari 6), minSize=(60,60), padding=0.15
- Hasil: **97 dari 120 gambar berhasil dideteksi**, **23 di-skip**
- Aturan fallback level-dataset: jika gambar gagal >50% dari total, seluruh dataset preprocessing dipakai langsung tanpa cropping (pada eksperimen ini kondisi tersebut TIDAK terpicu karena rasio gagal hanya 23/120 ≈ 19%)

#### 4.2.2 Hasil Preprocessing dan Normalisasi Citra
- CLAHE pada kanal L* CIELAB, clipLimit=2.0, tileGridSize=(8,8)
- Gaussian Blur kernel 5×5
- (Tetap kualitatif — tidak ada data histogram numerik before/after di notebook)

#### 4.2.3 Hasil Segmentasi Area Kulit
- Metode: majority voting 3 ruang warna — **RGB, HSV, YCrCb** (bukan RGB+HSV+CIELAB; LAB dipakai untuk ekstraksi pixel/clustering, bukan untuk threshold segmentasi)
- Aturan ambang batas SUDAH ADA datanya di notebook, bisa dikutip langsung:
  - RGB: R>95, G>40, B>20, R>G, R>B, |R-G|>15
  - HSV: rentang Hue kulit ganda (0-25 dan 160-179), Saturation 25-180, Value 70-255
  - YCrCb: Cr 133-173, Cb 77-127
- Voting: piksel jadi kulit jika lolos minimal 2 dari 3 aturan
- Morphological cleanup: opening + closing kernel 5×5
- **Hasil kuantitatif: total 3.363.613 piksel kulit valid** terekstraksi dari 97 sampel wajah terdeteksi (sama jumlahnya di RGB, HSV, LAB karena piksel sumbernya identik, hanya representasi warnanya berbeda)

#### 4.2.4 Penanganan Fallback Deteksi Wajah
- Dua pipeline berbeda: pipeline dataset (boleh skip) vs pipeline prediksi pengguna (`predict_skin_and_recommend`, wajib fallback)
- Pada pipeline live prediction: jika `detect_and_crop_face` mengembalikan None, sistem otomatis memakai *gambar hasil preprocessing utuh* sebagai pengganti area wajah (bukan data sintetis acak — ini detail yang perlu dikoreksi dari draf lama)
- Contoh nyata fallback INI YANG SUDAH TEREKAM: pada pengujian gambar pengguna (Section 14), `Face detected: True` — fallback tidak terpicu pada sampel uji yang tersimpan, sehingga tidak ada contoh visual fallback aktif yang tersimpan di notebook. **[Perlu diuji manual dengan gambar yang sengaja sulit dideteksi jika ingin menampilkan Gambar 4.6 kasus fallback aktif]**

### 4.3 Hasil Penentuan Jumlah Cluster (K) Optimal

- Elbow Method dijalankan pada sampel 4.000 piksel dari RGB saja (representatif, bukan keseluruhan 3,3 juta piksel — alasan efisiensi komputasi)
- Hasil: **Elbow Method merekomendasikan K=4** untuk RGB
- Namun: kandidat final yang **benar-benar diuji lintas tiga color space** adalah **K ∈ {3, 5, 7}** — bukan rentang elbow penuh
- Tabel Inertia (WCSS) hasil aktual:

| Color Space | K=3 | K=5 | K=7 |
|---|---|---|---|
| RGB | 7.406.524,00 | 4.254.135,50 | 3.281.391,75 |
| HSV | 12.162.169,00 | 7.470.458,00 | 5.620.293,00 |
| LAB | 2.514.213,25 | 1.447.773,50 | 1.120.766,38 |

- Justifikasi K=3 dipilih sebagai final: **bukan dari elbow (yang menyarankan K=4)**, melainkan dari composite score yang mempertimbangkan Silhouette, DBI, CHI, dan Stability secara bersamaan (dijelaskan di 4.5)
- **Perlu narasi eksplisit yang menjelaskan KONTRADIKSI ini secara akademik**: elbow=4 vs composite-terbaik=3, dan kenapa composite score yang dijadikan keputusan akhir

### 4.4 Hasil Eksperimen Clustering pada Tiga Skenario Color Space

Centroid yang ditampilkan HARUS yang K=3 (karena ini konfigurasi final), bukan rata K=3/5/7 sekaligus. Centroid K=3 aktual:

#### 4.4.1 Skenario S1 (RGB, K=3)
- Centroid: **#AF7F68** (Tan/Cool), **#6A4638** (Dark/Cool), **#E7BDA5** (Very Light/Neutral)
- Inertia: 7.406.524,00
- Silhouette=0,4784 | DBI=0,6783 | CHI=6.951,57

#### 4.4.2 Skenario S2 (HSV, K=3)
- Centroid RGB-equivalent: **perlu dikonversi ulang dari HSV** — catatan: dokumen draf lama menulis #7B5343/#D9AA92/#905F69 untuk HSV, ini PERLU DIVERIFIKASI ulang dari notebook karena saya tidak menemukan print eksplisit untuk centroid HSV K=3 di output yang tersimpan (hanya tersedia untuk RGB, model terbaik). **[Jalankan ulang `plot_centroids(results_hsv, "HSV")` dan catat angka HEX-nya sebelum menulis sub-bab ini]**
- Inertia: 12.162.169,00 (tertinggi di antara ketiganya — mengindikasikan klaster HSV paling longgar/tidak kompak)
- Silhouette=0,4461 | DBI=0,7986 | CHI=2.589,12 (CHI jauh lebih rendah dari RGB/LAB)

#### 4.4.3 Skenario S3 (CIELAB, K=3)
- Centroid: **#E6BDA3, #694538, #AB7D67** (sesuai draf, ini sudah benar)
- Inertia: 2.514.213,25 (**terendah** — bukan berarti terbaik secara struktur, karena skala unit LAB ≠ skala unit RGB/HSV sehingga inertia TIDAK BISA dibandingkan lintas color space secara langsung; ini penting ditegaskan agar tidak salah baca)
- Silhouette=0,4769 | DBI=0,6770 | CHI=6.972,03

### 4.5 Hasil Evaluasi dan Perbandingan Performa Color Space

#### 4.5.1 Hasil Evaluasi Struktur Clustering (K=3, K=5, K=7 — seluruh kandidat, bukan hanya K=3)

**Tabel 4.1 Hasil Evaluasi Struktur Clustering per Color Space dan K**

| Color Space | K | Silhouette | DBI | CHI |
|---|---|---|---|---|
| RGB | 3 | 0,4784 | 0,6783 | 6.951,57 |
| RGB | 5 | 0,3759 | 0,8436 | 6.547,56 |
| RGB | 7 | 0,3100 | 1,0033 | 5.775,46 |
| HSV | 3 | 0,4461 | 0,7986 | 2.589,12 |
| HSV | 5 | 0,3774 | 0,8460 | 2.602,26 |
| HSV | 7 | 0,3631 | 0,7928 | 2.502,81 |
| LAB | 3 | 0,4769 | 0,6770 | 6.972,03 |
| LAB | 5 | 0,3707 | 0,8494 | 6.535,20 |
| LAB | 7 | 0,3085 | 1,0035 | 5.768,30 |

*(Data ini PERSIS dari output `df_eval`, sudah lengkap dan tidak butuh placeholder lagi)*

#### 4.5.2 Hasil Analisis Stabilitas Klaster *(sub-bab baru, sebelumnya tidak ada — menggantikan slot "waktu komputasi" yang dihapus)*

**Tabel 4.2 Hasil Stability Score per Color Space dan K**

| Color Space | K | Stability Score |
|---|---|---|
| RGB | 3 | 0,1533 |
| RGB | 5 | 0,4333 |
| RGB | 7 | 0,5891 |
| HSV | 3 | 0,0000 |
| HSV | 5 | 0,0000 |
| HSV | 7 | 2,4492 |
| LAB | 3 | 0,4599 |
| LAB | 5 | 0,5067 |
| LAB | 7 | 0,1271 |

- Stability Score mengukur variasi centroid antar 5 run K-Means dengan seed berbeda — semakin kecil semakin stabil
- **Temuan yang perlu dibahas**: HSV K=3 dan K=5 mencatat stability **0,0000 persis** — ini kemungkinan bukan stabilitas sempurna, melainkan artefak pembulatan/konversi warna HSV→RGB yang menghasilkan nilai integer identik antar run. Perlu dicatat sebagai catatan kehati-hatian interpretasi, bukan diklaim sebagai keunggulan HSV.

#### 4.5.3 Skor Komposit dan Ranking Color Space Terbaik

**Tabel 4.3 Skor Komposit dan Ranking Akhir (Top 3 dari 9 kombinasi)**

| Ranking | Color Space | K | Silhouette | DBI | CHI | Stability | Composite Score |
|---|---|---|---|---|---|---|---|
| 1 | RGB | 3 | 0,4784 | 0,6783 | 6.951,57 | 0,1533 | **0,9856** |
| 2 | LAB | 3 | 0,4769 | 0,6770 | 6.972,03 | 0,4599 | 0,9594 |
| 3 | HSV | 3 | 0,4461 | 0,7986 | 2.589,12 | 0,0000 | 0,6442 |

- Formula composite score (sebutkan singkat saja, tanpa breakdown rumus per skor ternormalisasi): **0,35×Silhouette + 0,25×DBI(invers) + 0,20×CHI + 0,20×Stability(invers)**
- **Model terbaik: RGB, K=3, composite score = 0,9856**
- Catatan penting: RGB dan LAB nyaris setara (0,9856 vs 0,9594) — keduanya jauh mengungguli HSV. Disarankan dibahas bahwa keunggulan RGB di sini tipis dan didorong terutama oleh Stability Score yang lebih baik, bukan karena RGB jauh lebih unggul di Silhouette/DBI/CHI (yang nilainya hampir identik dengan LAB)

#### 4.5.4 Hasil Validasi Akurasi Warna (CIEDE2000)

**Tabel 4.4 Validasi CIEDE2000 Centroid Model Terbaik (RGB, K=3)**

| Cluster | Centroid Hex | ITA (°) | Skintone | Undertone | Referensi Terdekat | CIEDE2000 | Interpretasi |
|---|---|---|---|---|---|---|---|
| 1 | #AF7F68 | 19,94 | Tan | Cool | Tan (ITA 10–28) | 10,435 | Sedang – masih dalam toleransi |
| 2 | #6A4638 | -48,01 | Dark | Cool | Brown (ITA -30–10) | 11,135 | Sedang – masih dalam toleransi |
| 3 | #E7BDA5 | 58,70 | Very Light | Neutral | Very Light (ITA>55) | 10,020 | Sedang – masih dalam toleransi |

- **Rata-rata CIEDE2000 model terbaik (RGB K=3): 10,530** — kategori "Sedang, masih dalam toleransi" untuk ketiganya. **Tidak ada cluster yang "JAUH"/out-of-tolerance pada level dataset** — koreksi penting dari narasi sebelumnya.

**Tabel 4.5 Ringkasan CIEDE2000 Rata-Rata Seluruh Kombinasi (diurutkan terbaik)**

| Color Space | K | Avg CIEDE2000 | Min | Max |
|---|---|---|---|---|
| LAB | 5 | 9,464 | 6,028 | 12,098 |
| RGB | 7 | 9,495 | 5,679 | 12,374 |
| RGB | 5 | 9,511 | 6,205 | 12,494 |
| LAB | 7 | 9,607 | 3,978 | 12,053 |
| RGB | 3 | 10,530 | 10,020 | 11,135 |
| LAB | 3 | 10,558 | 9,494 | 11,563 |
| HSV | 7 | 12,636 | 7,407 | 22,702 |
| HSV | 5 | 13,111 | 9,083 | 22,702 |
| HSV | 3 | 15,122 | 9,503 | 22,702 |

- **Temuan penting untuk dibahas**: jika murni berdasarkan CIEDE2000, model RGB K=3 (model terbaik berdasar composite score) sebenarnya **bukan yang paling akurat** secara perseptual warna — RGB/LAB K=5 dan K=7 punya rata-rata CIEDE2000 lebih kecil. Ini layak dibahas sebagai keterbatasan/trade-off di 4.9: composite score mengoptimalkan struktur klaster + stabilitas, bukan akurasi perseptual warna kulit secara langsung. HSV konsisten menjadi yang **terburuk** di semua K untuk CIEDE2000, memperkuat kesimpulan bahwa HSV kurang sesuai untuk ekstraksi warna kulit pada sistem ini.

### 4.6 Hasil Klasifikasi Skintone dan Undertone

- Metode: ITA dihitung dari L* dan b* CIELAB; kategori Very Light/Light/Intermediate/Tan/Brown/Dark
- Undertone: aturan berbasis a*/b* (Warm jika b*>5 & a*<10; Cool jika b*<-2 atau a*>12; selain itu Neutral)
- Hasil klasifikasi 3 centroid model terbaik (RGB K=3) — **ini SUDAH data lengkap, gunakan langsung**:

| Cluster | Hex | Skintone | ITA | Undertone |
|---|---|---|---|---|
| 1 | #AF7F68 | Tan | 19,94° | Cool |
| 2 | #6A4638 | Dark | -48,01° | Cool |
| 3 | #E7BDA5 | Very Light | 58,70° | Neutral |

- Catatan: sampel klasifikasi yang ditampilkan notebook hanya 3 centroid hasil clustering (representasi tingkat dataset), BUKAN distribusi per-sampel-individu (120 wajah tidak diklasifikasi ITA satu per satu secara terpisah di notebook ini). Jika ingin distribusi populasi 120 sampel, perlu tambahan kode baru — **[CATATAN: belum tersedia, perlu keputusan apakah ditambah atau cukup di level cluster]**

### 4.7 Hasil Rancangan Output Rekomendasi Warna Pakaian

#### 4.7.1 Pemetaan Skintone–Undertone ke Palet Warna
- Tabel lookup lengkap SUDAH ADA persis di kode (`RECOMMENDATION_TABLE`), bisa dikutip apa adanya — tidak perlu placeholder, datanya 6 kategori skintone × undertone-map masing-masing

#### 4.7.2 Contoh Output Sistem Lengkap
- Gunakan 3 cluster model terbaik sebagai 3 "sampel" representatif (karena tidak ada multi-sampel real lain yang tersimpan outputnya), ATAU
- Gunakan hasil testing gambar pengguna tunggal (Section 14) sebagai studi kasus tambahan:

| Item | Nilai |
|---|---|
| Face detected | True |
| Skin RGB/Hex | (185,142,148) / #B98E94 |
| Skintone ITA | Very Light (ITA=77,14°) |
| Undertone | Cool |
| CIEDE2000 ke referensi terdekat (Tan) | 24,066 — JAUH, kemungkinan noise/background |
| Rekomendasi | Royal Blue, Emerald, Lavender, Silver |
| Dihindari | Warna sangat pucat |

- **Ini jadi studi kasus bagus untuk membahas keterbatasan**: gambar tunggal pengguna nyata bisa menghasilkan CIEDE2000 jauh lebih tinggi (24,066) dibanding rata-rata dataset terkontrol (10,530), kemungkinan karena noise non-kulit, kondisi pencahayaan, atau area wajah yang tidak presisi ter-crop.

### 4.8 Hasil Implementasi Purwarupa Antarmuka

⚠️ **Catatan kritis**: notebook ini **TIDAK memuat Streamlit sama sekali**. Tidak ada `import streamlit`, tidak ada file `app.py`, tidak ada screenshot UI. Pengujian "live prediction" yang ada hanya berbentuk `files.upload()` di Google Colab (Section 14), bukan antarmuka web. 

**Ini perlu konfirmasi Anda**: apakah file Streamlit terpisah dari notebook ini (di file lain yang belum diupload), atau sub-bab 4.8 ini perlu diubah judulnya menjadi "Hasil Pengujian Prediksi pada Data Pengguna (Colab Upload Interface)" agar sesuai kenyataan implementasi saat ini?

### 4.9 Pembahasan

- Jawab RM1–RM4 dengan mengaitkan ke 4.2–4.8
- **Wajib bahas 3 trade-off/kontradiksi konkret yang muncul dari data**:
  1. Elbow Method merekomendasikan K=4, tapi composite score memilih K=3 — perlu dijelaskan mengapa keputusan akhir tidak mengikuti elbow murni
  2. Model dengan composite score terbaik (RGB K=3) bukan yang punya CIEDE2000 terbaik (LAB K=5 lebih akurat secara perseptual) — trade-off antara struktur klaster vs akurasi warna
  3. CIEDE2000 pada pengujian gambar pengguna nyata (24,066) jauh melebihi rata-rata dataset (10,530) — menunjukkan gap antara performa di data terkontrol vs data dunia nyata
- Keterbatasan penelitian **yang didukung data**: (a) tidak ada pengukuran waktu komputasi sehingga efisiensi belum bisa dibandingkan kuantitatif antar color space — sebagai catatan terbuka untuk penelitian lanjutan; (b) Stability Score HSV=0,0000 berpotensi artefak pembulatan, bukan stabilitas riil, sehingga perbandingan composite score dengan HSV perlu dibaca hati-hati; (c) sistem belum diuji pada antarmuka pengguna nyata (Streamlit) di tahap ini.

---

## RINGKASAN ANGKA KUNCI YANG SUDAH FIX (siap dipakai, tidak perlu placeholder lagi)

- Dataset: 120 citra → 97 terdeteksi wajah, 23 di-skip
- Total piksel kulit: 3.363.613
- K kandidat diuji: 3, 5, 7 (bukan rentang elbow penuh untuk ketiga color space)
- Elbow Method (RGB saja): merekomendasikan K=4
- Model terbaik: **RGB, K=3, composite score 0,9856**
- Centroid RGB K=3: #AF7F68 (Tan/Cool), #6A4638 (Dark/Cool), #E7BDA5 (Very Light/Neutral)
- Rata-rata CIEDE2000 model terbaik: 10,530 (semua "Sedang — masih dalam toleransi")
- CIEDE2000 terbaik secara keseluruhan: LAB K=5 (9,464) — BUKAN model yang dipilih final
- HSV secara konsisten terburuk di semua metrik kecuali sempat unggul di DBI K=7

## YANG MASIH PERLU ANDA LENGKAPI SEBELUM MENULIS BAB IV FINAL

1. Centroid HEX untuk HSV K=3 (untuk sub-bab 4.4.2) — jalankan ulang `plot_centroids(results_hsv, "HSV")` dan catat nilainya
2. Klarifikasi apakah Streamlit benar-benar sudah diimplementasikan di file terpisah, atau judul 4.8 perlu disesuaikan
3. Keputusan: distribusi ITA per-sampel (120 wajah individual) ditambahkan ke notebook atau cukup di level 3 cluster
4. Contoh kasus fallback aktif (wajah gagal terdeteksi) belum ada rekaman visualnya — perlu generate manual jika ingin sub-bab 4.2.4 punya ilustrasi nyata
