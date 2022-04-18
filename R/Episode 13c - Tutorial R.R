################################################################################
# Perusahaan PDAM di Kota Delft digunakan untuk pemerintah, masyarakat, dan industri. Dengan kententuan sebagai berikut: 
# 1. Populasi Masyarakat (M) adalah yang paling besar namun membayar tarif air paling kecil.
# 2. Populasi Pemerintah (P) adalah menengah dengan tarif air rerata.
# 3. Populasi Industri (I) adalah yang paling kecil namun membayar tarif air paling besar.

# Keubutuhan debit iar tiap departemen
q.m <- 7500                                        #Permintaan debit air dari masyarakat
q.p <- 2500                                        #Permintaan debit air dari pemerintah
q.i <- 10000                                       #Permintaan debit air dari industri
q.sum <- q.m + q.p + q.i

# Kalkulasi Tarif air yang dikenakan pada tiap instansi
m0 <- 1000                                         #Tarif utama untuk masyarakat
m1 <- 1200                                         #Tarif tambahan untuk masyarakat

p0 <- 800                                          #Tarif utama untuk pemerintah
p1 <- 1000                                         #Tarif tambahan untuk pemerintah

i0 <- 1200                                         #Tarif utama untuk industri
i1 <- 1400                                         #Tarif tambahan untuk industri 

# Biaya penggunaan air untuk sektor masyarakat 
i.m <- function(d.m){
  if (d.m>=200){
    debit.tambahan.m <- (d.m-200)
    biaya.tambahan.m <- debit.tambahan.m * m1
    print(paste('Biaya tambahan yang dikenakan pada sektor masyarakat adalah sebesar', biaya.tambahan.m,'rupiah'))
  
    debit.utama.m <- (d.m-debit.tambahan.m)
    biaya.utama.m <- debit.utama.m * m0 
    print(paste('Biaya utama yang dikenakan pada sektor masrayakat adalah sebesar', biaya.utama.m,'Rupiah'))
    
    print(paste('Biaya total yang dikenakan pada sektor masyarakat adalah sebesar', biaya.utama.m+biaya.tambahan.m,'Rupiah'))
  } 
  else if (d.m<200){
    biaya.utama.m <- d.m * m0 
    print(paste('Biaya utama yang dikenakan pada sektor masrayakat adalah sebesar', biaya.utama.m,'Rupiah'))
    
    print(paste('Biaya total yang dikenakan pada sektor masyarakat adalah sebesar', biaya.utama.m,'Rupiah'))
  }
}
    
# Biaya penggunaaan air untuk sektor pemerintah
i.p <- function(d.p){
  if (d.p>=180){
    debit.tambahan.p <- (d.p-180)
    biaya.tambahan.p <- debit.tambahan.p * p1
    print(paste('Biaya tambahan yang dikenakan pada sektor pemerintah adalah sebesar', biaya.tambahan.p,'rupiah'))
    
    debit.utama.p <- (d.p-debit.tambahan.p)
    biaya.utama.p <- debit.utama.p * p0 
    print(paste('Biaya utama yang dikenakan pada sektor pemerintah adalah sebesar', biaya.utama.p,'Rupiah'))
    
    print(paste('Biaya total yang dikenakan pada sektor pemerintah adalah sebesar', biaya.utama.p+biaya.tambahan.p,'Rupiah'))
  } 
  else if (d.p<180){
    biaya.utama.p <- d.p * p0 
    print(paste('Biaya utama yang dikenakan pada sektor pemerintah adalah sebesar', biaya.utama.p,'Rupiah'))
    
    print(paste('Biaya total yang dikenakan pada sektor pemerintah adalah sebesar', biaya.utama.p,'Rupiah'))
  }
}

# Biaya penggunaan air untuk sektor industri 
i.i <- function(d.i){
  if (d.i>=220){
    debit.tambahan.i <- (d.i-220)
    biaya.tambahan.i <- debit.tambahan.i * i1
    print(paste('Biaya tambahan yang dikenakan pada sektor industri adalah sebesar', biaya.tambahan.i,'rupiah'))
    
    debit.utama.i <- (d.i-debit.tambahan.i)
    biaya.utama.i <- debit.utama.i * i0 
    print(paste('Biaya utama yang dikenakan pada sektor industri adalah sebesar', biaya.utama.i,'Rupiah'))
    
    print(paste('Biaya total yang dikenakan pada sektor industri adalah sebesar', biaya.utama.i+biaya.tambahan.i,'Rupiah'))
  } 
  else if (d.i<220){
    biaya.utama.i <- d.i * i0 
    print(paste('Biaya utama yang dikenakan pada sektor industri adalah sebesar', biaya.utama.i,'Rupiah'))
    
    print(paste('Biaya total yang dikenakan pada sektor industri adalah sebesar', biaya.utama.i,'Rupiah'))
  }
}

################################################################################
# Perhitungan pembagian debit air 

