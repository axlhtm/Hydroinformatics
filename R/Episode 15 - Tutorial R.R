## ANALISA DATA WAKTU DI R
# Sistem waktu yang di set default adalah menggunakan susunan "Tahun-Bulan-Tanggal
waktu <- Sys.Date()                             #Menunjukan waktu pada sistem

# Cara merubah susunan waktu tanggal
waktu2 <- '17-Aug-1945'                         #Jika tulisan '17-Aug-1945' dicek menggunakan class() maka akan terdeteksi sebagai karakter
waktu2 <- as.Date(waktu2, format='%d-%b-%Y')    #Merubah tulisan tersebut menjadi format tanggal, '%d' adalah tanggal, '%b' adalah bulan angka, dan '%Y' adalah tahun angka penuh
 
# Cara merubah susunan waktu jam
as.POSIXct('10:15:40', format='%H:%M:%S')       #Simbol '%H' merujuk pada jam, '%M' pada menit, dan '%S' adalah detik
as.POSIXct('Nov,10,1976 00:01:50', format='%b,%d,%Y %H:%M:%S')

strptime('Nov,10,1976 00:01:50', format='%b, %d, %Y %H:%M:%S')
