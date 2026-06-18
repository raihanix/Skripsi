**PENGEMBANGAN SISTEM REKOMENDASI WARNA PAKAIAN BERBASIS EKSTRAKSI WARNA KULIT MENGGUNAKAN CLUSTERING DAN EVALUASI MULTI-COLOR SPACE**

**PROPOSAL PENELITIAN**

**Diajukan untuk Memenuhi Salah Satu Syarat kelulusan Strata 1**

**di Program Studi Sistem Informasi Universitas Widyatama**

**Oleh**

|  |  |
| --- | --- |
| **NAMA** | **: Muhamad Raihan al ghazali** |
| **NPM** | **: 41121100033** |

![](data:image/jpeg;base64...)

**PROGRAM STUDI SISTEM INFORMASI**

**FAKULTAS TEKNIK UNIVERSITAS WIDYATAMA**

**BANDUNG**

**2026**

# DAFTAR ISI

DAFTAR ISI i

DAFTAR TABEL iii

DAFTAR GAMBAR iv

BAB I PENDAHULUAN 1

1.1 Latar Belakang Masalah 1

1.2 Identifikasi dan Rumusan Masalah 1

1.2.1 Identifikasi Masalah 1

1.2.2 Rumusan Masalah 2

1.3 Batasan Masalah 2

1.4 Tujuan Penelitian 2

1.5 Manfaat Penelitian 3

BAB II KAJIAN PUSTAKA 4

2.1 Tinjauan Pustaka 4

2.1.1 Ekstraksi Warna Kulit 4

2.1.2 Clustering pada Pengolahan Citra 5

2.1.3 Sistem Rekomendasi Berbasis Warna 7

2.1.4 Evaluasi Multi-Color Space 8

2.1.5 Analisis Gap 9

2.2.1 Konsep Dasar Pengolahan Citra Digital 12

2.2.2 Teori Ruang Warna (Color Space) 13

2.2.3 Teori Clustering 15

2.2.4 Algoritma K-Means 16

2.2.5 Evaluasi Kualitas Clustering 19

2.2.6 Konsep Sistem Rekomendasi 20

2.2.7 Teori Harmoni Warna dalam Fashion 21

BAB III METODOLOGI 24

3.1 Desain Penelitian 24

3.2 Metode Pengumpulan Data 24

3.2.1 Dataset Citra Wajah (Data Primer dan Sekunder) 25

3.2.2 Dataset Rekomendasi Warna Pakaian 25

3.2.3 Instrumen Penelitian 25

3.3 Tahapan Penelitian 26

3.4 Prapemrosesan Citra Digital 26

3.5 Perancangan Sistem 27

3.5.1 Arsitektur Pipeline Sistem 27

3.5.2 Rancangan Aturan Rekomendasi Warna 28

3.6 Teknik Analisis Data 29

3.6.1 Evaluasi Kuantitatif *Clustering* 29

3.6.2 Analisis Komparatif *Multi-Color Space* 30

3.6.3 Validasi Rekomendasi Warna Pakaian 31

3.7 Jadwal Penelitian 31

DAFTAR PUSTAKA 33

# DAFTAR TABEL

Tabel 2.1 Perbandingan Studi Terkait 11

Tabel 2.2 Perbandingan Karakteristik Color Space 14

Tabel 2.3 Perbandingan Metode Clustering 18

Tabel 3.1 Logika Pemetaan Rekomendasi Warna Pakaian Berdasarkan Skin Tone dan Undertone 28

Tabel 3.2 Jadwal Penelitian 31

# DAFTAR GAMBAR

Gambar 2.1 Ilustrasi Visual Model Ruang Warna (RGB, HSV, dan CIELAB) 15

Gambar 2.2 Konsep dan cara kerja K-Means pada ekstraksi warna kulit 19

Gambar 3.1 Diagram Alur Sistem dan Desain Eksperimental 24

Gambar 3.2 Flowchart Tahapan Penelitian Sistem Rekomendasi 26

Gambar 3.6 Diagram Arsitektur Pipeline Sistem 27

Gambar 3.7 Diagram Alir Perhitungan Metrik Evaluasi Kuantitatif Clustering 30

# BAB I PENDAHULUAN

## 1.1 Latar Belakang Masalah

Pemilihan warna pakaian yang sesuai dengan warna kulit merupakan aspek krusial dalam dunia fashion yang berkaitan erat dengan persepsi visual, psikologi konsumen, dan kepercayaan diri individu [1]. Secara tradisional, penentuan harmoni warna antara kulit pengguna dan pakaian seringkali dilakukan secara manual dan subjektif berdasarkan intuisi, tren, atau pengalaman pribadi pendesain busana. Pendekatan manual ini rentan menghasilkan keputusan yang tidak konsisten, memiliki bias persepsi, dan sulit direplikasi secara terstandarisasi [2], [3]. Dalam konteks personalisasi gaya, kecocokan warna pakaian tidak dapat dipisahkan dari karakteristik fisik bawaan individu, yang menuntut adanya sebuah sistem yang mampu memberikan rekomendasi secara lebih objektif dan terukur.

Seiring dengan pesatnya perkembangan pengolahan citra digital (digital image processing) dan kecerdasan buatan, pendekatan algoritmik mulai banyak dimanfaatkan untuk mengekstraksi representasi fitur manusia secara otomatis, termasuk ekstraksi warna kulit dari citra wajah. Namun, tantangan utama yang dihadapi dalam deteksi kulit manusia di lingkungan nyata adalah ketidakstabilan representasi warna akibat variasi kondisi pencahayaan (iluminasi) [4]. Penggunaan ruang warna (color space) konvensional seringkali gagal memisahkan antara informasi warna murni dan intensitas cahaya. Literatur menunjukkan bahwa penggunaan ruang warna yang berbeda seperti RGB, HSV, dan CIELAB memberikan karakteristik ketahanan dan akurasi persepsi yang sangat berbeda dalam merepresentasikan warna kulit [5], [6]. Oleh karena itu, diperlukan evaluasi komprehensif terhadap performa masing-masing ruang warna guna menemukan representasi kulit yang paling stabil terhadap variasi pencahayaan.

Dalam proses ekstraksi fitur warna, algoritma clustering memainkan peran yang sangat penting. Secara khusus, algoritma K-Means clustering telah terbukti sangat efisien dan efektif dalam mengekstraksi warna dominan dari data citra digital, tanpa membebani sistem dengan komputasi perangkat keras yang masif layaknya arsitektur Deep Learning [7], [8]. Pendekatan unsupervised learning ini memungkinkan sistem untuk menemukan titik pusat klaster (centroid) yang menjadi signature atau perwakilan warna kulit pengguna secara representatif.

Melalui integrasi antara segmentasi berbasis ambang batas (rule-based thresholding), algoritma K-Means clustering, dan evaluasi multi-color space, dimungkinkan untuk membangun sebuah sistem rekomendasi warna pakaian yang tangguh (robust). Setelah centroid warna kulit divalidasi pada ruang warna yang paling presisi secara visual, sistem dapat memetakannya ke dalam palet rekomendasi pakaian menggunakan landasan teori harmoni warna fashion [1], [3].

Berdasarkan latar belakang dan identifikasi celah penelitian tersebut, penelitian ini berupaya untuk mengembangkan sistem komputasional yang mengekstraksi warna kulit secara otomatis dari citra wajah, mengevaluasi hasilnya pada berbagai ruang warna (RGB, HSV, CIELAB), dan mengonversinya menjadi rekomendasi pakaian yang relevan secara perseptual.

## 1.2 Identifikasi dan Rumusan Masalah

### 1.2.1 Identifikasi Masalah

Berdasarkan latar belakang yang telah diuraikan, identifikasi masalah dalam penelitian ini adalah sebagai berikut:

1. Penentuan warna pakaian yang sesuai dengan warna kulit saat ini masih didominasi oleh pendekatan yang subjektif dan tidak konsisten [2].
2. Representasi hasil ekstraksi warna kulit dari citra digital rentan bergeser dan sangat dipengaruhi oleh variasi kondisi pencahayaan (iluminasi) lingkungan [4].
3. Belum terdapat panduan evaluasi yang komprehensif terkait performa ruang warna (RGB, HSV, dan CIELAB) secara spesifik untuk kebutuhan pembentukan centroid warna kulit pada sistem rekomendasi fashion [5].
4. Kurangnya integrasi konseptual antara teknik ekstraksi warna kulit komputasional berbasis clustering dengan mekanisme deduksi perekomendasian berbasis teori harmoni warna [1], [3].

### 1.2.2 Rumusan Masalah

Berdasarkan identifikasi masalah di atas, rumusan masalah dalam penelitian ini ditetapkan sebagai berikut:

1. Bagaimana merancang pipeline ekstraksi warna kulit wajah yang efisien menggunakan metode rule-based thresholding dan algoritma K-Means clustering?
2. Ruang warna manakah di antara RGB, HSV, dan CIELAB yang menghasilkan representasi centroid warna kulit paling stabil berdasarkan evaluasi kuantitatif?
3. Bagaimana memetakan output clustering warna kulit menjadi rekomendasi palet warna pakaian yang relevan berdasarkan teori harmoni warna fashion?
4. Bagaimana tingkat performa dari purwarupa sistem rekomendasi warna pakaian yang dikembangkan secara keseluruhan?

## 1.3 Batasan Masalah

Batasan masalah dalam penelitian ini ditetapkan agar ruang lingkup penelitian tetap terarah dan sesuai dengan tujuan yang telah ditetapkan, batasan masalah ditetapkan sebagai berikut:

1. Masukan (input) sistem berupa citra wajah dua dimensi yang diambil dengan kondisi pencahayaan (iluminasi) yang memadai, dan tidak dalam kondisi gelap gulita atau backlight ekstrem.
2. Ruang warna (color space) yang dievaluasi dan dikomparasi dibatasi hanya pada RGB, HSV, dan CIELAB.
3. Algoritma clustering utama yang diimplementasikan untuk ekstraksi warna adalah K-Means. Algoritma lain seperti Fuzzy C-Means (FCM) dan Gaussian Mixture Model (GMM) hanya dieksplorasi sebagai landasan perbandingan teoritis.
4. Rekomendasi warna pakaian didasarkan secara eksklusif pada teori harmoni warna (komplementer, analogus, dan triadik). Sistem tidak mencakup analisis postur tubuh, bentuk wajah, atau preferensi gaya berpakaian.
5. Hasil akhir dari penelitian ini difokuskan pada sebuah purwarupa (prototype) sistem untuk memvalidasi algoritma, bukan sebuah aplikasi mobile atau web berskala komersial penuh.

## 1.4 Tujuan Penelitian

Penelitian ini bertujuan untuk menjembatani pengolahan citra komputasional dengan teori estetika visual guna menghasilkan sistem rekomendasi yang objektif, tangguh (robust), dan efisien. Secara spesifik, tujuan yang ingin dicapai adalah sebagai berikut:

1. Merancang dan membangun pipeline ekstraksi warna kulit wajah yang efisien berbasis rule-based thresholding dan algoritma K-Means clustering.
2. Mengevaluasi performa algoritma K-Means clustering pada berbagai ruang warna (RGB, HSV, CIELAB) untuk menemukan representasi centroid warna kulit yang paling stabil.
3. Menerapkan prinsip psikologi dan teori harmoni warna fashion ke dalam mekanisme rekomendasi berbasis output clustering.
4. Membangun purwarupa (prototype) sistem rekomendasi warna pakaian yang ringan secara komputasi dan relevan secara perseptual bagi pengguna.

## 1.5 Manfaat Penelitian

Penelitian ini diharapkan dapat memberikan manfaat yang signifikan, baik dari segi pengembangan ilmu pengetahuan maupun penerapan praktis di masyarakat. Manfaat tersebut diuraikan sebagai berikut:

1. **Manfaat Teoritis**
2. Memberikan kontribusi keilmuan dalam bidang pengolahan citra digital (digital image processing), khususnya terkait evaluasi komparatif multi-color space (RGB, HSV, dan CIELAB) untuk ekstraksi fitur warna kulit manusia secara otomatis.
3. Memperkaya literatur akademik mengenai integrasi algoritma pembelajaran tanpa pengawasan (unsupervised learning), seperti K-Means clustering, dengan sistem rekomendasi berbasis persepsi visual dalam domain teknologi fashion.
4. Menyediakan kerangka kerja evaluasi kuantitatif yang dapat dijadikan acuan atau tolok ukur (benchmark) bagi penelitian-penelitian serupa di masa mendatang.
5. **Manfaat Praktis**
6. Membantu pengguna akhir (end-user) dalam memilih palet warna pakaian yang serasi dengan tone kulit mereka secara lebih otomatis, cepat, dan objektif tanpa harus menebak-nebak.
7. Menyediakan referensi teknis dan cetak biru (blueprint) algoritma bagi pengembang sistem fashion technology dalam membangun fitur rekomendasi cerdas, tanpa mengharuskan spesifikasi komputasi perangkat keras yang tinggi (seperti pada model Deep Learning).
8. Menjadi landasan awal yang tangguh untuk pengembangan purwarupa atau aplikasi personal styling interaktif yang lebih komprehensif di masa depan.

