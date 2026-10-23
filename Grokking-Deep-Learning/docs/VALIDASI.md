# Validasi

Validasi memeriksa 16 notebook, metadata Jupyter, identitas, keberadaan teori/kesimpulan, output error, dan checksum seluruh dataset. Eksekusi dilakukan pada kernel baru melalui `scripts/execute_notebooks.py` dengan working directory `notebooks/`.

## Hasil akhir - 23 Oktober 2026

- 16 notebook berhasil dijalankan pada kernel baru.
- 50 sel kode menyimpan nomor eksekusi dan output aktual.
- Tidak terdapat output error.
- 7 berkas dataset cocok dengan ukuran dan checksum SHA-256 pada manifest.
- Seluruh notebook memakai `MODE_CEPAT=True` untuk pemeriksaan CPU yang konsisten.

Keberhasilan teknis tidak membuktikan generalisasi atau kelayakan deployment. Mode cepat dipakai untuk pemeriksaan; eksperimen penuh dapat menghasilkan angka berbeda dan membutuhkan waktu lebih lama.
