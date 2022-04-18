# CARA MENGGUNAKAN DATA FRAME YANG SUDAH ADA
df <- iris
df2 <- mtcars
str(df)
str(df2)
df3 <- state.x77
str(df3)
summary(df3)
summary(df)
summary(df2)

# CARA MEMBUAT DATA FRAME DARI AWAL
cowok <- c('Bambang', 'Joko', 'Budi', 'Anton', 'Koko')
berat <- c(100,50,60,70,86)
golongan <- factor(c('gemuk', 'kurus', 'kurus', 'sedang', 'sedang'))
kelompok <- data.frame(cowok, berat, golongan)
str(kelompok)

# LATIHAN MANDIRI 
# KLASIFIKASI KONTRAKTOR
Nama.Kontraktor <- c('PT. Trikkon Graha Mandiri', 'PT. Tiokindo Electrics Utama',
                     'PT. Cahaya Paras Utama', 'PT. Puspa Graha Utama', 'PT. Cupu Intan Adyapermata')
Sertifikat.Badan.Usaha <- c('Ada', 'Ada', 'Tidak Ada', 'Tidak Ada', 'Ada')
Modal.Dasar <- c(50,100,50,75,175)
Tenaga.Ahli <- c(5,6,7,8,9)
Kualifikasi.Dasar <- c('IPP', 'IPP','IPM', 'IPU', 'IPU')
Klasifikasi.Kontraktor <- c('Besar','Kecil','Sedang','Kecil','Besar')
Klasifikasi.JasaUsaha <- data.frame(Nama.Kontraktor, Sertifikat.Badan.Usaha,
                                    Modal.Dasar, Tenaga.Ahli, Klasifikasi.Kontraktor,Kualifikasi.Dasar)

SLICING DATA KONTRAKTOR