# BAB II KAJIAN PUSTAKA

## 2.1 Tinjauan Pustaka

### 2.1.1 Ekstraksi Warna Kulit

Ekstraksi warna kulit (*skin color extraction*) dalam pengolahan citra digital dapat dipahami sebagai rangkaian proses untuk memperoleh informasi warna kulit dari citra manusia—umumnya dimulai dari deteksi/segmentasi piksel kulit (memisahkan *skin* dan *non-skin*), lalu dilanjutkan dengan perumusan representasi warna (misalnya statistik warna, histogram, atau warna dominan) dari area kulit yang telah dipisahkan. Secara konseptual, tahapan ini penting karena kualitas segmentasi dan representasi warna akan menentukan kestabilan fitur warna kulit ketika digunakan pada tahap analisis berikutnya (misalnya pengelompokan/kuantisasi warna).

Untuk memperjelas batasan konsep “deteksi kulit” yang menjadi fondasi ekstraksi warna kulit, Kolkur dkk. menyatakan bahwa deteksi kulit berkaitan dengan pengenalan piksel dan region yang berwarna kulit pada sebuah citra. [1] Definisi ini menegaskan bahwa objek utama pada tahap awal ekstraksi adalah piksel (unit terkecil citra) yang kemudian dapat membentuk region kulit (kumpulan piksel yang saling berdekatan). Kolkur dkk. juga menekankan bahwa penggunaan warna kulit sebagai fitur sering dipilih karena pemrosesannya relatif cepat dan tidak bergantung pada orientasi maupun ukuran objek manusia dalam citra. [1]

Dalam praktiknya, deteksi/segmentasi kulit menghadapi tantangan besar karena penampakan kulit sangat dipengaruhi kondisi akuisisi. Moumene dkk. menegaskan bahwa deteksi warna kulit telah banyak diteliti dan menjadi tugas penting untuk berbagai aplikasi visi komputer (misalnya pelacakan wajah/tangan dan analisis gestur). [2] Mereka juga menjelaskan adanya dua arus pendekatan: metode *machine learning* efektif untuk deteksi kulit, namun sering tidak ideal untuk real-time karena komputasinya berat; sedangkan pendekatan ringan dapat dibangun dari aturan segmentasi yang diperoleh dari distribusi warna kulit, tetapi tidak ada aturan universal karena variasi tipe citra, parameter akuisisi, dan iluminasi pemandangan. [2] Dengan kata lain, ekstraksi warna kulit tidak cukup hanya “menentukan ambang” sekali, melainkan perlu mempertimbangkan robustness terhadap perubahan pencahayaan dan variasi kondisi nyata.

Pada sisi teknik, Kolkur dkk. menunjukkan penggunaan beberapa ruang warna sebagai dasar aturan segmentasi, khususnya RGB, HSV, dan YCbCr, untuk mengenali piksel kulit. [1] Pendekatan berbasis ambang (*thresholding*) semacam ini memiliki keunggulan dari sisi kesederhanaan dan efisiensi, namun juga memiliki konsekuensi: performanya sensitif terhadap pergeseran iluminasi, bayangan, latar yang menyerupai warna kulit, serta perbedaan karakteristik warna kulit antar individu. [1] Pada konteks ini, pemilihan ruang warna menjadi aspek penting karena setiap ruang warna merepresentasikan komponen luminansi dan krominansi secara berbeda—yang dapat berdampak pada separabilitas piksel kulit dari non-kulit.

Moumene dkk. kemudian memperkuat aspek efisiensi tersebut melalui pendekatan adaptive HSV thresholding untuk deteksi kulit real-time. Mereka menekankan bahwa meskipun aturan segmentasi dapat diperoleh dari distribusi warna kulit, variasi kondisi membuat aturan statis tidak selalu memadai; karena itu, ambang perlu disesuaikan secara adaptif mengikuti perubahan kondisi. [2] Gagasan adaptif ini penting dalam ekstraksi warna kulit karena segmentasi yang lebih stabil akan menghasilkan area kulit yang lebih “bersih”, sehingga representasi warna kulit yang dihitung dari area tersebut menjadi lebih konsisten.

Setelah area kulit diperoleh, ekstraksi warna kulit tidak berhenti pada mask/segmentasi, tetapi berlanjut pada pembentukan representasi warna yang ringkas dan bermakna. Dalam ranah ekstraksi warna, Chang & Mukai menjelaskan bahwa warna dominan dalam citra dapat dimanfaatkan untuk berbagai kebutuhan seperti pencarian citra, pengeditan warna, dan pembangkitan palet. [3] Mereka juga menyoroti bahwa metode konvensional berbasis clustering atau histogram sering gagal menangkap warna dominan pada region kecil, padahal region kecil bisa penting untuk analisis skema warna. [3] Konsep “warna dominan” ini relevan untuk ekstraksi warna kulit karena area kulit yang tersegmentasi pada dasarnya merupakan suatu region yang dapat diringkas oleh satu atau beberapa warna representatif (misalnya centroid cluster atau kandidat warna dominan), sehingga fitur warna kulit menjadi lebih informatif daripada sekadar nilai rata-rata global.

Dengan demikian, ekstraksi warna kulit dalam penelitian ini berdiri pada dua fondasi utama: (1) deteksi/segmentasi kulit yang efisien dan cukup robust terhadap variasi akuisisi, sebagaimana digambarkan pada pendekatan berbasis multi–color space dan adaptasi ambang; serta (2) perumusan representasi warna dari area kulit yang telah dipisahkan, dengan prinsip bahwa ringkasan warna seperti warna dominan/palet dapat meningkatkan kualitas representasi warna untuk tahap pengolahan berikutnya. [1] [2] [3].

### 2.1.2 Clustering pada Pengolahan Citra

Clustering merupakan metode *unsupervised* yang mengelompokkan data berdasarkan kemiripan sehingga objek-objek yang berada dalam satu kelompok memiliki karakteristik yang relatif serupa. Dalam pengolahan citra digital, clustering lazim digunakan untuk segmentasi dan ekstraksi representasi warna, karena piksel-piksel citra dapat dipandang sebagai himpunan data pada ruang fitur (misalnya ruang warna). Dengan cara ini, proses segmentasi tidak harus bergantung pada model terlatih (*machine learning* atau *deep learning*) yang umumnya membutuhkan data latih dan komputasi lebih tinggi, melainkan dapat dibangun melalui pengelompokan piksel yang efisien dan interpretable.

Kerangka teoretik yang menjelaskan hubungan antar-metode clustering dipaparkan oleh Komori & Eguchi melalui formulasi terunifikasi yang mengaitkan k-means, fuzzy c-means, dan Gaussian mixture model (GMM) dalam satu perspektif matematis. [4] Melalui sudut pandang ini, k-means dipahami sebagai *hard clustering* (setiap data masuk tepat ke satu cluster), fuzzy c-means sebagai *soft clustering* (data memiliki derajat keanggotaan), sedangkan GMM memodelkan cluster secara probabilistik. Diferensiasi ini penting pada data citra, karena transisi warna antar-region sering gradual dan tidak selalu “tegas”, terutama pada batas objek.

Implementasi clustering untuk segmentasi berbasis warna ditunjukkan oleh Rosyani dkk. yang melakukan investigasi segmentasi citra bunga menggunakan K-Means dan Fuzzy C-Means (FCM) dengan memanfaatkan fitur dari beberapa ruang warna (RGB, HSV, LAB, dan YCbCr). [5] Mereka menggunakan citra sampel yang memuat 1–4 objek bunga dari ImageCLEF 2017 dan menilai performa segmentasi dengan memanfaatkan *ground truth*. Evaluasi dilakukan menggunakan jarak Hausdorff serta metrik performa berbasis confusion matrix seperti akurasi, tingkat kesalahan, sensitivitas, dan spesifisitas. [5] Temuan penting dari studi ini adalah bahwa hasil segmentasi sangat dipengaruhi oleh pemilihan komponen warna, dan penggunaan komponen dari model warna LAB memberi dampak yang kuat terhadap keberhasilan segmentasi. Selain itu, mereka menunjukkan bahwa komponen AB merupakan model warna yang konsisten berhasil mendeteksi objek secara benar pada skenario uji yang mereka lakukan. [5] Hasil tersebut menegaskan bahwa keberhasilan clustering pada citra tidak hanya dipengaruhi algoritmanya, tetapi juga oleh representasi warna yang digunakan.

Di luar segmentasi objek, clustering juga menjadi dasar penting dalam ekstraksi warna dominan untuk merangkum informasi warna suatu citra/region. Chang & Mukai mengajukan metode ekstraksi warna dominan yang diawali dengan menghitung kandidat warna dominan menggunakan K-Means pada ruang warna CIELAB, lalu menggabungkannya dengan *graph cut* pada *region adjacency graph (RAG)* dari citra yang telah disegmentasi. [3] Setelah kandidat cluster terbentuk, mereka menghitung fitur warna yang lazim dipertimbangkan dalam analisis skema warna—seperti saturasi, kontras, dan area—untuk menyeleksi warna yang benar-benar dominan. [3] Pendekatan ini menekankan bahwa ringkasan warna berbasis clustering menjadi lebih kuat ketika digabungkan dengan informasi spasial (keterhubungan region) dan kriteria seleksi fitur yang relevan terhadap persepsi visual.

Walaupun K-Means sering digunakan karena sederhana dan cepat, literatur juga menegaskan keterbatasan klasiknya, yaitu sensitivitas terhadap inisialisasi dan kebutuhan menentukan jumlah cluster K sejak awal. Sinaga & Yang menyatakan bahwa k-means dan banyak pengembangannya tetap dipengaruhi inisialisasi serta memerlukan jumlah cluster *a priori*, sehingga pada praktiknya k-means tidak sepenuhnya *unsupervised*. [6] Untuk mengatasi hal tersebut, mereka mengusulkan skema Unsupervised K-Means (U-k-means) yang diarahkan agar bebas inisialisasi dan mampu menemukan jumlah cluster optimal tanpa seleksi parameter. [6] Gagasan ini relevan untuk pengelompokan warna (termasuk warna kulit), karena penentuan K yang tidak tepat dapat menghasilkan representasi yang terlalu kasar (K kecil) atau terlalu sensitif terhadap noise/variasi iluminasi (K besar).

Selain pengembangan pada k-means, terdapat pula pendekatan clustering yang memodelkan ketidakpastian melalui konsep *three-way decision*. Chen & Wang memperkenalkan *three-way clustering* yang terinspirasi operasi pengolahan citra digital berupa blurring dan sharpening, dengan cara mengkuantifikasi kepadatan data menjadi nilai “gray” melalui fungsi kernel. [7] Dalam paradigma *three-way*, semesta data dipisahkan menjadi tiga bagian yang saling lepas: core region (objek dengan konsentrasi tinggi di dalam cluster), fringe region (area ketidakpastian/objek yang lebih longgar), dan trivial region (bagian di luar cluster yang relevan). [7] Setelah sampel berkepadatan rendah dieliminasi, clustering konvensional diterapkan pada sampel berkepadatan tinggi, kemudian core dan fringe pada tiap cluster diperoleh melalui operasi blurring dan sharpening. [7] Walaupun konteks eksperimennya menggunakan dataset umum, kerangka ini memperlihatkan cara alternatif untuk menangani area “ambigu”—isu yang juga sering muncul pada data warna citra ketika terdapat transisi halus atau gangguan pencahayaan.

Secara keseluruhan, literatur menunjukkan bahwa clustering pada pengolahan citra digital memainkan peran utama untuk membangun segmentasi dan ringkasan warna: (1) K-Means/FCM efektif untuk segmentasi berbasis warna dan sangat dipengaruhi oleh pilihan ruang warna/komponen fitur, (2) clustering dapat digunakan untuk mengekstrak warna dominan ketika digabungkan dengan struktur spasial dan seleksi fitur warna, dan (3) keterbatasan k-means terkait inisialisasi serta pemilihan K dapat diatasi melalui skema *unsupervised* yang lebih kuat atau paradigma *three-way* yang mengakomodasi ketidakpastian. [5], [3], [6], [4], [7].

### 2.1.3 Sistem Rekomendasi Berbasis Warna

