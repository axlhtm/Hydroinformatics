## LATIHAN MANDIRI FUNGSI R

# Batang emas 6 kg
# Barang emas 1 kg

# Batang ini digunakan untuk menghitung emas

# Buatlah fungsi untuk menghitung emas dengan meminimasi jumlah batang emas:
# 1. Mencetak berapa banyak batang 6 kg yang dipakai
# 2. Mencetak berapa banyak batang 1 kg yang dipakai
# 3. Mencetak berapa banyak total batang emas yang dipakai
# 4. Return total batang emas yang dipakai ke variabel

# Misal 16 kg = 2 batang 6 kg dan 4 batang 1 kg, total 6 batang

x <- 6
y <- 1

jumlah.batang <- function(a,b,c){
  if (b*x+c*y==a){
  return(paste(a,'kg emas dapat dibuat dengan menggunakan', b, 'batang 6 kg dan', c, 'batang 1 kg, dengan total sebanyak', b+c, 'batang'))
  }else if (!b*x+c*y==a){
  return(paste('Jumlah batang kurang atau lebih dari yang diperlukan'))
  }
}
  
jumlah.emas <- function(num1){
  sisa.bagi.y <- num1%%x
  print(paste('Jumlah batang emas dengan berat',y,'kg adalah sebanyak',sisa.bagi.y,'batang'))
  sisa.bagi.x <- (num1-sisa.bagi.y)/x
  return(paste('Jumlah batang emas dengan berat',x,'kg adalah sebanyak',sisa.bagi.x,'batang'))
}

jumlah.emas(16)
jumlah.emas(20)
jumlah.emas(24)

################################################################################
# Perusahaan PDAM di Kota Delft digunakan untuk pemerintah, masyarakat, dan industri. Dengan kententuan sebagai berikut: 
# 1. Populasi Masyarakat (M) adalah yang paling besar namun membayar tarif air paling kecil.
# 2. Populasi Pemerintah (P) adalah menengah dengan tarif air rerata.
# 3. Populasi Industri (I) adalah yang paling kecil namun membayar tarif air paling besar.

# Kalkulasi Tarif air yang dikenakan pada tiap instansi
m0 <- 1000                                         #Tarif utama untuk masyarakat
m1 <- 1200                                         #Tarif tambahan untuk masyarakat

p0 <- 800                                          #Tarif utama untuk pemerintah
p1 <- 1000                                         #Tarif tambahan untuk pemerintah

i0 <- 1200                                         #Tarif utama untuk industri
i1 <- 1400                                         #Tarif tambahan untuk industri 


# Keubutuhan debit iar tiap departemen
q.m <- 7500                                        #Permintaan debit air dari masyarakat
q.p <- 2500                                        #Permintaan debit air dari pemerintah
q.i <- 10000                                       #Permintaan debit air dari industri
q.sum <- q.m + q.p + q.i

# Tingkat efisiensi pipa
supply <- 20000
eff <- 0.6*supply

#Distribusi debit air
Debit.Air <- function(supply){
 if(supply>=20000){
   
 }
}

a <- 0

# Biaya penggunaan air di tingkat masyarakat
i.m <- function(a){
  debit.tambahan.m <- (a-7500)
  biaya.tambahan.m <- debit.tambahan.m * q.m
  print(paste('Biaya tambahan yang dikenakan pada masyarakat adalah sebesar', biaya.tambahan.m,'rupiah'))
  
  debit.utama.m <- (a-debit.tambahan.m)
  biaya.utama.m <- debit.utama.m * q.m 
  print(paste('Biaya utama yang dikenakan pada masrayakat adalah sebesar', biaya.utama.m,'Rupiah'))
  
  print(paste('Biaya total yang dikenakan pada masyarakat adalah sebesar', biaya.utama.m+biaya.tambahan.m,'Rupiah'))
}

i.m(8000)
