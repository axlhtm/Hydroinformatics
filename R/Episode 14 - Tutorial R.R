# Belajar Jenis-Jenis Fungsi di R

# seq()            #Menuliskan urutan angka pada 1 sequece
seq(1,20)          #Menuliskan angka 1-20 dalam 1 sequence
seq(1,20,3)        #Menuliskan angka 1-20 dalam 1 sequence dengan longkapan 3 
seq(5, 34.7, 0.76) #Menuliskan angka 5-34.7 dalam q sequence dengan longkapan 0.76

# sort()           #Mengurutkan data numerik dan variabel pada 1 sequence. Bisa diurutkan secara naik ataupun turun. 
nilai.ujian <- c(90,20,70,50,40)        #Contoh data numerik acak pada 1 sequence
sort(nilai.ujian, decreasing=FALSE)     #Mengurutkan komponen data numerik secara naik
sort(nilai.ujian, decreasing=TRUE)      #Mengurutkan komponen data numerik secara turun

ipk.siswa <-c('A','C','B','E','F','b')  #Contoh data variable acak pada 1 sequence
sort(ipk.siswa, decreasing=FALSE)       #Mengurutkan komponen data variabel secara naik
sort(ipk.siswa, decreasing=TRUE)        #Mengurutkan komponen data variabel secara turun

# rev()            #Mengurutkan data numerik dan variable pada 1 sequence mulai dari item paling akhir. 
nilai.ujian <- c(90,20,70,50,40)        #Contoh data numerik acak pada 1 sequence
rev(nilai.ujian)                        #Mengurutkan komponen data numerik mulai dari paling akhir

# str()            #Menunjukan struktur dataset
nilai.ujian <- c(90,20,70,50,40)        #Contoh data numerik acak pada 1 sequence
str(nilai.ujian)                        #Menunjukan struktur data tersebut yang mana merupakan numerik

# append()         #Menambahkan item vector pada vector lainnya
append(ipk.siswa, nilai.ujian)          #Menggabungkan vector ipk.siswa dan nilai ujian

# lapply()         #Mengaplikasikan fungsi kedalam list
a <- function (b){                      #Contoh fungsi
  return(b*2)
}

a(nilai.ujian)                          #Memasukan nilai.ujian kedalam fungsi a
lapply(nilai.ujian, a)                  #Merubah fungsi menjadi list dimana dimasukan nilai.ujian kedalam fungsi a

# sapply()         #Mengaplikasikan fungsi kedalam vector/matriks
hasil <- sapply(nilai.ujian, function(c){c*2})

nilai.rerata <- function(x,y){
  return((x+y)/20)
}
sapply(nilai.ujian, nilai.rerata, y=100) #Memasukan 1 list dalam fungsi yang memiliki 2 parameter. Salah satu parameter harus didefaultkan


# is.XXX()         #Mengecheck jenis data yang terdapat pada suatu komponen
is.vector(nilai.ujian)                  #Mengecheck apakah jenis data nilai.ujian adalah vector. Hasilnya adalah benar (TRUE).
is.data.frame(nilai.ujian)              #Mengecheck apakah jenis data nilai.ujian adalah data frame. Hasilnya adalah salah (FALSE).

is.na()                                 #Mengecheck apakah ada data yang hilang pada data set
is.na(nilai.ujian)                      #Tidak ada data yang hilang, maka semua FALSE
nilai.ujian.baru <- c(0,5,10,NA,15)     #Contoh data yang hilang, ditulis dalam NA
is.na(nilai.ujian.baru)                 #Terdapat data yang hilang, maka tertulis TRUE pada set data ke 4
