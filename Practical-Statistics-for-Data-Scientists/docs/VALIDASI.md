# Laporan validasi

Tanggal: 27 September 2026. Lingkungan: Python 3.12.14, Windows 11.

| Bab | Sel kode nonkosong | Sel dieksekusi | Output error | Status |
|---|---:|---:|---:|---|
| 1 | 42 | 42 | 0 | Lulus |
| 2 | 19 | 19 | 0 | Lulus |
| 3 | 34 | 34 | 0 | Lulus |
| 4 | 58 | 58 | 0 | Lulus |
| 5 | 37 | 37 | 0 | Lulus |
| 6 | 33 | 33 | 0 | Lulus |
| 7 | 35 | 35 | 0 | Lulus |

## Metode pemeriksaan

- Semua 7 reproduksi sumber dieksekusi pada kernel baru. Semua 7 eksperimen tambahan dieksekusi mandiri pada kernel baru.
- Setelah digabung, Bab 1–5 dan 7 dijalankan lagi berurutan sebagai notebook utuh. Bab 6 mempertahankan output reproduksi lengkap (725,62 detik) dan tambahan mandiri (10,12 detik); notebook gabungannya belum dieksekusi ulang dalam satu kernel. Kode kedua bagian tidak berubah setelah penggabungan.
- Sel kosong sumber dibuang; tidak dihitung sebagai sel yang perlu dieksekusi.
- Tidak ada output bertipe error. Peringatan numerik/deprecation dari paket tetap terlihat, termasuk peringatan inferensi GAM dan konvergensi pada bagian demonstrasi tertentu.
- Assertion memeriksa mean populasi, definisi MAD, peluang binomial, ANOVA lintas library, pemisahan indeks train/test, lebar interval, dan sifat matriks Gower.
- Validasi struktur notebook menggunakan nbformat; SHA-256 memeriksa keutuhan seluruh dataset.
- Pemeriksaan visual mencakup 21 grafik representatif dari semua bab (awal, tengah, akhir), termasuk scatterplot, boxplot, QQ-plot, ROC, kurva ensemble, dan dendrogram. Grafik sampel terbaca tanpa pemotongan bermakna.

## Batas pemeriksaan

Keberhasilan eksekusi bukan bukti asumsi statistik terpenuhi. Peringatan teori tentang target leakage, sampel tersusun, skor training, dan interpretasi kausal dijelaskan dalam notebook. Validasi eksternal/temporal dan uji kausal tidak diklaim dilakukan.

## Pengujian perbaikan dependensi — 28 September 2026

Bab 1, 4, 5, dan 7 dijalankan ulang lengkap pada kernel baru setelah perbaikan ModuleNotFoundError; semua lulus tanpa output error. Bab 2 dan 3 juga dijalankan ulang setelah penambahan sel persiapan. Sel persiapan Bab 6 diuji mandiri menggunakan interpreter pengujian; komputasi reproduksi panjangnya tidak diulang karena tidak diubah. Pada tahap pengujian ini terdapat 258 sel kode; paket final kemudian bertambah menjadi 266 sel setelah penyempurnaan ringkasan.

Cabang modul hilang diuji dengan simulasi wquantiles tidak ditemukan dan pemeriksaan bahwa perintah instalasi menggunakan sys.executable serta requirements-lock dari repositori. Pengujian cabang tersebut tidak mengunduh ulang paket. Kernel yang dipilih pengguna di VS Code belum diamati langsung; pemasangan pada kernel tersebut terjadi ketika sel persiapan dijalankan.

Peringatan rank-deficient/GAM pada Bab 4 tetap terlihat dan dibahas sebagai keterbatasan model/inferensi, berbeda dari ModuleNotFoundError. Peringatan tersebut tidak disembunyikan.

## Pengujian mode cepat Bab 4 dan 6

Kedua notebook mode cepat dijalankan pada kernel baru dan lulus tanpa error: Bab 4 25,33 detik; Bab 6 44,22 detik pada mesin pengujian. Waktu komputer pengguna dapat berbeda dan belum termasuk pemasangan paket. Sebagai pembanding, reproduksi Bab 6 penuh sebelumnya memerlukan 725,62 detik. Mode penuh tidak dijalankan ulang pada revisi ini. Output pengujian kembali dikosongkan sesuai permintaan pengguna; semua hasil akan muncul saat sel dijalankan.

## Paket final

Mode lengkap kembali aktif pada Bab 4 dan 6. Pada 29 September 2026, notebook Bab 1–4 dijalankan ulang pada kernel baru dengan konfigurasi final dan seluruhnya lulus tanpa error: Bab 1 87,60 detik, Bab 2 15,47 detik, Bab 3 64,43 detik, dan Bab 4 19,64 detik. Output aktual dan nomor eksekusi dari keempat notebook tersebut disimpan sebagai bukti reproduksi. Bab 5–7 tetap tanpa output tersimpan.

Validasi akhir mendeteksi 7 notebook, 266 sel kode, 157 sel dengan nomor eksekusi, 0 output error, dan 19 dataset yang cocok dengan manifest SHA-256. Hasil terstruktur tersedia di `validation_summary.json`.
