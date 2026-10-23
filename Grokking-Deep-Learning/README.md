# Grokking Deep Learning

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-from%20scratch-013243?logo=numpy&logoColor=white)

Reproduksi kode dan pendalaman teori berbahasa Indonesia untuk seluruh 16 bab buku *Grokking Deep Learning* oleh Andrew W. Trask (Manning, 2019).

## Identitas

| | |
|---|---|
| Tugas | Tugas 2 - Code Reproduction + Theoretical Deep-Dive |
| Nama | Nanda Pratama Itma |
| NIM | 101032330212 |
| Kelas | TK 47 01 |

## Tentang proyek

Setiap notebook merangkum konsep bab, menjelaskan teori dan asumsi, mereproduksi ide kode utama menggunakan NumPy, serta memberi interpretasi. Bab yang dominan teori tetap mempunyai penjelasan komprehensif dan contoh kecil sesuai catatan tugas. Implementasi sengaja tidak bergantung pada framework deep learning tingkat tinggi agar mekanisme forward propagation, gradient descent, backpropagation, convolution, recurrence, autograd, LSTM, dan federated averaging dapat terlihat.

## Daftar notebook

| Bab | Notebook | Ringkasan |
|---:|---|---|
| 1 | [Introducing Deep Learning](notebooks/Bab_01.ipynb) | Alasan mempelajari deep learning, prasyarat, dan siklus eksperimen. |
| 2 | [Fundamental Concepts](notebooks/Bab_02.ipynb) | Supervised/unsupervised, parametrik/nonparametrik, serta predict-compare-learn. |
| 3 | [Neural Prediction](notebooks/Bab_03.ipynb) | Forward propagation, weighted sum, banyak input/output, dan jaringan bertumpuk. |
| 4 | [Gradient Descent](notebooks/Bab_04.ipynb) | Loss, turunan, learning rate, divergence, dan generalization. |
| 5 | [Generalizing Gradient Descent](notebooks/Bab_05.ipynb) | Banyak bobot, outer product, credit assignment, dan bentuk gradien. |
| 6 | [Backpropagation](notebooks/Bab_06.ipynb) | Hidden layer, ReLU, batch/stochastic learning, dan backpropagation. |
| 7 | [How to Picture Neural Networks](notebooks/Bab_07.ipynb) | Graf komputasi, visualisasi jaringan, dan bentuk tensor. |
| 8 | [Regularization and Batching](notebooks/Bab_08.ipynb) | MNIST, overfitting, early stopping, dropout, dan mini-batch. |
| 9 | [Activation Functions](notebooks/Bab_09.ipynb) | ReLU, tanh, sigmoid, softmax, cross-entropy, dan turunannya. |
| 10 | [Convolutional Neural Networks](notebooks/Bab_10.ipynb) | Patch citra, weight sharing, kernel, feature map, dan klasifikasi. |
| 11 | [Word Embeddings](notebooks/Bab_11.ipynb) | Bag of words, embedding, sentimen, kemiripan, dan bias representasi. |
| 12 | [Recurrent Layers](notebooks/Bab_12.ipynb) | Sequence, hidden state, BPTT, next-word prediction, dan perplexity. |
| 13 | [Automatic Optimization](notebooks/Bab_13.ipynb) | Tensor, graf komputasi, autograd, layer, loss, dan optimizer. |
| 14 | [Long Short-Term Memory](notebooks/Bab_14.ipynb) | Language modeling, truncated BPTT, gradien, serta gate LSTM. |
| 15 | [Federated Learning](notebooks/Bab_15.ipynb) | Federated averaging, ancaman privasi, secure aggregation, dan enkripsi. |
| 16 | [Where to Go from Here](notebooks/Bab_16.ipynb) | Roadmap PyTorch, paper, portofolio, komunitas, dan tanggung jawab. |

## Struktur repositori

```text
Grokking-Deep-Learning/
  notebooks/              # Notebook Bab 1-16
  data/                   # Dataset dari repositori pendamping resmi
  docs/                   # Cakupan, sumber, perubahan, dan validasi
  scripts/                # Eksekusi dan pemeriksaan otomatis
  requirements.txt
  requirements-lock.txt
  NOTICE.md
  README.md
```

## Menjalankan proyek

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-lock.txt
python scripts/execute_notebooks.py --jobs 1
python scripts/validate_artifacts.py
```

Pada macOS/Linux, aktifkan environment dengan `source .venv/bin/activate`. Buka notebook di VS Code/Jupyter, pilih kernel `.venv`, lalu jalankan dari atas. Mode cepat aktif secara default agar seluruh contoh dapat diuji pada CPU; ubah `MODE_CEPAT=False` di notebook untuk eksperimen lebih panjang.

## Reproduksibilitas

- Semua notebook memakai seed eksplisit untuk bagian acak.
- Dataset disimpan lokal dan checksum SHA-256 dicatat di `docs/data_manifest.json`.
- Script eksekusi memakai kernel baru dan berhenti jika ada error.
- Seluruh 16 notebook telah dijalankan berurutan dalam mode cepat; 50 sel kode menyimpan output aktual tanpa error.
- PDF buku tidak disertakan karena hak cipta tetap milik penerbit/penulis.

## Referensi dan integritas akademik

1. Trask, A. W. (2019). *Grokking Deep Learning*. Manning Publications. ISBN 9781617293702.
2. [Repositori pendamping resmi](https://github.com/iamtrask/Grokking-Deep-Learning), commit `e665168b4aefe3256360951504103cf98827ca51`.

Kode dalam notebook merupakan reproduksi/adaptasi edukatif dari gagasan dan kode pendamping buku, bukan klaim karya kode asli. Sumber dipertahankan pada dokumentasi. LLM digunakan untuk membantu menyusun penjelasan teori; seluruh hasil tetap harus dipahami, ditinjau, dan dapat dijelaskan oleh mahasiswa sebelum dikumpulkan. Tidak ada lisensi eksplisit pada repositori pendamping yang diperiksa, sehingga penggunaan kembali di sini dibatasi untuk konteks tugas pendidikan dan atribusi dipertahankan.
