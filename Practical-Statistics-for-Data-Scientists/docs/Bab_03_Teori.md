# Ringkasan dan pendalaman teori Bab 3

Eksperimen membandingkan efek yang diamati dengan variasi yang mungkin terjadi secara kebetulan. Bab ini menghubungkan desain eksperimen, hipotesis, resampling, pengujian parametrik, dan ukuran sampel. Signifikansi perlu dibaca bersama ukuran efek serta konteks penggunaan.

## A/B testing dan hipotesis
A/B testing membagi unit secara acak ke kontrol A dan perlakuan B. Kontrol membantu memisahkan efek perlakuan dari perubahan umum seperti musim. Tentukan metrik, unit randomisasi, ukuran sampel, durasi, dan arah hipotesis sebelum melihat hasil. Pengunjung berulang atau unit yang berinteraksi dapat melanggar independensi. Menambah banyak versi meningkatkan masalah multiple testing.

H0 biasanya menyatakan tidak ada perbedaan; H1 menyatakan perbedaan yang ingin dideteksi. Uji dua sisi mendeteksi kedua arah, sedangkan satu sisi hanya arah yang telah ditentukan. Gagal menolak H0 tidak membuktikan kesetaraan. Uji ekuivalensi memerlukan batas efek yang dianggap tidak bermakna dan desain tersendiri.

## Permutation test
Jika label perlakuan dapat dipertukarkan di bawah H0, gabungkan hasil lalu acak label dengan ukuran kelompok tetap. Hitung statistik, misalnya rata-rata B dikurangi A, pada setiap permutasi. Posisi selisih aktual terhadap distribusi nol menunjukkan keekstreman hasil. Asumsi exchangeability penting; data berpasangan perlu pengacakan sesuai pasangan.

Permutasi exhaustive mencakup seluruh susunan label; Monte Carlo hanya sebagian. Bootstrap mengambil ulang dengan pengembalian dan berbeda dari permutasi. Estimasi p Monte Carlo dapat memakai $(b+1)/(B+1)$ agar tidak melaporkan p=0 akibat simulasi terbatas. Contoh sumber memakai proporsi sederhana sehingga hasilnya dipahami sebagai estimasi simulasi.

## p-value, alpha, dan error
p-value adalah peluang statistik minimal se-ekstrem yang diamati jika H0 dan asumsi model berlaku. Ini bukan peluang H0 benar, bukan ukuran efek, dan bukan peluang hasil akan bereplikasi. Alpha adalah ambang keputusan yang ditetapkan sebelumnya. Error tipe I berarti menolak H0 yang benar; tipe II berarti gagal menolak H0 ketika alternatif tertentu benar. Power adalah 1-beta.

Sampel besar dapat membuat efek sangat kecil signifikan. Laporkan selisih absolut, relatif, ketidakpastian, dan manfaat/biaya tindakan. Pada contoh konversi, selisih proporsi yang dikali 100 dibaca sebagai poin persentase. Melihat p-value berulang lalu berhenti ketika signifikan mengubah tingkat kesalahan; gunakan desain sequential yang sesuai jika pemantauan diperlukan.

## t-test dan derajat bebas
Welch t-test memakai $t=(\bar{x}_A-\bar{x}_B)/\sqrt{s_A^2/n_A+s_B^2/n_B}$ dan tidak mengharuskan varians populasi sama. Derajat bebas Welch bergantung pada ukuran dan varians kelompok. Uji berpasangan diterapkan pada selisih pasangan dan berbeda dari uji independen. Di notebook, hipotesis waktu B lebih lama ditulis sebagai A lebih kecil melalui `alternative='less'`.

Derajat bebas adalah banyaknya informasi bebas setelah parameter atau batasan diestimasi. Pada varians sampel, residual terhadap mean berjumlah nol sehingga hanya n-1 residual bebas. Ketepatan inferensi sampel kecil dipengaruhi bentuk distribusi dan pencilan. Pilihan uji tidak memperbaiki desain atau sampling yang bias.

