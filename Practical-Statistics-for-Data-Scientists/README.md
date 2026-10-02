# Practical Statistics for Data Scientists

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-blue.svg)

Reproduksi kode Python dan pembahasan teori berbahasa Indonesia untuk seluruh tujuh bab buku *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python* edisi kedua oleh Peter Bruce, Andrew Bruce, dan Peter Gedeck.

> **Catatan:** notebook Bab 1–4 menyimpan output eksekusi sebagai bukti reproduksi. Bab 5–7 tetap dapat dijalankan dari atas untuk menghasilkan tabel, metrik, dan visualisasi.

## Identitas

| | |
|---|---|
| Tugas | Code Reproduction + Theoretical Deep-Dive |
| Nama | Nanda Pratama ITM |
| NIM | 101032330212 |
| Kelas | TK 47 01 |

## Tentang proyek

Proyek ini menggabungkan reproduksi notebook resmi, penjelasan konsep statistik, eksperimen tambahan, dan interpretasi hasil. Materi mencakup analisis eksploratif hingga pembelajaran tanpa pengawasan. Penyesuaian kode untuk kompatibilitas dan koreksi statistik didokumentasikan agar prosesnya dapat ditinjau dan direproduksi.

Setiap notebook memuat:

- ringkasan konsep dan tujuan pembelajaran;
- rumus, asumsi, dan batasan metode;
- adaptasi kode Python dari sumber resmi;
- eksperimen tambahan dan evaluasi model; serta
- interpretasi hasil dalam bahasa Indonesia.

## Daftar notebook

| Bab | Notebook | Isi dan tujuan |
|---|---|---|
| 1 | [Exploratory Data Analysis](notebooks/Bab_01.ipynb) | Jenis data; mean, median, trimmed/weighted mean; varians, IQR, MAD; histogram, density, korelasi, crosstab, serta visualisasi multivariabel. Memahami data sebelum pemodelan. |
| 2 | [Data and Sampling Distributions](notebooks/Bab_02.ipynb) | Sampling, bias, distribusi sampling, CLT, bootstrap, confidence interval, normal, t, binomial, chi-square, F, Poisson, eksponensial, dan Weibull. Mengukur ketidakpastian statistik. |
| 3 | [Statistical Experiments and Significance Testing](notebooks/Bab_03.ipynb) | A/B testing, hipotesis, permutasi, p-value, t-test, multiple testing, ANOVA, chi-square, Fisher, bandit, power, dan ukuran sampel. Membedakan efek dengan variasi acak. |
| 4 | [Regression and Prediction](notebooks/Bab_04.ipynb) | Regresi sederhana/berganda, residual, evaluasi, CV, seleksi fitur, WLS, faktor, interaksi, diagnostik, polinomial, spline, GAM, dan tambahan Lasso. Memprediksi respons numerik dan memahami batas interpretasi. |
| 5 | [Classification](notebooks/Bab_05.ipynb) | Naive Bayes, LDA, logistik/GLM, odds ratio, confusion matrix, precision/recall, ROC-AUC, lift, imbalance, dan biaya kesalahan. Mengevaluasi kelas serta probabilitas dengan benar. |
| 6 | [Statistical Machine Learning](notebooks/Bab_06.ipynb) | KNN, scaling, pohon, impurity, bagging, random forest, OOB, importance, boosting/XGBoost, regularisasi, dan tuning. Memahami fleksibilitas model dan generalisasi. |
| 7 | [Unsupervised Learning](notebooks/Bab_07.ipynb) | PCA, correspondence analysis, K-means, hierarchical clustering, Gaussian mixtures, BIC, scaling, dan Gower. Mengeksplorasi representasi serta kelompok tanpa target. |

## Hasil utama

Angka berikut berasal dari eksekusi validasi sebelumnya. Detail metode, asumsi, dan interpretasi tersedia di setiap notebook.

| Analisis | Hasil | Interpretasi |
|---|---|---|
| Populasi negara bagian | Mean 6.162.876,3; median 4.436.369,5 | Beberapa populasi besar menarik rata-rata ke atas. |
| ANOVA empat sesi | F=2,7398; p=0,0776 | Tidak menolak kesamaan mean pada alpha 0,05; tidak membuktikan ekuivalensi. |
| Regresi rumah, test 20% | RMSE 272.594 vs baseline 404.572; R²=0,5459 | Lebih baik dari baseline pada split ini, dengan error yang masih besar. |
| Logistik, holdout | Accuracy 0,6058; ROC-AUC 0,6411 | Kemampuan prediksi moderat pada sampel pinjaman seimbang. |
| Gradient boosting tambahan | ROC-AUC 0,6481 | Sedikit di atas random forest 0,6467; bukan bukti superioritas umum. |
| K-means XOM/CVX standar | Silhouette tertinggi di kandidat 2–8: k=2, skor 0,4431 | Petunjuk internal, bukan label kebenaran. |

