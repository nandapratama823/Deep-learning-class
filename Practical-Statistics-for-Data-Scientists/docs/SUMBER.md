# Asal kode dan data

Referensi utama: Bruce, Bruce, & Gedeck (2020), *Practical Statistics for Data Scientists*, edisi ke-2. PDF pengguna diperiksa untuk memastikan 7 bab dan cakupan teori. PDF tidak disertakan dalam paket.

Kode dan dataset berasal dari [repositori resmi](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/8a6d3bb6468e979c861d4b37215e1413702dfdfa), commit `8a6d3bb6468e979c861d4b37215e1413702dfdfa`. Salinan LICENSE GPL-3.0 dipertahankan. Identitas penulis asli dipertahankan di setiap notebook.

| Bab | Sumber notebook | Dataset yang dibaca |
|---|---|---|
| 1 | python/notebooks/Chapter 1 - Exploratory Data Analysis.ipynb | airline_stats.csv, dfw_airline.csv, kc_tax.csv.gz, lc_loans.csv, sp500_data.csv.gz, sp500_sectors.csv, state.csv |
| 2 | python/notebooks/Chapter 2 - Data and sampling distributions.ipynb | loans_income.csv, sp500_data.csv.gz |
| 3 | python/notebooks/Chapter 3 - Statistical Experiments and Significance Testing.ipynb | click_rates.csv, four_sessions.csv, imanishi_data.csv, web_page_data.csv |
| 4 | python/notebooks/Chapter 4 - Regression and Prediction.ipynb | LungDisease.csv, house_sales.csv |
| 5 | python/notebooks/Chapter 5 - Classification.ipynb | full_train_set.csv.gz, loan3000.csv, loan_data.csv.gz |
| 6 | python/notebooks/Chapter 6 - Statistical Machine Learning.ipynb | loan200.csv, loan3000.csv, loan_data.csv.gz |
| 7 | python/notebooks/Chapter 7 - Unsupervised Learning.ipynb | housetasks.csv, loan_data.csv.gz, sp500_data.csv.gz, sp500_sectors.csv |

## Keutuhan dan penggunaan data

Data disalin tanpa perubahan byte dari repositori penulis. Nama, ukuran, dan SHA-256 berada pada `data_manifest.json`. Pengolahan seperti filtering/encoding dilakukan di memori notebook. Data riil dari buku dibedakan dari simulasi pada bagian tambahan. Asal lebih rinci tiap dataset mengikuti penjelasan buku dan repositori penulis; tidak diklaim sebagai data yang dikumpulkan mahasiswa.

## Kontribusi

Reproduksi/adaptasi kode berlisensi diberi atribusi kepada penulis. LLM digunakan untuk membantu penyusunan ringkasan dan penjelasan teori berbahasa Indonesia sebagaimana diizinkan dalam instruksi tugas. Perubahan kode, eksperimen tambahan, dan hasil eksekusi dicatat agar dapat ditinjau kembali oleh Nanda Pratama ITM, NIM 101032330212, TK 47 01.
