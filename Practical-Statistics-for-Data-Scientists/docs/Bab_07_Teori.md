# Ringkasan dan pendalaman teori Bab 7

Unsupervised learning mencari struktur tanpa target untuk fitting. PCA merangkum variasi; clustering mengelompokkan berdasarkan kemiripan. Hasil tergantung representasi, skala, jarak, dan kompleksitas.

## PCA
PCA mencari arah varians maksimum dan komponen berikut yang ortogonal. Pada matriks terpusat $X_c$, SVD $X_c=U\Sigma V^T$ memberi arah komponen pada V dan score pada $X_cV$. Eigenvalue kovarians menyatakan varians komponen. Scikit-learn PCA melakukan centering tetapi tidak otomatis standardisasi.

Loadings menunjukkan kontribusi fitur terhadap arah komponen. Tanda seluruh komponen boleh terbalik tanpa mengubah subruang/informasi; perbedaan tanda antarversi bukan kesalahan. Explained variance ratio menyatakan proporsi varians dipertahankan. Scree plot membantu memilih dimensi tetapi tidak memberi satu jawaban universal. Varians besar belum tentu informasi terbaik untuk target downstream.

## Interpretasi dan correspondence analysis
Pada saham, komponen dapat merepresentasikan pergerakan bersama atau perbedaan sektor. Ini pola periode sampel, bukan bukti sebab-akibat. PCA sensitif pada skala dan pencilan. Jika dipakai sebelum classifier, fit scaler/PCA hanya di training fold.

CA bekerja pada tabel kontingensi dan memetakan deviasi profil baris/kolom dari independensi dalam geometri chi-square. Inertia berkaitan dengan chi-square yang dinormalisasi total. Peta pekerjaan rumah menunjukkan asosiasi profil. Jarak antara titik baris dan kolom tidak selalu memiliki interpretasi Euclidean yang sama seperti jarak sesama baris. Periksa inertia yang ditangkap dua dimensi sebelum membaca peta.

## K-means
K-means meminimalkan $\sum_k\sum_{i\in C_k}\|x_i-\mu_k\|^2$. Algoritma bergantian menugaskan pengamatan ke centroid terdekat dan menghitung ulang centroid sebagai mean. Inisialisasi bisa memberi optimum lokal berbeda; notebook memakai 10 inisialisasi dan seed. Nomor cluster arbitrer, bukan urutan mutu.

K-means cocok untuk kelompok relatif kompak dalam geometri Euclidean. Perbedaan ukuran, densitas, bentuk memanjang, dan pencilan dapat mengubah hasil. Centroid tidak harus merupakan observasi nyata. Periksa ukuran cluster dan profil centroid dalam satuan asli untuk memberi makna pada kelompok.

## Jumlah cluster
Inertia mentah tidak meningkat ketika k bertambah; memilih minimum saja akan memilih terlalu banyak kelompok. Elbow mencari manfaat tambahan yang mulai menurun dan sering ambigu. Silhouette membandingkan jarak dalam kelompok terhadap kelompok lain, antara -1 dan 1, tetapi dipengaruhi geometri/skala. Stabilitas resampling dan kegunaan domain juga penting.

Grafik sumber membagi inertia dengan k dan dipertahankan dengan catatan. Tambahan notebook menghitung inertia mentah dan silhouette pada fitur standar. Tanpa label kebenaran, skor internal clustering bukan accuracy.

## Hierarchical clustering
Agglomerative clustering mulai dari tiap observasi tunggal lalu menggabungkan pasangan bertahap. Dendrogram menampilkan urutan/tinggi penggabungan. Memotong pada tinggi tertentu memberi kelompok. Single linkage menggunakan pasangan terdekat dan mudah chaining; complete memakai terjauh dan cenderung kompak; average memakai rata-rata; Ward meminimalkan kenaikan within-cluster sum of squares dan berkaitan dengan Euclidean.

Pada contoh yang ditranspos, objek cluster adalah saham; pada contoh pasangan perubahan harga, objeknya hari. Orientasi tabel mengubah pertanyaan. Matriks jarak pairwise membutuhkan memori kuadrat sehingga subset mungkin diperlukan pada data besar.

## Gaussian mixture
Normal multivariat ditentukan vektor mean dan kovarians yang mengatur bentuk/arah elips. Mixture $p(x)=\sum_k\pi_k\mathcal N(x|\mu_k,\Sigma_k)$ memakai bobot nonnegatif dengan jumlah satu. EM bergantian menghitung tanggung jawab posterior dan memperbarui parameter. Berbeda dari hard assignment K-means, tiap pengamatan mempunyai peluang keanggotaan pada semua komponen.

Covariance full, tied, diag, atau spherical mengontrol fleksibilitas. BIC $=k\log n-2\log\hat L$ menyeimbangkan likelihood dengan jumlah parameter. Pada scikit-learn, BIC lebih kecil lebih baik. Komponen Gaussian tidak selalu sama dengan kelompok semantik; kelompok kompleks bisa membutuhkan beberapa komponen. Inisialisasi dan regularisasi kovarians membantu menghindari solusi degenerat.

## Scaling dan fitur dominan
Standardisasi mengurangi dominasi satuan besar tetapi memberikan bobot varians sama juga merupakan keputusan analisis. Periksa fitur dominan pada loading/centroid. Inverse transform mengembalikan centroid standar ke satuan asli agar mudah diinterpretasikan.

Gower menggabungkan selisih numerik yang dibagi rentang dengan ketidakcocokan kategori (beda satu, sama nol). Rata-rata berbobot komponen yang tersedia menjadi jarak total. Rentang nol tidak boleh menjadi pembagi nol; data hilang perlu dikeluarkan dari denominator pasangan. Implementasi tambahan mencakup numerik dan nominal lengkap, menolak missing values secara eksplisit. Ini melengkapi bagian Python sumber yang belum menyediakan implementasi Gower.

## Masalah data campuran
One-hot lalu standardisasi kategori langka dapat memberi bobot besar pada perbedaan kategori tersebut. Banyak dummy untuk satu konsep juga dapat menghitung konsep itu berulang. Pilih bobot, jarak, dan algoritma sesuai tujuan serta uji sensitivitas. Cluster bukan bukti kategori alami permanen dalam populasi.

## Interpretasi dan kesimpulan
Periksa explained variance, loading besar, centroid/ukuran kelompok, sensitivitas linkage, serta kurva BIC. Tambahan Gower memperlihatkan alternatif untuk data campuran. PCA/clustering relevan untuk kompresi fitur, eksplorasi embedding DL, dan segmentasi, dengan validasi domain dan pemeriksaan stabilitas.
