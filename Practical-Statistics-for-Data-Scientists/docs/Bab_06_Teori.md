# Ringkasan dan pendalaman teori Bab 6

Bab ini mencakup KNN, pohon keputusan, random forest, dan boosting. Fokusnya hubungan fleksibilitas, metrik jarak, agregasi, serta regularisasi dengan bias, varians, dan prediksi di luar sampel.

## KNN dan jarak
KNN memilih k tetangga training terdekat dari observasi baru. Klasifikasi memakai voting/proporsi kelas; regresi memakai rata-rata respons. Euclidean $d(x,z)=\sqrt{\sum_j(x_j-z_j)^2}$ sensitif pada satuan; Manhattan menjumlahkan selisih absolut. Jarak harus mencerminkan kemiripan yang relevan. Pada dimensi tinggi, jarak dapat kehilangan daya pembeda (curse of dimensionality).

K kecil menghasilkan batas fleksibel, bias rendah, varians tinggi. K besar memperhalus tetapi dapat mengabaikan struktur lokal. Pilih k melalui validasi/CV. Prediksi KNN dapat mahal karena pencarian tetangga. Bobot jarak memberi pengaruh lebih besar kepada tetangga yang lebih dekat.

## Encoding, scaling, dan fitur KNN
One-hot mencegah kategori nominal dianggap memiliki urutan angka. Standardisasi $z_j=(x_j-\bar{x}_j)/s_j$ menyetarakan skala, bukan menjamin semua fitur sama relevannya. Fit scaler hanya pada training. Bandingkan tetangga sebelum/sesudah scaling saldo dan rasio utang.

KNN dapat membuat fitur proporsi tetangga yang lunas. Sumber menghitung borrower_score pada data fit sendiri sehingga tetangga dapat mencakup observasi yang diprediksi. Ini dipertahankan sebagai reproduksi dengan catatan. Untuk prediksi model berikutnya, fitur berbasis target harus dibuat out-of-fold pada training, dan dari training penuh untuk test. Tambahan perbandingan memakai fitur asli tanpa borrower_score.

## Pohon keputusan
Recursive partitioning membagi ruang fitur melalui pertanyaan X<t. Algoritma greedy memilih penurunan impurity terbesar pada tiap node. Leaf menghasilkan kelas/probabilitas empiris atau mean untuk regresi. Pohon menangkap interaksi dan nonlinearitas serta biasanya tidak membutuhkan standardisasi.

Gini $1-\sum_kp_k^2$ dan entropy $-\sum_kp_k\log_2p_k$ nol pada node murni. Penurunan impurity dibobot ukuran anak. Pohon terlalu dalam dapat menghafal training; depth, minimum leaf, minimum impurity decrease, dan pruning mengontrol kompleksitas. Satu pohon dapat berubah besar akibat sedikit perubahan data.

## Bagging, random forest, dan OOB
Bagging melatih model pada bootstrap samples lalu mengagregasi prediksi. Random forest juga mengacak subset fitur pada tiap split sehingga korelasi antarpohon berkurang. Agregasi model yang tidak terlalu berkorelasi menurunkan varians. Peluang sebuah observasi tidak masuk bootstrap berukuran n mendekati $e^{-1}$ atau 36.8%; observasi itu out-of-bag bagi pohon tersebut.

OOB score menggunakan pohon yang tidak melatih pengamatan yang dinilai. Namun preprocessing berbasis semua target sebelum forest tetap bisa bocor dan tidak diperbaiki OOB. Menambah pohon menstabilkan ensemble; depth dan minimum leaf lebih langsung mengatur kompleksitas masing-masing pohon. Jumlah pohon juga berdampak pada memori/waktu.

## Feature importance
Impurity importance menjumlahkan penurunan impurity dan bisa bias terhadap fitur kontinu atau kategori dengan banyak kandidat split. Permutation importance mengacak satu fitur di validation dan mengukur penurunan skor. Fitur berkorelasi bisa saling menggantikan sehingga importance individual kecil. Importance adalah kontribusi prediktif dalam model/data/metrik tertentu, bukan pengaruh kausal.

Sumber menghitung penurunan accuracy relatif setelah pengacakan. Pengacakan hanya pada training dapat mengagungkan fitur yang dihafal. Jangan memakai test berulang untuk memilih fitur; gunakan validation untuk pengembangan dan test untuk penilaian akhir.

## Boosting dan XGBoost
Boosting menambah learner secara berurutan untuk memperbaiki ensemble. Gradient boosting mengikuti negative gradient loss, yang lebih umum daripada sekadar residual regresi. XGBoost memakai gradient, Hessian, dan penalti kompleksitas.

Learning rate mengecilkan kontribusi tiap pohon; nilai kecil biasanya butuh lebih banyak pohon. Depth mengontrol interaksi, subsample mengacak baris, dan L1/L2 memberi regularisasi. Training loss dapat turun ketika validation loss justru naik. Karena default dikodekan 1, probabilitas default harus berasal dari kolom kelas 1; sumber yang memilih kelas sebaliknya telah dikoreksi.

## Regularisasi dan tuning
Bandingkan kurva training dan validation sepanjang iterasi. Gap membesar dapat menandakan overfitting; noise dan distribution shift juga perlu dipertimbangkan. Early stopping memilih iterasi lewat validation, bukan test akhir. Prediksi bertahap diperbaiki agar menyertakan pohon pertama dengan rentang mulai nol.

Grid search mencoba kombinasi parameter dan merangkum skor antar fold. Makin banyak konfigurasi dicoba, makin besar peluang memilih noise validation. Nested CV atau test akhir terpisah membantu. Pencarian learning rate dan depth sumber tetap direproduksi. Karena borrower_score sumber berbasis target, skor bagian itu merupakan demonstrasi algoritma, bukan klaim generalisasi bebas kebocoran. Holdout tambahan menggunakan fitur asli dan seed tetap.

## Interpretasi dan kesimpulan
Bandingkan tetangga sebelum/sesudah scaling, struktur pohon, OOB terhadap jumlah pohon, serta error training dan validation boosting. Model paling fleksibel tidak otomatis menang pada data baru. Hubungan dengan DL meliputi loss, gradient optimization, regularisasi, hyperparameter, dan pemisahan train/validation/test.