Sistem rekomendasi berbasis warna dalam konteks fashion pada dasarnya berangkat dari asumsi bahwa warna bukan sekadar atribut visual, melainkan stimulus yang memengaruhi persepsi, emosi, dan preferensi pengguna. Dalam pengambilan keputusan pemilihan warna pakaian, faktor psikologis sering berinteraksi dengan faktor estetika (harmoni warna), konteks sosial, serta karakteristik individu. Oleh karena itu, rancangan rekomendasi warna yang baik idealnya tidak hanya memetakan “warna yang serasi”, tetapi juga mempertimbangkan “warna yang dirasakan tepat” oleh pengguna berdasarkan preferensi dan persepsi.

Kajian psikologi warna pada fashion dijelaskan oleh Wei & Zhang melalui pembahasan hubungan warna dan psikologi konsumen. Mereka menempatkan psikologi konsumen sebagai kajian yang mempelajari perubahan psikologis dan perilaku konsumen dalam aktivitas konsumsi, yang dipengaruhi oleh faktor internal maupun eksternal. Pada konteks fashion design, warna diposisikan sebagai elemen desain yang memiliki efek berbeda terhadap emosi dan kesadaran individu, sehingga pemilihan dan padu padan warna pakaian seharusnya disesuaikan dengan kebutuhan psikologis kelompok konsumen yang berbeda. [8].

Untuk memotret pengaruh elemen desain terhadap psikologi konsumsi, Wei & Zhang melakukan pengumpulan data pada 100 konsumen yang dipilih secara acak dari tiga pusat perbelanjaan, dengan fokus pada kebutuhan konsumsi, kecenderungan konsumsi, kecenderungan pemilihan warna pakaian, dan karakteristik kepribadian. Evaluasi pengaruh elemen desain dilakukan menggunakan *fuzzy evaluation method* dengan skala penilaian 1–5, di mana nilai lebih tinggi menunjukkan pengaruh yang lebih besar. Hasil penilaian mereka menunjukkan bahwa warna memiliki pengaruh paling besar pada kelompok *juvenile* (skor 5), kemudian *youth* (skor 4), dan *young and middle-aged* (skor 3). [8]

Temuan tersebut memperkuat posisi warna sebagai variabel yang layak dijadikan dasar rekomendasi pada domain fashion, khususnya bila sistem rekomendasi diarahkan untuk menyesuaikan saran warna terhadap karakter pengguna (misalnya kelompok usia, preferensi, dan kecenderungan psikologis). Dalam paper yang sama, Wei & Zhang juga menekankan bahwa perancangan warna pakaian dapat mengacu pada prinsip desain seperti keseimbangan, ritme, dan proporsi, serta menggunakan beberapa pendekatan psikologis dalam desain pakaian agar hasil desain memenuhi kebutuhan psikologis konsumen. [8]

Pada sisi representasi warna (yang menjadi input penting bagi sistem rekomendasi berbasis warna), Muratbekova dkk. menegaskan bahwa pemilihan model warna/ruang warna bersifat *task-dependent*, karena setiap model memiliki kompromi antara akurasi perseptual, biaya komputasi, dan ketergantungan perangkat. Mereka mereview model tradisional (mis. RGB), model yang lebih mendekati persepsi (mis. CIELAB/CIELUV), serta pendekatan berbasis fuzzy, lalu melakukan eksperimen untuk membandingkan aspek-aspek seperti ketergantungan perangkat, konsistensi kromatik, dan kompleksitas komputasi. [9] Dalam konteks aplikasi yang menargetkan kesesuaian persepsi pengguna—seperti rekomendasi warna—kajian ini relevan karena menyoroti bahwa persepsi manusia dipengaruhi faktor neural, konteks, dan subjektivitas yang tidak sepenuhnya ditangkap oleh representasi numerik statis. [9]

Lebih lanjut, Muratbekova dkk. juga menandai arah penelitian yang makin menonjol pada keterkaitan warna dengan aspek *human-centric*, termasuk *color-emotion associations*, serta menekankan adanya kebutuhan validasi yang lebih berorientasi pengguna untuk aplikasi-aplikasi berbasis persepsi. [9] Perspektif ini sejalan dengan karakter sistem rekomendasi warna pada fashion: selain mengandalkan aturan/fitur warna, kualitas rekomendasi idealnya diuji melalui penilaian pengguna karena target akhirnya adalah “keterterimaan” rekomendasi oleh manusia.

Jika sistem rekomendasi warna pakaian diintegrasikan dengan pipeline pengolahan citra (misalnya dari citra wajah), maka aspek efisiensi komputasi juga menjadi pertimbangan. Pada ranah deteksi/segmentasi kulit, Moumene dkk. menunjukkan bahwa pendekatan ringan berbasis ambang adaptif dapat berjalan cepat dan kompetitif untuk real-time, sedangkan pendekatan *deep learning* menghasilkan performa lebih tinggi namun jauh lebih mahal secara komputasi pada eksperimen yang mereka laporkan. [2] Konteks ini relevan karena sistem rekomendasi berbasis citra pada perangkat nyata sering membutuhkan trade-off yang jelas antara kualitas dan biaya komputasi.

Berangkat dari temuan psikologi warna dalam fashion, warna dapat diperlakukan sebagai atribut rekomendasi yang tidak semata-mata “sesuai secara teori”, tetapi juga harus “diterima secara persepsi” oleh pengguna. Wei & Zhang memperlihatkan bahwa pengaruh warna terhadap keputusan dan respons konsumen dapat berbeda pada kelompok usia, sehingga rekomendasi warna di domain fashion pada dasarnya beririsan langsung dengan preferensi dan reaksi psikologis pengguna. [8] Pada saat yang sama, bila rekomendasi dihasilkan dari pipeline pengolahan citra (misalnya dari citra wajah), maka konsistensi representasi warna menjadi prasyarat agar rekomendasi tidak berubah drastis hanya karena perubahan iluminasi atau perangkat. Di titik inilah pemilihan model/ruang warna menjadi krusial: Muratbekova dkk. menegaskan bahwa pemilihan color model/space bersifat bergantung tugas, karena model yang populer seperti RGB tidak selalu selaras dengan persepsi manusia, sementara model yang lebih konsisten secara perseptual dapat membawa konsekuensi komputasi. [9] Selain itu, pertimbangan efisiensi pipeline juga relevan: Moumene dkk. menunjukkan bahwa pendekatan ringan pada deteksi/segmentasi kulit dapat berjalan cepat untuk real-time, sedangkan metode *deep learning* dapat lebih akurat namun jauh lebih mahal secara komputasi pada pengujian mereka. [2] Oleh karena itu, sistem rekomendasi berbasis warna pada penelitian ini diletakkan sebagai integrasi antara pemaknaan warna dalam fashion dan representasi warna komputasional yang stabil, sehingga rekomendasi yang dihasilkan tetap masuk akal secara persepsi sekaligus konsisten secara teknis.

### 2.1.4 Evaluasi Multi-Color Space

Evaluasi multi-color space dilakukan untuk memastikan bahwa proses ekstraksi dan representasi warna tidak bergantung pada satu ruang warna tertentu, mengingat setiap *color model/space* membawa karakteristik yang berbeda dalam memisahkan informasi luminansi dan krominansi, menjaga kedekatan perseptual, serta menahan distorsi akibat perubahan pencahayaan. Muratbekova dkk. menekankan bahwa model tradisional seperti RGB banyak digunakan, namun memiliki keterbatasan pada keseragaman perseptual (*perceptual uniformity*), sedangkan keluarga CIE dan HS\* meningkatkan konsistensi perseptual tetapi cenderung lebih mahal secara komputasi. [9]

Dalam kerangka konseptual, Muratbekova dkk. juga membedakan “color model” dan “color space”. Color model dipahami sebagai konsep representasi numerik warna menggunakan seperangkat nilai (misalnya RGB, CMYK, HSV), sedangkan color space merupakan implementasi spesifik dari model tersebut yang sekaligus menentukan gamut warna (misalnya sRGB, Adobe RGB, CIELAB). [9] Pembedaan ini penting karena penelitian yang menilai “kinerja ruang warna” pada praktiknya menilai dampak implementasi representasi warna terhadap pemisahan kelas/cluster warna pada data citra.

Pada ranah ekstraksi kulit, kebutuhan evaluasi lintas ruang warna terlihat dari studi Moumene dkk. yang membandingkan segmentasi kulit pada RGB, YCrCb, dan HSV. Mereka melaporkan bahwa konfigurasi berbasis HSV memberikan performa terbaik dibanding RGB dan YCrCb pada dua dataset yang berbeda (Pratheepan dan HGR), dengan F1 yang tinggi dan waktu komputasi rendah untuk skenario real-time. [2] Hasil ini menegaskan bahwa pemilihan ruang warna dapat memengaruhi kualitas mask kulit yang dihasilkan; padahal mask kulit yang stabil merupakan prasyarat agar fitur warna kulit yang diekstrak tidak “terkontaminasi” oleh piksel latar atau bayangan.

Di sisi clustering berbasis warna, Rosyani dkk. juga menunjukkan bahwa performa segmentasi berbasis K-Means dan FCM dipengaruhi secara kuat oleh pemilihan ruang warna/komponen fitur warna, di mana komponen pada LAB (khususnya kanal chromatic) memperlihatkan kontribusi yang signifikan terhadap keberhasilan segmentasi pada eksperimen mereka. [5] Walaupun domain yang diuji adalah citra bunga, pola temuannya tetap relevan untuk penelitian ini: ketika fitur yang dipakai adalah warna, maka ruang warna yang lebih selaras dengan persepsi/struktur pemisahan warna sering memberi hasil segmentasi/cluster yang lebih stabil.

Selain itu, kebutuhan evaluasi multi-color space juga terkait langsung dengan cara kita merangkum warna menjadi representasi yang ringkas. Chang & Mukai menggunakan K-Means pada CIELAB sebagai tahap awal untuk menghasilkan kandidat warna, lalu memperkuatnya melalui seleksi berbasis fitur (misalnya saturasi, kontras, dan area) agar warna dominan yang dipilih lebih representatif. [3] Ini menegaskan bahwa pemilihan ruang warna bukan hanya memengaruhi “seberapa mudah data terpisah”, tetapi juga memengaruhi “seberapa representatif centroid/warna dominan” terhadap persepsi visual.

Dengan demikian, evaluasi multi-color space dalam penelitian ini memiliki dasar literatur yang jelas: (1) secara konseptual, setiap color model/space membawa kompromi perseptual–komputasi; (2) secara empiris, kinerja segmentasi kulit dapat berubah antar ruang warna; dan (3) pada tugas clustering/ekstraksi warna, pemilihan ruang warna dapat mengubah kualitas cluster maupun representasi warna yang dihasilkan. [9] [2] [5] [3]

### 2.1.5 Analisis Gap

Berdasarkan kajian pada subbab sebelumnya, terlihat bahwa penelitian-penelitian terkait telah menyediakan fondasi kuat pada sisi deteksi/segmentasi kulit, pemilihan ruang warna, dan pemanfaatan clustering untuk segmentasi/ekstraksi warna. Namun, keterhubungan antar komponen tersebut—khususnya untuk membentuk representasi warna kulit yang stabil sebagai dasar rekomendasi—masih menyisakan ruang pengembangan. Hal ini menjadi penting karena kualitas rekomendasi berbasis warna pada akhirnya sangat bergantung pada konsistensi ekstraksi warna kulit terhadap variasi kondisi akuisisi, serta kesesuaian representasi warna terhadap persepsi pengguna. [9] [2]

Secara lebih spesifik, gap penelitian dapat dirumuskan sebagai berikut.

1. Segmentasi kulit berbasis aturan efektif dan ringan, tetapi rentan variasi kondisi nyata
   Pendekatan thresholding dengan memanfaatkan beberapa ruang warna (RGB/HSV/YCbCr) menunjukkan bahwa deteksi kulit dapat dilakukan secara efisien. Namun performa metode berbasis aturan sangat dipengaruhi oleh iluminasi, latar, dan variasi tone kulit, sehingga penentuan ambang tidak bersifat universal untuk semua kondisi. [1] [2]
2. Perbandingan color space pada deteksi kulit ada, tetapi fokusnya masih terbatas pada kualitas mask (segmentasi), belum pada representasi warna kulit untuk kebutuhan lanjutan
   Studi real-time berbasis ambang adaptif membandingkan RGB–YCrCb–HSV dan menunjukkan perbedaan performa nyata antar ruang warna. Akan tetapi, evaluasi tersebut berhenti pada keluaran segmentasi (skin/non-skin) dan belum diarahkan menjadi evaluasi end-to-end terhadap pembentukan *signature* warna kulit (misalnya warna dominan/centroid yang siap di-cluster) yang menjadi masukan bagi sistem rekomendasi. [2]
3. Clustering berbasis warna terbukti sensitif terhadap ruang warna/komponen fitur, tetapi bukti kuatnya lebih banyak pada domain non-kulit
   Penelitian segmentasi objek berbasis K-Means/FCM menegaskan bahwa pemilihan ruang warna (misalnya LAB) dapat sangat menentukan keberhasilan segmentasi berbasis clustering. Namun temuan ini belum divalidasi secara khusus pada domain warna kulit wajah, yang memiliki karakteristik noise pencahayaan dan kemiripan warna latar yang khas. [5]