## Multiple testing
Untuk m uji independen pada alpha yang sama, peluang setidaknya satu false positive adalah $1-(1-\alpha)^m$. Bonferroni memakai alpha/m untuk mengontrol family-wise error dan tetap valid sebagai batas konservatif tanpa independensi. Benjamini-Hochberg mengendalikan false discovery rate pada kondisi yang sesuai. Pemilihan fitur dan pencarian hyperparameter berulang juga menimbulkan optimisme; evaluasi akhir perlu data terpisah.

## ANOVA
ANOVA menguji kesamaan mean beberapa kelompok. $F=MS_{antara}/MS_{dalam}$ membandingkan variasi mean kelompok terhadap variasi residual. Dengan g kelompok dan N pengamatan, derajat bebasnya g-1 dan N-g. p-value berasal dari ekor kanan F. **F dan p-value tidak dibagi dua**; kesalahan pada contoh sumber telah diperbaiki. Signifikan berarti setidaknya satu mean berbeda, bukan semua pasangan berbeda. Post-hoc memerlukan koreksi yang tepat.

ANOVA klasik mengasumsikan error independen, varians sebanding, serta normalitas residual untuk inferensi eksak. ANOVA dua arah melibatkan dua faktor dan dapat mencakup interaksi: efek suatu faktor bergantung pada level faktor lain. Jenis sum of squares perlu diperhatikan untuk desain tidak seimbang. Tambahan notebook memperagakan interaksi dua faktor pada data simulasi yang diberi label jelas.

## Chi-square, Fisher, dan pola digit
Untuk independensi pada tabel, expected count $E_{ij}=R_iC_j/N$. Statistik $\chi^2=\sum_{ij}(O_{ij}-E_{ij})^2/E_{ij}$ memiliki df (r-1)(c-1) pada pendekatan asimtotik. Expected count kecil dapat membuat pendekatan kurang akurat; gunakan metode eksak/simulasi yang sesuai. Pearson residual membantu menemukan sel penyumbang penyimpangan.

Fisher exact mengondisikan pada margin tabel dan cocok untuk contoh 2x2 kecil. Notebook menambahkan contoh 2x2 Python yang dieksekusi. Asosiasi kategori bukan bukti kausalitas. Pola digit yang tidak seragam pada contoh Imanishi dapat memicu pemeriksaan kualitas, tetapi tidak cukup untuk menyimpulkan kecurangan tanpa mekanisme pengukuran dan bukti lain.

## Multi-arm bandit
Bandit menyeimbangkan exploration (mencoba untuk belajar) dan exploitation (memakai pilihan terbaik saat ini). Epsilon-greedy memilih acak dengan peluang epsilon. Thompson sampling mengambil sampel dari posterior; upper confidence bound memberi bonus ketidakpastian. Tujuannya meningkatkan reward selama eksperimen. Data adaptif tidak boleh dianalisis seolah alokasinya A/B tetap. Tambahan simulasi memperlihatkan jumlah pemilihan dan reward setiap arm; itu bukan estimasi hasil eksperimen riil.

## Power dan ukuran sampel
Ukuran sampel bergantung pada alpha, power, variasi, rasio alokasi, dan efek minimum bermakna. Efek kecil membutuhkan sampel lebih besar. Cohen's h untuk proporsi adalah $2\arcsin\sqrt{p_1}-2\arcsin\sqrt{p_2}$. Sumber menggunakan transformasi itu dalam perhitungan power; tambahan memakai pendekatan normal dua proporsi dan membulatkan kebutuhan per kelompok ke atas. Angka yang keluar adalah kebutuhan desain berdasarkan asumsi, bukan bukti efek akan terjadi.

## Interpretasi dan kesimpulan
Bandingkan selisih waktu aktual dengan histogram permutasi dan Welch t-test. Cocokkan ANOVA SciPy dengan tabel statsmodels. Amati penurunan kebutuhan sampel ketika efek minimum diperbesar. Dalam ML/DL, membandingkan model memerlukan rancangan evaluasi konsisten, ukuran efek, dan pertimbangan banyaknya percobaan.
