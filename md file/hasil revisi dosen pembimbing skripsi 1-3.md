Diperkuat bagian latar belakang dan alasan urgensinya kenapa harus dibuat penelitian

Gapnya ekstraksi warna pada pencahayaan. Kontribusi penelitian perbandingan antara HSV,RGB,Cielab.

Kontribusinya apa? Penggunaan centroid sebagai dasar rekomendasi. Kontribusinya dapat

Kontribusinya rekomendasi warna skintone.

Gapnya evaluasi si hasil model sering berhenti pada bagian segmentasi. > tambah evaluasi clustering validasi rekomendasi.

Gap terlalu banyak.

Gap dideskripsikan di latar belakang. Setelah sotanya.

Tujuannya di bab 1. Tujuannya sesuai dengan metriksnya. Misalnya

Pada bagian 1.2.2 jelaskan performa lebih dalam. Jelaskan apakah modelnya lebih cepat,

Tinjauan Pustaka ditulis ulang juga.

Revisi :

1. Ambil dari modelnya, rulebase thresholding untuk akurasi clustering perfoma atau bagaimana cara pemetaan skintone dan rekomendasi warna pakaian sebagai rumusan masalah.
2. Batasan masalah. Hanya mendetek wajah dengan ekspresi natural. Tidak bisa mendeteksi seluruh badan hanya wajah. System tidak mendeteksi terkait bahan pakaian
3. Penentuan rekomendasi warna bukan terkait rekoemndasi filtering. Kita tidak menggunakan histori dari pengguna tersebut.
4. Satu rumusan punya tujuan.
5. Bab 2. Hilang tinjauan teori 2.1 tentang pengolahan citra digital, 2.2 ruang warna.
6. Bab 3 terkait K-Means pertanyaan yang tidak bisa dijawab : cara menentukan nilai K. tambahkan.
7. Elbow method tidak ada. Apakah menggunakan sealhood tertinggi atau tidak.
8. K-means nya apakah tetap atau dinamis > dinamis.
9. Beritahu bahwa nilai K nya itu untuk mencari warna kulit tidak ada warna background
10. Sillhoute index dll. Harus hati hati > digital image processing ini sudah tepat untuk model ini. Sillhoute,dbi, CHI, untuk mengukur struktur cluster. Bukan otomatis membuktikan warna kulit itu benar. Butuh validasi tambahan. Tidak bisa membuktikan warn aitu benar secara visual > perlu ada validasi tambahan ~~berdasarkan orang, ribet.~~ Metode untuk **Teknik pengukuran jarak antar warna**. Atau bisa manual dengan cara membedakan warna dengan
11. Di halaman 20 ada yang kosong terkait DBI
12. Bab 3, jenis penelitian perlu diberitahu > pembuatan purwarupa dengan metode eksperimental. Kalau diurutkan input citra wajah > variable perlakuan 3 variabel masalah colorspace RGB,HSV, CIELAB. Outputnya centroid warna dan rekomendasi warna. Evaluasinya menggunakan silhoud,DBI,CHI. Tambah validasi terkait pengukuran jarak antar warna atau manual.
13. Metode pengumpulan data. Dibuat table aja. Buat lebih gampang buat pake table aja. Headernya aspek dataset, isinya apa, sarannya apa
14. Jumlah citranya berapa? Jumlah responden > 120 orang. Variasi skintonenya. Di table. Format filenya apa, variasi skintone. Format citranya, sumber data. Biar valid. Cantumkan dataset dari Kaggle. Tipe gambarnya indoor dan outdoor.
15. 3.2.2. kalau berdasarkan undertone. Bagaimana system menentukan skintone pada system tersebut. Ambil centeroid warna kulit > konversi ke cielab > baru dihitung kategori skintonenya menggunakan ITA baru cek skintonenya.
16. Palet warrna mengikuti aturan dan baru ditampilkan paletnya
17. 3.2.3. buat instrument bikin pake table. Tools sama fungsi sebagai header. Pakai streamlit
18. Tahapan penelitian setelah evaluasi baru masuk ke colorspace terbaik, baru di klasifikasi skintone dan undertone. Baru pemetaan untuk ke rekomendasi warna pakaian. Setelah itu validasi hasil rekomendasi. Baru analisis hasilnya.
19. 3.5.1 perjelas deteksi wajahnya metodenya pakai apa, metode cropingnya pakai apa, apakah rambut mata bibir dihapus, threshold yang digunakan apa? Jelaskan penanganan shadow bagaimana
20. Deteksi wajahnya pakai apa? Dnn atau hars.
21. Skinmaskingnya menggunakan HSV kasih tau nantinya.
22. Color normalisasi menggunakan sistogram atau apa?
23. 3.5. hasil teknis dan hasil system > buat table dengan header (skintone, undertone, warna yang direkomendasikan, warna yang dihindarinya apa?
24. Bisa ditambahkan output system seperti warna utama, kode hex, contoh paletnya, alasan rekomendasinya. Tambahkan di rancangan aturan disananya.
25. 3.6 hasilnya belum dapat, buatkan hasil matrix untuk setiap colorspace. Terus tentuin rankingnya, jelaskan colorspace terbaik, outputnya. Buat kriteria table untuk sillhoute score kriteria dan nilainya. Beritahu semakin tinggi semakin baik. DBI itu semakin rendah semakin baik, CHI sama seperti sillhoute score semakin tinggi semakin baik. Waktu komputasi, validasi pengguna. Dihasil akhir jadi tahu hasil akhirnya.
26. 3.6.1. tambahin terkait evaluasi ketiga tersebut. Tidak menjamin centroid sesuai. Tambahkan validasi sesuai atau tidaknya.
27. 3.6.2 buatkan table headernya (scenario, input, colorspace, metode, output) buatkan scenario s1,s2,s3 yang diinput citra wajah, colorpsacenya scenario 1 RGB, HSV, CIELAb, semuanya K-means, hasil outputnya dibandingkan dengan metrics warna yang sama.
28. Bab 3 desain penelitian > penelitian pengembangan prototype dengan eksperimen komputasional. Bagi 2, pengembangan prototype, dan eksperimen perbandingan colorspace. Supaya desainnya jelas.
29. Validasi warnanya aja berdasarkan orang, atau cari menggunakan perhitungan jarak warna
30. Tambahkan terkait K-meansnya K nya berdasarkan apa, elbownya apa, validasi K nya sesuainya darimana
31. Validasinya menggunakan CIEDE20000
32. Masukan dari sempro