Di luar tiga poin utama di atas, terdapat gap metodologis yang lebih teknis namun berdampak langsung pada kualitas representasi warna kulit.

1. Penentuan jumlah cluster (K) dan sensitivitas inisialisasi pada K-Means masih menjadi kendala saat clustering dipakai sebagai “representasi warna”
   K-Means sering dipakai untuk kuantisasi warna karena sederhana dan cepat, tetapi isu pemilihan K dan inisialisasi dapat menghasilkan centroid yang tidak stabil—terutama ketika data warna dipengaruhi iluminasi. Usulan *unsupervised* yang dapat menemukan jumlah cluster optimal dan mengurangi ketergantungan inisialisasi sudah dibahas dalam literatur, tetapi belum banyak dipakai sebagai landasan eksplisit untuk clustering warna kulit lintas ruang warna. [6]
2. Metode ekstraksi warna dominan sudah maju untuk kebutuhan umum, namun belum diposisikan sebagai representasi “warna kulit” untuk rekomendasi
   Pendekatan ekstraksi warna dominan berbasis clustering (misalnya K-Means pada CIELAB yang kemudian diperkaya seleksi fitur warna dan koherensi spasial) menunjukkan bahwa representasi warna yang lebih “perseptual” dapat diperoleh dibanding ringkasan sederhana. Namun pendekatan tersebut tidak secara spesifik diarahkan untuk membangun representasi warna kulit (skin signature) yang konsisten untuk kebutuhan downstream seperti rekomendasi warna pakaian. [3]
3. Gap ML/DL muncul sebagai trade-off: akurasi meningkat, tetapi biaya komputasi jauh lebih besar dibanding pendekatan citra+aturan/clustering
   Literatur memperlihatkan bahwa metode *machine learning* dan *deep learning* memang menawarkan performa klasifikasi yang sangat tinggi pada berbagai domain analisis visual yang kompleks [10], [11]. Namun, pendekatan ML/DL memiliki kompensasi teknis yang signifikan. Waktu komputasi dan kebutuhan sumber daya pada arsitektur *deep learning* jauh melebihi pendekatan ringan berbasis ambang adaptif atau *clustering* [2], [10]. Lebih lanjut, performa analisis citra berbasis *machine learning* terbukti sangat bergantung pada metrik kualitas citra masukan (*image quality assessment*) [12]. Pada kasus ekstraksi warna kulit di mana variasi iluminasi dan perangkat akuisisi sering menurunkan kualitas citra secara tak terduga, ketergantungan pada model ML/DL mengharuskan ketersediaan data latih yang sangat masif dan spesifik. Kondisi ini menegaskan ruang penelitian yang wajar: alih-alih menegasikan ML/DL, penelitian ini memosisikan integrasi pengolahan citra dan *clustering* konvensional sebagai pendekatan yang lebih proporsional, efisien, dan representatif untuk membangun sistem rekomendasi warna tanpa harus terbebani oleh kompleksitas komputasi model *deep learning*.

Terakhir, pada domain fashion, penelitian psikologi warna menegaskan bahwa rekomendasi warna tidak cukup hanya “benar” secara komputasional; rekomendasi perlu masuk akal secara persepsi dan preferensi pengguna. Namun integrasi aspek persepsi ini dengan pipeline teknis ekstraksi warna kulit → representasi (clustering) → evaluasi multi-color space masih belum terlihat jelas pada rujukan yang kita gunakan saat ini. [8] [9]

Kesimpulan gap (posisi penelitian)**:** penelitian ini memfokuskan kontribusi pada penguatan pipeline end-to-end berbasis pengolahan citra (ekstraksi warna kulit yang efisien), dilanjutkan pembentukan representasi warna kulit melalui clustering yang dapat dipertanggungjawabkan, serta evaluasi multi–color space untuk memastikan stabilitas representasi—dengan ML/DL ditempatkan sebagai pembanding trade-off akurasi vs biaya komputasi, bukan sebagai fokus utama pendekatan. [2] [6] [9]

Tabel 2.1 Perbandingan Studi Terkait

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| No | Peneliti | Tahun | Fokus/Metode Utama | Ruang Warna / Fitur | Dataset/Evaluasi | Temuan Kunci | Keterbatasan terhadap penelitian ini |
| 1 | Muratbekova dkk. | 2025 | Review dan eksperimen komparatif model warna dalam pengolahan citra | RGB, HSV, CIE, luma-chroma | Studi literatur + eksperimen komparatif | Pemilihan color space sangat bergantung pada konteks tugas dan mempengaruhi akurasi serta efisiensi komputasi | Tidak spesifik pada ekstraksi warna kulit; belum mengarah ke sistem rekomendasi warna pakaian [9] |
| 2 | Chang & Mukai | 2022 | Dominant color extraction berbasis K-Means + graph cut + analisis fitur warna | CIELAB + fitur warna (saturasi, kontras, area) | Evaluasi citra + uji persepsi manusia (skala 1–5) | Metode mampu menangkap warna dominan termasuk area kecil dengan lebih stabil | Tidak fokus pada warna kulit manusia; belum digunakan untuk personalisasi rekomendasi fashion [3] |
| 3 | Moumene dkk. | 2022 | Deteksi warna kulit real-time menggunakan adaptive HSV thresholding | RGB, HSV, YCrCb | Dataset Pratheepan & HGR; evaluasi F1-score dan waktu komputasi | HSV memberikan keseimbangan terbaik antara akurasi dan efisiensi dibanding pendekatan lain | Hanya menghasilkan segmentasi kulit, belum mengubahnya menjadi representasi warna berbasis clustering [2] |
| 4 | Komori & Eguchi | 2021 | Formulasi teoritis clustering (K-Means, FCM, GMM) dalam satu kerangka unified | — | Simulasi dan benchmark dataset | Memberikan dasar matematis hubungan antar metode clustering dan fleksibilitas pemodelan | Tidak spesifik pada data citra atau warna kulit; perlu implementasi kontekstual pada domain visual [4] |
| 5 | Wei & Zhang | 2022 | Penerapan psikologi warna dalam desain fashion berbasis survei konsumen | — | Survei 100 responden; evaluasi fuzzy (skala 1–5) | Warna memiliki pengaruh signifikan terhadap persepsi dan preferensi konsumen dalam fashion | Tidak berbasis pengolahan citra; belum mempertimbangkan personalisasi berdasarkan warna kulit individu [8] |

Tabel ini digunakan untuk menganalisis posisi penelitian yang dilakukan dibandingkan dengan studi sebelumnya secara sistematis dan terstruktur. Berdasarkan tabel tersebut, dilakukan identifikasi kesenjangan penelitian yang menjadi dasar pengembangan sistem dalam penelitian ini.

**2.2 Tinjauan Teori**

### 2.2.1 Konsep Dasar Pengolahan Citra Digital

Pengolahan citra digital merupakan disiplin ilmu yang berfokus pada manipulasi dan analisis citra menggunakan sistem komputasi. Secara matematis, sebuah citra digital dapat direpresentasikan sebagai fungsi intensitas cahaya dua dimensi , di mana dan y melambangkan koordinat spasial, sedangkan amplitudo pada pasangan koordinat tersebut menyatakan nilai intensitas atau warna pada titik tersebut. Setiap titik fundamental dalam grid representasi ini dikenal sebagai piksel (*pixel* atau *picture element*), yang menyimpan informasi kuantitatif visual pembentuk citra secara keseluruhan [9].

Dalam analisis berbasis warna, distribusi frekuensi dari nilai intensitas piksel pada sebuah citra sering divisualisasikan menggunakan histogram warna. Histogram ini memberikan gambaran statistik mengenai komposisi warna, pencahayaan, dan tingkat kontras suatu citra. Pemahaman terhadap distribusi piksel melalui histogram sangat krusial, karena variasi iluminasi pada saat akuisisi citra dapat secara drastis mengubah profil warna objek yang terekam [2], [9].

Secara operasional, sistem pengolahan citra digital untuk keperluan analisis visual umumnya melewati tiga tahapan dasar yang saling berkesinambungan:

1. **Pra-pengolahan (*preprocessing*)**: Tahap awal ini bertujuan untuk meningkatkan kualitas visual citra dan mempersiapkannya untuk analisis lebih lanjut. Operasi yang umum dilakukan meliputi normalisasi pencahayaan, penyesuaian ukuran (*resizing*), serta pengurangan derau (*noise reduction*). Pada konteks citra wajah, tahapan ini krusial untuk meminimalisasi gangguan sebelum informasi warna diekstrak.
2. **Segmentasi (*segmentation*)**: Proses ini membagi citra ke dalam beberapa area atau *region* yang memiliki kesamaan atribut tertentu, dengan tujuan memisahkan objek utama (*region of interest*) dari latar belakang (*background*). Dalam domain ekstraksi warna kulit, segmentasi sering diimplementasikan melalui aturan ambang batas (*thresholding*) untuk memisahkan kelas *skin* dan *non-skin* berdasarkan komponen ruang warna [1], [2].
3. **Ekstraksi Fitur (*feature extraction*)**: Setelah objek target berhasil disegmentasi, tahap selanjutnya adalah mengekstrak atribut atau karakteristik khusus yang dapat merepresentasikan objek tersebut dalam bentuk yang lebih ringkas. Fitur dapat berupa tekstur, bentuk geometris, atau representasi warna. Pada penelitian ini, ekstraksi fitur difokuskan pada perumusan nilai warna (seperti warna dominan atau *centroid*) dari area kulit yang telah disegmentasi, yang nantinya akan dikelompokkan menggunakan teknik *clustering* [3].

Tiga fondasi dasar pengolahan citra inilah yang menjadi kerangka kerja operasional dalam mengekstraksi parameter warna kulit wajah secara komputasional, sebelum nantinya diterjemahkan ke dalam bentuk *signature* warna yang relevan untuk sistem rekomendasi.

### 2.2.2 Teori Ruang Warna (Color Space)

Ruang warna (*color space*) merupakan spesifikasi matematis yang mendefinisikan suatu warna berdasarkan kombinasi nilai numerik tertentu pada sistem koordinat multidimensi. Secara konseptual, literatur membedakan antara model warna (*color model*) sebagai representasi numerik abstrak, dengan ruang warna yang merupakan implementasi spesifik dari model tersebut beserta rentang warnanya (*gamut*) [9]. Pemilihan ruang warna yang tepat sangat krusial dalam pengolahan citra karena setiap representasi menawarkan kompromi yang berbeda antara akurasi persepsi manusia, kompleksitas komputasi, dan ketahanan terhadap variasi pencahayaan [9]. Pada penelitian ekstraksi warna kulit ini, digunakan tiga ruang warna dengan karakteristik yang saling melengkapi:

**1. RGB (*Red, Green, Blue*)**

Ruang warna RGB merupakan model *additive* yang menjadi standar utama pada perangkat keras seperti sensor kamera digital dan monitor [1], [9]. Ruang ini merepresentasikan warna sebagai kombinasi intensitas cahaya merah, hijau, dan biru, yang direpresentasikan dalam koordinat kartesian tiga dimensi. Meskipun sangat efisien secara komputasi untuk akuisisi citra mentah, model RGB memiliki kelemahan struktural yang signifikan untuk analisis visual tingkat lanjut. Ketiga komponen warnanya memiliki tingkat korelasi yang sangat tinggi dan ketiganya secara bersamaan memuat informasi kecerahan cahaya (*luminance*) [1]. Konfigurasi ini menyebabkan nilai piksel pada ruang RGB menjadi sangat sensitif dan mudah bergeser apabila terdapat perubahan iluminasi lingkungan, sehingga kurang optimal jika digunakan secara tunggal untuk deteksi warna kulit [2].

**2. HSV (*Hue, Saturation, Value*)**

Model HSV dirancang untuk mendeskripsikan warna dengan parameter yang lebih selaras dengan intuisi visual manusia [9]. Komponen *Hue* mendefinisikan jenis gelombang warna (seperti merah, kuning, atau biru) dalam bentuk sudut melingkar, *Saturation* mengukur tingkat kemurnian atau saturasi warna, sedangkan *Value* merepresentasikan intensitas kecerahan absolut [1]. Keunggulan utama dari transformasi RGB ke HSV dalam ekstraksi fitur adalah kemampuannya memisahkan informasi krominansi (*Hue* dan *Saturation*) dari informasi luminansi (*Value*). Pemisahan ini memungkinkan penyusunan aturan segmentasi piksel kulit yang jauh lebih *robust* terhadap keberadaan bayangan (*shadows*) dan sorotan cahaya (*highlights*), menjadikannya sangat kompetitif untuk pemrosesan *real-time* [1], [2].

