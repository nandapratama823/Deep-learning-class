# Ringkasan dan pendalaman teori Bab 4

Regresi memodelkan respons numerik dari satu atau beberapa prediktor. Contoh fungsi paru dan harga rumah menunjukkan estimasi koefisien, pemeriksaan residual, pembandingan model, dan perluasan nonlinear melalui polinomial, spline, serta GAM.

## Regresi sederhana dan least squares
Model $Y=\beta_0+\beta_1X+\epsilon$ memisahkan hubungan rata-rata dan variasi yang tidak dijelaskan. Fitted value $\hat y_i=b_0+b_1x_i$; residual $e_i=y_i-\hat y_i$. Least squares meminimalkan $\sum_ie_i^2$. Koefisien Exposure menunjukkan perubahan rata-rata PEFR per satuan Exposure dalam model, bukan otomatis efek kausal. Intercept X=0 perlu konteks bila berada di luar kondisi yang relevan.

## Regresi berganda dan penilaian
Model $\hat y=b_0+\sum_jb_jx_j$ membaca koefisien sebagai perubahan prediksi ketika satu prediktor berubah dan yang lain tetap. RMSE $=\sqrt{\sum_i(y_i-\hat y_i)^2/n}$ bersatuan target dan sensitif pada error besar. $R^2=1-SSE/SST$ membandingkan error terhadap baseline mean. Di data uji, R-squared dapat negatif. Adjusted R-squared memperhitungkan jumlah prediktor tetapi tidak menggantikan evaluasi data baru.

Statsmodels menampilkan koefisien, standard error, interval, dan uji di bawah asumsi model. OLS berbasis matriks tidak otomatis menambah intercept. Skor dari data fit pada reproduksi adalah ukuran training; tambahan notebook menyediakan holdout dan CV yang dipisahkan. Tujuan prediksi menekankan akurasi data baru, sedangkan explanation menekankan interpretasi parameter; keduanya tetap memerlukan asumsi dan data yang sesuai.

## Cross-validation, seleksi model, dan AIC
K-fold melatih di k-1 fold dan memvalidasi pada sisanya. Preprocessing yang mempelajari parameter harus berada di dalam fold. Data temporal membutuhkan split sesuai waktu. AIC $=2k-2\log\hat L$ memberi penalti kompleksitas; lebih kecil lebih baik pada model dengan data/likelihood yang sebanding.

Stepwise menambah/membuang fitur berdasarkan kriteria. Pencarian lokal ini dapat tidak stabil pada fitur berkorelasi; p-value pascaseleksi tidak boleh diperlakukan seperti hipotesis yang ditentukan sebelumnya. Ridge/Lasso mengendalikan kompleksitas lewat penalti. Lasso menambah $\lambda\sum_j|b_j|$ dan dapat membuat koefisien nol. Standardisasi penting karena penalti dipengaruhi satuan fitur. Materi Lasso sumber ditandai sebagai tambahan di luar isi utama buku.

## Regresi berbobot
Weighted least squares meminimalkan $\sum_iw_ie_i^2$. Bobot inverse variance cocok ketika varians error diketahui/diestimasi memadai. Pada contoh, bobot tahun membuat transaksi lebih baru berpengaruh lebih besar; itu pilihan relevansi waktu, bukan otomatis koreksi heteroskedastisitas. Bandingkan perubahan koefisien dan error per tahun.

## Ekstrapolasi dan interval
Prediksi jauh di luar rentang training adalah ekstrapolasi, yang berisiko salah meski skor training tinggi. Confidence interval menggambarkan ketidakpastian mean respons pada x tertentu; prediction interval menambahkan variasi individual dan biasanya lebih lebar. Ketergantungan residual atau heteroskedastisitas yang diabaikan dapat membuat interval terlalu sempit.

## Faktor, banyak kategori, dan ordinal
Dengan intercept, k kategori nominal lazim dikodekan dengan k-1 dummy. Kategori yang dihilangkan menjadi acuan; koefisien dummy membandingkan dengan acuan pada fitur lain yang tetap. Semua dummy plus intercept menghasilkan ketergantungan linear sempurna. Kode ordinal 1,2,3 mengasumsikan jarak dan efek linear yang belum tentu tepat.

Sumber mengelompokkan kode pos berdasarkan median residual seluruh data. Ini dipertahankan untuk reproduksi deskriptif. **ZipGroup seperti ini berpotensi bocor untuk evaluasi prediksi** karena sudah melihat target. Untuk generalisasi, kelompok harus dipelajari hanya dari training/fold. Tambahan holdout memakai fitur numerik asli sehingga tidak memakai kelompok berbasis residual tersebut.

## Multikolinearitas, confounding, dan interaksi
Fitur berkorelasi kuat membuat koefisien sensitif dan standard error besar, meski prediksi gabungan masih baik. Tanda koefisien Bedrooms harus dibaca setelah mengondisikan luas dan kualitas rumah. Confounding terjadi ketika variabel terkait prediktor sekaligus respons tidak dimasukkan, sehingga asosiasi berubah setelah penyesuaian. Penyesuaian statistik tidak otomatis membuktikan kausalitas.

Interaksi $b_3X_1X_2$ membuat slope X1 menjadi $b_1+b_3X_2$. Formula `SqFtTotLiving*ZipGroup` memasukkan main effects dan interaksi, sehingga slope luas dapat berbeda antarwilayah. Interpretasi main effect harus menyebut nilai acuan variabel yang berinteraksi.

## Diagnostik
Outlier respons memiliki residual besar; leverage tinggi berarti fitur jauh dari pusat data. Cook's distance menggabungkan residual dan leverage untuk menilai perubahan fit bila observasi dihilangkan. Observasi berpengaruh perlu ditelusuri, bukan dibuang otomatis untuk meningkatkan skor.

Pola kipas residual terhadap fitted mengindikasikan heteroskedastisitas. Normalitas residual berkaitan terutama dengan inferensi kecil-sampel; target mentah tidak harus normal agar regresi dapat dipasang. Error berkorelasi, misalnya properti berdekatan atau serial, membuat standard error biasa tidak tepat. Pola melengkung menunjukkan bentuk mean belum cukup linear. Partial residual plot membantu mengisolasi pola suatu prediktor setelah fitur lain diperhitungkan, tetapi tetap dipengaruhi spesifikasi model.

## Polinomial, spline, dan GAM
Polinomial menambah pangkat X; nonlinear terhadap X tetapi linear terhadap koefisien. Derajat tinggi dapat berosilasi dan buruk untuk ekstrapolasi. Spline menggabungkan potongan polinomial dengan syarat kehalusan pada knot; jumlah knot dan derajat bebas mengatur kompleksitas lokal.

GAM memakai $g(E[Y|X])=\beta_0+\sum_j f_j(X_j)$. Link identitas cocok untuk respons Gaussian; keluarga lain memerlukan link sesuai. Komponen halus memudahkan membaca pola nonlinear, namun additivity membatasi interaksi kecuali ditambahkan. Penalti kehalusan perlu dituning. Inferensi p-value GAM setelah tuning perlu memperhatikan keterbatasan paket, termasuk peringatan yang dicetak pada output.

## Interpretasi dan kesimpulan
Bandingkan slope fungsi paru, model rumah berganda, serta perubahan setelah faktor wilayah dan interaksi. Periksa residual dan observasi berpengaruh. Pada evaluasi tambahan, bandingkan RMSE terhadap baseline mean, skor CV training, dan lebar confidence/prediction interval. Regresi memperkenalkan loss, regularisasi, dan generalisasi yang juga mendasari deep learning.