Skor pada bagian reproduksi yang dihitung dari data fit adalah **skor training/deskriptif**. Evaluasi holdout tambahan memakai fitur asli dan memisahkan data sebelum fitting. `borrower_score` dan `ZipGroup` berbasis target tidak dipakai pada evaluasi tambahan agar menghindari kebocoran dari rekayasa fitur sumber. Data pinjaman yang dipakai memiliki proporsi kelas tersusun; prevalensinya tidak mewakili otomatis populasi kredit nyata.

## Isi folder

```text
Practical-Statistics-for-Data-Scientists/
  notebooks/              # 7 notebook; Bab 1–4 menyimpan output eksekusi
  data/                   # 19 dataset dari sumber resmi
  docs/                   # teori, cakupan, perubahan, asal data, validasi
  scripts/                # menjalankan ulang dan memeriksa notebook
  requirements.txt
  requirements-lock.txt
  LICENSE                 # GPL-3.0 dari sumber kode
  README.md
  .gitignore
```

## Menjalankan ulang

Lingkungan yang diuji: **Python 3.12.14, Windows 11**. Paket yang benar-benar digunakan tercatat pada `requirements-lock.txt`. Gunakan environment terpisah.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-lock.txt
python scripts/execute_notebooks.py --chapters 1 2 3 4 --jobs 2
python scripts/execute_notebooks.py --chapters 5 6 7 --jobs 2
python scripts/validate_artifacts.py
```

Di macOS/Linux, aktifkan environment dengan `source .venv/bin/activate` dan gunakan `requirements.txt` bila ada versi pada lock file Windows yang tidak tersedia. Versi paket yang berbeda dapat sedikit mengubah hasil numerik atau peringatan.

Untuk penggunaan interaktif, buka folder ini di VS Code dengan dukungan Jupyter lalu pilih interpreter `.venv`. Jalankan notebook dari atas ke bawah. Script otomatis menyiapkan kernel lokal sendiri; tidak memerlukan instalasi kernel global. Bab 6 penuh membutuhkan sekitar 12 menit pada mesin pengujian karena random forest, permutation importance, dan grid search. Jumlah pohon/fold sumber dipertahankan.

## Cakupan, perubahan, dan validasi

Paket unggahan telah diperiksa: 7 notebook dan 266 sel kode terdeteksi serta 19 dataset dicocokkan dengan manifest SHA-256. Bab 1–4 dijalankan pada kernel baru dan menyimpan output aktual tanpa error; Bab 5–7 disediakan tanpa output tersimpan.

- [Pemetaan bab dan bagian teori](docs/CAKUPAN.md)
- [Koreksi statistik dan kompatibilitas](docs/PERUBAHAN.md)
- [Asal kode dan data](docs/SUMBER.md)
- [Laporan validasi](docs/VALIDASI.md)
- [Petunjuk unggah GitHub](docs/PANDUAN_GITHUB.md)

Seluruh sel Python nonkosong dari 7 notebook resmi dipertahankan, dengan penyesuaian yang dicatat. Contoh R di komentar tidak dianggap kode Python yang sudah dijalankan. Bagian Gower dan Fisher yang belum lengkap pada notebook sumber dilengkapi sebagai eksperimen tambahan. Tidak ada hasil eksekusi yang dikarang.

## Referensi dan atribusi

1. Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python* (2nd ed.). O'Reilly Media. ISBN 978-1492072942.
2. [Repositori resmi penulis](https://github.com/gedeck/practical-statistics-for-data-scientists), commit `8a6d3bb6468e979c861d4b37215e1413702dfdfa`, diakses 27 September 2026.
3. [Contoh format pengumpulan](https://github.com/farrelrassya/Practical-Statistics-for-Data-Scientist-Books), digunakan sebagai referensi struktur tugas.

Kode yang diadaptasi dari repositori resmi tetap mengikuti lisensi **GPL-3.0** yang tersedia pada [LICENSE](LICENSE). Hak cipta buku dan materi sumber tetap dimiliki oleh pemegang hak masing-masing. Berkas PDF buku tidak disertakan dalam repositori ini.

Kode reproduksi diadaptasi dari repositori resmi dan atribusinya dipertahankan. LLM digunakan untuk membantu penyusunan penjelasan teori sebagaimana diizinkan dalam instruksi tugas. Setiap perubahan kode, eksperimen tambahan, dan hasil eksekusi ditinjau serta didokumentasikan agar dapat diperiksa kembali.
