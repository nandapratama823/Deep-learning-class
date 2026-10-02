# Ringkasan dan pendalaman teori Bab 2

Bab ini menjelaskan bagaimana statistik berubah ketika sampel berubah. Distribusi data individual, distribusi sampling statistik, dan distribusi model teoretis adalah objek berbeda. Perbedaan ini mendasari standard error, confidence interval, dan penilaian ketidakpastian.

## Populasi, sampling, dan bias
Populasi adalah seluruh unit sasaran, sedangkan sampel bagian yang diamati. Parameter seperti mu tetap dalam pendekatan frequentist; statistik seperti mean sampel berubah antar sampel. Random sampling memberi mekanisme peluang pada pemilihan unit. Dengan pengembalian, satu unit dapat terpilih ulang; tanpa pengembalian tidak. Stratified sampling menjaga representasi subkelompok; cluster sampling mengambil kelompok dan membutuhkan perhatian terhadap dependensi dalam kelompok.

Bias adalah kesalahan sistematis. Sampel besar mengurangi variasi sampling tetapi tidak menyembuhkan selection bias, nonresponse, atau cakupan populasi yang buruk. Random selection terkait representativitas; random assignment pada eksperimen terkait pembandingan perlakuan. Selection bias juga muncul ketika hanya melaporkan pola paling menarik setelah mencoba banyak kandidat. Regression to the mean berarti nilai yang ekstrem akibat campuran sinyal dan noise cenderung kurang ekstrem pada pengukuran ulang, tanpa perlu efek perlakuan.

## Distribusi sampling, CLT, dan standard error
Distribusi sampling menggambarkan suatu statistik pada pengulangan sampling dengan ukuran serta mekanisme yang sama. Simulasi pendapatan membandingkan observasi individual dengan rata-rata sampel ukuran 5 dan 20. Distribusi rata-rata biasanya lebih terkonsentrasi.

Untuk pengamatan identik dan independen dengan varians terbatas, central limit theorem menyatakan bahwa rata-rata yang distandardisasi mendekati normal saat n besar. Ini tidak menyatakan data mentah menjadi normal. Standard error mean dapat diestimasi dengan $SE(\bar{x})\approx s/\sqrt n$. Memperbesar n empat kali kira-kira membagi SE menjadi dua. Data temporal atau berkelompok membutuhkan penyesuaian; rumus independensi dapat terlalu optimistis.

## Bootstrap
Bootstrap mengambil sampel ulang berukuran n dengan pengembalian dari data, lalu menghitung statistik pada setiap replikasi. Simpangan baku statistik bootstrap mengestimasi SE. Rata-rata bootstrap dikurangi statistik awal mengestimasi bias bootstrap. Pada contoh, statistiknya median pendapatan, bukan hanya mean. Menambah replikasi mengurangi noise Monte Carlo, bukan menciptakan informasi populasi baru.

Bootstrap adalah jenis resampling; permutation test mengacak label di bawah H0 dan menjawab pertanyaan berbeda. Bootstrap tidak memperbaiki sampel yang tidak representatif. Dependensi temporal dapat membutuhkan block bootstrap. Untuk sampel kecil atau statistik ekstrem, cakupan interval persentil dapat kurang baik.

## Confidence interval
Interval bootstrap persentil 90% memakai kuantil 0.05 dan 0.95; interval 95% memakai 0.025 dan 0.975. Interval 95% biasanya lebih lebar. Makna frequentist 95% adalah prosedur mencakup parameter sebenarnya pada sekitar 95% pengulangan sampling sesuai asumsi. Bukan berarti 95% observasi berada di interval, dan bukan probabilitas frequentist parameter tetap berada dalam satu interval yang sudah dihitung. Prediction interval untuk observasi baru biasanya lebih lebar karena memasukkan variasi individual.

## Normal, QQ-plot, dan ekor panjang
Distribusi normal simetris dengan parameter mean mu dan skala sigma. Standardisasi $z=(x-\mu)/\sigma$ menghasilkan normal standar jika x normal. QQ-plot membandingkan kuantil data dengan acuan. Kedekatan pada garis lurus mendukung kesesuaian bentuk; slope tidak harus satu bila data tidak memiliki skala standar. Penyimpangan ekor menunjukkan frekuensi ekstrem berbeda dari acuan.

Contoh NFLX resmi dipertahankan sebagai reproduksi transformasi. `sp500_data` berisi perubahan harga; menyaring nilai positif kemudian mengambil selisih log tidak boleh diklaim sebagai return log dari seri harga lengkap. Diagram itu menggambarkan hasil transformasi tersebut. Tambahan notebook menampilkan QQ-plot perubahan asli dengan garis fit. Distribusi berekor panjang membutuhkan perhatian ketika mengestimasi mean dan memakai asumsi normal.

## Student t, chi-square, dan F
Distribusi t simetris dengan ekor lebih berat daripada normal. Pada data normal independen dengan sigma tidak diketahui, $(\bar{x}-\mu)/(s/\sqrt n)$ mengikuti t dengan n-1 derajat bebas. t mendekati normal ketika derajat bebas besar.

Chi-square dengan k derajat bebas adalah jumlah kuadrat k normal standar independen. Distribusi ini nonnegatif dan digunakan dalam inferensi varians serta tabel kontingensi. F adalah rasio dua chi-square independen yang dibagi derajat bebas masing-masing: $F=(U/d_1)/(V/d_2)$. F mendasari ANOVA dan pembandingan model tertentu. Pemilihan distribusi harus mengikuti statistik uji dan asumsi, bukan sekadar kemiripan histogram.

## Binomial dan keluarga kejadian
Binomial menghitung sukses dari n percobaan independen dengan peluang p tetap: $P(X=k)={n\choose k}p^k(1-p)^{n-k}$, mean np, varians np(1-p). PMF memberi peluang tepat k; CDF peluang paling banyak k.

Poisson memodelkan hitungan pada interval dengan laju konstan: $P(X=k)=e^{-\lambda}\lambda^k/k!$, mean dan varians lambda. Varians jauh lebih besar dapat menunjukkan overdispersion. Pada proses Poisson, waktu antar kejadian mengikuti eksponensial dengan mean $1/\lambda$; `scale=5` berarti mean lima satuan waktu, bukan laju lima. Hazard eksponensial konstan dan bersifat memoryless.

Weibull memiliki survival $S(t)=\exp[-(t/\eta)^k]$. Shape k<1 memberi hazard menurun, k=1 eksponensial, k>1 hazard meningkat. Laju kegagalan membutuhkan exposure/waktu observasi, bukan hitungan mentah saja; censoring perlu dipertimbangkan dalam data survival.

## Interpretasi reproduksi dan kesimpulan
Bandingkan lebar distribusi mean ukuran 5 dan 20, SE bootstrap median, serta interval 90% dan 95%. Seed membuat hasil simulasi dapat diulang tetapi tidak mengubah validitas asumsi. Dalam ML/DL, konsep ini membantu memisahkan variasi akibat split data dari perbaikan model yang konsisten.
