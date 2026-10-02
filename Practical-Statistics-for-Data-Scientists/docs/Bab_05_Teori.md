# Ringkasan dan pendalaman teori Bab 5

Klasifikasi memprediksi kelas atau peluang kelas. Data pinjaman dipakai untuk Naive Bayes, LDA, regresi logistik, evaluasi, dan strategi ketidakseimbangan kelas. Definisi positif harus eksplisit; pada eksperimen tambahan kelas positif adalah default.

## Naive Bayes
Bayes memberi $P(C|x)\propto P(C)P(x|C)$. Distribusi bersama semua fitur membutuhkan sangat banyak data. Naive Bayes menyederhanakan melalui independensi bersyarat: $P(x|C)=\prod_jP(x_j|C)$. Asumsi ini sering tidak sepenuhnya benar, namun klasifikasi dapat tetap berguna; probabilitas dapat terlalu percaya diri jika fitur saling bergantung.

Sumber menggunakan MultinomialNB pada indikator kategori. GaussianNB mendukung numerik kontinu dengan asumsi Gaussian per kelas, sehingga pernyataan lama bahwa scikit-learn tidak mendukung numerik untuk Naive Bayes tidak berlaku umum. Smoothing alpha mencegah frekuensi nol mematikan likelihood. `fit_prior=False` memakai prior seragam, berbeda dari prior empiris. One-hot multinomial juga berbeda dari categorical Naive Bayes langsung.

## Discriminant analysis
LDA memodelkan fitur per kelas dengan normal multivariat dan kovarians bersama. Matriks kovarians memuat varians fitur dan pergerakan bersamanya. Kovarians bersama menghasilkan batas keputusan linear pada log-rasio posterior. Arah diskriminan memisahkan mean kelas relatif terhadap variasi dalam kelas. QDA mengizinkan kovarians berbeda sehingga batasnya kuadratik, dengan lebih banyak parameter. Kovarians singular dan penyimpangan distribusi berat dapat mengganggu LDA.

## Logistik dan GLM
Regresi logistik memakai $\log[p/(1-p)]=\beta_0+\sum_j\beta_jx_j$ dan sigmoid $p=1/(1+e^{-\eta})$. Respons biner dimodelkan Bernoulli/binomial; parameter diestimasi melalui likelihood, bukan least squares biasa. GLM menghubungkan keluarga distribusi respons, linear predictor, dan link. Regresi linear memakai identity link pada Gaussian; logistik memakai logit pada binomial.

Koefisien b adalah perubahan log-odds per satuan fitur, dengan fitur lain tetap. Odds ratio $e^b$ bukan kenaikan probabilitas sebesar b atau e^b; perubahan peluang bergantung baseline. Urutan `classes_` menentukan kolom `predict_proba`. Memilih kolom 1 tanpa memeriksa label dapat membalik kesimpulan. C sangat besar pada reproduksi mendekati fit tanpa penalti. Separation dapat membuat koefisien tak berhingga atau tidak stabil.

## Penilaian model
Deviance membandingkan kecocokan dengan model jenuh. AIC menambahkan penalti kompleksitas tetapi tidak menggantikan test set. Linearitas logistik berlaku pada logit, bukan pada probabilitas. Spline memperluas bentuk hubungan. Residual/diagnostik membantu mendeteksi spesifikasi salah dan pengamatan berpengaruh.

Beberapa metrik sumber dihitung pada training dan merupakan apparent performance. Tambahan notebook memakai split terstratifikasi, dengan fitting hanya pada training. Borrower_score yang disediakan sumber tidak digunakan pada evaluasi tambahan karena dapat dibentuk menggunakan label dari luar training. Untuk penggunaan nyata, validasi temporal kredit sering lebih relevan daripada split acak.

## Confusion matrix dan kelas langka
Dengan default sebagai positif, TP adalah default terdeteksi, FN default terlewat, FP pinjaman lancar ditandai default, dan TN lancar yang benar. Accuracy $(TP+TN)/N$, precision $TP/(TP+FP)$, recall $TP/(TP+FN)$, specificity $TN/(TN+FP)$. F1 adalah rata-rata harmonik precision dan recall. Jika denominator nol, kebijakan perhitungan harus jelas.

Pada kelas langka, menebak semua negatif dapat memberi accuracy tinggi dengan recall nol. Precision mengukur keandalan alarm; recall mengukur cakupan deteksi positif. Threshold mengubah kompromi keduanya. Threshold 0.5 bukan keharusan; pilih dengan validation set dan biaya keputusan, lalu evaluasi sekali di test.

## ROC, AUC, precision-recall, dan lift
ROC membandingkan true-positive rate dengan false-positive rate pada berbagai threshold. AUC mengukur kemampuan ranking: peluang skor positif lebih tinggi daripada negatif, dengan penanganan ties. AUC 0.5 setara ranking acak, bukan berarti accuracy pasti 50%. AUC tidak menilai kalibrasi dan dapat tampak baik pada kelas sangat jarang meski precision rendah.

Precision-recall curve dan average precision berfokus pada kelas positif. Lift pada fraksi skor teratas membandingkan proporsi positif kelompok itu dengan prevalensi keseluruhan. Pilih metrik sesuai kapasitas tindak lanjut dan biaya, bukan setelah melihat angka yang paling bagus.

## Imbalance dan biaya
Undersampling mengurangi mayoritas dan dapat membuang informasi. Oversampling mereplikasi minoritas. Class weight mengubah kontribusi loss. SMOTE menginterpolasi tetangga minoritas; ADASYN lebih berfokus area yang sulit. Interpolasi dummy kategori bisa menghasilkan nilai yang tidak bermakna; gunakan metode sesuai tipe fitur, misalnya SMOTENC jika diperlukan.

Resampling hanya dilakukan pada training dan di dalam fold CV. Resampling sebelum split menyebabkan kebocoran. Perubahan prior efektif dapat membuat probabilitas perlu kalibrasi/koreksi untuk deployment. Cost-based classification mempertimbangkan kerugian FN dan FP, sehingga accuracy tertinggi belum tentu memberi biaya terendah.

## Eksplorasi prediksi dan kesimpulan
Batas keputusan memperlihatkan fleksibilitas model, bukan bukti model terumit paling baik. LinearGAM pada target 0/1 dalam sumber adalah demonstrasi permukaan skor, bukan probabilitas yang dijamin pada [0,1]; logistic GAM lebih sesuai untuk peluang biner. Interpretasikan confusion matrix, ROC-AUC, dan average precision bersama prevalensi dan baseline. Konsep loss, imbalance, kelas positif, serta threshold juga berlaku pada neural network classifier.