**3. CIELAB**

Ruang warna CIELAB diperkenalkan oleh *Commission Internationale de l'Eclairage* (CIE) untuk mengatasi kelemahan RGB terkait keseragaman persepsi (*perceptual uniformity*) [9]. Dalam ruang CIELAB, jarak geometris antar titik warna dirancang agar berbanding lurus dengan perbedaan warna yang dirasakan oleh sistem visual manusia. Komponen menyatakan tingkat kecerahan, sementara merepresentasikan transisi kromatik dari hijau ke merah, dan merepresentasikan transisi dari biru ke kuning [3]. Ruang warna ini terbukti sangat krusial dalam analisis fitur manusia, khususnya karena kemampuannya merepresentasikan warna kulit (*skin tone*) secara presisi. Analisis *skin tone* sering kali diukur menggunakan standar sudut topologi individu (*Individual Typology Angle* atau ITA) yang dikalkulasi langsung dari komponen dan pada ruang warna ini [13]. Lebih lanjut, konversi data warna ke dalam ruang LAB sangat penting untuk menghitung metrik jarak warna (seperti formula CIEDE2000) agar penentuan kemiripan warna kulit benar-benar selaras dengan akurasi perseptual penglihatan manusia [14]. Oleh karena sifatnya yang konsisten secara visual, ruang warna ini menjadi standar ideal untuk ekstraksi warna dominan dan evaluasi kualitas jarak *centroid* [3], [5].

Sebagai justifikasi pemilihan pendekatan evaluasi multi-ruang warna dalam penelitian ini, perbandingan karakteristik dari ketiga representasi tersebut diuraikan pada Tabel 2.2.

Tabel 2.2 Perbandingan Karakteristik Color Space

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Color Space** | **Representasi Komponen** | **Kelebihan** | **Kekurangan** | **Cocok untuk** |
| RGB | *Red, Green, Blue* | Perhitungan sederhana, merupakan format standar akuisisi pada perangkat keras. | Sensitif terhadap cahaya, kurang selaras dengan persepsi visual manusia. | Akuisisi citra awal, *display* perangkat, dan pemrosesan basis. |
| HSV | *Hue, Saturation, Value* | Memisahkan kecerahan dan warna, lebih *robust* terhadap variasi iluminasi. | Singulitas pada nilai kecerahan ekstrem, transformasi memerlukan komputasi tambahan. | Deteksi objek, segmentasi *real-time*, dan analisis berbasis *thresholding*. |
| CIELAB |  | Memiliki *perceptual uniformity* yang tinggi, konsisten dengan penglihatan manusia. | Komputasi transformasi non-linear yang paling berat, bergantung pada *reference white*. | Evaluasi jarak warna, *clustering* warna dominan, dan representasi akurasi perseptual. |

Paparan teori dan tabel perbandingan di atas memperlihatkan bahwa setiap ruang warna memiliki peruntukan yang spesifik. Penggunaan evaluasi *multi-color space* menjadi esensial untuk mengisolasi area kulit dari latar belakang secara adaptif, sekaligus menjaga agar representasi nilai warna akhir yang dihasilkan oleh algoritma klastering tetap relevan secara perseptual. Pemetaan komputasional yang presisi ini nantinya akan menjadi fondasi kokoh untuk rekomendasi *fashion*, guna memastikan warna pakaian—maupun atribut gaya spesifik seperti pemilihan warna hijab—benar-benar serasi dengan *tone* kulit penggunanya [8], [9], [16].

![](data:image/png;base64...)

Gambar 2.1 Ilustrasi Visual Model Ruang Warna (RGB, HSV, dan CIELAB)

### 2.2.3 Teori Clustering

*Clustering* atau pengelompokan merupakan salah satu teknik analisis data eksploratif dalam ranah pembelajaran mesin tanpa pengawasan (*unsupervised learning*). Algoritma ini bertujuan untuk menemukan struktur tersembunyi dengan cara mengorganisasikan kumpulan objek data ke dalam beberapa kelompok (*cluster*) tanpa adanya label data awal [6]. Prinsip fundamental dari teknik ini adalah memaksimalkan tingkat kesamaan (*similarity*) antar anggota di dalam satu kelompok yang sama (*intra-cluster*), dan pada saat yang bersamaan meminimalkan tingkat kesamaan antar anggota yang berada di kelompok yang berbeda (*inter-cluster*). Dalam konteks pengolahan citra dan ekstraksi fitur warna, metode *cluster analysis* terbukti sangat efektif untuk memisahkan, memetakan, serta meringkas distribusi piksel warna kulit wajah menjadi representasi titik pusat (*centroid*) yang bermakna [13].

Secara metodologis, literatur mengklasifikasikan algoritma *clustering* ke dalam beberapa tipe utama yang memiliki pendekatan komputasi berbeda:

1. ***Partitioning Clustering***: Mengelompokkan data secara langsung ke dalam jumlah K kelompok yang telah ditentukan, di mana setiap objek data secara tegas (*hard clustering*) hanya dapat menjadi anggota dari satu *cluster* tunggal. Contoh paling fundamental dari tipe ini adalah algoritma *K-Means* [6].
2. ***Fuzzy-based Clustering***: Memberikan derajat keanggotaan (*membership degree*) bagi setiap titik data terhadap seluruh *cluster* yang ada. Pendekatan *soft clustering* ini mengizinkan satu objek untuk berada di beberapa *cluster* sekaligus dengan probabilitas tertentu. Algoritma seperti *Fuzzy C-Means* (FCM) dan *Gaussian Mixture Model* (GMM) sering diimplementasikan untuk menangani data visual yang memiliki batas transisi warna yang ambigu [4], [5].
3. ***Three-Way Clustering***: Merupakan paradigma perluasan yang membagi hasil pengelompokan ke dalam tiga area konseptual: wilayah inti (*core region*), wilayah pinggiran (*fringe region*), dan derau (*noise*). Dalam ranah pengolahan citra digital, pendekatan ini dapat diintegrasikan dengan operasi spasial seperti pelembutan (*blurring*) untuk mendapatkan area dengan kepadatan data tinggi, dan penajaman (*sharpening*) untuk mengekstraksi area batas, sehingga mampu menghasilkan *cluster* yang jauh lebih *robust* terhadap data pencilan [7].

Keberhasilan seluruh proses pengelompokan data visual sangat bergantung pada pemilihan metrik jarak (*distance metric*). Dalam analisis citra, konsep "jarak" bukan berarti jarak fisik, melainkan kalkulasi matematis untuk mengukur tingkat kesamaan (*similarity*) antar titik koordinat warna; semakin kecil nilai jaraknya, semakin identik pula kedua warna tersebut. Jarak *Euclidean* (*Euclidean distance*) merupakan metrik geometris yang paling standar dan sederhana, yang bekerja ibarat menarik garis lurus antar dua piksel di dalam ruang fitur linier [6].

Meskipun jarak *Euclidean* sangat efisien secara komputasi, metrik ini memiliki kelemahan fundamental ketika diterapkan pada warna: kedekatan secara matematis di ruang linier tidak selalu sejalan dengan kemiripan yang dilihat oleh mata manusia. Oleh karena itu, kalkulasi jarak warna—terutama untuk ekstraksi warna kulit manusia yang memiliki gradasi sangat halus—membutuhkan formulasi yang selaras dengan sistem penglihatan manusia. Literatur menunjukkan bahwa penggunaan jarak warna berbasis metrik perseptual yang lebih maju, seperti formula CIEDE2000 pada ruang warna CIELAB, mampu memberikan tingkat keakuratan yang jauh lebih tinggi [14]. Berbeda dengan perhitungan garis lurus biasa, CIEDE2000 memperhitungkan pembobotan kroma (*chroma*) dan rona (*hue*) secara non-linear. Metrik ini secara adaptif menyesuaikan kalkulasi berdasarkan kepekaan mata manusia, sehingga penentuan kemiripan antar pusat klaster (*centroid*) warna benar-benar selaras dengan akurasi persepsi visual (*perceptual accuracy*) [14]. Oleh karena itu, sinergi antara metode *clustering* dan metrik jarak yang tepat menjadi kunci untuk mengekstrak fitur warna yang valid.

### 2.2.4 Algoritma K-Means

Algoritma *K-Means* merupakan salah satu metode pengelompokan partisional (*partitioning clustering*) yang paling luas digunakan dalam analisis data dan visi komputer karena tingkat efisiensi dan kesederhanaannya [6]. Prinsip kerja utama dari *K-Means* adalah membagi sekumpulan observasi data yang berjumlah ke dalam sejumlah kelompok (*cluster*) yang telah ditetapkan sebelumnya (*a priori*). Dalam konteks ekstraksi warna, setiap piksel direpresentasikan sebagai titik data dalam koordinat ruang warna, dan *K-Means* bertugas untuk menemukan pusat klaster (*centroid*) yang dapat secara optimal mewakili kumpulan piksel yang memiliki kemiripan warna [5].

Secara matematis, *K-Means* beroperasi dengan mengoptimalkan fungsi objektif yang dikenal sebagai *within-cluster sum of squares* (WCSS). Algoritma ini berusaha meminimalkan total varians atau kuadrat jarak antara setiap titik data dengan *centroid* pada klasternya masing-masing. Fungsi objektif tersebut dirumuskan sebagai berikut [6]:

di mana:

1. adalah total nilai fungsi objektif.
2. adalah jumlah klaster yang diinginkan.
3. adalah titik data ke-(nilai koordinat warna piksel).
4. adalah himpunan titik data yang tergabung dalam klaster ke-.
5. adalah nilai rata-rata (*mean*) atau *centroid* dari klaster ke-.
6. melambangkan kuadrat jarak (umumnya jarak *Euclidean*) antara titik data dan *centroid*.

