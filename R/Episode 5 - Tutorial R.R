matriks.bil <- matrix(bil, nrow = 4)
matriks.bil <- matrix(bil, byrow = T, nrow = 4)

#Saham 
TLKM <- c(3000, 3100, 3050, 3020, 3200)
KLBF <- c(324, 343, 300, 321, 355)

saham <- c(TLKM, KLBF)
saham.matrix <- matrix(saham, byrow = T, nrow=2)

hari <- c('Senin', 'Selasa', 'Rabu', 'Kamis','Jumat')
nama.saham <- c('TLKM','KLBF')

colnames(saham.matrix) <- hari
rownames(saham.matrix) <- nama.saham

BBCA <- c(1501, 1510, 1490, 1520, 1500)
saham.baru <- rbind(saham.matrix, BBCA)

colSums(saham.baru)
rowSums(saham.baru)
rowMeans(saham.baru)
colMeans(saham.baru)

Rataan <- rowMeans(saham.baru)
saham.baru <- cbind(saham.baru, Rataan)
