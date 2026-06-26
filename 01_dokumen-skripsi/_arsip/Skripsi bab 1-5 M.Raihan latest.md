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

Pemilihan warna pakaian yang sesuai dengan warna kulit merupakan aspek krusial dalam dunia *fashion* yang berkaitan erat dengan persepsi visual, psikologi konsumen, dan kepercayaan diri individu [8]. Secara tradisional, penentuan harmoni warna antara kulit pengguna dan pakaian seringkali dilakukan secara manual dan subjektif, yang rentan menghasilkan keputusan yang bias dan tidak konsisten [2]. Seiring dengan pesatnya perkembangan komputasi digital, pendekatan algoritmik mulai dieksplorasi untuk mengotomatisasi pengenalan representasi karakteristik fisik manusia secara objektif, termasuk ekstraksi warna kulit dari citra wajah.

Sejumlah penelitian terdahulu telah mendemonstrasikan kelayakan teknologi *computer vision* untuk mengekstraksi area kulit. Kolkur dkk. mengeksplorasi penggunaan model warna RGB, HSV, dan YCbCr untuk mendeteksi area kulit manusia melalui formulasi batasan matematis [1]. Selanjutnya, Moumene dkk. menerapkan segmentasi *real-time* berbasis adaptasi *thresholding* pada ruang warna HSV untuk meningkatkan efisiensi komputasi dalam mengisolasi objek kulit [2]. Dari sisi pembentukan representasi fitur warna, teknik *clustering* tanpa pengawasan (*unsupervised learning*) seperti algoritma *K-Means* dan *Fuzzy C-Means* telah diujikan secara luas oleh Rosyani dkk. untuk melakukan segmentasi citra [5]. Muratbekova dkk. juga secara spesifik mengevaluasi performa berbagai model ruang warna, serta menyoroti keunggulan CIELAB dalam menjaga keseragaman perseptual (*perceptual uniformity*) yang sejalan dengan penglihatan manusia [9].

