# Perubahan kompatibilitas dan desain

- Kode menggunakan Python 3.12 dan NumPy tanpa TensorFlow/Keras.
- MNIST dibaca langsung dari `mnist.npz`, sehingga tidak membutuhkan framework deep learning atau unduhan saat eksekusi.
- Contoh komputasi panjang memiliki `MODE_CEPAT=True` sebagai default untuk validasi CPU; algoritma dan aliran gradien tetap ditampilkan.
- Notebook sumber lama yang bergantung pada state notebook lain disusun ulang menjadi notebook mandiri.
- Softmax dibuat stabil secara numerik dengan mengurangi nilai maksimum.
- Pembagian train/test dan batas interpretasi ditulis eksplisit.
- Bab dominan teori (1, 2, 7, dan 16) diberi contoh kecil serta penjelasan komprehensif sesuai catatan tugas.
- `reviews.txt`, `spam.txt`, dan `ham.txt` dikompresi ke format `.gz`; Bab 11 dan Bab 15 membacanya langsung dengan `gzip` agar semua berkas aman diunggah melalui halaman web GitHub.