Proses optimasi fungsi objektif tersebut dicapai melalui tahapan iteratif (*Lloyd's algorithm*) yang mencakup empat langkah utama:

1. Inisialisasi: Menentukan jumlah klaster (K) dan memilih letak K buah titik *centroid* awal secara acak di dalam ruang data.
2. Alokasi Data (*Assignment*): Menghitung jarak setiap titik data ke seluruh *centroid* yang ada, kemudian mengalokasikan data tersebut secara tegas (*hard assignment*) ke dalam klaster dengan jarak *centroid* terdekat [4].
3. Pembaruan Pusat Klaster (*Update*): Menghitung ulang koordinat posisi *centroid* untuk setiap klaster berdasarkan nilai rata-rata aritmatika dari seluruh titik data yang baru saja dialokasikan ke klaster tersebut.
4. Konvergensi: Mengulangi langkah 2 dan 3 secara terus-menerus hingga letak *centroid* tidak lagi mengalami perubahan yang signifikan atau telah mencapai batas iterasi maksimum [6].

Ditinjau dari aspek komputasi, *K-Means* memiliki kompleksitas waktu , di mana adalah jumlah data, adalah jumlah iterasi, dan adalah dimensi fitur. Kompleksitas linear ini menjadikan *K-Means* sangat ringan dan cocok diterapkan pada pengolahan citra digital yang melibatkan ratusan ribu hingga jutaan piksel [6]. Meskipun demikian, algoritma ini memiliki keterbatasan fundamental. *K-Means* sangat sensitif terhadap nilai inisialisasi letak *centroid* awal dan kehadiran derau (*noise*) atau data pencilan (*outlier*). Selain itu, kewajiban untuk mendefinisikan jumlah di awal proses sering kali menjadi tantangan, sehingga literatur mendorong pemanfaatan skema *unsupervised* untuk mencari nilai yang paling optimal [6].

Untuk memperkuat justifikasi pemilihan algoritma *K-Means* dalam membangun representasi warna kulit (*skin signature*), perlu dilakukan komparasi dengan pendekatan *clustering* lain yang umum dipakai dalam pengolahan citra. Perbandingan tersebut dirangkum pada Tabel 2.3.

Tabel 2.3 Perbandingan Metode Clustering

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Metode** | **Prinsip Dasar** | **Sensitif terhadap Noise** | **Kompleksitas** | **Kelebihan** |
| *K-Means* | *Hard assignment* berbasis jarak ke *centroid*. | Tinggi | Rendah | Sangat efisien, komputasi ringan untuk data citra berjumlah besar, mudah diimplementasikan [6]. |
| *Fuzzy C-Means* (FCM) | *Soft assignment* berbasis derajat keanggotaan probabilitas. | Sedang | Sedang | Mampu menangani ambiguitas area batas (*fringe region*) antar warna yang bergradasi [4], [5]. |
| *Gaussian Mixture Model* (GMM) | Pemodelan data sebagai kombinasi dari beberapa distribusi probabilitas Gaussian. | Rendah | Tinggi | Sangat adaptif untuk bentuk distribusi data yang kompleks atau elips, bukan hanya sferis [4]. |

Berdasarkan komparasi di atas, *K-Means* dipilih sebagai metode ekstraksi warna kulit karena fokus penelitian ini membutuhkan efisiensi dan kestabilan kalkulasi untuk mencapai waktu pemrosesan yang dapat diterima pada sistem rekomendasi, sambil tetap mempertimbangkan evaluasi penentuan nilai yang optimal [6].

![](data:image/png;base64...)

Gambar 2.2 Konsep dan cara kerja K-Means pada ekstraksi warna kulit

### 2.2.5 Evaluasi Kualitas Clustering

Mengingat *clustering* merupakan metode pembelajaran tanpa pengawasan (*unsupervised learning*), algoritma ini tidak memiliki label data aktual (*ground truth*) untuk mengukur akurasi secara langsung. Oleh karena itu, evaluasi performa *clustering*—termasuk penentuan jumlah klaster optimal—dilakukan melalui metrik validasi internal (*internal validity metrics*). Metrik ini mengukur kualitas arsitektur klaster berdasarkan dua prinsip utama: kekompakan data di dalam satu klaster yang sama (*intra-cluster cohesion*) dan tingkat keterpisahan data antar klaster yang berbeda (*inter-cluster separation*) [6].

Dalam mengevaluasi hasil ekstraksi warna kulit, stabilitas dan keunikan setiap pusat warna (*centroid*) dapat diukur menggunakan tiga metrik evaluasi standar berikut:

**1. *Silhouette Score***

Metrik ini mengukur seberapa mirip suatu objek data dengan klasternya sendiri dibandingkan dengan klaster lain yang berdekatan. Nilai *Silhouette Score* untuk satu titik data $i$ dirumuskan sebagai:

di mana:

1. adalah rata-rata jarak titik ke seluruh titik lain di dalam klaster yang sama (representasi kohesi).
2. adalah rata-rata jarak minimum dari titik ke titik-titik pada klaster terdekat yang bukan klasternya (representasi separasi).

Rentang nilai rata-rata *Silhouette Score* berada di antara -1 hingga 1. Nilai yang mendekati 1 mengindikasikan bahwa titik data berada pada klaster yang sangat tepat dan terpisah jauh dari klaster lain, sedangkan nilai negatif menunjukkan bahwa data kemungkinan besar dialokasikan pada klaster yang salah [6].

**2. *Davies-Bouldin Index* (DBI)**

*Davies-Bouldin Index* melakukan evaluasi dengan menghitung rasio antara sebaran data di dalam klaster (*within-cluster scatter*) dan jarak antar pusat klaster (*between-cluster separation*). Formula matematis DBI didefinisikan sebagai:

di mana:

1. melambangkan jumlah total klaster.
2. dan melambangkan tingkat sebaran data atau diameter internal dari klaster dan klaster .
3. melambangkan jarak geometris (seperti jarak *Euclidean* atau jarak perseptual CIEDE2000) antara pusat klaster dan pusat klaster .

Interpretasi nilai DBI berbanding terbalik dengan *Silhouette Score*. Semakin kecil nilai DBI (mendekati 0), semakin baik kualitas *clustering* tersebut, karena nilai yang rendah mengindikasikan bahwa klaster-klaster yang terbentuk sangat padat secara internal dan terpisah sangat jauh antara satu sama lain [6].

**3. *Calinski-Harabasz Index* (CHI)**

Sering juga disebut sebagai kriteria rasio varians (*variance ratio criterion*), metrik ini mengevaluasi kualitas pengelompokan berdasarkan perbandingan antara varians antar-klaster dan varians intra-klaster. Rumus CHI dinyatakan sebagai:

di mana:

1. adalah *trace* dari matriks dispersi antar-klaster (mengukur seberapa jauh setiap *centroid* dari pusat gravitasi seluruh data).
2. adalah *trace* dari matriks dispersi intra-klaster (mengukur sebaran data terhadap *centroid* klasternya masing-masing).
3. adalah jumlah total titik data (piksel).
4. adalah jumlah klaster.

Semakin tinggi nilai *Calinski-Harabasz Index*, semakin optimal partisi data yang dihasilkan. Dalam penelitian ekstraksi warna kulit, kombinasi ketiga metrik ini digunakan secara bersamaan untuk memastikan bahwa pemilihan jumlah tidak hanya efisien secara komputasi, tetapi juga menghasilkan perwakilan palet warna yang kohesif dan dapat dibedakan secara visual oleh sistem rekomendasi [6], [13].

### 2.2.6 Konsep Sistem Rekomendasi

Sistem rekomendasi pada dasarnya merupakan algoritma penyaringan informasi yang dirancang untuk memprediksi preferensi atau tingkat ketertarikan seorang pengguna terhadap suatu item tertentu. Dalam ekosistem ritel digital dan *fashion*, sistem ini berperan krusial sebagai antarmuka cerdas yang mengarahkan konsumen pada pilihan produk yang paling relevan dengan karakteristik pribadi mereka. Pada konteks penelitian ini, sistem rekomendasi difokuskan untuk menjembatani hasil komputasi (ekstraksi fitur warna kulit) dengan teori estetika visual, sehingga luaran yang dihasilkan bukan sekadar tebakan acak, melainkan saran palet warna pakaian yang memiliki landasan kecocokan secara personal [8], [16].

Secara arsitektural, sistem rekomendasi dapat dibangun melalui beberapa paradigma pendekatan (*filtering*). Tiga pendekatan utama yang sering dieksplorasi dalam literatur adalah sebagai berikut:

* + - 1. Pendekatan Berbasis Aturan (*Rule-Based Recommendation*) Metode ini beroperasi dengan mengandalkan sekumpulan aturan logis (seperti logika IF-THEN) dan basis pengetahuan (*knowledge base*) yang diformulasikan dari kepakaran domain tertentu. Dalam sistem rekomendasi warna *fashion*, pendekatan *rule-based* sangat relevan diimplementasikan karena kecocokan warna tidak selalu membutuhkan data historis pengguna, melainkan dapat dipetakan secara deterministik melalui aturan baku teori harmoni warna terhadap nilai koordinat representasi kulit (*skin tone*) yang telah diekstrak [14].
      2. Penyaringan Berbasis Konten (*Content-Based Filtering*) Pendekatan ini memberikan rekomendasi dengan cara menganalisis deskripsi atau atribut dari item yang pernah dipilih atau disukai oleh pengguna di masa lalu, kemudian mencari item baru yang memiliki fitur serupa. Meskipun metode ini sangat tangguh untuk personalisasi mandiri, kelemahan utamanya adalah potensi spesialisasi yang berlebihan (*over-specialization*), di mana pengguna hanya akan direkomendasikan warna-warna yang berulang tanpa adanya variasi silang.
      3. Rekomendasi Hibrida (*Hybrid Recommendation*) Sistem hibrida menggabungkan dua atau lebih teknik rekomendasi (misalnya mengawinkan *rule-based* dengan *content-based*) guna mengeliminasi kelemahan dari masing-masing metode tunggal. Pendekatan ini umumnya menghasilkan tingkat akurasi yang lebih tinggi dan cakupan rekomendasi yang lebih dinamis pada aplikasi berskala besar.

Untuk batasan ruang lingkup skripsi ini, paradigma yang dibangun lebih menitikberatkan pada pendekatan berbasis aturan. Sistem memosisikan beban komputasi utamanya pada akurasi penemuan *centroid* warna kulit wajah menggunakan *clustering* [16]. Setelah pusat warna kulit pengguna berhasil diisolasi dan divalidasi pada ruang warna terbaik, sistem akan menerapkan matriks aturan psikologi dan harmoni warna untuk mendeduksi warna pakaian apa saja yang secara perseptual paling serasi bagi pengguna tersebut.

### 2.2.7 Teori Harmoni Warna dalam Fashion

Pemilihan warna dalam desain fesyen (*fashion design*) bukan sekadar keputusan estetika acak, melainkan sebuah proses yang sangat dipengaruhi oleh prinsip-prinsip psikologi warna dan teori harmoni. Literatur menunjukkan bahwa warna memiliki dampak psikologis yang signifikan terhadap emosi, persepsi, dan perilaku konsumen [8]. Penerapan warna yang tepat pada pakaian tidak hanya meningkatkan daya tarik visual, tetapi juga memberikan kenyamanan psikologis bagi pemakainya. Dalam konteks personalisasi gaya, kecocokan warna pakaian tersebut tidak dapat dipisahkan dari karakteristik fisik bawaan individu, khususnya warna kulit (*skin tone*) [14].

Harmoni warna secara definisi merujuk pada kombinasi susunan warna yang menyenangkan secara visual dan mampu menciptakan rasa keseimbangan perseptual. Dalam ekosistem *fashion*, teori harmoni warna sering kali dioperasionalkan menggunakan roda warna (*color wheel*) untuk merumuskan palet pakaian yang serasi dengan warna dasar tubuh manusia. Beberapa skema harmoni yang paling umum diimplementasikan sebagai basis aturan (*rule-based*) dalam sistem rekomendasi meliputi:

1. Harmoni Komplementer (*Complementary Harmony*): Memadukan warna yang saling berhadapan persis di roda warna. Skema ini menciptakan kontras yang tinggi dan menonjolkan kedua warna agar terlihat lebih dinamis.
2. Harmoni Analog (*Analogous Harmony*): Menggabungkan dua hingga tiga warna yang posisinya saling berdampingan di roda warna, menghasilkan kombinasi dengan transisi yang lembut dan alami.
3. Harmoni Monokromatik (*Monochromatic Harmony*): Menggunakan berbagai variasi nilai kecerahan (*lightness*) dan saturasi dari satu jenis rona dasar (*hue*) yang sama.

![](data:image/png;base64...)

Gambar 2.3 *Color Wheel* Dan Skema Harmoni Teoritis

Implementasi teori harmoni ini menjadi landasan evaluasi fungsional dalam sistem rekomendasi, karena warna pakaian harus mampu melengkapi dan tidak bertabrakan dengan representasi warna kulit pengguna. Penelitian terkait menegaskan bahwa pencocokan warna pakaian yang berbasis pada klasifikasi *tone* kulit sangat esensial untuk memastikan penampilan yang serasi, baik untuk busana secara umum maupun untuk atribut spesifik seperti pemilihan warna hijab [16].

Melalui pendekatan ini, representasi titik pusat klaster (*centroid*) warna kulit yang sebelumnya diekstrak menggunakan algoritma *K-Means* akan diposisikan sebagai warna jangkar (*anchor color*). Sistem kemudian menerapkan aturan matematis harmoni warna, yang dikalkulasi menggunakan metrik jarak pada ruang warna seperti CIELAB, untuk mendeduksi kandidat warna pakaian yang paling kompatibel [14]. Sinergi antara ekstraksi komputasional dan teori harmoni ini memastikan bahwa luaran rekomendasi sistem tidak hanya akurat secara matematis, tetapi juga dapat dipertanggungjawabkan secara estetika dan psikologi desain [8], [16].

# BAB III METODOLOGI

## 3.1 Desain Penelitian

Penelitian ini menggunakan pendekatan eksperimental kuantitatif yang berfokus pada pengembangan dan evaluasi *pipeline* sistem informasi berbasis pengolahan citra digital (*digital image processing*). Desain penelitian ini dirancang untuk menguji secara komparatif efektivitas berbagai ruang warna (*color space*) dan algoritma *unsupervised learning* dalam mengekstraksi parameter biologis manusia, yakni warna kulit, untuk kebutuhan sistem rekomendasi personal. Kerangka kerja penelitian disusun secara sistematis mengikuti alur komputasi yang meliputi tahap akuisisi citra, prapemrosesan (*preprocessing*), transformasi ruang warna, klasterisasi fitur, hingga tahap formulasi rekomendasi busana.

Fokus utama dari desain ini adalah mengatasi permasalahan ketidakstabilan representasi warna yang disebabkan oleh variasi intensitas cahaya (*illumination variance*). Oleh karena itu, penelitian ini mendesain skenario pengujian multi-dimensi menggunakan ruang warna RGB, HSV, dan YCbCr untuk membedakan antara informasi pencahayaan (*luminance*) dan informasi warna murni (*chrominance*) [1], [21]. Melalui desain eksperimental ini, sistem akan mengevaluasi akurasi sentroid yang dihasilkan oleh algoritma *K-Means clustering* terhadap nilai kebenaran (*ground truth*) dari spektrum warna kulit individu [6], [19]. Hasil akhir dari metodologi ini adalah sebuah model sistem informasi yang mampu mentransformasikan data piksel mentah menjadi keputusan rekomendasi yang berbasis pada metrik jarak warna perseptual (*perceptual color distance*) [14].

*![](data:image/png;base64...)*

Gambar 3.1 Diagram Alur Sistem dan Desain Eksperimental

## 3.2 Metode Pengumpulan Data

Metode pengumpulan data dalam penelitian ini dibagi menjadi dua kategori utama, yakni data citra wajah manusia dan data preferensi warna pakaian yang berbasis pada teori harmoni warna. Penataan dataset dilakukan secara teliti untuk memastikan bahwa sistem memiliki basis pengetahuan yang kuat mengenai keragaman warna kulit manusia (*skin tone diversity*) [15].

### 3.2.1 Dataset Citra Wajah (Data Primer dan Sekunder)

Data citra yang digunakan merupakan kombinasi dari dataset publik berskala besar dan pengambilan sampel mandiri. Dataset sekunder diambil dari repositori penglihatan komputer (*computer vision*) seperti dataset SFHQ (*Skin Feature High Quality*) yang menyediakan ribuan citra wajah dengan resolusi tinggi dan variabilitas etnis yang luas [14]. Penggunaan dataset publik ini bertujuan untuk mengkalibrasi sensitivitas algoritma terhadap spektrum warna kulit yang sangat kontras, mulai dari *very light* hingga *very dark* [15].

Selain data sekunder, penelitian ini melakukan pengumpulan data primer melalui pengambilan foto wajah subjek menggunakan sensor kamera digital dalam kondisi pencahayaan yang terkontrol dan tidak terkontrol (alami). Spesifikasi teknis pengambilan data primer adalah sebagai berikut:

1. **Sudut Pandang:** Citra wajah tampak depan (*frontal face*) dengan ekspresi netral.
2. **Resolusi:** Minimal 1280 x 720 piksel untuk memastikan kerapatan piksel (*pixel density*) memadai bagi proses klasterisasi [12].
3. **Kondisi Pencahayaan:** Variasi antara cahaya dalam ruangan (*indoor*) sebesar 300-500 lux dan cahaya luar ruangan (*outdoor*) untuk menguji ketangguhan model transformasi ruang warna [10], [20].

### 3.2.2 Dataset Rekomendasi Warna Pakaian

Data pendukung berupa aturan rekomendasi warna disusun berdasarkan studi psikologi warna dalam desain busana dan prinsip *seasonal color analysis* [8]. Data ini dikumpulkan melalui tinjauan pustaka sistematis terhadap standar industri *fashion* yang memetakan kecocokan warna kain tertentu dengan profil *undertone* kulit (dingin, hangat, atau netral) [16]. Dataset ini kemudian dikonversi ke dalam nilai digital (HEX atau RGB) yang akan digunakan oleh mesin sistem informasi sebagai tabel rujukan (*lookup table*) saat mencocokkan hasil ekstraksi warna kulit pengguna dengan rekomendasi pakaian yang paling harmonis secara visual [13], [17].

### 3.2.3 Instrumen Penelitian

Instrumen yang digunakan dalam proses pengumpulan dan pengolahan data meliputi perangkat keras berupa komputer dengan spesifikasi komputasi grafis yang memadai untuk menjalankan algoritma *clustering* secara iteratif, serta perangkat lunak pengembangan berbasis Python. Pustaka pemrograman seperti OpenCV digunakan untuk manipulasi piksel, Scikit-Learn untuk implementasi *unsupervised machine learning*, dan Matplotlib untuk visualisasi hasil evaluasi ruang warna [4], [22]. Seluruh data yang terkumpul disimpan dalam format repositori digital yang terstruktur guna memudahkan proses validasi silang pada tahap pengujian sistem.

## 3.3 Tahapan Penelitian

Prosedur penelitian ini dikembangkan melalui pendekatan sistematis yang lazim digunakan dalam rekayasa sistem informasi dan pengolahan citra digital. Alur penelitian dirancang untuk memastikan bahwa setiap tahap pemrosesan data berkontribusi langsung pada akurasi rekomendasi akhir. Secara garis besar, tahapan penelitian ini dibagi menjadi empat fase utama: akuisisi dan kondisionalitas data, prapemrosesan citra (*preprocessing*), ekstraksi fitur warna kulit menggunakan multi-ruang warna dan algoritma klasterisasi, serta fase evaluasi dan pemetaan rekomendasi.

Fase pertama diawali dengan pengumpulan dataset yang merepresentasikan diversitas *skin tone* manusia untuk memastikan inklusivitas sistem [15]. Fase kedua, prapemrosesan, dilakukan untuk meningkatkan kualitas data mentah agar algoritma ekstraksi dapat bekerja secara optimal [12]. Fase ketiga merupakan inti dari penelitian ini, di mana dilakukan transformasi ruang warna (*color space transformation*) dari RGB ke HSV dan YCbCr untuk meminimalkan efek pencahayaan, diikuti dengan penerapan algoritma *K-Means clustering* untuk menentukan sentroid warna kulit [1], [21]. Terakhir, nilai sentroid tersebut dievaluasi menggunakan metrik jarak warna perseptual untuk memberikan output berupa palet warna pakaian yang paling harmonis [14], [17].

![](data:image/png;base64...)

Gambar 3.2 Flowchart Tahapan Penelitian Sistem Rekomendasi

## 3.4 Prapemrosesan Citra Digital

Tahap prapemrosesan bertujuan untuk mereduksi derau (*noise*) dan menstandardisasi input citra agar memiliki karakteristik yang konsisten. Langkah awal adalah melakukan penyesuaian ukuran (*resizing*) citra menjadi dimensi yang seragam. Standardisasi dimensi ini krusial dalam sistem informasi untuk menjaga efisiensi penggunaan memori dan kecepatan waktu eksekusi saat algoritma klasterisasi melakukan iterasi pada ribuan piksel [6], [12].

Selanjutnya, diaplikasikan penapis *Gaussian Blur* untuk menghaluskan tekstur kulit yang tidak rata dan menghilangkan *pixel-level noise* yang ditimbulkan oleh sensor kamera. Penggunaan *Gaussian filter* sebelum proses klasterisasi terbukti mampu meningkatkan akurasi sentroid warna karena algoritma tidak lagi terdistraksi oleh variasi warna kecil pada pori-pori atau artefak citra [14]. Selain itu, dilakukan proses normalisasi intensitas cahaya (*illumination normalization*) untuk mengurangi dampak bayangan (*shadows*) yang dapat menyebabkan pergeseran nilai warna pada ruang warna RGB [10], [24].

## 3.5 Perancangan Sistem

Perancangan sistem dalam penelitian ini difokuskan pada pengembangan arsitektur informasi yang mampu mengintegrasikan algoritma pengolahan citra dengan teori estetika busana secara otomatis. Tujuan utama dari perancangan ini adalah membangun kerangka kerja (*framework*) yang objektif untuk mentransformasikan data visual mentah dari sensor kamera menjadi keputusan rekomendasi warna pakaian yang dipersonalisasi.

### 3.5.1 Arsitektur Pipeline Sistem

Sistem yang dikembangkan mengikuti arsitektur linear yang terdiri dari empat tahap utama pemrosesan data. Setiap tahap dirancang untuk meminimalkan ambiguitas data piksel dan memaksimalkan akurasi klasifikasi *skin tone*.

*![](data:image/png;base64...)*

Gambar 3.6 Diagram Arsitektur Pipeline Sistem

* + 1. **Deteksi dan Segmentasi Kulit** Tahap awal ini melibatkan prapemrosesan (*preprocessing*) citra untuk menormalisasi kondisi masukan. Deteksi area kulit dilakukan menggunakan metode *rule-based adaptive thresholding*. Teknik ini diterapkan dengan mengonversi citra ke ruang warna YCbCr dan HSV untuk mengisolasi piksel kulit berdasarkan karakteristik krominansinya [1], [21]. Penggunaan *masking* biner memastikan bahwa hanya piksel pada wilayah wajah yang akan diproses pada tahap berikutnya, sehingga mengurangi gangguan dari objek latar belakang atau rambut [2].
    2. **Ekstraksi Warna** Piksel yang telah berhasil terisolasi kemudian diolah menggunakan algoritma *unsupervised learning*, yaitu *K-Means clustering*. Algoritma ini akan mengelompokkan data warna piksel ke dalam sejumlah klaster yang telah ditentukan nilainya untuk menemukan sentroid warna yang paling dominan [6]. Nilai sentroid ini dianggap sebagai representasi digital dari warna kulit asli pengguna, yang mencakup informasi mengenai kecerahan (*lightness*) dan saturasi warna [19].
    3. Evaluasi Multi-Color Space Penelitian ini melakukan pengujian komparatif untuk mengevaluasi kualitas klasterisasi pada tiga ruang warna yang berbeda, yakni RGB, HSV, dan CIELAB. Kualitas hasil ekstraksi pada masing-masing ruang warna diukur menggunakan metrik validasi klaster internal yang komprehensif, meliputi *Silhouette Score*, *Davies-Bouldin Index* (DBI), dan *Calinski-Harabasz Index* [18], [25]. Tahap evaluasi ini krusial untuk menentukan ruang warna mana yang paling konsisten dalam menghadapi variasi intensitas cahaya dan keragaman pigmen kulit manusia [9].
    4. Rekomendasi Warna Pakaian Fase akhir dari *pipeline* ini adalah pemetaan hasil ekstraksi warna kulit ke dalam mesin rekomendasi. Mesin ini menggunakan logika *mapping* untuk mencocokkan profil kulit pengguna dengan palet warna pakaian yang telah dikurasi. Penentuan rekomendasi didasarkan pada prinsip harmoni warna universal, seperti skema komplementer (*complementary*), analog (*analogous*), dan triadik (*triadic*) guna menjamin keserasian visual secara teoretis [8], [17].

### 3.5.2 Rancangan Aturan Rekomendasi Warna

Mekanisme pemberian rekomendasi pada sistem ini dirancang menggunakan pendekatan *rule-based* (berbasis aturan) yang mengadopsi standar industri desain busana. Aturan ini tidak bekerja secara acak, melainkan menggunakan hasil analisis dari ruang warna CIELAB sebagai parameter utama.

Sistem akan mengklasifikasikan hasil sentroid klasterisasi ke dalam tiga kategori utama *skin undertone*: *cool* (dingin), *neutral* (netral), dan *warm* (hangat). Klasifikasi ini dilakukan dengan mengevaluasi distribusi nilai pada kanal *a*\* dan *b*\* dalam ruang CIELAB, di mana nilai *a*\* mewakili spektrum hijau-merah dan *b*\* mewakili spektrum biru-kuning [14]. Selain itu, tingkat kecerahan kulit dikalibrasi menggunakan metrik *Individual Typology Angle* (ITA) untuk memastikan rekomendasi bersifat inklusif terhadap spektrum kulit yang sangat terang hingga sangat gelap [13], [15].

Setelah kategori *undertone* ditentukan, sistem akan merujuk pada tabel rujukan (*lookup table*) yang berisi daftar warna garmen yang telah divalidasi oleh teori psikologi warna [8]. Sebagai contoh, pengguna dengan kategori *warm tone* akan diprioritaskan untuk menerima rekomendasi warna pakaian dengan nuansa bumi (*earth tone*), sementara pengguna *cool tone* akan diarahkan pada palet warna biru atau ungu yang bersifat komplementer terhadap rona kulit mereka [16], [17].

Mekanisme rekomendasi warna pakaian dalam penelitian ini tidak hanya didasarkan pada tingkat kecerahan kulit semata, tetapi merupakan hasil integrasi antara klasifikasi *Individual Typology Angle* (ITA) dan analisis *undertone* pada ruang warna CIELAB. Tabel 3.1 menyajikan matriks logika pemetaan yang menjadi algoritma dasar bagi mesin rekomendasi sistem.

Tabel 3.1 Logika Pemetaan Rekomendasi Warna Pakaian Berdasarkan Skin Tone dan Undertone

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Kategori Kulit (ITA) | Rentang Sudut ITA | *Undertone (Lab)* | Rekomendasi Palet Warna Pakaian | Harmoni Warna |
| *Very Light* | >55∘ | *Cool* | *Royal Blue, Emerald, Lavender, Silver* | *Complementary* |
| *Light* | 41∘ s.d. 55∘ | *Neutral* | *Dusty Pink, Jade Green, Off-white, Grey* | *Analogous* |
| *Intermediate* | 28∘ s.d. 41∘ | *Warm* | *Mustard, Olive Green, Terracotta, Coral* | *Triadic* |
| *Tan* | 10∘ s.d. 28∘ | *Warm* | *Golden Yellow, Deep Orange, Warm Brown* | *Monochromatic* |
| *Brown* | −30∘ s.d. 10∘ | *Neutral* | *Cream, Beige, Burgundy, Forest Green* | *Analogous* |
| *Dark* | <−30∘ | *Cool/Warm* | *Cobalt Blue, Magenta, Maroon, Turquoise* | *Complementary* |

## 3.6 Teknik Analisis Data

Tahap analisis data merupakan instrumen krusial dalam penelitian ini untuk mengukur validitas, keandalan, dan efektivitas dari model sistem yang dibangun. Analisis dilakukan secara sistematis dan komprehensif, mencakup evaluasi performa algoritma secara komputasional hingga pengujian relevansi hasil luaran berdasarkan teori estetika busana. Mengacu pada arsitektur sistem yang telah dirancang, teknik analisis data dipartisi menjadi tiga instrumen pengujian utama: evaluasi kuantitatif algoritma *clustering*, analisis komparatif performa antar ruang warna, dan validasi akurasi mesin rekomendasi.

### 3.6.1 Evaluasi Kuantitatif *Clustering*

Untuk mengukur kualitas partisi piksel kulit yang dihasilkan oleh algoritma *K-Means clustering*, sistem menerapkan tiga metrik evaluasi internal secara paralel. Penggunaan metrik internal ini sangat esensial untuk menilai struktur klaster secara objektif tanpa harus bergantung pada pelabelan manual (*ground truth*).

Pertama, *Silhouette Score* digunakan untuk menguji tingkat kohesi dan separasi piksel. Metrik ini mengkalkulasi seberapa dekat jarak spasial sebuah piksel data terhadap piksel lain di dalam klaster yang sama (*intra-cluster distance*) jika dibandingkan dengan jaraknya ke klaster terdekat lainnya (*inter-cluster distance*) [18]. Nilai *Silhouette Score* berkisar pada rentang matematis -1 hingga 1. Nilai yang mendekati 1 secara empiris menunjukkan bahwa titik-titik warna kulit telah membentuk konfigurasi *clustering* yang terpusat dan terpisah secara absolut dari objek non-kulit, seperti latar belakang atau atribut visual lainnya.

Kedua, *Davies-Bouldin Index* (DBI) diimplementasikan guna mengevaluasi rasio penyebaran titik data di dalam sebuah klaster terhadap jarak antar sentroid klaster [18]. Berbeda dengan metrik sebelumnya, DBI berfokus pada minimalisasi parameter jarak. Semakin kecil nilai DBI (mendekati nol), maka semakin optimal performa algoritma tersebut. Hal ini mengindikasikan bahwa data piksel warna kulit terdistribusi secara rapat pada pusatnya masing-masing dan memiliki jarak antar-klaster yang sangat signifikan.

Ketiga, *Calinski-Harabasz Index* (CHI) atau yang secara akademis direferensikan sebagai *Variance Ratio Criterion* diaplikasikan untuk menghitung rasio antara dispersi varians antar-klaster dengan varians di dalam klaster [6]. Nilai CHI yang tinggi mendemonstrasikan bahwa sentroid warna dominan yang terekstraksi memiliki variansi internal yang sangat rendah sekaligus terpisah secara tegas dari kelompok warna lain, yang berguna untuk menghindari efek *over-segmentation* pada proses isolasi wajah.

![](data:image/png;base64...)

Gambar 3.7 Diagram Alir Perhitungan Metrik Evaluasi Kuantitatif Clustering

### 3.6.2 Analisis Komparatif *Multi-Color Space*

Data agregat dari hasil metrik evaluasi komputasional sebelumnya kemudian digunakan untuk keperluan analisis komparatif. Pengujian silang ini dilakukan untuk menguji tingkat ketangguhan deteksi warna kulit pada tiga model ruang warna multi-dimensi, yakni RGB, HSV, dan CIELAB [1], [2]. Tujuan utama dari komparasi ini adalah untuk menentukan representasi dimensi warna yang paling stabil ketika dihadapkan pada skenario fluktuasi intensitas pencahayaan (*illumination variance*) yang ekstrem.

Pada tahap operasional ini, sistem akan memetakan dan membandingkan degradasi nilai *Silhouette Score* pada masing-masing ruang warna. Analisis pada ruang warna RGB difokuskan pada tingkat kerentanannya terhadap korelasi linier antara parameter cahaya dan komponen warna pigmen. Sementara itu, pengujian pada ruang warna HSV ditujukan untuk membuktikan apakah pemisahan komponen kecerahan (*Value*) dari rona murni (*Hue* dan *Saturation*) mampu mereduksi derau visual dengan lebih baik [2]. Selanjutnya, performa dimensi CIELAB dianalisis secara khusus karena sifat ruang warnanya yang *perceptually uniform*, mereplikasi dengan presisi bagaimana sistem optik manusia membedakan rona gradasi kulit [14]. Ruang warna yang menghasilkan nilai indeks klasterisasi terbaik secara konsisten akan ditetapkan sebagai fondasi komputasi untuk sistem informasi akhir.

### 3.6.3 Validasi Rekomendasi Warna Pakaian

Tahap terminasi dari analisis data adalah melakukan validasi komprehensif terhadap fungsionalitas mesin luaran. Berbeda dengan evaluasi algoritma yang bersandar pada kalkulasi matematis kuantitatif, validasi rekomendasi ini mengintegrasikan penalaran komputasi dengan teori harmoni warna dalam kajian psikologi desain busana (*fashion aesthetics*) [8].

Analisis validasi direalisasikan dengan mengevaluasi kecocokan jarak warna menggunakan skema metrik perseptual terhadap prinsip fundamental roda warna (*color wheel*). Hasil klasifikasi *undertone* kulit pengguna akan diuji silang dengan parameter rekomendasi standar: skema komplementer (*complementary*) yang menyandingkan warna berlawanan untuk menciptakan kontras visual, skema analog (*analogous*) yang memadukan rona berdekatan untuk harmoni bertingkat, dan skema triadik (*triadic*) yang membentuk keseimbangan spasial tinggi [16], [17]. Tingkat keandalan sistem diukur dari presisi penerjemahan nilai sentroid kulit menjadi saran palet garmen yang terbukti ekuivalen dan selaras secara visual dari sudut pandang estetika profesional.

## 3.7 Jadwal Penelitian

Penelitian ini dilaksanakan dalam rentang waktu dari bulan Februari hingga Juli 2026. Kegiatan penelitian disusun secara bertahap mulai dari penyusunan proposal hingga sidang skripsi. Rincian jadwal pelaksanaan kegiatan penelitian dapat dilihat pada tabel berikut.

Tabel 3.2 Jadwal Penelitian

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No | Kegiatan Penelitian | Fase | Feb | Mar | Apr | Mei | Jun | Jul |
| 1 | Studi pustaka dan telaah literatur | Fase Persiapan | 🗸 | 🗸 |  |  |  |  |
| 2 | Penyusunan proposal (Bab 1, 2, 3) | Fase Persiapan | 🗸 | 🗸 | 🗸 |  |  |  |
| 3 | Seminar proposal | Fase Persiapan |  |  | 🗸 |  |  |  |
| 4 | Implementasi Algoritma dan Pipeline Sistem | Fase Persiapan |  | 🗸 | 🗸 |  |  |  |
| 5 | Pengujian dan Evaluasi Multi-Ruang Warna | Fase Implementasi |  |  | 🗸 | 🗸 |  |  |
| 6 | Analisis Hasil dan Validasi Rekomendasi | Fase Implementasi |  |  |  | 🗸 |  |  |
| 7 | Penyusunan Laporan Akhir Skripsi | Fase Implementasi |  |  |  |  | 🗸 | 🗸 |
| 8 | Penyusunan laporan akhir | Fase Implementasi |  |  |  |  | 🗸 | 🗸 |
| 9 | Sidang akhir | Fase Implementasi |  |  |  |  |  | 🗸 |

# DAFTAR PUSTAKA

[1] M. Kolkur, D. Kalbande, P. Shimpi, C. Bapat, dan J. Jarti, "Human Skin Detection Using RGB, HSV and YCbCr Color Models," *ICCASP*, 2016.

[2] A. Moumene, A. Jilbab, dan C. Nacir, "Real Time Skin Color Detection Based on Adaptive HSV Thresholding," *IAES International Journal of Artificial Intelligence (IJ-AI)*, vol. 12, no. 1, hal. 313–321, Mar. 2023.

[3] Y. Chang dan T. Mukai, "Color Feature Based Dominant Color Extraction," *MVA*, 2015.

[4] K. Komori dan S. Eguchi, "A Unified Formulation of k-Means, Fuzzy c-Means and Gaussian Mixture Model by the Kolmogorov–Nagumo Average," *Entropy*, vol. 23, no. 518, hal. 1-14, 2021.

[5] Rosyani, S. Saryani, S. Hartati, dan R. Wardoyo, "Color Features Based Flower Image Segmentation Using K-Means and Fuzzy C-Means," *International Journal of Advanced Computer Science and Applications (IJACSA)*, vol. 12, no. 10, hal. 535-542, 2021.

[6] K. P. Sinaga dan M. S. Yang, "Unsupervised K-Means Clustering Algorithm," *IEEE Access*, vol. 8, hal. 80716–80727, 2020.

[7] Y. Chen dan J. Wang, "Three-Way Clustering Based on Digital Image Processing," *Knowledge-Based Systems*, 2021.

[8] Y. Wei dan J. Zhang, "The Application of Color Psychology in Fashion Design," *Journal of Physics: Conference Series*, vol. 1792, 2021.

[9] G. Muratbekova, M. S. Al-kaabi, H. Sellahewa, dan S. Jassim, "Color Models in Image Processing: A Review and Experimental Comparison," *IAES International Journal of Artificial Intelligence (IJ-AI)*, vol. 14, no. 4, hal. 2366-2382, Des. 2025.

[10] M. S. Al-kaabi, G. Muratbekova, S. Jassim, dan H. Sellahewa, "Deepfake Detection: A Performance Comparison of Machine Learning and Deep Learning Methods," *Information Retrieval Journal*, 2025.

[11] L. S. G. L. Waas, D. J. Hemanth, dan S. S. Jassim, "Deep Learning Based Human Activity Recognition Using Smartphone Sensors," *Sensors*, vol. 25, no. 7261, 2025.

[12] J. S. de S. Oliveira, J. M. R. S. Tavares, dan J. G. M. dos Santos, "Image Quality Assessment for Machine Learning-Based Medical Image Analysis," *Journal of Imaging*, 2025.

[13] G. Jung, S. Kim, dan S. Yoo, "Skin Tone Analysis Through Skin Tone Map Generation With Optical Approach and Deep Learning," *Skin Research and Technology*, 2024.

[14] R. Alyoubi, T. Alharbi, A. Alghamdi, Y. Alshehri, dan E. Alghamdi, "Colors Matter: AI-Driven Exploration of Human Feature Colors," *arXiv preprint arXiv:2505.14931*, 2025.

[15] W. Xie, G. Overgoor, H. H. M. Lee, dan Z. Han, "Automated Detection of Skin Tone Diversity in Visual Marketing Communication," dalam *Proceedings of the 56th Hawaii International Conference on System Sciences (HICSS)*, hal. 3817, 2023.

[16] A. D. Putri, S. Adrianto, dan D. I. Mulyana, "Prediksi Pemilihan Warna Hijab Berdasarkan Tone Kulit Menggunakan Algoritma K-Nearest Neighbor (KNN)," *Jurnal Indonesia : Manajemen Informatika dan Komunikasi (JIMIK)*, vol. 6, no. 3, hal. 1742-1755, Sep. 2025.

[17] H. P. Dissanayake dan J. M. C. S. Manukalpa, "A Deep Learning Framework for Personalized Fashion Recommendations Based on Skin Tone Analysis," IJLTEMAS, vol. XIV, no. VI, 2025.

[18] F. A. Totti dan N. Setiyawati, "Perbandingan Algoritma Clustering K-Means, Gaussian Mixture Model, dan Spectral Clustering untuk Facial Emotion Recognition," Sistemasi: Jurnal Sistem Informasi, vol. 14, no. 6, hal. 3007-3019, 2025.

[19] S. Basar, M. Ali, G. Ochoa-Ruiz, dkk., "Unsupervised color image segmentation: A case of RGB histogram based K-means clustering initialization," PLOS ONE, vol. 15, no. 10, 2020.

[20] M. Rai, V. Bhootna, dan R. K. Yadav, "Performance based Algorithm for the Detection and Extraction of Human Skin," dalam Proc. ABLAZE, 2015.

[21] M. V. Daithankar, K. J. Karande, dan A. D. Rarale, "Analysis of Skin Color Models for Face Detection," 2014.

[22] Selecting optimal k for K-means in image segmentation using GLCM, Multimedia Tools and Applications, 2024.

[23] IET Image Processing (Vol. 13), terkait optimasi K-Means dan Fuzzy C-Means, 2019

[24] M. Mortazavi T. dan O. M. Ebadati E., "An improved human skin detection and localization by using machine learning techniques in RGB and YCbCr color spaces," PeerJ Preprints, 2018.

[25] S. Arumugadevi dan V. Seenivasagam, "Comparison of Clustering Methods for Segmenting Color Images," Indian Journal of Science and Technology, vol. 8, no. 7, hal. 670–677, Apr. 2015.