Meskipun fondasi pengolahan citra telah banyak diteliti, terdapat kesenjangan penelitian (*research gap*) yang harus diselesaikan untuk implementasi rekomendasi *fashion*. Pertama, ekstraksi warna kulit yang tepat di bawah kondisi pencahayaan berbeda (*indoor*/*outdoor*) masih menjadi tantangan komputasional [1], [2], [9]. Kedua, evaluasi model pada literatur terdahulu sering berhenti di segmentasi, belum sampai pada evaluasi kualitas *clustering* dan validasi rekomendasi pada tahapan akhir [5], [7], [18]. Ketiga, belum ada perbandingan sistematis RGB, HSV, CIELAB khusus untuk kasus *skintone* dan rekomendasi warna pakaian [1], [9], [14].

Untuk menjembatani celah penelitian tersebut, penelitian ini mengusulkan pengembangan purwarupa sistem rekomendasi yang dirancang untuk mengintegrasikan pengolahan citra digital dan teori estetika fesyen. Kontribusi utama dari penelitian ini meliputi: (1) penggunaan titik pusat klaster (*centroid*) warna sebagai dasar rekomendasi pakaian yang objektif [3], [6]; (2) perbandingan empiris ruang warna RGB, HSV, dan CIELAB dalam merepresentasikan fitur warna wajah [1], [9]; serta (3) rekomendasi warna berbasis *skintone* dari pengguna aktual [13], [14], [16].

## 1.2 Identifikasi dan Rumusan Masalah

### 1.2.1 Identifikasi Masalah

Berdasarkan latar belakang yang telah diuraikan, identifikasi masalah dalam penelitian ini adalah sebagai berikut:

1. Penentuan warna pakaian masih didominasi oleh intuisi subjektif yang tidak konsisten dan rentan terhadap bias persepsi visual [2].
2. Tingkat akurasi ekstraksi warna kulit sangat fluktuatif ketika dihadapkan pada perubahan kondisi pencahayaan lingkungan (*indoor* atau *outdoor*) [1], [2], [9].
3. Kurangnya pedoman evaluasi komparatif yang membuktikan performa ruang warna (RGB, HSV, CIELAB) secara khusus untuk penentuan titik pusat klaster *skin tone* [1], [9], [14].
4. Belum adanya pemodelan komprehensif yang mengintegrasikan hasil *clustering* warna citra wajah langsung menjadi rekomendasi produk fesyen berbasis teori harmoni [5], [7], [18].

### 1.2.2 Rumusan Masalah

Berdasarkan identifikasi masalah di atas, rumusan masalah dalam penelitian ini ditetapkan sebagai berikut:

1. Bagaimana merancang pipeline deteksi dan segmentasi wilayah kulit wajah yang optimal menggunakan metode rule-based adaptive thresholding?
2. Bagaimana tingkat akurasi partisi dan efisiensi komputasi algoritma K-Means clustering pada ruang warna RGB, HSV, dan CIELAB jika dievaluasi menggunakan metrik Silhouette Score, Davies-Bouldin Index (DBI), dan Calinski-Harabasz Index (CHI)?
3. Bagaimana merumuskan aturan logis (rule-based) untuk memetakan representasi sentroid skin tone menjadi rekomendasi palet warna pakaian berdasarkan teori harmoni warna?
4. Bagaimana tingkat performa dari purwarupa sistem rekomendasi warna pakaian yang dikembangkan secara keseluruhan?

## 1.3 Batasan Masalah

Batasan masalah dalam penelitian ini ditetapkan agar ruang lingkup penelitian tetap terarah dan sesuai dengan tujuan yang telah ditetapkan, batasan masalah ditetapkan sebagai berikut:

1. Masukan citra digital merupakan gambar representasi wajah dua dimensi dengan pencahayaan memadai. Sistem murni memindai wajah berekspresi natural, dan tidak melakukan deteksi citra postur seluruh badan.
2. Parameter ruang warna (*color space*) yang dievaluasi difokuskan secara eksklusif pada RGB, HSV, dan CIELAB.
3. Metode perumusan ekstraksi warna dibatasi pada penggunaan algoritma pembelajaran tanpa pengawasan, yaitu *K-Means clustering*.
4. Sistem tidak melakukan deteksi terhadap variabel tekstur material, jenis kain (*fabric*), maupun potongan desain garmen pakaian.
5. Algoritma rekomendasi warna pakaian bekerja mutlak berdasarkan matriks jarak *skin tone*, tidak menggunakan penyaringan (*filtering*) berbasis data historis atau preferensi pengguna sebelumnya.

## 1.4 Tujuan Penelitian

Penelitian ini bertujuan untuk menjembatani pengolahan citra komputasional dengan teori estetika visual guna menghasilkan sistem rekomendasi yang objektif, tangguh (robust), dan efisien. Secara spesifik, tujuan yang ingin dicapai adalah sebagai berikut:

1. Merancang arsitektur perangkat lunak untuk menjalankan *pipeline* ekstraksi warna kulit menggunakan operasi dasar *rule-based thresholding*.
2. Membuktikan secara matematis ruang warna mana di antara RGB, HSV, dan CIELAB yang menghasilkan partisi *clustering K-Means* paling optimal melalui uji metrik kuantitatif *Silhouette Score*, *Davies-Bouldin Index* (DBI), dan *Calinski-Harabasz Index* (CHI).
3. Membangun model pemetaan yang menghubungkan ekstraksi sentroid kulit pengguna dengan tabel rujukan garmen sehingga menghasilkan luaran rekomendasi pakaian yang tervalidasi secara estetika fesyen.
4. Mengevaluasi tingkat keberhasilan purwarupa sistem rekomendasi secara menyeluruh dalam menghasilkan keputusan rekomendasi yang presisi.

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

Pengembangan sistem rekomendasi pakaian berbasis ekstraksi warna kulit membutuhkan landasan teori yang kuat terkait pengolahan citra digital, segmentasi warna, dan analisis ruang warna (*color space*). Subbab ini menguraikan berbagai penelitian terdahulu yang relevan sebagai acuan untuk membangun arsitektur sistem sekaligus mengidentifikasi celah penelitian (*research gap*).

### 2.1.1 Ekstraksi Warna Kulit

Ekstraksi warna kulit merupakan tahapan fundamental dalam pengolahan citra yang melibatkan manusia sebagai objek utama. Penelitian oleh Kolkur dkk. [1] melakukan deteksi warna kulit manusia menggunakan kombinasi model warna RGB, HSV, dan YCbCr untuk meningkatkan akurasi pengenalan piksel kulit. Moumene dkk. [2] mengusulkan metode deteksi warna kulit *real-time* berbasis *adaptive thresholding* pada ruang warna HSV, yang terbukti tangguh terhadap variasi pencahayaan sekitar. Pendekatan lain oleh Rai dkk. [20] menguji algoritma berbasis kinerja untuk mendeteksi dan mengekstraksi kulit manusia dari latar belakang yang kompleks. Daithankar dkk. [21] turut menganalisis berbagai model warna untuk deteksi wajah, dan menyimpulkan bahwa transformasi ruang warna sangat menentukan akurasi segmentasi fitur wajah dan kulit.

Untuk memperjelas batasan konsep “deteksi kulit” yang menjadi fondasi ekstraksi warna kulit, Kolkur dkk. menyatakan bahwa deteksi kulit berkaitan dengan pengenalan piksel dan region yang berwarna kulit pada sebuah citra. [1] Definisi ini menegaskan bahwa objek utama pada tahap awal ekstraksi adalah piksel (unit terkecil citra) yang kemudian dapat membentuk region kulit (kumpulan piksel yang saling berdekatan). Kolkur dkk. juga menekankan bahwa penggunaan warna kulit sebagai fitur sering dipilih karena pemrosesannya relatif cepat dan tidak bergantung pada orientasi maupun ukuran objek manusia dalam citra. [1]

Dalam praktiknya, deteksi/segmentasi kulit menghadapi tantangan besar karena penampakan kulit sangat dipengaruhi kondisi akuisisi. Moumene dkk. menegaskan bahwa deteksi warna kulit telah banyak diteliti dan menjadi tugas penting untuk berbagai aplikasi visi komputer (misalnya pelacakan wajah/tangan dan analisis gestur). [2] Mereka juga menjelaskan adanya dua arus pendekatan: metode *machine learning* efektif untuk deteksi kulit, namun sering tidak ideal untuk real-time karena komputasinya berat; sedangkan pendekatan ringan dapat dibangun dari aturan segmentasi yang diperoleh dari distribusi warna kulit, tetapi tidak ada aturan universal karena variasi tipe citra, parameter akuisisi, dan iluminasi pemandangan. [2] Dengan kata lain, ekstraksi warna kulit tidak cukup hanya “menentukan ambang” sekali, melainkan perlu mempertimbangkan robustness terhadap perubahan pencahayaan dan variasi kondisi nyata.

Pada sisi teknik, Kolkur dkk. menunjukkan penggunaan beberapa ruang warna sebagai dasar aturan segmentasi, khususnya RGB, HSV, dan YCbCr, untuk mengenali piksel kulit. [1] Pendekatan berbasis ambang (*thresholding*) semacam ini memiliki keunggulan dari sisi kesederhanaan dan efisiensi, namun juga memiliki konsekuensi: performanya sensitif terhadap pergeseran iluminasi, bayangan, latar yang menyerupai warna kulit, serta perbedaan karakteristik warna kulit antar individu. [1] Pada konteks ini, pemilihan ruang warna menjadi aspek penting karena setiap ruang warna merepresentasikan komponen luminansi dan krominansi secara berbeda—yang dapat berdampak pada separabilitas piksel kulit dari non-kulit.

Moumene dkk. kemudian memperkuat aspek efisiensi tersebut melalui pendekatan adaptive HSV thresholding untuk deteksi kulit real-time. Mereka menekankan bahwa meskipun aturan segmentasi dapat diperoleh dari distribusi warna kulit, variasi kondisi membuat aturan statis tidak selalu memadai; karena itu, ambang perlu disesuaikan secara adaptif mengikuti perubahan kondisi. [2] Gagasan adaptif ini penting dalam ekstraksi warna kulit karena segmentasi yang lebih stabil akan menghasilkan area kulit yang lebih “bersih”, sehingga representasi warna kulit yang dihitung dari area tersebut menjadi lebih konsisten.

Setelah area kulit diperoleh, ekstraksi warna kulit tidak berhenti pada mask/segmentasi, tetapi berlanjut pada pembentukan representasi warna yang ringkas dan bermakna. Dalam ranah ekstraksi warna, Chang & Mukai menjelaskan bahwa warna dominan dalam citra dapat dimanfaatkan untuk berbagai kebutuhan seperti pencarian citra, pengeditan warna, dan pembangkitan palet. [3] Mereka juga menyoroti bahwa metode konvensional berbasis clustering atau histogram sering gagal menangkap warna dominan pada region kecil, padahal region kecil bisa penting untuk analisis skema warna. [3] Konsep “warna dominan” ini relevan untuk ekstraksi warna kulit karena area kulit yang tersegmentasi pada dasarnya merupakan suatu region yang dapat diringkas oleh satu atau beberapa warna representatif (misalnya centroid cluster atau kandidat warna dominan), sehingga fitur warna kulit menjadi lebih informatif daripada sekadar nilai rata-rata global.

Dengan demikian, ekstraksi warna kulit dalam penelitian ini berdiri pada dua fondasi utama: (1) deteksi/segmentasi kulit yang efisien dan cukup robust terhadap variasi akuisisi, sebagaimana digambarkan pada pendekatan berbasis multi–color space dan adaptasi ambang; serta (2) perumusan representasi warna dari area kulit yang telah dipisahkan, dengan prinsip bahwa ringkasan warna seperti warna dominan/palet dapat meningkatkan kualitas representasi warna untuk tahap pengolahan berikutnya. [1] [2] [3].

### 2.1.2 Clustering pada Pengolahan Citra

Pendekatan *unsupervised learning*, khususnya algoritma *clustering*, sering diadopsi untuk proses segmentasi piksel citra. Rosyani dkk. [5] membandingkan K-Means dan Fuzzy C-Means untuk segmentasi citra berdasarkan fitur warna, di mana inisialisasi titik pusat memegang peran penting. Selanjutnya, Totti dan Setiyawati [18] mengevaluasi efisiensi algoritma K-Means, Gaussian Mixture Model (GMM), dan Spectral Clustering. Penelitian tersebut membuktikan bahwa K-Means mampu melakukan pengelompokan yang efisien dengan kompleksitas komputasi yang relatif rendah. Selain itu, Chen dan Wang [7] memperkenalkan pendekatan *three-way clustering* pada pengolahan citra digital untuk menangani piksel-piksel pada area batas (*boundary regions*) yang ambigu. Namun, penerapan algoritma pengelompokan tersebut mayoritas hanya digunakan untuk memisahkan latar depan dan belakang, belum dioptimalkan untuk mengekstraksi palet warna dominan.

Kerangka teoretik yang menjelaskan hubungan antar-metode clustering dipaparkan oleh Komori & Eguchi melalui formulasi terunifikasi yang mengaitkan k-means, fuzzy c-means, dan Gaussian mixture model (GMM) dalam satu perspektif matematis. [4] Melalui sudut pandang ini, k-means dipahami sebagai *hard clustering* (setiap data masuk tepat ke satu cluster), fuzzy c-means sebagai *soft clustering* (data memiliki derajat keanggotaan), sedangkan GMM memodelkan cluster secara probabilistik. Diferensiasi ini penting pada data citra, karena transisi warna antar-region sering gradual dan tidak selalu “tegas”, terutama pada batas objek.

Implementasi clustering untuk segmentasi berbasis warna ditunjukkan oleh Rosyani dkk. yang melakukan investigasi segmentasi citra bunga menggunakan K-Means dan Fuzzy C-Means (FCM) dengan memanfaatkan fitur dari beberapa ruang warna (RGB, HSV, LAB, dan YCbCr). [5] Mereka menggunakan citra sampel yang memuat 1–4 objek bunga dari ImageCLEF 2017 dan menilai performa segmentasi dengan memanfaatkan *ground truth*. Evaluasi dilakukan menggunakan jarak Hausdorff serta metrik performa berbasis confusion matrix seperti akurasi, tingkat kesalahan, sensitivitas, dan spesifisitas. [5] Temuan penting dari studi ini adalah bahwa hasil segmentasi sangat dipengaruhi oleh pemilihan komponen warna, dan penggunaan komponen dari model warna LAB memberi dampak yang kuat terhadap keberhasilan segmentasi. Selain itu, mereka menunjukkan bahwa komponen AB merupakan model warna yang konsisten berhasil mendeteksi objek secara benar pada skenario uji yang mereka lakukan. [5] Hasil tersebut menegaskan bahwa keberhasilan clustering pada citra tidak hanya dipengaruhi algoritmanya, tetapi juga oleh representasi warna yang digunakan.

Di luar segmentasi objek, clustering juga menjadi dasar penting dalam ekstraksi warna dominan untuk merangkum informasi warna suatu citra/region. Chang & Mukai mengajukan metode ekstraksi warna dominan yang diawali dengan menghitung kandidat warna dominan menggunakan K-Means pada ruang warna CIELAB, lalu menggabungkannya dengan *graph cut* pada *region adjacency graph (RAG)* dari citra yang telah disegmentasi. [3] Setelah kandidat cluster terbentuk, mereka menghitung fitur warna yang lazim dipertimbangkan dalam analisis skema warna—seperti saturasi, kontras, dan area—untuk menyeleksi warna yang benar-benar dominan. [3] Pendekatan ini menekankan bahwa ringkasan warna berbasis clustering menjadi lebih kuat ketika digabungkan dengan informasi spasial (keterhubungan region) dan kriteria seleksi fitur yang relevan terhadap persepsi visual.

Walaupun K-Means sering digunakan karena sederhana dan cepat, literatur juga menegaskan keterbatasan klasiknya, yaitu sensitivitas terhadap inisialisasi dan kebutuhan menentukan jumlah cluster K sejak awal. Sinaga & Yang menyatakan bahwa k-means dan banyak pengembangannya tetap dipengaruhi inisialisasi serta memerlukan jumlah cluster *a priori*, sehingga pada praktiknya k-means tidak sepenuhnya *unsupervised*. [6] Untuk mengatasi hal tersebut, mereka mengusulkan skema Unsupervised K-Means (U-k-means) yang diarahkan agar bebas inisialisasi dan mampu menemukan jumlah cluster optimal tanpa seleksi parameter. [6] Gagasan ini relevan untuk pengelompokan warna (termasuk warna kulit), karena penentuan K yang tidak tepat dapat menghasilkan representasi yang terlalu kasar (K kecil) atau terlalu sensitif terhadap noise/variasi iluminasi (K besar).

Selain pengembangan pada k-means, terdapat pula pendekatan clustering yang memodelkan ketidakpastian melalui konsep *three-way decision*. Chen & Wang memperkenalkan *three-way clustering* yang terinspirasi operasi pengolahan citra digital berupa blurring dan sharpening, dengan cara mengkuantifikasi kepadatan data menjadi nilai “gray” melalui fungsi kernel. [7] Dalam paradigma *three-way*, semesta data dipisahkan menjadi tiga bagian yang saling lepas: core region (objek dengan konsentrasi tinggi di dalam cluster), fringe region (area ketidakpastian/objek yang lebih longgar), dan trivial region (bagian di luar cluster yang relevan). [7] Setelah sampel berkepadatan rendah dieliminasi, clustering konvensional diterapkan pada sampel berkepadatan tinggi, kemudian core dan fringe pada tiap cluster diperoleh melalui operasi blurring dan sharpening. [7] Walaupun konteks eksperimennya menggunakan dataset umum, kerangka ini memperlihatkan cara alternatif untuk menangani area “ambigu”—isu yang juga sering muncul pada data warna citra ketika terdapat transisi halus atau gangguan pencahayaan.

Secara keseluruhan, literatur menunjukkan bahwa clustering pada pengolahan citra digital memainkan peran utama untuk membangun segmentasi dan ringkasan warna: (1) K-Means/FCM efektif untuk segmentasi berbasis warna dan sangat dipengaruhi oleh pilihan ruang warna/komponen fitur, (2) clustering dapat digunakan untuk mengekstrak warna dominan ketika digabungkan dengan struktur spasial dan seleksi fitur warna, dan (3) keterbatasan k-means terkait inisialisasi serta pemilihan K dapat diatasi melalui skema *unsupervised* yang lebih kuat atau paradigma *three-way* yang mengakomodasi ketidakpastian. [5], [3], [6], [4], [7].

### 2.1.3 Sistem Rekomendasi Berbasis Warna

Personalisasi rekomendasi busana (*fashion*) semakin berkembang dengan mengintegrasikan analisis atribut fisik pengguna. Dissanayake dan Manukalpa [17] mengembangkan kerangka *deep learning* untuk memberikan rekomendasi mode berdasarkan identifikasi *tone* warna kulit. Dalam skala lokal, Putri dkk. [16] membangun sistem prediksi pemilihan warna hijab yang sesuai dengan kecenderungan *tone* kulit menggunakan algoritma K-Nearest Neighbor (KNN). Dari perspektif desain, Wei dan Zhang [8] menegaskan bahwa aplikasi psikologi warna dalam mode memberikan dampak signifikan pada harmoni visual dan tingkat kecocokan warna pakaian.

Kajian psikologi warna pada fashion dijelaskan oleh Wei & Zhang melalui pembahasan hubungan warna dan psikologi konsumen. Mereka menempatkan psikologi konsumen sebagai kajian yang mempelajari perubahan psikologis dan perilaku konsumen dalam aktivitas konsumsi, yang dipengaruhi oleh faktor internal maupun eksternal. Pada konteks fashion design, warna diposisikan sebagai elemen desain yang memiliki efek berbeda terhadap emosi dan kesadaran individu, sehingga pemilihan dan padu padan warna pakaian seharusnya disesuaikan dengan kebutuhan psikologis kelompok konsumen yang berbeda. [8].

Untuk memotret pengaruh elemen desain terhadap psikologi konsumsi, Wei & Zhang melakukan pengumpulan data pada 100 konsumen yang dipilih secara acak dari tiga pusat perbelanjaan, dengan fokus pada kebutuhan konsumsi, kecenderungan konsumsi, kecenderungan pemilihan warna pakaian, dan karakteristik kepribadian. Evaluasi pengaruh elemen desain dilakukan menggunakan *fuzzy evaluation method* dengan skala penilaian 1–5, di mana nilai lebih tinggi menunjukkan pengaruh yang lebih besar. Hasil penilaian mereka menunjukkan bahwa warna memiliki pengaruh paling besar pada kelompok *juvenile* (skor 5), kemudian *youth* (skor 4), dan *young and middle-aged* (skor 3). [8]

Temuan tersebut memperkuat posisi warna sebagai variabel yang layak dijadikan dasar rekomendasi pada domain fashion, khususnya bila sistem rekomendasi diarahkan untuk menyesuaikan saran warna terhadap karakter pengguna (misalnya kelompok usia, preferensi, dan kecenderungan psikologis). Dalam paper yang sama, Wei & Zhang juga menekankan bahwa perancangan warna pakaian dapat mengacu pada prinsip desain seperti keseimbangan, ritme, dan proporsi, serta menggunakan beberapa pendekatan psikologis dalam desain pakaian agar hasil desain memenuhi kebutuhan psikologis konsumen. [8]

Pada sisi representasi warna (yang menjadi input penting bagi sistem rekomendasi berbasis warna), Muratbekova dkk. menegaskan bahwa pemilihan model warna/ruang warna bersifat *task-dependent*, karena setiap model memiliki kompromi antara akurasi perseptual, biaya komputasi, dan ketergantungan perangkat. Mereka mereview model tradisional (mis. RGB), model yang lebih mendekati persepsi (mis. CIELAB/CIELUV), serta pendekatan berbasis fuzzy, lalu melakukan eksperimen untuk membandingkan aspek-aspek seperti ketergantungan perangkat, konsistensi kromatik, dan kompleksitas komputasi. [9] Dalam konteks aplikasi yang menargetkan kesesuaian persepsi pengguna—seperti rekomendasi warna—kajian ini relevan karena menyoroti bahwa persepsi manusia dipengaruhi faktor neural, konteks, dan subjektivitas yang tidak sepenuhnya ditangkap oleh representasi numerik statis. [9]

Lebih lanjut, Muratbekova dkk. juga menandai arah penelitian yang makin menonjol pada keterkaitan warna dengan aspek *human-centric*, termasuk *color-emotion associations*, serta menekankan adanya kebutuhan validasi yang lebih berorientasi pengguna untuk aplikasi-aplikasi berbasis persepsi. [9] Perspektif ini sejalan dengan karakter sistem rekomendasi warna pada fashion: selain mengandalkan aturan/fitur warna, kualitas rekomendasi idealnya diuji melalui penilaian pengguna karena target akhirnya adalah “keterterimaan” rekomendasi oleh manusia.

Jika sistem rekomendasi warna pakaian diintegrasikan dengan pipeline pengolahan citra (misalnya dari citra wajah), maka aspek efisiensi komputasi juga menjadi pertimbangan. Pada ranah deteksi/segmentasi kulit, Moumene dkk. menunjukkan bahwa pendekatan ringan berbasis ambang adaptif dapat berjalan cepat dan kompetitif untuk real-time, sedangkan pendekatan *deep learning* menghasilkan performa lebih tinggi namun jauh lebih mahal secara komputasi pada eksperimen yang mereka laporkan. [2] Konteks ini relevan karena sistem rekomendasi berbasis citra pada perangkat nyata sering membutuhkan trade-off yang jelas antara kualitas dan biaya komputasi.

Berangkat dari temuan psikologi warna dalam fashion, warna dapat diperlakukan sebagai atribut rekomendasi yang tidak semata-mata “sesuai secara teori”, tetapi juga harus “diterima secara persepsi” oleh pengguna. Wei & Zhang memperlihatkan bahwa pengaruh warna terhadap keputusan dan respons konsumen dapat berbeda pada kelompok usia, sehingga rekomendasi warna di domain fashion pada dasarnya beririsan langsung dengan preferensi dan reaksi psikologis pengguna. [8] Pada saat yang sama, bila rekomendasi dihasilkan dari pipeline pengolahan citra (misalnya dari citra wajah), maka konsistensi representasi warna menjadi prasyarat agar rekomendasi tidak berubah drastis hanya karena perubahan iluminasi atau perangkat. Di titik inilah pemilihan model/ruang warna menjadi krusial: Muratbekova dkk. menegaskan bahwa pemilihan color model/space bersifat bergantung tugas, karena model yang populer seperti RGB tidak selalu selaras dengan persepsi manusia, sementara model yang lebih konsisten secara perseptual dapat membawa konsekuensi komputasi. [9] Selain itu, pertimbangan efisiensi pipeline juga relevan: Moumene dkk. menunjukkan bahwa pendekatan ringan pada deteksi/segmentasi kulit dapat berjalan cepat untuk real-time, sedangkan metode *deep learning* dapat lebih akurat namun jauh lebih mahal secara komputasi pada pengujian mereka. [2] Oleh karena itu, sistem rekomendasi berbasis warna pada penelitian ini diletakkan sebagai integrasi antara pemaknaan warna dalam fashion dan representasi warna komputasional yang stabil, sehingga rekomendasi yang dihasilkan tetap masuk akal secara persepsi sekaligus konsisten secara teknis.

### 2.1.4 Evaluasi Multi-Color Space

Evaluasi *multi-color space* dibutuhkan untuk menemukan representasi warna yang paling relevan dengan persepsi penglihatan manusia. Muratbekova dkk. [9] menyusun tinjauan komprehensif dan eksperimen yang membandingkan keandalan berbagai ruang warna dalam pengolahan citra digital. Meskipun banyak model warna yang telah diuji, pencarian model yang paling konsisten dan toleran terhadap perubahan intensitas cahaya pada objek spesifik seperti kulit manusia masih menjadi tantangan utama dalam disiplin keilmuan *computer vision*.

Dalam kerangka konseptual, Muratbekova dkk. juga membedakan “color model” dan “color space”. Color model dipahami sebagai konsep representasi numerik warna menggunakan seperangkat nilai (misalnya RGB, CMYK, HSV), sedangkan color space merupakan implementasi spesifik dari model tersebut yang sekaligus menentukan gamut warna (misalnya sRGB, Adobe RGB, CIELAB). [9] Pembedaan ini penting karena penelitian yang menilai “kinerja ruang warna” pada praktiknya menilai dampak implementasi representasi warna terhadap pemisahan kelas/cluster warna pada data citra.

Pada ranah ekstraksi kulit, kebutuhan evaluasi lintas ruang warna terlihat dari studi Moumene dkk. yang membandingkan segmentasi kulit pada RGB, YCrCb, dan HSV. Mereka melaporkan bahwa konfigurasi berbasis HSV memberikan performa terbaik dibanding RGB dan YCrCb pada dua dataset yang berbeda (Pratheepan dan HGR), dengan F1 yang tinggi dan waktu komputasi rendah untuk skenario real-time. [2] Hasil ini menegaskan bahwa pemilihan ruang warna dapat memengaruhi kualitas mask kulit yang dihasilkan; padahal mask kulit yang stabil merupakan prasyarat agar fitur warna kulit yang diekstrak tidak “terkontaminasi” oleh piksel latar atau bayangan.

Di sisi clustering berbasis warna, Rosyani dkk. juga menunjukkan bahwa performa segmentasi berbasis K-Means dan FCM dipengaruhi secara kuat oleh pemilihan ruang warna/komponen fitur warna, di mana komponen pada LAB (khususnya kanal chromatic) memperlihatkan kontribusi yang signifikan terhadap keberhasilan segmentasi pada eksperimen mereka. [5] Walaupun domain yang diuji adalah citra bunga, pola temuannya tetap relevan untuk penelitian ini: ketika fitur yang dipakai adalah warna, maka ruang warna yang lebih selaras dengan persepsi/struktur pemisahan warna sering memberi hasil segmentasi/cluster yang lebih stabil.

Selain itu, kebutuhan evaluasi multi-color space juga terkait langsung dengan cara kita merangkum warna menjadi representasi yang ringkas. Chang & Mukai menggunakan K-Means pada CIELAB sebagai tahap awal untuk menghasilkan kandidat warna, lalu memperkuatnya melalui seleksi berbasis fitur (misalnya saturasi, kontras, dan area) agar warna dominan yang dipilih lebih representatif. [3] Ini menegaskan bahwa pemilihan ruang warna bukan hanya memengaruhi “seberapa mudah data terpisah”, tetapi juga memengaruhi “seberapa representatif centroid/warna dominan” terhadap persepsi visual.

Dengan demikian, evaluasi multi-color space dalam penelitian ini memiliki dasar literatur yang jelas: (1) secara konseptual, setiap color model/space membawa kompromi perseptual–komputasi; (2) secara empiris, kinerja segmentasi kulit dapat berubah antar ruang warna; dan (3) pada tugas clustering/ekstraksi warna, pemilihan ruang warna dapat mengubah kualitas cluster maupun representasi warna yang dihasilkan. [9] [2] [5] [3]

### 2.1.5 Analisis Gap

Berdasarkan kajian pada subbab sebelumnya, terlihat bahwa penelitian-penelitian terkait telah menyediakan fondasi kuat pada sisi deteksi/segmentasi kulit, pemilihan ruang warna, dan pemanfaatan clustering untuk segmentasi/ekstraksi warna. Namun, keterhubungan antar komponen tersebut—khususnya untuk membentuk representasi warna kulit yang stabil sebagai dasar rekomendasi—masih menyisakan ruang pengembangan. Hal ini menjadi penting karena kualitas rekomendasi berbasis warna pada akhirnya sangat bergantung pada konsistensi ekstraksi warna kulit terhadap variasi kondisi akuisisi, serta kesesuaian representasi warna terhadap persepsi pengguna. [9] [2]

Secara lebih spesifik, gap penelitian dapat dirumuskan sebagai berikut.

1. Belum adanya pengujian komparatif yang membandingkan ruang warna RGB, HSV, dan CIELAB secara bersamaan yang difokuskan pada pengujian ekstraksi *skin tone* secara komprehensif. Kolkur dkk. [1] menggunakan kombinasi model warna RGB, HSV, dan YCbCr untuk deteksi kulit, namun evaluasi ketiganya tidak dilakukan secara paralel pada satu kerangka pengujian yang sama, melainkan sebagai kombinasi aturan ambang batas tunggal. Muratbekova dkk. [9] menyusun perbandingan model warna secara umum dan menegaskan bahwa pemilihan *color space* bersifat *task-dependent*, tetapi eksperimen tersebut tidak diarahkan secara khusus pada domain warna kulit manusia. Di sisi lain, Daithankar dkk. [21] menganalisis beberapa model warna untuk deteksi wajah, namun analisis tersebut berfokus pada melokalisasi area wajah (*face localization*), bukan pada evaluasi sistematis tiga ruang warna RGB, HSV, dan CIELAB sebagai dasar representasi *skin tone* untuk kebutuhan lanjutan. Dengan demikian, belum ditemukan studi yang mengevaluasi ketiga ruang warna tersebut secara bersamaan dengan metrik yang konsisten khusus untuk kasus warna kulit.
2. Evaluasi pada literatur pengolahan citra terdahulu mayoritas membatasi metodenya hanya hingga tahap akurasi segmentasi klaster objek, dan belum ada kelanjutan pengujian menuju validasi akurasi rekomendasi fungsional. Rosyani dkk. [5] mengevaluasi performa K-Means dan Fuzzy C-Means hingga tahap akurasi segmentasi citra berdasarkan fitur warna menggunakan *ground truth*, tanpa melanjutkan hasil pengelompokan tersebut menjadi sebuah sistem keputusan rekomendasi. Chen dan Wang [7] memperkenalkan pendekatan *three-way clustering* untuk menangani area batas yang ambigu pada pengolahan citra digital, namun kerangka tersebut juga berhenti pada level pembentukan klaster. Totti dan Setiyawati [18] membandingkan efisiensi K-Means, Gaussian Mixture Model, dan Spectral Clustering, yang menempatkan evaluasi akhir pada akurasi klasterisasi ekspresi wajah semata. Pola ini menunjukkan adanya jarak metodologis antara pembentukan klaster yang optimal secara matematis dan pengujian validitas keluaran terhadap fungsionalitas rekomendasi pengguna akhir.

Belum optimalnya penggunaan formula metrik jarak warna CIEDE2000 sebagai tahap validasi objektif pasca-*clustering* dalam menentukan kecocokan palet warna. Sebagian besar studi pengelompokan warna masih mengandalkan jarak *Euclidean* sederhana pada ruang warna tertentu untuk menghitung kemiripan antar-*centroid* [5], [6]. Meskipun Alyoubi dkk. [14] telah menerapkan metrik Delta E (CIEDE2000) bersama algoritma *clustering* untuk meningkatkan akurasi diferensiasi warna dasar manusia (*human feature colors*), pemanfataannya belum diintegrasikan sebagai instrumen evaluasi akhir untuk memvalidasi kedekatan *centroid* warna kulit hasil pengelompokan dengan ruang harmoni warna pakaian. Formula CIEDE2000 menawarkan perhitungan jarak warna yang selaras dengan persepsi visual manusia dibandingkan jarak linier biasa, sehingga penerapannya krusial untuk memastikan bahwa hasil ekstraksi sistem tidak hanya valid secara statistik tetapi juga akurat secara perseptual.

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

Penelitian ini menggunakan jenis penelitian pengembangan purwarupa (*prototype*) dengan metode eksperimental komputasional. Pendekatan kuantitatif diterapkan secara terstruktur untuk menguji efektivitas manipulasi data piksel visual secara objektif. Desain penelitian ini secara eksplisit dipartisi ke dalam dua bagian utama sebagai berikut:

1. Pengembangan *Prototype* Sistem Rekomendasi: Merancang dan mengimplementasikan sistem informasi berbasis aplikasi web interaktif yang mampu memproses input citra digital secara otomatis hingga menghasilkan luaran keputusan rekomendasi palet warna pakaian.
2. Eksperimen Perbandingan *Color Space*: Menguji secara empiris performa pengelompokan fitur piksel pada tiga ruang warna yang berbeda, yaitu *Red, Green, Blue* (RGB), *Hue, Saturation, Value* (HSV), dan *Commission Internationale de l'Eclairage L\*, a\*, b\** (CIELAB).

Alur pemrosesan data di dalam desain eksperimental ini melibatkan pemetaan komponen input-output yang didefinisikan secara tegas. Input utama sistem berupa citra digital wajah manusia dua dimensi dengan ekspresi natural. Variabel perlakuan yang diterapkan adalah tiga jenis *color space* (RGB, HSV, dan CIELAB) untuk memisahkan parameter intensitas cahaya (*luminance*) dan informasi warna murni (*chrominance*) [1], [9]. Luaran (*output*) akhir yang dihasilkan oleh *pipeline* komputasi ini adalah titik pusat klaster (*centroid*) warna kulit pengguna serta rekomendasi palet warna pakaian yang tervalidasi secara estetika mode [8], [17]. Untuk menentukan ruang warna yang paling optimal, evaluasi kualitas *clustering* diukur melalui tiga metrik internal, yaitu *Silhouette Score*, *Davies-Bouldin Index* (DBI), dan *Calinski-Harabasz Index* (CHI) [18]. Selanjutnya, keandalan saran pakaian divalidasi berdasarkan kalkulasi jarak perseptual menggunakan formula standar CIEDE2000 [14].

*![](data:image/png;base64...)*

Gambar 3.1 Diagram Alur Sistem dan Desain Eksperimental

## 3.2 Metode Pengumpulan Data

Metode pengumpulan data dalam penelitian ini dibagi menjadi dua kategori utama, yakni data citra wajah manusia dan data preferensi warna pakaian yang berbasis pada teori harmoni warna. Penataan dataset dilakukan secara teliti untuk memastikan bahwa sistem memiliki basis pengetahuan yang kuat mengenai keragaman warna kulit manusia (*skin tone diversity*) [15].

### 3.2.1 Dataset Citra Wajah (Data Primer dan Sekunder)

Data citra yang digunakan merupakan kombinasi dari dataset publik berskala besar dan pengambilan sampel berdasarkan *website kaggle*. Dataset sekunder diambil dari repositori penglihatan komputer (*computer vision*) seperti dataset SFHQ (*Skin Feature High Quality*) yang menyediakan ribuan citra wajah dengan resolusi tinggi dan variabilitas etnis yang luas [14]. Penggunaan dataset publik ini bertujuan untuk mengkalibrasi sensitivitas algoritma terhadap spektrum warna kulit yang sangat kontras, mulai dari *very light* hingga *very dark* [15].

Prosedur pengumpulan data dirancang untuk membangun basis pengetahuan komprehensif mengenai diversitas warna kulit (*skin tone diversity*) manusia [15]. Data dikumpulkan secara terstruktur ke dalam beberapa aspek teknis yang dijabarkan pada tabel berikut:

Tabel 3.1 Spesifikasi Karakteristik Dataset Penelitian

|  |  |  |
| --- | --- | --- |
| Aspek Dataset | Isi | Keterangan |
| Jumlah citra / Responden | 120 orang dengan warna kulit yang berbeda-beda | Representasi sampel yang memadai untuk pengujian klasterisasi |
| Variasi *Skintone* | Very light, light, intermediate, tan, brown, dark | Menjamin inklusivitas sistem terhadap keragaman etnis |
| Format *file* | JPG atau PNG | Format standar kompresi citra digital tanpa kehilangan detail fitur |
| Tipe gambar | *Indoor* (300–500 lux) dan *outdoor* (alami) | Menguji ketangguhan transformasi terhadap fluktuasi *illumination variance* |
| Sumber data | Repositori publik Kaggle (*Dataset Skin Tone*) dan Data Primer | Tautan:[www.kaggle.com/datasets/ducnguyen168/dataset-skin-tone](http://www.kaggle.com/datasets/ducnguyen168/dataset-skin-tone). Pengambilan data primer menggunakan kamera digital dengan resolusi minimal 1280x720 piksel. |

### 3.2.2 Dataset Rekomendasi Warna Pakaian

Data pendukung berupa aturan rekomendasi warna disusun berdasarkan studi psikologi warna dalam desain busana dan prinsip *seasonal color analysis* [8]. Data ini dikumpulkan melalui tinjauan pustaka sistematis terhadap standar industri *fashion* yang memetakan kecocokan warna kain tertentu dengan profil *undertone* kulit (dingin, hangat, atau netral) [16]. Dataset ini kemudian dikonversi ke dalam nilai digital (HEX atau RGB) yang akan digunakan oleh mesin sistem informasi sebagai tabel rujukan (*lookup table*) saat mencocokkan hasil ekstraksi warna kulit pengguna dengan rekomendasi pakaian yang paling harmonis secara visual [13], [17].

### 3.2.3 Instrumen Penelitian

Instrumen yang digunakan dalam proses pengumpulan dan pengolahan data meliputi perangkat keras berupa komputer dengan spesifikasi komputasi grafis yang memadai untuk menjalankan algoritma *clustering* secara iteratif, serta perangkat lunak pengembangan berbasis Python. Pustaka pemrograman seperti OpenCV digunakan untuk manipulasi piksel, Scikit-Learn untuk implementasi *unsupervised machine learning*, dan Matplotlib untuk visualisasi hasil evaluasi ruang warna [4], [22]. Seluruh data yang terkumpul disimpan dalam format repositori digital yang terstruktur guna memudahkan proses validasi silang pada tahap pengujian sistem.

## 3.3 Tahapan Penelitian

Pelaksanaan penelitian ini disusun secara sistematis dan kronologis melalui delapan tahapan terstruktur untuk memastikan bahwa setiap proses komputasi berkontribusi langsung terhadap akurasi dan keandalan sistem rekomendasi. Alur pengerjaan eksperimental komputasional ini dirancang guna mentransformasikan data visual mentah dari repositori digital menjadi keputusan rekomendasi palet busana yang valid. Penjabaran dari masing-masing tahapan operasional tersebut diuraikan sebagai berikut:

1. Prapemrosesan (*Preprocessing*) dan Segmentasi Citra Wajah: Tahap awal ini difokuskan pada pengondisian citra masukan yang berasal dari data primer maupun dataset publik *Kaggle*. Aktivitas prapemrosesan meliputi operasi standardisasi ukuran (*resizing*) matriks piksel untuk menjaga efisiensi penggunaan memori, dilanjutkan dengan reduksi derau (*noise reduction*) menggunakan penapis *Gaussian Blur* guna meminimalisasi gangguan tekstur pori-pori wajah. Setelah kualitas citra ditingkatkan, dilakukan segmentasi wilayah target menggunakan metode *rule-based adaptive thresholding* pada ruang warna YCbCr dan HSV untuk memisahkan area *skin* dan *non-skin* secara otomatis, sehingga menghasilkan *masking* biner wajah yang bersih dari gangguan rambut atau latar belakang.
2. *Clustering* K-Means pada Tiga *Color Space*: Data piksel hasil segmentasi selanjutnya ditransformasikan ke dalam tiga jenis model ruang warna yang dievaluasi, yaitu RGB, HSV, dan CIELAB. Algoritma pembelajaran mesin tanpa pengawasan (*unsupervised learning*) K-Means kemudian diterapkan pada masing-masing ruang warna tersebut secara paralel. Proses kuantisasi ini mempartisi distribusi warna piksel kulit ke dalam sejumlah klaster dinamis untuk menemukan nilai titik pusat (*centroid*) yang merepresentasikan fitur warna dominan secara spesifik pada masing-masing dimensi koordinat.
3. Evaluasi *Clustering*: Kualitas hasil partisi data dari ketiga ruang warna diuji secara kuantitatif tanpa mengandalkan label manual (*ground truth*) melalui metrik validasi internal. Pengujian dilakukan dengan menghitung nilai *Silhouette Score* untuk mengukur tingkat kekompakan dan keterpisahan objek, *Davies-Bouldin Index* (DBI) untuk mengevaluasi rasio penyebaran data terhadap jarak antar-sentroid, serta *Calinski-Harabasz Index* (CHI) untuk menilai perbandingan varians intra-klaster dan antar-klaster secara paralel.
4. Penentuan *Color Space* Terbaik: Data agregat yang diperoleh dari metrik evaluasi internal pada tahap sebelumnya digunakan sebagai basis analisis komparatif. Karakteristik dari masing-masing model warna diuji di bawah kondisi fluktuasi intensitas pencahayaan (*illumination variance*) yang berbeda. Ruang warna yang menghasilkan nilai indeks klasterisasi paling optimal—ditandai oleh *Silhouette Score* tertinggi serta nilai DBI terkecil—akan ditetapkan secara mutlak sebagai fondasi representasi komputasi utama untuk tahapan downstream.
5. Klasifikasi *Skintone* dan *Undertone*: Setelah ruang warna terbaik terpilih, sistem melakukan ekstraksi parameter biologis pengguna menggunakan nilai *centroid* dominan yang telah tervalidasi. Tingkat kecerahan warna kulit dikalibrasi secara objektif menggunakan metrik *Individual Typology Angle* (ITA) yang dikalkulasi secara matematis melalui komponen *Lightness* dan koordinat kuning-biru . Pada saat yang sama, arah sebaran nilai pada kanal (hijau-merah) dan digunakan untuk mendeduksi kategori *skin undertone* ke dalam kelompok *cool*, *neutral*, atau *warm*.
6. Pemetaan ke Rekomendasi Warna Pakaian: Profil karakteristik fisik berupa tingkat kecerahan kulit (ITA) dan kategori *undertone* yang telah diperoleh kemudian diintegrasikan ke dalam mesin rekomendasi purwarupa. Mesin ini bekerja menggunakan pendekatan berbasis aturan (*rule-based*) dengan merujuk langsung pada tabel rujukan digital (*lookup table*) yang disusun berdasarkan teori harmoni estetika visual dan psikologi desain busana. Sistem secara otomatis akan memetakan *anchor color* kulit pengguna untuk menghasilkan saran kombinasi warna pakaian yang serasi.
7. Validasi Hasil Rekomendasi: Palet warna busana yang dikeluarkan oleh sistem tidak langsung disajikan kepada pengguna, melainkan wajib melewati fase pengujian reliabilitas luaran. Validasi dilakukan secara komputasional dengan mengukur kedekatan jarak perseptual antara sentroid kulit aktual dengan nilai warna garmen pakaian yang direkomendasikan menggunakan standar formula kalkulasi jarak non-linear CIEDE2000. Proses ini menjamin bahwa luaran sistem terbukti ekuivalen dan konsisten secara estetika profesional.
8. Analisis dan Penarikan Kesimpulan: Tahap akhir dari penelitian ini adalah melakukan sintesis menyeluruh terhadap seluruh data eksperimen, performa komputasi lintas ruang warna, serta akurasi fungsional dari purwarupa aplikasi berbasis *Streamlit* yang telah dikembangkan. Hasil analisis tersebut kemudian digunakan sebagai landasan ilmiah untuk menarik kesimpulan akhir, menjawab rumusan masalah penelitian, serta menyusun rekomendasi pengembangan sistem informasi untuk masa mendatang.

![A diagram of a flowchart](data:image/png;base64...)

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

* + 1. Deteksi dan Segmentasi Kulit Tahap awal ini melibatkan prapemrosesan (*preprocessing*) citra untuk menormalisasi kondisi masukan. Deteksi area kulit dilakukan menggunakan metode *rule-based adaptive thresholding*. Teknik ini diterapkan dengan mengonversi citra ke ruang warna YCbCr dan HSV untuk mengisolasi piksel kulit berdasarkan karakteristik krominansinya [1], [21]. Penggunaan *masking* biner memastikan bahwa hanya piksel pada wilayah wajah yang akan diproses pada tahap berikutnya, sehingga mengurangi gangguan dari objek latar belakang atau rambut [2].
    2. Ekstraksi Warna Piksel yang telah berhasil terisolasi kemudian diolah menggunakan algoritma *unsupervised learning*, yaitu *K-Means clustering*. Algoritma ini akan mengelompokkan data warna piksel ke dalam sejumlah klaster yang telah ditentukan nilainya untuk menemukan sentroid warna yang paling dominan [6]. Nilai sentroid ini dianggap sebagai representasi digital dari warna kulit asli pengguna, yang mencakup informasi mengenai kecerahan (*lightness*) dan saturasi warna [19].
    3. Evaluasi Multi-Color Space Penelitian ini melakukan pengujian komparatif untuk mengevaluasi kualitas klasterisasi pada tiga ruang warna yang berbeda, yakni RGB, HSV, dan CIELAB. Kualitas hasil ekstraksi pada masing-masing ruang warna diukur menggunakan metrik validasi klaster internal yang komprehensif, meliputi *Silhouette Score*, *Davies-Bouldin Index* (DBI), dan *Calinski-Harabasz Index* [18], [25]. Tahap evaluasi ini krusial untuk menentukan ruang warna mana yang paling konsisten dalam menghadapi variasi intensitas cahaya dan keragaman pigmen kulit manusia [9].
    4. Rekomendasi Warna Pakaian Fase akhir dari *pipeline* ini adalah pemetaan hasil ekstraksi warna kulit ke dalam mesin rekomendasi. Mesin ini menggunakan logika *mapping* untuk mencocokkan profil kulit pengguna dengan palet warna pakaian yang telah dikurasi. Penentuan rekomendasi didasarkan pada prinsip harmoni warna universal, seperti skema komplementer (*complementary*), analog (*analogous*), dan triadik (*triadic*) guna menjamin keserasian visual secara teoretis [8], [17].

### 3.5.2 Rancangan Aturan Rekomendasi Warna

Mekanisme pemberian rekomendasi pada sistem ini dirancang menggunakan pendekatan *rule-based* (berbasis aturan) yang mengadopsi standar industri desain busana. Aturan ini tidak bekerja secara acak, melainkan menggunakan hasil analisis dari ruang warna CIELAB sebagai parameter utama.

Sistem akan mengklasifikasikan hasil sentroid klasterisasi ke dalam tiga kategori utama *skin undertone*: *cool* (dingin), *neutral* (netral), dan *warm* (hangat). Klasifikasi ini dilakukan dengan mengevaluasi distribusi nilai pada kanal *a*\* dan *b*\* dalam ruang CIELAB, di mana nilai *a*\* mewakili spektrum hijau-merah dan *b*\* mewakili spektrum biru-kuning [14]. Selain itu, tingkat kecerahan kulit dikalibrasi menggunakan metrik *Individual Typology Angle* (ITA) untuk memastikan rekomendasi bersifat inklusif terhadap spektrum kulit yang sangat terang hingga sangat gelap [13], [15].

Setelah kategori *undertone* ditentukan, sistem akan merujuk pada tabel rujukan (*lookup table*) yang berisi daftar warna garmen yang telah divalidasi oleh teori psikologi warna [8]. Sebagai contoh, pengguna dengan kategori *warm tone* akan diprioritaskan untuk menerima rekomendasi warna pakaian dengan nuansa bumi (*earth tone*), sementara pengguna *cool tone* akan diarahkan pada palet warna biru atau ungu yang bersifat komplementer terhadap rona kulit mereka [16], [17].

Mekanisme rekomendasi warna pakaian dalam penelitian ini tidak hanya didasarkan pada tingkat kecerahan kulit semata, tetapi merupakan hasil integrasi antara klasifikasi *Individual Typology Angle* (ITA) dan analisis *undertone* pada ruang warna CIELAB. Tabel 3.1 menyajikan matriks logika pemetaan yang menjadi algoritma dasar bagi mesin rekomendasi sistem.

Tabel 3.2 Logika Pemetaan Rekomendasi Warna Pakaian Berdasarkan Skin Tone dan Undertone

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

Tabel 3.5 Rancangan Matriks Hasil Perbandingan Ruang Warna

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Metrik | RGB | HSV | CIELAB | Keterangan |
| Silhouette Score | - | - | - | Semakin tinggi semakin baik |
| DBI | - | - | - | Semakin rendah semakin baik |
| CHI | - | - | - | Semakin tinggi semakin baik |
| Waktu Komputasi (ms) | - | - | - | Penilaian efisiensi algoritma |
| Peringkat Akhir | - | - | - | Ruang warna paling optimal |

Pengujian tersebut dioperasionalkan melalui skenario perlakuan yang diatur pada Tabel 3.6. Seluruh luaran dari ketiga skenario tersebut secara mutlak akan dibandingkan secara terpusat menggunakan dasar kalkulasi metrik warna yang ekuivalen.

Tabel 3.6 Skenario Pengujian *Clustering* Ruang Warna

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Skenario** | **Input** | **Color Space** | **Metode** | **Output yang Dibandingkan** |
| S1 | Citra wajah | RGB | K-Means | "Centroid + Silhouette, DBI, CHI" |
| S2 | Citra wajah | HSV | K-Means | "Centroid + Silhouette, DBI, CHI" |
| S3 | Citra wajah | CIELAB | K-Means | "Centroid + Silhouette, DBI, CHI" |

### 3.6.3 Validasi Rekomendasi Warna Pakaian

Sebagai tahap pemastian luaran akhir, sistem menerapkan formula metrik CIEDE2000. Metode ini berfungsi sebagai instrumen ukur validasi objektif untuk mengonfirmasi apakah palet kandidat warna pakaian yang direkomendasikan benar-benar selaras dan kompatibel secara presisi dengan warna kulit aktual hasil ekstraksi *clustering* [14]. CIEDE2000 diimplementasikan karena secara arsitektural metrik ini mampu mengukur perbedaan intensitas kromatik dengan meniru cara penglihatan sistem perseptual mata manusia bekerja, sehingga kualitas rekomendasi fesyen dapat dipertanggungjawabkan validitasnya secara saintifik.

Untuk menjamin bahwa luaran sistem purwarupa tidak hanya akurat secara komputasional tetapi juga relevan secara persepsi visual manusia, tahap validasi rekomendasi warna pakaian dijalankan menggunakan metrik jarak warna CIEDE2000. Berbeda dengan formulasi jarak *Euclidean* konvensional (seperti formula CIE76) yang mengkalkulasi garis lurus di dalam ruang koordinat kartesian multidimensi, formula CIEDE2000 dirancang secara komprehensif oleh *Commission Internationale de l'Eclairage* (CIE) untuk mengatasi masalah ketidakseragaman persepsi (*perceptual non-uniformity*) [9], [14]. Metrik ini bekerja dengan memperhitungkan pembobotan (*weighting factors*) yang kompleks pada parameter perbedaan tingkat kecerahan , perbedaan kroma , dan perbedaan rona atau *hue* Melalui koreksi matematis yang bersifat non-linear ini, nilai perbedaan warna (direpresentasikan sebagai ) yang dihasilkan benar-benar merepresentasikan bagaimana sistem penglihatan biologis manusia mendeteksi perbedaan, kemiripan, atau keserasian warna secara sangat presisi dan objektif [14].

Implementasi pengujian CIEDE2000 di dalam alur kerja purwarupa ini dilakukan dengan menjadikan titik pusat klaster (*centroid*) warna kulit pengguna yang telah diekstraksi pada ruang CIELAB sebagai titik referensi utama atau warna jangkar (*anchor color*). Selanjutnya, algoritma sistem akan mengukur jarak antara *centroid* kulit tersebut dengan kandidat palet warna pakaian (direpresentasikan dalam kode *HEX*) yang ditarik dari pangkalan data aturan rekomendasi [16]. Kalkulasi jarak perseptual ini berfungsi sebagai mekanisme filtrasi (*filtering mechanism*). Kalkulasi ini memastikan bahwa rekomendasi yang tergolong dalam harmoni *analogous* memiliki transisi jarak perseptual yang cukup dekat dan dapat ditoleransi oleh mata, sedangkan untuk aturan harmoni *complementary*, jaraknya terukur secara pasti berada pada kuadran spektrum warna yang berlawanan secara matematis namun tetap menghasilkan keseimbangan visual yang estetis [8], [14].

Lebih lanjut, hasil dari kalkulasi metrik CIEDE2000 ini akan diuji silang (*cross-validation*) dengan prinsip-prinsip dasar teori psikologi warna yang berlaku di dalam industri desain mode (*fashion design*) [8]. Palet warna pakaian akhir yang direkomendasikan dan ditampilkan pada antarmuka *Streamlit* wajib mencerminkan kesesuaian dengan metrik *Individual Typology Angle* (ITA) serta kategori *undertone* pengguna. Sebagai contoh skenario validasi, jika nilai jarak warna perseptual menunjukkan adanya deviasi visual yang melanggar logika pemetaan—misalnya kandidat garmen berwarna pastel pucat diukur dan terbukti memiliki jarak harmoni yang salah terhadap pengguna berspektrum kulit *warm undertone* kategori *Tan* maka algoritma sistem akan merevisi nilai tersebut dan menggantinya dengan kandidat warna pakaian lain dari pangkalan data [15], [17]. Melalui mekanisme validasi ganda yang mengawinkan tingkat presisi matematis metrik CIEDE2000 dengan pakem aturan estetika *fashion* ini, sistem informasi dapat memberikan tingkat akurasi personalisasi gaya yang sangat tinggi dan sepenuhnya terhindar dari bias subjektivitas pengamatan manual yang selama ini menjadi kendala konvensional [8], [17].

.

## 3.7 Jadwal Penelitian

Penelitian ini dilaksanakan dalam rentang waktu dari bulan Februari hingga Juli 2026. Kegiatan penelitian disusun secara bertahap mulai dari penyusunan proposal hingga sidang skripsi. Rincian jadwal pelaksanaan kegiatan penelitian dapat dilihat pada tabel berikut.

Tabel 3.2 Jadwal Penelitian

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **No** | **Kegiatan Penelitian** | **Fase** | **Feb** | **Mar** | | **Apr** | | **Mei** | **Jun** | **Jul** |
| 1 | Studi pustaka dan penelaahan literatur (Color Space & Clustering) | Persiapan | X | X | |  | |  |  |  |
| 2 | "Penyusunan draf proposal skripsi (Bab I Bab II dan Bab III)" | Persiapan | X | X | |  | |  |  |  |
| 3 | Seminar proposal dan revisi instrumen metodologi | Persiapan |  |  | | X | |  |  |  |
| 4 | "Implementasi algoritma preprocessing dan pipeline sistem" | Implementasi |  |  | | X | | X |  |  |
| 5 | "Pengujian komparatif K-Means pada ruang warna RGB HSV CIELAB" | Implementasi |  |  | |  | | X | X |  |
| 6 | "Evaluasi clustering (DBI CHI Silhouette) dan validasi CIEDE2000" | Implementasi |  |  | |  | |  | X |  |
| 7 | Penyusunan laporan akhir skripsi dan pelaporan hasil analisis | Pelaporan |  |  | |  | |  | X | X |
| 8 | Sidang akhir komprehensif | Pelaporan |  | |  | |  |  |  | X |

# BAB IV HASIL DAN PEMBAHASAN

## 4.1 Gambaran Umum Implementasi Sistem

Implementasi sistem rekomendasi warna pakaian ini dikembangkan menggunakan pendekatan komputasional yang mengintegrasikan teknik pengolahan citra digital dan algoritma klasterisasi ( *clustering* ). Pengembangan lingkungan komputasi beroperasi di atas platform Google Colaboratory dengan memanfaatkan bahasa pemrograman Python. Ekosistem pustaka perangkat lunak yang diimplementasikan mencakup beberapa modul utama yang bekerja secara hierarkis. Pustaka OpenCV versi 4.13.0 digunakan untuk keperluan manipulasi dan prapemrosesan citra digital dasar, sedangkan pustaka NumPy versi 2.0.2 difungsikan untuk memproses operasi matriks numerik dari piksel gambar. Tahapan inti berupa ekstraksi warna dominan berbasis pembelajaran tanpa pengawasan ( *unsupervised learning* ) dijalankan menggunakan pustaka Scikit-Learn; pustaka ini menangani eksekusi algoritma *K-Means*, kalkulasi penentuan jumlah klaster optimal melalui *Elbow Method*, serta perhitungan metrik evaluasi klaster secara internal [6], [18]. Selanjutnya, guna memastikan validitas rekomendasi warna secara perseptual, pustaka *colormath* dioperasikan secara khusus untuk mengeksekusi kalkulasi metrik perbedaan warna CIEDE2000 [14]. Secara arsitektural, purwarupa sistem ini direncanakan akan menggunakan *framework* Streamlit sebagai rencana pengembangan antarmuka ( *interface* ), guna memfasilitasi integrasi antara model *back-end* algoritma dan interaksi pengguna di tahap akhir implementasi.

[SISIPKAN GAMBAR 4.1: Screenshot lingkungan pengembangan Google Colaboratory yang menampilkan baris kode eksekusi atau import library Python yang digunakan] Gambar 4.1 Lingkungan Pengembangan Sistem Komputasi pada Google Colaboratory

Pada aspek manajemen arsitektur data, purwarupa sistem ini dikalibrasi menggunakan basis dataset yang terdiri atas 120 sampel citra wajah manusia dengan dukungan ekstensi format standar JPG dan PNG. Untuk menjaga stabilitas komputasi dan meminimalisasi kompleksitas dimensi spasial saat algoritma iteratif dijalankan, seluruh matriks citra masukan distandardisasi ke dalam resolusi konstan berukuran 256x256 piksel. Himpunan data ini dikompilasi dari dua sumber utama, yakni hasil akuisisi data primer secara mandiri yang digabungkan secara proporsional dengan kurasi dataset sekunder dari repositori publik "Dataset Skin Tone" pada platform Kaggle [26].

Guna menjamin ketangguhan ( *robustness* ) sistem dalam memproses keragaman karakteristik fisik demografi secara nyata, dataset yang dihimpun sengaja mencakup variasi spektrum warna kulit manusia yang komprehensif. Distribusi sampel warna wajah ( *skintone* ) diklasifikasikan ke dalam rentang *Individual Typology Angle* (ITA) yang mencakup seluruh spektrum dasar, mulai dari kategori *Very Light*, *Light*, *Intermediate*, *Tan*, *Brown*, hingga *Dark* [15]. Selain variasi biologis, dataset juga merepresentasikan perbedaan fluktuasi pencahayaan di lapangan untuk menguji ketahanan ekstraksi sentroid, yang mencakup pengambilan sampel pada kondisi dalam ruangan ( *indoor* ) maupun luar ruangan ( *outdoor* ) dengan pencahayaan alami [CATATAN: data numerik spesifik terkait tingkat *lux* pencahayaan tidak tersedia dalam pengujian ini].

[SISIPKAN GAMBAR 4.2: Sampel grid atau kolase citra wajah dari dataset yang memperlihatkan keragaman kategori tingkat kecerahan warna kulit (Very Light hingga Dark) beserta variasi kondisi pencahayaan indoor dan outdoor] Gambar 4.2 Sampel Dataset Citra Wajah dengan Variasi *Skintone* dan Kondisi Pencahayaan

## 4.2 Hasil Preprocessing dan Segmentasi Kulit

### 4.2.1 Hasil Deteksi dan Cropping Wajah

Tahapan komputasional pertama yang dilakukan setelah proses akuisisi citra mentah adalah melokalisasi area wajah (*face localization*). Pemisahan area target observasi dari latar belakang ini sangat penting untuk memastikan bahwa algoritma selanjutnya hanya mengekstraksi piksel pada wilayah kulit wajah. Pada purwarupa sistem ini, proses deteksi wajah diimplementasikan menggunakan metode *Haar Cascade Classifier* bawaan dari pustaka OpenCV, secara spesifik menggunakan modul haarcascade\_frontalface\_default.xml. Pemilihan algoritma dasar ini didasarkan pada tingkat efisiensi komputasinya yang ringan dan memadai untuk melokalisasi struktur citra wajah frontal, tanpa memerlukan akselerasi komputasi perangkat keras tingkat tinggi seperti *Graphics Processing Unit* (GPU).

Secara operasional, proses pemindaian area wajah dikalibrasi menggunakan parameter deteksi spesifik guna mengoptimalkan ketepatan pembacaan sistem. Parameter pencarian objek multiresolusi diatur melalui nilai scaleFactor=1.1, sedangkan parameter minNeighbors=5 diaplikasikan untuk memvalidasi kandidat wajah dan meminimalisasi deteksi palsu (*false positive*). Untuk mencegah sistem mengklasifikasikan objek latar belakang yang berukuran kecil sebagai wajah, parameter minSize diatur pada batas dimensi (60, 60) piksel. Apabila di dalam satu citra masukan terdeteksi lebih dari satu objek wajah, logika program secara otomatis akan mengambil dan mengisolasi wajah dengan area *bounding box* terbesar sebagai subjek utama. Setelah *bounding box* utama terbentuk, sistem mengaplikasikan perluasan (*padding*) sebesar 15% (padding=0.15). Perluasan kotak pembatas ini berfungsi untuk memastikan bahwa wilayah periferal wajah pengguna, seperti area dahi dan pipi terluar, ikut tercakup sepenuhnya agar representasi piksel warna kulit tidak terpotong.

Berdasarkan hasil pengujian komputasional terhadap keseluruhan dataset akhir yang berjumlah 120 sampel citra wajah, algoritma pendeteksi menunjukkan keberhasilan deteksi pada 97 gambar, di mana wajah berhasil dilokalisasi dan di-*crop* dengan baik. Di sisi lain, sistem mencatat adanya kegagalan deteksi (gambar di-*skip*) pada 23 sampel citra. Kegagalan pelokalan pada 23 citra tersebut disebabkan oleh keterbatasan bawaan (*inherent limitation*) dari detektor *Haar Cascade*, yang secara konseptual rentan mengalami penurunan performa apabila dihadapkan pada citra dengan variasi sudut kemiringan wajah (pose ekstrem) atau adanya oklusi parsial (objek yang menutupi sebagian fitur utama wajah).

Untuk menjaga stabilitas evaluasi, purwarupa ini telah dirancang dengan aturan mitigasi (*fallback*) pada level dataset. Berdasarkan aturan tersebut, apabila rasio gambar yang gagal dideteksi melebihi ambang batas 50% dari total dataset, maka seluruh dataset akan diinstruksikan untuk menggunakan citra *preprocessing* secara langsung tanpa melalui tahap *cropping*. Namun, pada eksperimen ini, rasio kegagalan aktual yang tercatat adalah 23 dari 120 citra (berkisar pada ~19%). Karena tingkat kegagalan tersebut tidak melampaui ambang batas 50%, mekanisme *fallback* level-dataset ini tidak terpicu (tidak aktif), sehingga eksperimen dilanjutkan menggunakan 97 citra wajah yang berhasil di-*crop* secara optimal.

[SISIPKAN GAMBAR 4.1: Perbandingan visual antara citra masukan asli dan hasil cropping wajah menggunakan Haar Cascade Classifier pada beberapa sampel dataset, yang memperlihatkan efek penerapan perluasan bounding box (padding) 15% sehingga area pipi dan dahi tetap tercakup]

Gambar 4.1 Hasil Deteksi dan *Cropping* Wajah Menggunakan *Haar Cascade Classifier*

### 4.2.2 Hasil Preprocessing dan Normalisasi Citra

Tahapan prapemrosesan (*preprocessing*) dan normalisasi citra merupakan fase krusial yang bertujuan untuk menstandardisasi kondisi masukan citra wajah sebelum dilakukan proses ekstraksi warna kulit. Operasi ini secara metodologis dirancang untuk mengatasi masalah ketidakseragaman iluminasi dan derau visual yang dapat menurunkan kualitas pembentukan klaster pada tahap selanjutnya.

Berdasarkan arsitektur purwarupa yang dikembangkan, urutan operasi prapemrosesan diawali dengan penerapan penapis *Gaussian Blur* menggunakan ukuran kernel spasial 5x5. Tujuan utama dari operasi pelembutan ini adalah untuk mereduksi derau (*noise*) spasial dan menghaluskan ketidakteraturan tekstur mikro pada permukaan kulit, seperti pori-pori wajah maupun artefak kompresi citra. Reduksi tekstur mikro ini sangat penting agar algoritma *K-Means* pada tahapan berikutnya tidak terdistraksi oleh variasi piksel yang tidak relevan dengan warna dasar kulit.

Setelah citra dihaluskan, operasi dilanjutkan dengan proses normalisasi pencahayaan. Untuk menghindari rusaknya informasi warna asli kulit pengguna, normalisasi tidak dilakukan secara langsung pada format warna BGR (atau RGB) linier. Matriks citra BGR terlebih dahulu dikonversi ke dalam ruang warna perseptual CIELAB. Pemilihan ruang warna CIELAB didasarkan pada kemampuannya dalam memisahkan intensitas kecerahan dari warna murni. Algoritma *Contrast Limited Adaptive Histogram Equalization* (CLAHE) kemudian diterapkan secara eksklusif hanya pada kanal kecerahan L\* (*Lightness*).

Dalam eksekusi CLAHE, sistem menggunakan konfigurasi parameter tileGridSize=(8,8) yang berfungsi membagi citra ke dalam grid berukuran 8x8 piksel untuk pemerataan kontras secara lokal dan adaptif. Selanjutnya, parameter clipLimit=2.0 diaplikasikan untuk membatasi penguatan kontras agar tidak terjadi amplifikasi derau yang berlebihan pada area wajah yang seragam. Selama proses normalisasi kecerahan ini berlangsung, kanal a\* dan b\* yang menyimpan informasi krominansi (warna murni kulit) dibiarkan utuh dan tidak dimanipulasi sama sekali. Setelah pemerataan pada kanal L\* selesai, ketiga kanal tersebut digabungkan kembali dan dikonversi kembali ke dalam format BGR.

Melalui urutan operasi metodologis ini, sistem berhasil melakukan normalisasi pencahayaan secara efektif tanpa merusak atau mendistorsi informasi krominansi warna kulit asli. Meskipun tidak ada perekaman data kuantitatif berupa histogram numerik atau skor peningkatan kontras dalam eksperimen ini, evaluasi kualitatif secara visual menunjukkan bahwa integrasi *Gaussian Blur* dan CLAHE pada kanal L\* mampu menghasilkan citra wajah dengan distribusi pencahayaan yang lebih merata, minim bayangan asimetris, dan siap untuk diproses secara optimal oleh algoritma *K-Means*.

[SISIPKAN GAMBAR 4.1: perbandingan citra sebelum dan sesudah CLAHE + Gaussian Blur] Gambar 4.1 Perbandingan Kualitatif Visual Citra Wajah Asli dan Hasil Prapemrosesan (*Gaussian Blur* dan CLAHE)

**4.2.3 Hasil Segmentasi Area Kulit**

Tahapan krusial selanjutnya setelah citra wajah melalui proses prapemrosesan adalah segmentasi area kulit. Proses ini bertujuan untuk mengisolasi area target dari latar belakang serta atribut fitur wajah lainnya guna menghasilkan *skin mask* biner yang bersih. Untuk meminimalisasi deteksi palsu (*false positive*) yang sering terjadi jika hanya mengandalkan satu dimensi warna, sistem ini mengimplementasikan metode segmentasi berbasis *majority voting* dari tiga ruang warna independen: RGB, HSV, dan YCrCb [1], [24]. Perlu dicatat bahwa ruang warna CIELAB belum digunakan pada tahap segmentasi *thresholding* ini, melainkan baru akan dioperasikan pada tahapan *clustering* untuk mengekstraksi representasi piksel yang telah berhasil dilokalisasi.

Pemilihan kombinasi tiga ruang warna (RGB, HSV, dan YCrCb) didasarkan pada kemampuan masing-masing model dalam mendefinisikan batasan krominansi kulit. Aturan ambang batas (*thresholding*) yang ditetapkan untuk masing-masing ruang warna adalah sebagai berikut:

1. Ruang Warna RGB: Piksel diklasifikasikan sebagai kandidat kulit jika memenuhi parameter linier R > 95, G > 40, B > 20, dengan proporsi R > G dan R > B. Selain itu, digunakan pula parameter |R - G| > 15 serta selisih antara nilai maksimum dan minimum dari ketiga kanal > 15 [1].
2. Ruang Warna HSV: Karena mampu memisahkan kecerahan (Value) dari informasi warna (Hue dan Saturation), aturan HSV ditetapkan pada rentang Hue 0–25 dan 160–179, rentang Saturation 25–180, dan rentang Value 70–255. Parameter ini dirancang secara khusus untuk mengakomodasi spektrum warna kulit pengguna dari kategori terang hingga gelap [2].
3. Ruang Warna YCrCb: Segmentasi difokuskan pada isolasi komponen krominansi merah dan biru dengan menetapkan ambang batas nilai Cr pada rentang 133–173 dan nilai Cb pada rentang 77–127 [24].

Mekanisme *majority voting* kemudian diterapkan pada hasil deteksi ketiga aturan tersebut. Sebuah piksel secara definitif ditetapkan sebagai bagian dari *mask* kulit wajah hanya jika piksel tersebut berhasil lolos uji ambang batas pada minimal dua dari tiga aturan ruang warna (RGB, HSV, YCrCb). Melalui pendekatan *voting* ini, area wajah yang secara konseptual memiliki profil krominansi di luar rentang warna pigmen kulit, seperti bola mata, alis, dan bibir, berhasil dieksklusikan dari *mask* utama secara otomatis.

Guna menyempurnakan hasil segmentasi dan membersihkan sisa derau (*noise*) berukuran kecil pada *mask* biner, sistem menjalankan proses pembersihan morfologis (*morphological cleanup*). Operasi ini terdiri dari proses *opening* sebanyak 1 iterasi untuk membuang piksel derau terluar, yang dilanjutkan dengan operasi *closing* sebanyak 2 iterasi menggunakan matriks *kernel* berukuran 5x5 piksel untuk menutup celah-celah kecil (lubang) di dalam area kulit utama.

Secara kuantitatif, penerapan *pipeline* segmentasi pada 97 sampel citra wajah yang valid berhasil mengekstraksi total himpunan piksel kulit sebanyak 3.363.613 piksel. Kuantitas himpunan piksel kulit ini bersifat identik dan akan digunakan secara seragam sebagai data masukan (*input*) untuk representasi RGB, HSV, maupun CIELAB pada tahapan iterasi *clustering* selanjutnya.

Meskipun metode *rule-based thresholding* dengan mekanisme *majority voting* ini terbukti efisien secara komputasional, pendekatan ini secara konseptual tetap memiliki keterbatasan umum. Kesulitan segmentasi terkadang masih dapat dijumpai pada kasus variasi sudut wajah ekstrem atau adanya area oklusi parsial (seperti helaian rambut yang menutupi sebagian area pipi). Keterbatasan ini terjadi mengingat algoritma *thresholding* beroperasi murni pada level distribusi warna piksel, tanpa dibekali oleh analisis pemahaman semantik atau struktur geometris objek wajah itu sendiri [20], [21]. Namun secara keseluruhan, *masking* yang dihasilkan sudah sangat memadai untuk membuang elemen non-kulit dari citra observasi.

[SISIPKAN GAMBAR 4.x: visualisasi mask RGB, HSV, YCrCb, mask gabungan voting, dan overlay hasil segmentasi] Gambar 4.x Perbandingan Visual *Skin Mask* Independen, *Mask* Gabungan (*Majority Voting*), dan Hasil *Overlay* Segmentasi Kulit Wajah

**4.2.4 Penanganan Fallback Deteksi Wajah**

Dalam pengembangan sistem rekomendasi berbasis pengolahan citra, ketangguhan (*robustness*) alur pemrosesan data (*pipeline*) menjadi parameter operasional yang sangat krusial. Seperti yang telah diuraikan sebelumnya, algoritma pelokalan objek memiliki keterbatasan bawaan terhadap variasi pose atau oklusi. Untuk menjaga agar fungsionalitas sistem berjalan secara berkesinambungan ketika detektor wajah gagal melokalisasi target, purwarupa ini dirancang dengan dua mekanisme mitigasi (*fallback mechanism*) yang beroperasi secara terpisah. Kedua mekanisme ini disesuaikan dengan kebutuhan arsitektural yang berbeda, yakni *fallback* pada level dataset (untuk pemodelan) dan *fallback* pada level prediksi individual (untuk *live prediction* bagi pengguna).

Pada arsitektur *pipeline* pemrosesan dataset, kegagalan deteksi wajah umumnya ditangani dengan mengeliminasi atau melewati (*skip*) sampel citra yang bermasalah guna menjaga kemurnian data (*data purity*) pembentuk sentroid. Meskipun demikian, sistem tetap menetapkan sebuah aturan *fallback* level-dataset sebagai langkah pengamanan ( *failsafe* ). Aturan ini menetapkan bahwa apabila rasio kegagalan deteksi wajah melampaui ambang batas 50% dari total keseluruhan sampel, maka seluruh *pipeline* segmentasi akan membatalkan proses *cropping* dan beralih menggunakan citra hasil prapemrosesan secara utuh untuk seluruh basis data. Berdasarkan hasil pengujian eksperimental pada penelitian ini, jumlah kegagalan deteksi wajah tercatat sebanyak 23 dari total 120 sampel citra, atau berada pada rasio sekitar 19%. Karena angka tersebut berada jauh di bawah ambang batas toleransi 50%, mekanisme *fallback* level-dataset ini tidak terpicu dan tidak aktif selama eksperimen berlangsung.

Di sisi lain, perlakuan yang sama tidak dapat diimplementasikan pada *pipeline* prediksi individual (*live prediction*). Secara konseptual arsitektur, sebuah sistem rekomendasi yang berhadapan langsung dengan pengguna akhir tidak boleh mengalami kegagalan fungsi secara menyeluruh hanya karena satu citra masukan gagal dipindai area wajahnya. Untuk menghindari terhentinya layanan, sistem dilengkapi dengan *fallback* level-prediksi individual. Apabila fungsi prediksi (predict\_skin\_and\_recommend) mengembalikan nilai kosong karena ketiadaan koordinat wajah pada sebuah gambar, sistem secara otomatis akan menyubstitusi area *crop* wajah tersebut dengan citra hasil prapemrosesan utuh dari gambar asli pengguna itu sendiri. Substitusi ini murni menggunakan manipulasi citra prapemrosesan tanpa melibatkan *cropping*, dan sama sekali tidak menggunakan pembuatan data sintetis atau data dari luar sistem. Substitusi ini memastikan algoritma ekstraksi warna dan pencocokan rekomendasi tetap menerima matriks numerik yang valid untuk diproses hingga menjadi luaran rekomendasi pakaian.

Dalam pengujian operasional prediksi terhadap citra tunggal pengguna yang terekam di dalam sistem, fungsi pelokalan berhasil mendeteksi keberadaan wajah dengan status *Face detected: True*. Hal ini menunjukkan bahwa sistem mampu mengeksekusi *pipeline* utama dengan sempurna pada pengujian tersebut, sehingga mekanisme *fallback* individual tidak teramati aktif pada kasus uji tersebut. Lebih lanjut untuk kasus pengujian lainnya, [CATATAN: data jumlah kasus fallback level-prediksi individual yang terpicu pada pengujian belum tersedia] di dalam catatan komputasi saat ini. Walaupun demikian, keberadaan arsitektur *fallback* ganda ini membuktikan bahwa purwarupa sistem telah dirancang dengan tingkat ketersediaan (*availability*) yang tinggi dalam mengakomodasi berbagai kondisi masukan citra yang suboptimal di skenario dunia nyata.

[SISIPKAN GAMBAR 4.x: diagram alur perbandingan fallback level-dataset vs level-prediksi individual] Gambar 4.x Diagram Alur Perbedaan Arsitektur Penanganan Kegagalan Deteksi Wajah pada Level Dataset dan Prediksi Individual

## 4.3 Hasil Penentuan Jumlah Cluster (K) Optimal

Penentuan jumlah klaster ($K$) yang optimal merupakan tahapan matematis yang sangat krusial dalam implementasi algoritma *K-Means clustering*. Pemilihan nilai $K$ yang tidak tepat dapat berisiko memicu *under-segmentation* maupun *over-segmentation*, yang pada akhirnya akan mendistorsi representasi titik pusat (*centroid*) warna kulit asli pengguna [4], [22].

Pada tahap awal investigasi, sistem melakukan pengujian penentuan jumlah klaster menggunakan pendekatan *Elbow Method* yang berbasis pada minimalisasi nilai varians internal atau *Within-Cluster Sum of Squares* (WCSS/Inertia) [19]. Secara metodologis, pengujian *Elbow Method* ini dioperasikan pada rentang nilai $K=2$ hingga $K=10$ menggunakan sampel sebanyak 4.000 piksel. Perlu ditegaskan bahwa evaluasi *Elbow Method* ini hanya dijalankan secara eksklusif pada ruang warna RGB sebagai representasi ruang dimensi awal (baseline), dan tidak dieksekusi secara paralel pada ketiga ruang warna. Berdasarkan kurva grafik penurunan nilai inersia yang dihasilkan pada ruang warna RGB, titik infleksi atau patahan sudut yang menyerupai sikut (*elbow point*) terdeteksi dan merekomendasikan nilai $K=4$ [4].

[SISIPKAN GAMBAR 4.x: Grafik Elbow Method RGB (Inertia vs K, rentang K=2-10)]

Gambar 4.x Grafik *Elbow Method* pada Ruang Warna RGB untuk Penentuan Estimasi Awal Nilai *K*

Namun demikian, rekomendasi nilai $K=4$ dari hasil pengujian *Elbow* tersebut tidak serta-merta ditetapkan sebagai parameter final. Dalam tahapan operasional dan eksperimen lintas ruang warna secara keseluruhan, sistem secara definitif menggunakan nilai $K=3$. Perbedaan keputusan ini dilandasi oleh justifikasi akademik bahwa *Elbow Method* (yang murni bersandar pada WCSS) memiliki kelemahan interpretasi visual yang subjektif dan hanya mengukur tingkat kepadatan internal klaster tanpa memperhitungkan tingkat separasi data [6]. Oleh karena itu, penentuan nilai $K$ final dikoreksi dan dikalibrasi ulang menggunakan mekanisme *Composite Score* yang jauh lebih komprehensif. Skor komposit ini mengevaluasi matriks *Silhouette Score*, *Davies-Bouldin Index* (DBI), *Calinski-Harabasz Index* (CHI), dan *Stability Score* secara simultan (yang akan dibahas secara rinci pada sub-bab 4.5). Berdasarkan pengukuran metrik komposit tersebut, konfigurasi $K=3$ terbukti menghasilkan kualitas arsitektur partisi yang paling optimal dan stabil, dengan raihan nilai *composite score* mencapai 0,9856 pada ruang warna RGB [6], [22].

Untuk menindaklanjuti dan memvalidasi stabilitas konvergensi algoritma lintas representasi, kandidat jumlah klaster yang diuji lebih lanjut pada ketiga model ruang warna difokuskan pada nilai $K=3$, $K=5$, dan $K=7$. Tabel 4.1 menyajikan rekapitulasi nilai *Inertia* (WCSS) dari hasil eksekusi algoritma *K-Means* pada kandidat nilai $K$ tersebut melintasi ruang warna RGB, HSV, dan CIELAB.

Tabel 4.1 Nilai *Inertia* (WCSS) pada Berbagai Skenario Nilai *K* Lintas Ruang Warna

|  |  |  |  |
| --- | --- | --- | --- |
| Color Space | K=3 | K=5 | K=7 |
| RGB | "7.406.524,00" | "4.254.135,50" | "3.281.391,75" |
| HSV | "12.162.169,00" | "7.470.458,00" | "5.620.293,00" |
| CIELAB | "2.514.213,25" | "1.447.773,50" | "1.120.766,38" |

Berdasarkan data kuantitatif pada Tabel 4.1, terdapat catatan konseptual yang sangat penting terkait interpretasi nilai matematis tersebut. Penurunan nilai *Inertia* seiring dengan bertambahnya nilai $K$ merupakan sifat bawaan matematis yang wajar karena jarak ke *centroid* semakin menyempit [19]. Namun, nilai *Inertia* ini tidak dapat dikomparasikan secara langsung antar ruang warna (*cross-color space comparison*). Sebagai contoh, nilai inersia CIELAB yang tampak jauh lebih kecil dibandingkan RGB atau HSV tidak mengindikasikan bahwa CIELAB lebih superior dalam konteks metrik ini. Ketidakmampuan komparasi langsung ini disebabkan oleh perbedaan skala unit pengukuran fundamental dari masing-masing matriks warna; ruang RGB dan HSV beroperasi pada skala rentang numerik 0–255, sementara CIELAB memiliki skala kecerahan L\* dari 0–100 dengan skala oposisi krominansi a\* dan b\* yang sama sekali berbeda strukturnya. Oleh sebab itu, fungsi *Inertia* hanya valid digunakan sebagai metrik evaluasi internal untuk membandingkan perbedaan performa antar-nilai $K$ **di dalam satu ruang warna yang sama**, bukan untuk menilai dominasi performa lintas ruang warna [6], [19]. Evaluasi perbandingan performa sejati antar-ruang warna akan dieksekusi murni menggunakan metrik *Silhouette*, DBI, dan CHI yang sifatnya telah dinormalisasi.

## 4.4 Hasil Eksperimen *Clustering* Lintas Ruang Warna

Bagian ini memaparkan hasil pengelompokan matriks piksel warna kulit wajah yang telah disegmentasi untuk mengekstraksi representasi titik pusat (*centroid*) warna dominan. Eksekusi eksperimental ini dijalankan menggunakan algoritma *K-Means clustering* yang secara seragam dikonfigurasi pada parameter jumlah klaster final terpilih, yaitu $K=3$. Evaluasi kuantisasi warna ini didistribusikan ke dalam tiga skenario ruang warna yang berbeda guna mengidentifikasi karakteristik pembentukan klaster dan performa masing-masing model koordinat warna secara mandiri. Secara berturutan, sub-bab ini menguraikan luaran komputasi dari skenario S1 (ruang warna RGB), skenario S2 (ruang warna HSV), dan skenario S3 (ruang warna CIELAB).

### 4.4.1 Hasil Skenario S1 (Ruang Warna RGB)

Skenario eksperimen pertama (S1) dioperasikan dengan mendistribusikan piksel wajah pada ruang warna fundamental *Red, Green, Blue* (RGB). Secara teoretis arsitektural, RGB merupakan model linier aditif berbasis koordinat kartesian tiga dimensi yang dirancang sebagai standar utama akuisisi citra oleh perangkat keras sensor optik. Karakteristik utama dari model warna ini terletak pada kesederhanaan komputasi matematisnya, namun memiliki keterbatasan bawaan di mana seluruh komponen salurannya mengikat informasi intensitas cahaya (*luminance*) dan warna murni (*chrominance*) secara bersamaan dalam satu kesatuan ruang [9], [19].

Pada proses eksekusi algoritma *K-Means* dengan parameter klaster $K=3$, proses iterasi pada ruang warna RGB mencapai titik konvergensi dengan catatan nilai varians internal (*Inertia*) sebesar 7.406.524,00. Melalui proses kuantisasi tersebut, algoritma berhasil mengelompokkan jutaan piksel menjadi tiga titik *centroid* warna dominan yang merepresentasikan *skintone* pengguna secara digital. Ketiga warna representatif ini secara berurutan diekstraksi ke dalam format kode palet heksadesimal, yaitu #AF7F68, #6A4638, dan #E7BDA5.

Guna menilai kualitas struktur partisi yang terbentuk pada skenario mandiri ini, evaluasi dilakukan menggunakan tiga instrumen metrik validasi internal. Kinerja *clustering* pada ruang RGB menunjukkan tingkat kepadatan dan kohesi yang tergolong solid, dibuktikan oleh pencapaian nilai *Silhouette Score* sebesar 0,4784. Tingkat kerapatan internal di dalam masing-masing klaster tervalidasi melalui metrik *Davies-Bouldin Index* (DBI) yang menempati angka 0,6783, sementara rasio dispersi varians penentu pemisahan antar-klaster yang diukur menggunakan *Calinski-Harabasz Index* (CHI) berhasil mencapai nilai 6.951,57 [6].

[SISIPKAN GAMBAR 4.1: visualisasi hasil clustering K-Means K=3 pada ruang warna RGB, termasuk centroid warna]

Gambar 4.1 Visualisasi Klaster dan Palet *Centroid* Kulit Wajah pada Ruang Warna RGB (Skenario S1)

### 4.4.2 Hasil Skenario S2 (Ruang Warna HSV)

Skenario eksperimen kedua (S2) dijalankan dengan memproyeksikan himpunan piksel area kulit ke dalam model ruang warna *Hue, Saturation, Value* (HSV). Berbeda dengan RGB, model HSV beroperasi pada sistem koordinat silindris yang dirancang secara khusus agar lebih intuitif dalam mendeskripsikan elemen warna sebagaimana cara indra penglihatan manusia menafsirkannya. Transformasi matematis menuju ruang HSV memisahkan informasi warna murni secara independen pada komponen *Hue* (rona sudut melingkar) dan *Saturation* (tingkat kemurnian), menjauhkannya dari intensitas cahaya yang dikurung pada saluran *Value* [19].

Eksekusi algoritma *K-Means* ($K=3$) pada skenario S2 ini berhasil merumuskan tiga titik *centroid* baru yang mewakili variasi rona dan kemurnian pigmen wajah pada ruang silindris. Sentroid tersebut ditransformasikan kembali ke format digital standar dan direpresentasikan oleh kode heksadesimal #7B5343, #D9AA92, dan #905F69. Namun, proses konvergensi pada representasi ini mencatatkan nilai *Inertia* kumulatif tertinggi di antara seluruh skenario, yakni sebesar 12.162.169,00. Tingginya angka inersia pada pemrosesan HSV ini memberikan indikasi awal bahwa persebaran data piksel memiliki tingkat tumpang tindih (*overlapping*) yang cukup masif.

Evaluasi metrik internal mandiri untuk skenario HSV mengonfirmasi fenomena struktural tersebut. Perolehan nilai *Silhouette Score* tercatat pada angka 0,4461, sementara nilai batas kepadatan klaster membesar pada *Davies-Bouldin Index* (DBI) dengan angka 0,7986. Indikasi bahwa klaster pada ruang fitur silindris ini relatif kurang kompak dan memiliki separasi antar-sentroid yang tidak begitu tegas dibuktikan dengan anjloknya rasio metrik *Calinski-Harabasz Index* (CHI) menjadi hanya 2.589,12 [6].

[SISIPKAN GAMBAR 4.2: visualisasi hasil clustering K-Means K=3 pada ruang warna HSV, termasuk centroid warna]

Gambar 4.2 Visualisasi Klaster dan Palet *Centroid* Kulit Wajah pada Ruang Warna HSV (Skenario S2)

### 4.4.3 Hasil Skenario S3 (Ruang Warna CIELAB)

Skenario eksperimen ketiga (S3) dioperasikan dengan mentransformasikan matriks visual piksel kulit masukan ke dalam model ruang warna perseptual CIELAB (atau $L^\*a^\*b^\*$). Karakteristik fundamental yang mendasari ruang warna standar internasional ini adalah sifatnya yang *perceptually uniform* [9]. Pada ruang dimensi LAB, jarak geometris kartesian dikalibrasi secara matematis agar berbanding lurus dan selaras dengan perbedaan intensitas warna asli yang dirasakan oleh optik biologis manusia. Model ini memisahkan parameter kecerahan murni pada kanal $L^\*$ secara absolut dari informasi transisi oposisi kromatik pada kanal $a^\*$ dan $b^\*$ [3].

Ketika algoritma klasterisasi *K-Means* dengan parameter $K=3$ dijalankan pada matriks perseptual ini, sistem berhasil mengekstraksi tiga titik dominan yang direpresentasikan secara akurat oleh palet heksadesimal #E6BDA3, #694538, dan #AB7D67. Iterasi komputasi pada skenario CIELAB menghasilkan nilai akhir *Inertia* sebesar 2.514.213,25. Perlu dicatat secara metodologis bahwa skala metrik inersia LAB ini tidak berbanding lurus dan tidak dapat dikomparasikan secara langsung (*incomparable*) jika disandingkan dengan nilai inersia linier RGB maupun silindris HSV [19]. Hal ini murni disebabkan oleh perbedaan ekstrem pada skala rasio unit pembentuk saluran ($L^\*$ beroperasi pada rentang 0-100 dengan oposisi warna yang memiliki ekuivalen tersendiri), sehingga nilai inersia yang secara nominal terlihat lebih kecil ini tidak mengindikasikan superioritas klaster secara otomatis.

Performa pembentukan arsitektur partisi pada ruang CIELAB dibuktikan secara kuantitatif melalui perolehan nilai metrik validasi internal yang sangat kompetitif. Pada konfigurasi $K=3$ ini, skenario CIELAB mendemonstrasikan tingkat kedekatan kohesi internal dengan *Silhouette Score* pada angka 0,4769. Selain itu, sebaran data piksel terdistribusi dengan kepadatan struktur spasial yang sangat rapat dan jarak pemisah yang kuat, dibuktikan melalui capaian nilai *Davies-Bouldin Index* (DBI) di angka 0,6770 serta pencapaian metrik kriteria rasio varians pemisah pada *Calinski-Harabasz Index* (CHI) yang menembus angka 6.972,03 [6].

[SISIPKAN GAMBAR 4.3: visualisasi hasil clustering K-Means K=3 pada ruang warna CIELAB, termasuk centroid warna]

Gambar 4.3 Visualisasi Klaster dan Palet *Centroid* Kulit Wajah pada Ruang Warna CIELAB (Skenario S3)

## 4.5 Hasil Evaluasi dan Perbandingan Performa Color Space

**4.5.1 Hasil Evaluasi Struktur Clustering**

Evaluasi struktur klaster bertujuan untuk mengukur kualitas arsitektur partisi piksel warna kulit yang dihasilkan oleh algoritma *K-Means* secara objektif, tanpa bergantung pada pelabelan manual (*ground truth*). Pengujian kualitas klaster ini dilakukan pada tiga ruang warna yang berbeda (RGB, HSV, dan CIELAB) dengan mengomparasikan performa pada tiga konfigurasi jumlah klaster ($K$), yaitu $K=3$, $K=5$, dan $K=7$. Berdasarkan landasan teori evaluasi kualitas klaster, penilaian difokuskan pada tiga metrik validasi internal utama: *Silhouette Score* (bernilai optimal jika mendekati 1), *Davies-Bouldin Index* atau DBI (bernilai optimal jika semakin kecil/mendekati 0), dan *Calinski-Harabasz Index* atau CHI (bernilai optimal jika semakin tinggi) [6], [25].

Hasil rekapitulasi perhitungan komputasional dari ketiga metrik tersebut terhadap seluruh kombinasi ruang warna dan nilai $K$ disajikan secara lengkap pada Tabel 4.1.

Tabel 4.1 Hasil Evaluasi Struktur Clustering per Color Space dan K

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Color Space | K | Silhouette Score | DBI | CHI |
| RGB | 3 | 4,784 | 6,783 | 6.951,57 |
| RGB | 5 | 3,759 | 8,436 | 6.547,56 |
| RGB | 7 | 3,100 | 10,033 | 5.775,46 |
| HSV | 3 | 4,461 | 7,986 | 2.589,12 |
| HSV | 5 | 3,774 | 8,460 | 2.602,26 |
| HSV | 7 | 3,631 | 7,928 | 2.502,81 |
| LAB | 3 | 4,769 | 6,770 | 6.972,03 |
| LAB | 5 | 3,707 | 8,494 | 6.535,20 |
| LAB | 7 | 3,085 | 10,035 | 5.768,30 |

Berdasarkan data matriks pada Tabel 4.1, dapat diobservasi adanya pola degradasi kualitas arsitektur klaster yang konsisten seiring dengan peningkatan jumlah $K$. Ketika nilai $K$ dinaikkan dari 3 menuju 5 dan 7, perolehan *Silhouette Score* mengalami penurunan secara merata pada ketiga ruang warna. Bersamaan dengan itu, rasio kepadatan klaster yang diukur melalui DBI menunjukkan pembengkakan nilai (memburuk) secara signifikan pada ruang warna RGB dan LAB (dari kisaran 0,67 menjadi 1,00), meskipun pada ruang HSV cenderung berfluktuasi secara minor. Tren serupa juga terlihat pada nilai CHI yang terus menyusut pada RGB dan LAB seiring bertambahnya $K$. Fenomena ini mengonfirmasi landasan teoretis bahwa pemaksaan jumlah partisi yang lebih besar ($K=5$ atau $K=7$) memicu terjadinya *over-segmentation*, di mana titik data piksel kulit wajah mulai terpecah ke dalam klaster-klaster redundan yang memiliki jarak internal yang renggang dan batas separasi yang ambigu [19].

Analisis komparatif yang lebih mendalam pada konfigurasi optimal $K=3$ menunjukkan bahwa ruang warna RGB dan CIELAB (LAB) mendemonstrasikan performa struktural yang sangat ketat dan kompetitif. Pada konfigurasi ini, model RGB mencatatkan nilai *Silhouette Score* yang sedikit lebih unggul (0,4784 berbanding 0,4769 pada LAB), yang menandakan kohesi piksel terhadap sentroidnya sangat baik [6]. Di sisi lain, ruang warna LAB sedikit lebih superior pada dua metrik lainnya, yakni mencatatkan tingkat dispersi DBI yang lebih rendah (0,6770 berbanding 0,6783 pada RGB) serta varians rasio CHI yang lebih tinggi (6.972,03 berbanding 6.951,57 pada RGB). Kedua model linier dan perseptual ini secara signifikan mengungguli performa ruang warna HSV pada titik $K=3$ yang hanya menorehkan *Silhouette Score* sebesar 0,4461 dan DBI sebesar 0,7986.

Satu temuan penting yang wajib digarisbawahi dari pengujian lintas variasi ini adalah performa metrik kriteria rasio varians (CHI) pada ruang warna HSV. Terlepas dari berapapun nilai $K$ yang digunakan, ruang warna HSV secara konsisten mencatatkan perolehan nilai CHI yang anjlok secara drastis (berada pada rentang 2.502,81 hingga 2.602,26). Nilai ini tertinggal jauh di bawah perolehan model RGB dan LAB yang stabil pada rentang 5.700 hingga nyaris menyentuh 7.000 [25]. Rendahnya nilai CHI pada model silindris ini memberikan indikasi matematis yang kuat bahwa struktur klaster yang terbentuk pada ruang HSV kurang memiliki pemisahan jarak antar-sentroid yang tegas (*between-cluster separation*). Tingkat tumpang tindih (*overlapping*) data warna yang tinggi ini menyebabkan HSV kurang ideal jika diandalkan untuk mengekstrak titik pusat palet warna kulit wajah secara presisi [19].

[SISIPKAN GAMBAR 4.x: grafik garis Silhouette/DBI/CHI vs K untuk ketiga color space]

Gambar 4.x Grafik Perbandingan Tren Kualitas *Clustering* (Metrik *Silhouette*, DBI, dan CHI) terhadap Kenaikan Nilai *K* Lintas *Color Space*

### 4.5.2 Hasil Analisis Stabilitas Klaster

Salah satu keterbatasan fundamental yang melekat pada algoritma *K-Means* adalah sensitivitas metode ini terhadap inisialisasi letak titik pusat (*centroid*) awal yang dipilih secara acak [6]. Untuk memastikan bahwa arsitektur klasterisasi yang diekstraksi tidak terjadi secara kebetulan akibat konfigurasi *seed* tertentu, penelitian ini melakukan evaluasi tambahan menggunakan metrik *Stability Score*. Secara konseptual, metrik ini mengukur tingkat konsistensi posisi *centroid* ketika algoritma *K-Means* dieksekusi ulang sebanyak 5 kali secara independen menggunakan nilai *seed* inisialisasi acak yang berbeda. Pada setiap akhir iterasi, posisi *centroid* diurutkan terlebih dahulu berdasarkan rata-rata tingkat kecerahannya (*lightness*), kemudian dihitung nilai standar deviasinya lintas-eksekusi. Interpretasi dari metrik ini berbanding lurus dengan nilainya; semakin kecil nilai *Stability Score* yang dihasilkan, maka pembentukan klaster dinilai semakin stabil dan konsisten dalam menghadapi variasi inisialisasi [6], [19].

Hasil perhitungan agregat dari uji stabilitas untuk ketiga ruang warna pada berbagai konfigurasi jumlah klaster ($K$) dirangkum pada Tabel 4.2.

Tabel 4.2 Hasil Stability Score per Color Space dan K

|  |  |  |
| --- | --- | --- |
| Color Space | K | Stability Score |
| RGB | 3 | 1,533 |
| RGB | 5 | 4,333 |
| RGB | 7 | 5,891 |
| HSV | 3 | 0 |
| HSV | 5 | 0 |
| HSV | 7 | 24,492 |
| LAB | 3 | 4,599 |
| LAB | 5 | 5,067 |
| LAB | 7 | 1,271 |

Berdasarkan data pada Tabel 4.2, ruang warna RGB mendemonstrasikan pola degradasi stabilitas yang sejalan dengan peningkatan jumlah $K$. Pada konfigurasi awal $K=3$, model RGB menunjukkan tingkat konsistensi yang cukup kokoh di angka 0,1533. Namun, ketika partisi warna dipaksa untuk dipecah lebih banyak, stabilitasnya menurun secara konstan menjadi 0,4333 pada $K=5$ dan 0,5891 pada $K=7$. Di sisi lain, model ruang warna CIELAB (LAB) memperlihatkan tingkat stabilitas yang relatif moderat pada konfigurasi $K=3$ dengan skor 0,4599 dan 0,5067 pada $K=5$, sebelum akhirnya menunjukkan penurunan deviasi pada $K=7$ (0,1271). Fluktuasi stabilitas moderat pada LAB ini merupakan karakteristik yang wajar bagi metode heuristik ketika memetakan distribusi piksel pada ruang perseptual yang kompleks [9].

Dalam observasi metrik stabilitas ini, ditemukan sebuah anomali matematis yang sangat signifikan pada skenario ruang warna HSV. Model HSV mencatatkan nilai *Stability Score* persis di angka 0,0000 pada konfigurasi $K=3$ maupun $K=5$. Secara akademis, perolehan nilai deviasi nol mutlak ini menuntut kehati-hatian dalam interpretasinya dan tidak dapat serta-merta disimpulkan sebagai bukti bahwa HSV memiliki kualitas klasterisasi yang secara absolut sempurna dan konsisten [19]. Nilai nol tersebut kemungkinan besar merupakan manifestasi dari artefak komputasi (*computational artifact*) yang lahir selama proses pembulatan (*rounding*) atau konversi ruang dimensi warna.

Ketika *centroid* hasil ekstraksi dari ruang silindris HSV ditransformasikan kembali ke dalam format RGB—guna menyeragamkan unit pengukuran standar deviasi—deviasi desimal berskala sangat kecil yang sebenarnya terjadi antar-eksekusi telah terpotong akibat proses pembulatan paksa ke dalam rentang bilangan bulat 0-255 [19]. Kerapuhan struktur sesungguhnya dari ruang warna HSV ini tervalidasi secara empiris ketika konfigurasi dinaikkan menjadi $K=7$. Pada titik tersebut, *Stability Score* HSV melonjak sangat drastis dan tidak terkendali hingga menyentuh angka 2,4492, menjadikannya skenario komputasi paling tidak stabil di antara seluruh rangkaian eksperimen. Oleh karena itu, capaian 0,0000 pada *K=3* harus diposisikan sebagai limitasi metodologis konversi, bukan parameter keunggulan mutlak HSV dibandingkan model linier aditif maupun perseptual.

[SISIPKAN GAMBAR 4.x: grafik batang perbandingan Stability Score antar color space dan K]

Gambar 4.x Perbandingan Visual Tingkat *Stability Score* Lintas Ruang Warna Berdasarkan Nilai Konfigurasi *K*

### 4.5.3 Skor Komposit dan Ranking Color Space Terbaik

Evaluasi metrik struktural dan analisis stabilitas yang telah diuraikan pada bagian sebelumnya menunjukkan bahwa tidak ada satupun ruang warna yang secara absolut mendominasi seluruh instrumen pengujian. Oleh karena itu, sebagai sintesis akhir untuk mendeduksi representasi ruang warna paling optimal, purwarupa sistem mengkalkulasi sebuah metrik agregat yang disebut skor komposit (*composite score*). Secara ringkas, penentuan peringkat akhir ini dieksekusi melalui perhitungan matematis yang memformulasikan bobot metrik sebesar 0,35 untuk *Silhouette Score*, 0,25 untuk nilai inversi dari *Davies-Bouldin Index* (DBI), 0,20 untuk *Calinski-Harabasz Index* (CHI), dan 0,20 untuk nilai inversi dari *Stability Score* [6], [25].

Tabel 4.3 menyajikan peringkat tiga terbaik ( *top 3* ) dari total 9 kombinasi skenario pengujian ruang warna dan jumlah klaster (K) berdasarkan perolehan skor komposit akhir.

Tabel 4.3 Skor Komposit dan Ranking Akhir (Top 3 dari 9 kombinasi)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ranking | Color Space | K | Silhouette | DBI | CHI | Stability | Composite Score |
| 1 | RGB | 3 | 4,784 | 6,783 | 6.951,57 | 1,533 | 9,856 |
| 2 | LAB | 3 | 4,769 | 6,770 | 6.972,03 | 4,599 | 9,594 |
| 3 | HSV | 3 | 4,461 | 7,986 | 2.589,12 | 0 | 6,442 |

Berdasarkan hasil kalkulasi komprehensif pada Tabel 4.3, ruang warna RGB dengan konfigurasi K=3 secara objektif dinobatkan sebagai model ekstraksi terbaik dengan raihan *composite score* tertinggi sebesar 0,9856. Namun, tinjauan akademik yang mendalam memperlihatkan bahwa keunggulan model RGB atas peringkat kedua, yakni ruang warna CIELAB (LAB) dengan K=3 (0,9594), memiliki selisih persentase yang sangat berdekatan dan tipis [9].

Keunggulan ruang warna RGB di puncak peringkat pada dasarnya tidak didorong oleh dominasi performa struktural klaster yang jauh lebih superior dibandingkan LAB. Jika dikomparasikan secara *head-to-head*, perolehan nilai metrik internal kedua ruang warna tersebut hampir identik; *Silhouette Score* RGB berada di 0,4784 dan LAB di 0,4769, nilai kepadatan DBI RGB di 0,6783 dan LAB di 0,6770, serta rasio varians CHI pada RGB sebesar 6.951,57 dan LAB sebesar 6.972,03 [6]. Faktor penentu (*tie-breaker*) utama yang melontarkan RGB ke peringkat pertama murni didorong oleh pencapaian *Stability Score* RGB yang jauh lebih solid, yakni 0,1533 dibandingkan 0,4599 milik LAB. Hal ini mengonfirmasi bahwa meskipun LAB mampu menghasilkan arsitektur klaster yang sedikit lebih padat (terlihat dari DBI dan CHI yang secara marjinal lebih baik), koordinat awal *centroid* RGB terbukti jauh lebih konsisten dan tidak mudah bergeser saat dihadapkan pada inisialisasi iterasi yang acak.

Di sisi lain, model ruang warna silindris HSV dengan konfigurasi K=3 tertinggal sangat jauh di peringkat ketiga dengan *composite score* sebesar 0,6442. Keterpurukan angka komposit ini secara langsung diakibatkan oleh sangat rendahnya daya pisah antar-klaster yang direpresentasikan oleh nilai CHI (2.589,12). Lebih lanjut, pencapaian *Stability Score* HSV yang persis berada di angka 0,0000 kembali disorot sebagai anomali matematis akibat artefak konversi pembulatan (*rounding*) warna sebagaimana yang telah dianalisis pada Bab 4.5.2, sehingga nilai ini bersifat semu dan tidak dapat dijustifikasi sebagai bentuk stabilitas klaster yang sempurna [19], [25].

Oleh karena itu, mengacu pada justifikasi kuantitatif yang solid atas perpaduan antara kualitas struktural dan konsistensi inisialisasinya, model RGB dengan konfigurasi K=3 ditetapkan sebagai arsitektur final (*final model*). Keputusan komputasional dari representasi linier aditif inilah yang selanjutnya akan digunakan secara definitif untuk seluruh tahapan fungsional *pipeline* berikutnya, meliputi proses klasifikasi derajat *skintone*, penentuan arah *undertone*, hingga sinkronisasi matriks rekomendasi harmoni warna pakaian pengguna.

[SISIPKAN GAMBAR 4.x: grafik batang ranking composite score seluruh 9 kombinasi color space dan K] Gambar 4.x Grafik Batang Perbandingan *Composite Score* pada 9 Kombinasi *Color Space* dan Konfigurasi *K*

## 4.6 Hasil Klasifikasi Skintone dan Undertone

Setelah representasi warna dominan berhasil diekstraksi secara komputasional menggunakan model ruang warna terbaik (RGB dengan konfigurasi $K=3$), tahapan selanjutnya adalah menerjemahkan nilai matriks piksel tersebut ke dalam kategori biologis yang dapat dipahami dalam teori desain fesyen. Klasifikasi parameter fisik ini mencakup dua aspek utama: tingkat kecerahan warna kulit (skintone) dan rona dasar kulit (undertone).Pengukuran tingkat kecerahan skintone dikalibrasi secara objektif menggunakan standar metrik Individual Typology Angle (ITA). Nilai metrik ITA dihitung melalui formulasi matematis yang memanfaatkan proyeksi komponen kecerahan ($L^\*$) dan komponen spektrum warna kuning-biru ($b^\*$) dari ruang warna CIELAB [13], [15]. Berdasarkan derajat kemiringan sudut yang dihasilkan oleh formula tersebut, skintone secara universal diklasifikasikan ke dalam enam kategori: Very Light (ITA > 55°), Light (41° < ITA ≤ 55°), Intermediate (28° < ITA ≤ 41°), Tan (10° < ITA ≤ 28°), Brown (-30° < ITA ≤ 10°), dan Dark (ITA ≤ -30°) [15].Sementara itu, penentuan kategori undertone dilakukan dengan mengevaluasi sebaran nilai pada dimensi krominansi $a^\*$ (transisi hijau-merah) dan $b^\*$ (transisi biru-kuning) [14], [16]. Sistem mengimplementasikan aturan logika (rule-based) spesifik untuk pemetaan ini, yaitu: dikategorikan sebagai Warm (hangat) apabila nilai $b^\* > 5$ dan $a^\* < 10$; dikategorikan sebagai Cool (dingin) apabila nilai $b^\* < -2$ atau $a^\* > 12$; dan ditetapkan sebagai Neutral (netral) untuk nilai krominansi yang berada di luar kedua rentang kondisi ekstrem tersebut [16].Dalam menginterpretasikan hasil pengujian ini, terdapat sebuah keterbatasan konseptual dan ruang lingkup yang sangat penting untuk ditegaskan. Proses kalkulasi ITA dan klasifikasi undertone pada eksperimen ini hanya dieksekusi pada level sentroid (centroid-level classification), dan bukan merupakan proses klasifikasi per-sampel-individu terhadap 120 citra wajah yang termuat di dalam dataset. Dengan demikian, hasil pemetaan kategori ini murni merupakan representasi agregat dari tiga titik pusat warna paling dominan (anchor colors) yang mewakili seluruh dataset, bukan representasi dari distribusi populasi individual pengguna.Hasil klasifikasi metrik ITA (skintone) dan undertone untuk ketiga sentroid pada model eksperimen terbaik disajikan pada Tabel 4.4.

Tabel 4.4 Hasil Klasifikasi Skintone dan Undertone pada Sentroid Model Terbaik (RGB, K=3)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Cluster | Hex | Skintone (ITA) | Nilai ITA | Undertone |
| 1 | #AF7F68 | Tan | "19,94°" | Cool |
| 2 | #6A4638 | Dark | "-48,01°" | Cool |
| 3 | #E7BDA5 | Very Light | "58,70°", | Neutral |

Berdasarkan data kuantitatif pada Tabel 4.4, ketiga *centroid* yang terekstraksi oleh algoritma berhasil menjangkau rentang spektrum pigmen yang bervariasi. Klaster 1 yang direpresentasikan oleh kode heksadesimal #AF7F68 menorehkan nilai ITA sebesar 19,94°, yang mengklasifikasikannya ke dalam kelompok *skintone Tan* dengan profil rona dasar *Cool*. Klaster 2 (#6A4638) mewakili ekstraksi piksel yang jauh lebih gelap dengan nilai ITA -48,01°, sehingga dikategorikan sebagai *Dark* dengan kecenderungan *Cool undertone*. Sebaliknya, Klaster 3 (#E7BDA5) menempati titik luminansi tertinggi dengan capaian nilai ITA 58,70°, yang secara akurat memetakannya ke dalam kategori *skintone Very Light* dengan sifat *Neutral undertone*.

Ketiga profil *centroid* yang telah tervalidasi secara teoritis ini selanjutnya akan diposisikan sebagai parameter masukan fundamental ke dalam matriks rekomendasi. Sistem informasi kemudian akan mendeduksi kombinasi palet warna pakaian mana yang secara estetis paling kompatibel dan harmonis terhadap masing-masing representasi agregat warna kulit tersebut.

[SISIPKAN GAMBAR 4.x: visualisasi swatch warna ketiga centroid beserta label ITA dan undertone] Gambar 4.x Visualisasi Palet Warna *Centroid* Dominan Beserta Hasil Klasifikasi Kategori ITA dan *Undertone*

## 4.7 Hasil Rancangan Output Rekomendasi Warna Pakaian

### 4.7.1 Pemetaan Skintone–Undertone ke Palet Warna

Setelah parameter biologis pengguna berupa tingkat kecerahan kulit (*skintone*) dan rona dasar (*undertone*) berhasil diekstraksi dan diklasifikasikan, sistem memproses data tersebut ke dalam mesin inferensi berbasis aturan (*rule-based*). Tahapan ini bertujuan untuk mentransformasikan representasi matematis dari ruang warna menjadi keputusan rekomendasi palet pakaian yang aplikatif dan valid secara estetika visual. Proses pemetaan ini dibangun di atas fondasi teori psikologi warna dan prinsip harmoni desain fesyen (*fashion design*), yang memastikan bahwa rekomendasi yang diberikan mampu menciptakan keseimbangan perseptual serta menonjolkan karakteristik alami penggunanya [8], [16].

Secara konseptual, sistem menerapkan empat skema harmoni warna fundamental—komplementer (*complementary*), analog (*analogous*), triadik (*triadic*), dan monokromatik (*monochromatic*)—yang disesuaikan dengan kebutuhan visual spesifik dari setiap kategori *skintone*. Aturan rekomendasi warna yang diimplementasikan secara utuh di dalam sistem informasi ini disajikan pada Tabel 4.5.

Tabel 4.5 Matriks Pemetaan *Skintone* dan *Undertone* ke Palet Rekomendasi Pakaian

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Skintone | Undertone | Rekomendasi Warna | Harmoni | Dihindari | Alasan |
| Very Light | Cool | Royal Blue, Emerald, Lavender, Silver | Complementary | Warna sangat pucat (putih murni, cream sangat terang) | Kulit sangat terang memerlukan warna jewel tone untuk kontras visual sehat |
| Very Light | Neutral | Soft Pink, Ice Blue, Mint, Pearl White | Complementary | Warna sangat pucat (putih murni, cream sangat terang) | Kulit sangat terang memerlukan warna jewel tone untuk kontras visual sehat |
| Very Light | Warm | Blush Pink, Peach, Champagne, Warm Ivory | Complementary | Warna sangat pucat (putih murni, cream sangat terang) | Kulit sangat terang memerlukan warna jewel tone untuk kontras visual sehat |
| Light | Cool | Dusty Pink, Periwinkle, Soft Lavender, Slate Blue | Analogous | Warna neon terlalu terang dan orange yang terlalu jenuh | Skintone light cocok warna berdekatan (analogous) untuk tampilan harmonis |
| Light | Neutral | Jade Green, Off-White, Taupe, Grey | Analogous | Warna neon terlalu terang dan orange yang terlalu jenuh | Skintone light cocok warna berdekatan (analogous) untuk tampilan harmonis |
| Light | Warm | Warm Peach, Coral, Dusty Rose, Sand | Analogous | Warna neon terlalu terang dan orange yang terlalu jenuh | Skintone light cocok warna berdekatan (analogous) untuk tampilan harmonis |
| Intermediate | Cool | Mauve, Dusty Purple, Teal, Charcoal | Triadic | Warna neon dan kuning-hijau terlalu terang | Earth tones dan warna hangat melengkapi undertone medium |
| Intermediate | Neutral | Olive Green, Khaki, Caramel, Rust | Triadic | Warna neon dan kuning-hijau terlalu terang | Earth tones dan warna hangat melengkapi undertone medium |
| Intermediate | Warm | Mustard, Terracotta, Coral, Burnt Orange | Triadic | Warna neon dan kuning-hijau terlalu terang | Earth tones dan warna hangat melengkapi undertone medium |
| Tan | Cool | Cobalt Blue, Fuchsia, Forest Green, Burgundy | Monochromatic | Warna coklat muda yang terlalu mirip warna kulit | Warna hangat dan cerah menonjolkan kehangatan skintone tan |
| Tan | Neutral | Warm Brown, Copper, Amber, Olive | Monochromatic | Warna coklat muda yang terlalu mirip warna kulit | Warna hangat dan cerah menonjolkan kehangatan skintone tan |
| Tan | Warm | Golden Yellow, Deep Orange, Saffron, Rust | Monochromatic | Warna coklat muda yang terlalu mirip warna kulit | Warna hangat dan cerah menonjolkan kehangatan skintone tan |
| Brown | Cool | Cream, Lilac, Soft Turquoise, Powder Blue | Analogous | Warna coklat gelap yang menyatu dengan warna kulit | Warna cerah dan terang menonjolkan skintone brown |
| Brown | Neutral | Beige, Ivory, Forest Green, Burgundy | Analogous | Warna coklat gelap yang menyatu dengan warna kulit | Warna cerah dan terang menonjolkan skintone brown |
| Brown | Warm | Orange, Bright Yellow, Warm Red, Royal Blue | Analogous | Warna coklat gelap yang menyatu dengan warna kulit | Warna cerah dan terang menonjolkan skintone brown |
| Dark | Cool | Cobalt Blue, Magenta, Turquoise, Silver | Complementary | Warna gelap (hitam, navy gelap, coklat tua) | Warna vivid dan cerah menonjolkan keindahan skintone dark |
| Dark | Neutral | Maroon, Forest Green, Warm White, Emerald | Complementary | Warna gelap (hitam, navy gelap, coklat tua) | Warna vivid dan cerah menonjolkan keindahan skintone dark |
| Dark | Warm | Bright Red, Lime Green, Hot Pink, Electric Blue | Complementary | Warna gelap (hitam, navy gelap, coklat tua) | Warna vivid dan cerah menonjolkan keindahan skintone dark |

Dasar teoretis dari rancangan tabel pemetaan di atas bersandar pada korelasi antara kecerahan pigmentasi kulit pengguna dan respons psikologis terhadap kombinasi warna [8], [17]. Penjabaran prinsip harmoni untuk masing-masing klasifikasi adalah sebagai berikut:

1. Penerapan Harmoni Komplementer (*Very Light* dan *Dark*) Kategori *skintone* yang berada pada ekstrem spektrum kecerahan, yaitu *Very Light* dan *Dark*, menggunakan skema harmoni komplementer yang mengandalkan kontras tinggi [16]. Pada kulit *Very Light*, warna-*warna jewel tone* direkomendasikan untuk menciptakan kontras visual yang sehat dan mencegah pengguna terlihat pucat, sehingga warna putih murni atau *cream* sangat terang secara eksplisit dihindari [17]. Sebaliknya, pada kulit *Dark*, sistem merekomendasikan warna-warna *vivid* dan cerah (seperti *Bright Red* atau *Electric Blue*) untuk memancarkan keindahan alami kulit gelap, dengan menghindari pakaian berwarna sangat gelap seperti hitam atau cokelat tua yang dapat menyatu secara kamuflase dengan warna kulit pengguna.
2. Penerapan Harmoni Analog (*Light* dan *Brown*) Skema analog, yang memanfaatkan perpaduan warna-warna berdekatan pada roda warna (*color wheel*), digunakan untuk kategori *Light* dan *Brown* guna menciptakan tampilan yang lembut dan seimbang [16]. Pada kulit *Light*, palet *dusty* dan *soft* dipilih untuk menghasilkan tampilan harmonis, sembari secara ketat mengeksklusi warna neon atau oranye dengan saturasi terlalu tinggi agar tidak menenggelamkan fitur wajah. Untuk kategori *Brown*, harmoni analog diarahkan pada varian warna cerah dan terang (seperti *Lilac* atau *Beige*) guna memberikan sorotan pada warna kulit, sekaligus menghindari penggunaan warna cokelat gelap yang cenderung meniadakan dimensi visual pemakainya.
3. Penerapan Harmoni Triadik (*Intermediate*) Untuk *skintone* pada level menengah (*Intermediate*), sistem memanfaatkan harmoni triadik yang mengombinasikan warna-warna berjarak sama dalam roda warna, sehingga memberikan keseimbangan yang dinamis namun tidak berlebihan [8]. Pilihan warna pada *earth tones* (seperti *Olive Green* atau *Terracotta*) serta warna hangat lainnya direkomendasikan karena terbukti secara estetika melengkapi *undertone* medium dengan sempurna. Pada kategori ini, warna-warna neon dan kuning-hijau yang terlalu terang dijauhkan dari pengguna.
4. Penerapan Harmoni Monokromatik (*Tan*) Kategori *Tan* ditangani menggunakan prinsip monokromatik, yang bermain pada gradasi saturasi dari warna yang serumpun. Pendekatan ini difokuskan untuk menggunakan warna-warna hangat dan cerah (seperti *Golden Yellow* atau *Fuchsia*) guna menonjolkan dan memperkuat nuansa kehangatan alami yang dimiliki oleh *skintone Tan* [17]. Aturan mitigasi pada kategori ini secara khusus menghindari pakaian berwarna cokelat muda yang profilnya terlalu menyerupai warna basis kulit pengguna.

Melalui standardisasi tabel *rule-based* ini, algoritma sistem mampu mengambil keputusan (*decision-making*) secara instan dan deterministik dalam menghubungkan data biologis terkuantisasi dengan referensi rekomendasi di industri desain mode [8], [16].

[SISIPKAN GAMBAR 4.x: swatch visual palet warna untuk setiap kombinasi skintone-undertone] Gambar 4.x Visualisasi Matriks Pemetaan Palet Warna Pakaian Berdasarkan Klasifikasi Kategori *Skintone* dan *Undertone*

**4.7.2 Contoh Output Sistem Lengkap**

Sub-bab ini memaparkan purwarupa luaran akhir (*output*) dari sistem rekomendasi warna pakaian yang telah mengintegrasikan seluruh tahapan pemrosesan citra, klasterisasi *K-Means*, klasifikasi parameter biologis, dan aturan harmoni fesyen. Untuk mendemonstrasikan fungsionalitas sistem secara komprehensif dan objektif, evaluasi luaran disajikan melalui dua skenario studi kasus: pertama, representasi tingkat dataset menggunakan nilai sentroid dari model terbaik, dan kedua, hasil pengujian gambar pengguna individual pada skenario dunia nyata (*live prediction*).

**4.7.2.1. Luaran Tingkat Dataset (Representasi Agregat)**

Studi kasus pertama meninjau luaran sistem pada level dataset yang dikomputasi menggunakan model ruang warna linier RGB dengan konfigurasi optimal $K=3$. Pada skenario agregat ini, sistem memproses jutaan piksel dari 120 sampel citra secara terkontrol dan menghasilkan tiga *centroid* warna kulit dominan beserta luaran rekomendasi busananya. Hasil pemetaan sistem untuk representasi tingkat dataset ini dirangkum pada Tabel 4.6.

Tabel 4.6 Contoh Luaran Sistem Berdasarkan Sentroid Dataset (RGB, K=3)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Cluster | Hex | Skintone | ITA | Undertone | Rekomendasi Pakaian |
| 1 | #AF7F68 | Tan | 19,94° | Cool | Cobalt Blue, Fuchsia, Forest Green, Burgundy |
| 2 | #6A4638 | Dark | -48,01° | Cool | Cobalt Blue, Magenta, Turquoise, Silver |
| 3 | #E7BDA5 | Very Light | 58,70° | Neutral | Soft Pink, Ice Blue, Mint, Pearl White |

[SISIPKAN GAMBAR 4.x: tampilan hasil clustering/rekomendasi untuk sampel ini]

Gambar 4.x Visualisasi Luaran Antarmuka Sistem yang Menampilkan Ketiga Klaster Sentroid Dataset Beserta Rekomendasi Palet Warnanya

**4.7.2.2. Luaran Pengujian Gambar Pengguna Individual (*Live Prediction*)**

Studi kasus kedua mendemonstrasikan implementasi sistem ketika menerima masukan citra tunggal dari pengguna secara langsung (*live prediction*). Pada skenario ini, modul pelokalan mengidentifikasi area target dengan status valid (*Face detected: True*). Proses klasterisasi menggunakan model RGB ($K=3$) kemudian mengekstraksi klaster dominan pertama (Cluster 1) yang menempati titik koordinat warna RGB (185, 142, 148) atau ekuivalen dengan kode heksadesimal #B98E94.

Berdasarkan ekstraksi warna tersebut, kalkulasi *Individual Typology Angle* (ITA) pengguna terukur pada sudut 77,14° yang secara spesifik mengklasifikasikannya ke dalam kategori *skintone Very Light*, dengan hasil analisis krominansi menunjukkan profil *Cool undertone*. Mengacu pada parameter biologis tersebut, mesin rekomendasi menyimpulkan bahwa kulit yang sangat terang memerlukan warna bernuansa *jewel tone* guna memberikan kontras visual yang sehat. Oleh sebab itu, sistem secara otomatis merekomendasikan palet *Royal Blue*, *Emerald*, *Lavender*, dan *Silver*, sekaligus memberikan mitigasi eksplisit agar pengguna menghindari penggunaan pakaian berwarna sangat pucat (seperti putih murni atau *cream* sangat terang).

[SISIPKAN GAMBAR 4.y: tampilan hasil clustering/rekomendasi untuk sampel ini]

Gambar 4.y Luaran Prediksi dan Rekomendasi Sistem pada Skenario Pengujian Gambar Pengguna Individual

**4.7.2.3. Analisis Perbandingan Validasi CIEDE2000**

Aspek evaluasi yang paling esensial dalam membandingkan kedua studi kasus di atas terletak pada nilai validasi akurasi perseptual yang diukur melalui formula CIEDE2000. Pada pengujian representasi agregat (tingkat dataset), jarak rata-rata CIEDE2000 tercatat berada di angka 10,530, yang diklasifikasikan ke dalam kategori deviasi "Sedang". Tingkat akurasi ini secara signifikan jauh lebih baik dibandingkan dengan hasil pada pengujian gambar pengguna individual, yang mencatatkan pembengkakan nilai metrik jarak CIEDE2000 hingga mencapai angka 24,066. Jika dikomparasikan dengan warna referensi terdekatnya (berada pada rentang *Tan* dengan ITA 10-28°), deviasi perseptual pengguna individual ini diklasifikasikan ke dalam kategori "JAUH", yang secara konseptual mengindikasikan probabilitas tinggi adanya kontaminasi derau (*noise*).

Ketimpangan performa komputasional antara pengujian agregat dan pengujian individual (*live prediction*) ini dapat dijelaskan secara akademis melalui beberapa batasan teknis di lapangan. Pertama, kondisi perekaman di dunia nyata sangat bervariasi dan tidak terstandardisasi layaknya pengambilan sampel dataset eksperimen; fluktuasi pencahayaan ruangan, sorotan bayangan, dan kualitas sensor kamera gawai pengguna memberikan dampak langsung pada distorsi matriks warna [12], [24].

Kedua, pembengkakan deviasi tersebut sangat dipengaruhi oleh masuknya *noise* dari objek non-kulit akibat ketidaksempurnaan pada proses *cropping* wajah. Pada citra individual, komponen visual luar seperti helaian rambut yang menutupi pipi, aksesori, atau bahkan fragmen latar belakang yang tertangkap oleh perluasan *bounding box* sering kali ikut masuk ke dalam fase segmentasi [21]. Karena algoritma *K-Means* mengalkulasi seluruh piksel secara merata, keberadaan *noise* tersebut akan menarik titik pusat (*centroid*) menjauhi koordinat warna kulit murni, sehingga memicu pelebaran nilai CIEDE2000 pada saat divalidasi terhadap standar warna kulit manusia normal [14]. Fenomena ini menegaskan bahwa tingkat keberhasilan sistem prediksi langsung (*live prediction*) sangat bergantung pada kemurnian matriks masukan awal yang minim gangguan visual.

## 4.8 Pembahasan

Sub-bab ini merupakan sintesis komprehensif dari seluruh temuan eksperimental yang telah diuraikan pada sub-bab sebelumnya. Pembahasan diarahkan untuk mengkaji hasil komputasi secara analitis, menghubungkannya dengan landasan teori dan penelitian terdahulu pada Bab II, serta secara spesifik menjawab empat Rumusan Masalah (RM) guna mencapai Tujuan Penelitian (T) yang telah ditetapkan pada Bab I.

### 4.8.1 Evaluasi Pipeline Ekstraksi Warna Kulit

Menjawab Rumusan Masalah pertama terkait bagaimana merancang *pipeline* ekstraksi warna kulit yang efektif, penelitian ini telah berhasil membangun arsitektur pemrosesan yang solid. Evaluasi menunjukkan bahwa lokalisasi menggunakan *Haar Cascade Classifier* mampu mendeteksi 97 dari 120 citra, sementara 23 citra yang dilewati (*skipped*) mengonfirmasi kelemahan bawaan metode ini terhadap variasi pose ekstrem [21]. Kinerja *rule-based thresholding* yang menggunakan mekanisme *majority voting* dari tiga ruang warna (RGB, HSV, dan YCrCb) terbukti sangat tangguh dalam mengeksklusi area non-kulit, terbukti dari keberhasilannya mengekstrak 3.363.613 piksel murni sebagai material dasar pembentukan klaster [1], [24].

Dalam tahapan *K-Means clustering*, ditemukan sebuah dinamika komputasional yang menarik antara teori evaluasi awal dan keputusan final sistem. Pengujian *Elbow Method* pada ruang warna RGB memberikan rekomendasi titik sikut pada $K=4$. Namun, sistem secara definitif menetapkan $K=3$ sebagai parameter operasional final untuk seluruh eksperimen. Keputusan ini bukanlah sebuah kesalahan atau anomali, melainkan sebuah keputusan metodologis yang disengaja. *Elbow Method* memiliki keterbatasan karena hanya mengevaluasi varians internal (*Within-Cluster Sum of Squares* / WCSS) tanpa memedulikan jarak pisah antar-klaster [19]. Penetapan $K=3$ didasarkan pada *Composite Score* yang jauh lebih holistik, mengevaluasi *Silhouette Score*, *Davies-Bouldin Index* (DBI), *Calinski-Harabasz Index* (CHI), dan *Stability Score* secara simultan [6], [22]. Keputusan ini memastikan bahwa klaster yang dihasilkan tidak hanya padat di dalam, tetapi juga terpisah secara tegas dan stabil saat diinisialisasi ulang.

### 4.8.2 Analisis Komparatif Multi-Color Space

Menjawab Rumusan Masalah kedua mengenai ruang warna (*color space*) mana yang paling optimal untuk algoritma *clustering*, sistem telah mengevaluasi RGB, HSV, dan CIELAB. Berdasarkan sintesis *Composite Score*, model ruang warna RGB dengan konfigurasi $K=3$ berhasil menempati peringkat pertama dengan skor 0,9856. Namun, analisis mendalam terhadap angka tersebut menunjukkan fakta akademis yang krusial: keunggulan RGB atas ruang warna CIELAB (peringkat kedua dengan skor 0,9594) sebenarnya sangat tipis.

Secara struktural, kualitas klaster RGB dan CIELAB nyaris identik (*Silhouette* 0,4784 vs 0,4769; DBI 0,6783 vs 0,6770; CHI 6.951,57 vs 6.972,03). Keunggulan RGB didorong hampir sepenuhnya oleh *Stability Score* yang lebih superior (0,1533 berbanding 0,4599 milik CIELAB). Artinya, RGB memenangkan metrik komposit karena konsistensi posisi *centroid* saat algoritma diulang dengan *seed* acak, bukan karena ia secara struktural lebih padat dari CIELAB [6], [9]. Di sisi lain, ruang warna HSV secara konsisten menjadi yang terlemah (skor komposit 0,6442) di semua konfigurasi $K$. Rendahnya nilai CHI pada HSV membuktikan tingginya tingkat *overlapping* piksel, menegaskan temuan penelitian terdahulu bahwa singularitas pada ruang silindris membuatnya kurang ideal untuk partisi warna kulit yang memiliki gradasi sangat halus [2], [18].

### 4.8.3 Klasifikasi Skintone, Undertone, dan Pemetaan Rekomendasi

Menjawab Rumusan Masalah ketiga mengenai klasifikasi parameter biologis dan rekomendasinya, penelitian ini mengimplementasikan kalkulasi *Individual Typology Angle* (ITA) yang diekstrak dari kanal $L^\*$ dan $b^\*$ pada CIELAB [13], [15], serta logika *undertone* berbasis krominansi $a^\*/b^\*$ [16]. Hasil klasifikasi pada tiga *centroid* dominan dari model terbaik memetakan dataset ke dalam profil: *Tan/Cool* (#AF7F68), *Dark/Cool* (#6A4638), dan *Very Light/Neutral* (#E7BDA5).

Pemetaan profil ini kemudian dihubungkan dengan mesin inferensi *rule-based* yang bersandar pada teori harmoni warna fesyen (seperti *complementary* untuk warna ekstrem seperti *Dark* dan *Very Light*, serta *monochromatic/triadic* untuk *Tan/Intermediate*) [8], [17]. Pendekatan komputasional ini terbukti mampu mereplikasi logika penata gaya profesional ke dalam sistem otomatis. Meski demikian, perlu dicatat bahwa klasifikasi ITA dan *undertone* ini baru dioperasikan pada level sentroid klaster sebagai representasi agregat dataset, dan belum dilakukan secara individual untuk ke-120 sampel citra.

### 4.8.4 Validasi Jarak Perseptual CIEDE2000 dan Trade-off Akurasi

Menjawab Rumusan Masalah keempat terkait validasi perseptual, pengujian menggunakan metrik CIEDE2000 mengungkap temuan yang paling signifikan secara akademis. Model dengan struktur klaster terbaik (RGB $K=3$) mencatatkan rata-rata jarak CIEDE2000 sebesar 10,530, yang terkategori sebagai akurasi "Sedang" [14]. Secara kritis, model dengan evaluasi struktural terbaik ternyata **bukan** model dengan akurasi perseptual terbaik. Data komputasi membuktikan bahwa model CIELAB $K=5$ (Delta-E 9,464) dan RGB $K=7$ (Delta-E 9,495) justru menghasilkan *centroid* yang lebih akurat dan mendekati referensi warna kulit standar di mata manusia.

Fenomena ini mengonfirmasi adanya *trade-off* (tarik-ulur) fundamental dalam pengolahan citra: sebuah algoritma dapat dipaksa untuk menghasilkan struktur klaster matematis yang sangat rapi dan padat (tercermin dari *Silhouette* dan DBI yang sangat baik pada $K=3$), namun hal tersebut membuang varians alami pigmen kulit yang berakibat pada penurunan akurasi visual [9].

Lebih lanjut, pengujian terhadap gambar pengguna individual di skenario dunia nyata (*live prediction*) mencatatkan jarak CIEDE2000 sebesar 24,066 (kategori "Jauh"). Kesenjangan ekstrem antara performa dataset terkontrol (10,530) dengan data riil ini mengindikasikan bahwa variasi kondisi iluminasi dunia nyata, kualitas kamera gawai, serta distorsi dari *noise* non-kulit yang lolos dari proses *cropping*, memberikan dampak pergeseran *centroid* yang sangat masif saat diproses secara langsung [24].

[SISIPKAN GAMBAR 4.x: Diagram ringkasan keterkaitan antar temuan RM1-RM4 yang mengilustrasikan alur ekstraksi, kompetisi color space, klasifikasi ITA, hingga validasi CIEDE2000]

Gambar 4.x Diagram Sintesis Evaluasi Pipeline dan Multi-Color Space

### 4.8.5 Keterbatasan Penelitian

Sebagai bentuk pertanggungjawaban ilmiah serta untuk memberikan arah bagi pengembangan sistem di masa mendatang, penelitian ini mengidentifikasi beberapa keterbatasan operasional dan metodologis yang harus diperhatikan:

1. **Dualitas Validitas Metrik:** Metrik evaluasi struktural (*Silhouette Score*, DBI, CHI) terbukti tidak sepenuhnya menjamin validitas perseptual warna kulit yang diekstraksi. Diperlukan validasi metrik optik seperti CIEDE2000 sebagai pelengkap mutlak, meskipun keduanya dapat memberikan rekomendasi model yang saling bertolak belakang (seperti fenomena RGB $K=3$ menang di struktur, namun LAB $K=5$ menang di optik perseptual).
2. **Ketiadaan Analisis Efisiensi Waktu:** Penelitian ini tidak melakukan perekaman dan pengukuran waktu komputasi (*computational cost*). Oleh karenanya, perbandingan keunggulan *color space* ditinjau dari aspek kecepatan pemrosesan dan beban memori belum dapat disimpulkan.
3. **Pembatalan Implementasi Antarmuka (Streamlit):** Sub-bab mengenai perancangan antarmuka menggunakan Streamlit yang sebelumnya direncanakan telah dibatalkan dan dihapus dari arsitektur implementasi akhir. Pengujian purwarupa sistem saat ini sepenuhnya dilakukan secara terminal melalui mekanisme unggah gambar langsung di lingkungan Google Colaboratory.
4. **Cakupan Klasifikasi Parameter Biologis:** Eksekusi kalkulasi metrik ITA dan penentuan kategori *undertone* pada purwarupa ini baru diimplementasikan pada level sentroid (3 kelas representasi agregat dataset terpilih), dan belum diekspansi untuk melakukan klasifikasi individual pada seluruh 120 sampel dataset secara satu per satu.
5. **Artefak Metrik Stabilitas:** Temuan *Stability Score* pada ruang warna HSV untuk konfigurasi $K=3$ dan $K=5$ yang bernilai persis 0,0000 berpotensi kuat merupakan artefak matematis akibat pembulatan dan konversi paksa format matriks warna. Nilai nol absolut tersebut tidak merepresentasikan stabilitas riil yang sempurna, sehingga komparasi *composite score* yang melibatkan HSV harus diinterpretasikan dengan penuh kehati-hatian.

# BAB V PENUTUP

## 5.1 Kesimpulan

Berdasarkan keseluruhan tahapan perancangan, eksperimen komputasional, dan evaluasi hasil analisis yang telah dipaparkan pada bab-bab sebelumnya, penelitian ini menarik empat kesimpulan utama untuk menjawab rumusan masalah yang telah ditetapkan:

1. Perancangan *pipeline* ekstraksi warna kulit berhasil dibangun secara integratif dan tangguh melalui serangkaian tahapan prapemrosesan hingga partisi data. Proses lokalisasi menggunakan *Haar Cascade Classifier* berhasil mendeteksi 97 dari 120 citra, yang dilanjutkan dengan segmentasi kulit berbasis *majority voting* dari tiga ruang warna (RGB, HSV, dan YCrCb) yang secara efektif mengekstraksi 3.363.613 piksel valid. Pada tahap pengelompokan warna melalui *K-Means clustering*, nilai parameter optimal ditetapkan pada $K=3$ berdasarkan pendekatan *composite score*, yang secara metodologis dipilih untuk mengungguli rekomendasi awal $K=4$ dari *Elbow Method* guna memastikan batas separasi klaster yang lebih rasional secara komputasi.
2. Evaluasi komparatif multi-*color space* menyimpulkan bahwa model ruang warna RGB dengan konfigurasi $K=3$ merupakan representasi ekstraksi titik pusat (*centroid*) terbaik dengan perolehan skor komposit tertinggi sebesar 0,9856. Kendati demikian, keunggulan ruang linier RGB ini relatif tipis dan menempel ketat dengan model ruang warna perseptual CIELAB ($K=3$) yang meraih skor komposit 0,9594. Di sisi lain, ruang warna HSV terbukti secara konsisten menjadi dimensi yang paling lemah dan tertinggal (skor 0,6442) akibat anjloknya rasio dispersi varians (*Calinski-Harabasz Index*), yang mengindikasikan ketidakmampuannya dalam membentuk struktur klaster yang terpisah secara tegas.
3. Proses pemetaan luaran *clustering* ke dalam sistem rekomendasi berhasil dirumuskan dengan mengklasifikasikan nilai *centroid* agregat ke dalam standar *Individual Typology Angle* (ITA) dan rona dasar (*undertone*). Representasi *centroid* dari model terbaik (RGB $K=3$) secara akurat diklasifikasikan ke dalam kategori *Tan/Cool* (#AF7F68), *Dark/Cool* (#6A4638), dan *Very Light/Neutral* (#E7BDA5). Klasifikasi parameter biologis ini berhasil dipetakan ke dalam 18 kombinasi mesin inferensi *rule-based* yang bersandar pada teori harmoni warna mode (komplementer, analog, triadik, dan monokromatik) untuk menghasilkan palet pakaian yang tervalidasi secara estetika visual.
4. Evaluasi performa sistem secara menyeluruh mengungkap adanya fenomena *trade-off* (tarik-ulur) yang signifikan antara optimalitas struktur matematis klaster dengan akurasi warna secara perseptual. Hasil validasi jarak warna (CIEDE2000) memperlihatkan bahwa model RGB $K=3$ menghasilkan deviasi rata-rata sebesar 10,530 ("Sedang"), sementara akurasi perseptual yang lebih akurat justru dicatatkan oleh model CIELAB $K=5$ (9,464) dan RGB $K=7$ (9,495). Selain itu, pengujian prediksi pada citra pengguna individual (*live prediction*) mencatatkan jarak deviasi CIEDE2000 yang jauh lebih besar, yakni 24,066 (kategori "Jauh"). Kesenjangan ini secara empiris membuktikan bahwa fluktuasi pencahayaan dan masuknya *noise* pada kondisi pengambilan gambar di dunia nyata memiliki tingkat variabilitas gangguan yang jauh lebih tinggi dibandingkan data komputasi pada lingkungan dataset yang terkontrol.

## 5.2 Saran

Berdasarkan kesimpulan yang telah dijabarkan serta keterbatasan yang ditemukan selama proses perancangan hingga pengujian sistem, terdapat beberapa saran yang dapat direkomendasikan untuk pengembangan penelitian selanjutnya:

1. Pengembangan mekanisme deteksi dan lokalisasi wajah yang lebih tangguh (*robust*) terhadap variasi sudut pose dan kondisi pencahayaan yang ekstrem, misalnya dengan mengintegrasikan pendekatan *adaptive histogram equalization* atau *illumination normalization* secara lebih mendalam. Saran ini sangat relevan mengingat metode *Haar Cascade Classifier* yang digunakan pada penelitian ini masih mencatatkan tingkat kegagalan deteksi (*skipped*) sebesar 19% dari total dataset akibat faktor oklusi dan fluktuasi cahaya bawaan. Penerapan algoritma mitigasi pencahayaan tersebut diharapkan dapat menekan angka kegagalan deteksi secara signifikan, sehingga *pipeline* sistem mampu memproses masukan citra di lingkungan dunia nyata dengan jauh lebih stabil.
2. Eksplorasi pengimplementasian metode *clustering* lain yang bersifat probabilistik (*soft clustering*), seperti algoritma *Fuzzy C-Means* (FCM) atau *Gaussian Mixture Model* (GMM) [18]. Karena purwarupa saat ini murni dibangun dan dievaluasi menggunakan metode partisi kaku (*hard clustering*) berupa *K-Means*, pengujian metode alternatif sangat diperlukan untuk melihat respon algoritma terhadap piksel warna wajah yang saling tumpang tindih (*overlapping*). Melalui studi komparasi antar-metode pengelompokan ini, kualitas dari representasi titik pusat (*centroid*) warna kulit diharapkan dapat divalidasi dengan lebih komprehensif, khususnya dalam mempertahankan kehalusan gradasi pigmen alami pengguna.
3. Perluasan cakupan evaluasi pengujian ruang warna (*color space*) dengan menambahkan model dimensi lain seperti YCbCr maupun ruang standar CIE XYZ. Rekomendasi ini didasari oleh temuan evaluasi penelitian yang menunjukkan bahwa model silindris HSV secara konsisten menempati posisi terlemah pada perhitungan skor komposit maupun validasi perseptual CIEDE2000. Penambahan referensi ruang warna, khususnya YCbCr yang secara teoretis sangat lazim digunakan untuk memisahkan krominansi kulit [24], akan memberikan tolok ukur perbandingan tambahan sehingga evaluasi matriks multi-*color space* menjadi jauh lebih utuh dan objektif.
4. Pengembangan dan realisasi awal antarmuka pengguna (*user interface*) berbasis aplikasi *web* maupun *mobile* secara penuh. Mengingat purwarupa pada penelitian ini belum memiliki implementasi antarmuka dan seluruh tahapan pengujiannya murni tereksekusi secara terminal di dalam lingkungan komputasi awan (Google Colaboratory), sistem prediksi ini sama sekali belum dapat diakses secara praktis. Realisasi antarmuka interaktif akan berperan krusial dalam menjembatani fungsionalitas algoritma ekstraksi warna kulit di sisi *back-end* dengan kebutuhan eksplorasi pengguna akhir masyarakat umum di skenario nyata.
5. Pelibatan pakar di bidang mode pakaian (*fashion expert*) maupun pengujian subjektif oleh pengguna nyata dalam proses validasi tahap akhir rekomendasi palet warna pakaian. Pada penelitian ini, validasi kecocokan rekomendasi warna baru diuji secara deduktif melalui sistem *rule-based* yang bersandar pada landasan teoretis harmoni warna (komplementer, analog, triadik, dan monokromatik), tanpa melibatkan instrumen penilaian subjektif manusia. Adanya validasi empiris dan pengujian penerimaan (*user acceptance test*) dari sudut pandang pakar diharapkan dapat mengukur akurasi, mengoreksi bias, serta meningkatkan relevansi harmoni sistem dari perspektif estetika psikologi mode yang sesungguhnya.

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

[26] D. Nguyen, "Dataset Skin Tone," Kaggle, 2024. [Daring]. Tersedia: <https://www.kaggle.com/datasets/ducnguyen168/dataset-skin-tone>. (Diakses: 19 Jun. 2026).