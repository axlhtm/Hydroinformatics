# RATA-RATA NILAI SISWA DI SMA 10 
Nama.Siswa <- c('Budi', 'Anton', 'Danu', 'Axel')

Nilai.Siswa <- c(Budi, Anton, Danu, Axel)
Budi <- c(80,90,90,70,50)
Anton <- c(70,75,75,80,90)
Danu  <- c(60,70,60,55,70)
Axel <- c(85,90,80,80,90)

Matriks.Nilai <- matrix(Nilai.Siswa, byrow = T, nrow = 4)

Bahan.Ujian <- c('Bab I', 'Bab II', 'Bab III', 'Bab IV', 'Bab V')

colnames(Matriks.Nilai) <- Bahan.Ujian
rownames(Matriks.Nilai) <- Nama.Siswa

NilaiSiswa.Rerata <- rowMeans(Matriks.Nilai)
NilaiUjian.Rerata <- colMeans(Matriks.Nilai)

Matriks.Nilai <- cbind(Matriks.Nilai, NilaiSiswa.Rerata)
Matriks.Nilai <- rbind(Matriks.Nilai, NilaiUjian.Rerata)


#  RATA-RATA NILAI PERGERAKAN SAHAM 
Nama.Emiten <- c('TLKM','BBRI','PKWN','BBCA','SILO')
Harga.Harian <- c('Senin','Selasa','Rabu','Kamis','Jumat')

Emiten.Saham <- c(TLKM,BBRI,PKWN,BBCA,SILO)
TLKM <- c(1500,2000,2500,3000,3500)
BBRI <- c(5000,5500,6000,6500,7000)
PKWN <- c(1000,2000,3000,4000,5000)
BBCA <- c(100,200,300,400,500)
SILO <- c(1200,1500,1800,2100,2400)

Matriks.Saham <- matrix(Emiten.Saham, byrow = T, nrow = 5)

colnames(Matriks.Saham) <- Harga.Harian
rownames(Matriks.Saham) <- Nama.Emiten

Rerata.Saham <- rowMeans(Matriks.Saham)
Matriks.Saham <- cbind(Matriks.Saham, Rerata.Saham)
