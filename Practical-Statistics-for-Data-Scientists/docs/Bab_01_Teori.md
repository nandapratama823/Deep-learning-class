# Ringkasan dan pendalaman teori Bab 1

Bab ini membangun kebiasaan memahami bentuk, pusat, sebaran, dan hubungan data sebelum membuat model. EDA membantu mendeteksi kesalahan pencatatan, nilai ekstrem, kategori jarang, serta kebutuhan transformasi. Contoh negara bagian AS, keterlambatan penerbangan, saham, pinjaman, dan properti menunjukkan bahwa jenis variabel menentukan cara analisis.

## Jenis data dan struktur tabel
Data numerik dapat kontinu (luas rumah) atau diskret (jumlah kamar). Kategori dapat nominal (maskapai), ordinal (grade pinjaman), atau biner (gagal bayar). Angka kode pos adalah label, sehingga rata-rata kode pos tidak bermakna. Pada data persegi panjang, satu baris adalah unit pengamatan dan satu kolom adalah variabel. Indeks mengidentifikasi baris; indeks tidak otomatis layak menjadi prediktor. Teks, citra, graf, dan deret waktu membutuhkan representasi tambahan. Unit pengamatan dan waktu pencatatan harus jelas untuk menghindari duplikasi serta kebocoran informasi.

## Ukuran lokasi
Rata-rata $\bar{x}=\sum_i x_i/n$ memakai semua nilai sehingga sensitif terhadap pencilan. Median membagi observasi terurut menjadi dua bagian dan lebih tahan nilai ekstrem. Trimmed mean membuang proporsi tertentu di kedua ekor; `trim_mean(x, 0.1)` membuang 10% dari masing-masing sisi, bukan 10% keseluruhan. Mean populasi negara bagian lebih besar daripada median bila beberapa negara bagian sangat besar.

Rata-rata berbobot $\bar{x}_w=\sum_iw_ix_i/\sum_iw_i$ membedakan kontribusi observasi. Membobot tingkat pembunuhan dengan populasi menjawab pertanyaan untuk penduduk agregat; rata-rata tak berbobot memberi bobot sama kepada negara bagian. Weighted median membagi jumlah bobot menjadi dua. Pembobotan harus sesuai unit sasaran, bukan dipilih untuk mendapatkan angka tertentu.

## Variabilitas dan ukuran robust
Varians sampel $s^2=\sum_i(x_i-\bar{x})^2/(n-1)$ mengukur penyimpangan kuadrat. Simpangan baku s kembali ke satuan asal. Penyebut n-1 mengoreksi estimasi ketika mean populasi diganti mean sampel. IQR adalah $Q_{0.75}-Q_{0.25}$, yaitu rentang 50% tengah. MAD mentah adalah $\operatorname{median}|x_i-\operatorname{median}(x)|$.

`statsmodels.robust.scale.mad` membagi MAD mentah dengan sekitar 0.67449 secara default. Hasilnya konsisten dengan simpangan baku pada distribusi normal, sehingga jangan menyamakannya dengan MAD mentah tanpa menyebut normalisasi. Simpangan baku besar bersama IQR kecil dapat menandakan ekor berat. Robust tidak berarti semua pencilan harus dibuang: kesalahan input dan kejadian ekstrem yang valid perlu dibedakan.

## Kuantil, boxplot, histogram, dan density
Persentil adalah batas posisi pada distribusi terurut. Boxplot memperlihatkan median dan kuartil. Whisker biasanya mencapai observasi terakhir dalam 1.5 IQR dari kuartil; titik di luarnya adalah kandidat pencilan, bukan bukti kesalahan. Histogram menghitung frekuensi per interval; bentuknya sensitif pada batas dan jumlah bin. Density plot memperkirakan kepadatan melalui kernel. Luas di bawah kurva density adalah satu; tinggi pada suatu titik kontinu bukan probabilitas di titik itu. Bandwidth kecil menampilkan detail sekaligus noise; bandwidth besar dapat menyamarkan beberapa puncak.

## Kategorikal, modus, nilai harapan, dan peluang
Tabel frekuensi dan diagram batang merangkum kategori. Modus adalah kategori paling sering, dan tidak selalu unik. Nilai harapan $E(X)=\sum_xxP(X=x)$ menggabungkan nilai numerik dengan peluangnya; ini berbeda dari modus. Proporsi empiris mengestimasi peluang jika pengambilan data sesuai populasi sasaran. Penyebab keterlambatan yang paling sering belum tentu penyebab dengan total durasi terlama: definisi denominator dan metrik harus diperiksa.

## Korelasi dan scatterplot
Pearson $r=\sum_i(x_i-\bar{x})(y_i-\bar{y})/[(n-1)s_xs_y]$ mengukur hubungan linear, antara -1 dan 1 bila kedua varians positif. Korelasi nol tidak meniadakan hubungan nonlinear; korelasi tinggi tidak membuktikan sebab-akibat. Scatterplot mengungkap bentuk hubungan, kelompok, dan pencilan yang tersembunyi oleh satu koefisien. Heatmap membantu membandingkan banyak pasangan. Korelasi perubahan saham berlaku pada periode yang dipilih dan bukan jaminan hubungan masa depan.

## Dua atau lebih variabel
Hexbin dan kontur density mengurangi tumpang tindih saat dua fitur numerik memiliki banyak pengamatan. Sampling 10.000 baris untuk kontur mengikuti sumber agar komputasinya praktis. Pada dua kategori, crosstab menghitung frekuensi bersama. Persentase per baris dan per kolom menjawab pertanyaan berbeda, misalnya status pembayaran dalam setiap grade dibanding komposisi grade dalam setiap status.

Boxplot per maskapai membandingkan distribusi numerik antarkategori; violin menambahkan bentuk density. Facet kode pos menunjukkan apakah hubungan luas dan nilai properti berbeda antarwilayah. Hubungan agregat dapat berbeda dari hubungan di setiap kelompok (Simpson's paradox). Transformasi yang kemudian dipakai untuk prediksi harus dipelajari hanya dari training.

## Interpretasi reproduksi dan kesimpulan
Bandingkan mean, median, trimmed mean populasi serta simpangan baku, IQR, dan MAD terskala. Pada properti, bandingkan grafik agregat dengan facet kode pos sebelum mengasumsikan satu hubungan linear. EDA memberi dasar pemilihan fitur, transformasi, dan normalisasi pada ML/DL, tetapi belum membuktikan kausalitas maupun performa prediksi data baru.
