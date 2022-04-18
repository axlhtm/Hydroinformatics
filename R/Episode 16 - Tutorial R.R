### MANIPULASI DATA DENGAN (Dplyr) di R

## INSTAL LIBRARY (Dplyr)
library(dplyr)                    #Menginstall fungsi dplyr     
library(nycflights13)             #Contoh data penerbangan NYC di tahun 2013 

## MENYIAPKAN DATASET 
dataku <- flights
dataku <- cbind(nomor = rownames(dataku), dataku)
summary(dataku)

## MEMFILTER DATA DENGAN PERINTAH FILTER
baru <- filter(dataku, day==15, month==8, dest=='IND')                     #Memfiler data dengan ketentuan sesuai dengan nama kolom dengan menggunakan perintah "filter"
baru2 <- dataku[dataku$day==15 & dataku$month==8 & dataku$dest=='IND',]    #Memfiler data dengan ketentuan sesuai dengan nama kolom secara manual

axel <- filter(dataku, !day==15, month>=8, dest=='IND')                    #Menggunakan fitur filter
axel2 <- dataku[!dataku$day==15 & dataku$month>=8 & dataku$dest=='IND',]   #Menggunakan cara manual

coba <- filter(dataku, day==15, month==8, dep_time<=2000)                  #Menggunakan fitur filter
coba2<- dataku[dataku$day==15 & dataku$month==8 & dataku$dep_time<=2000,]  #Menggunakan cara manual

# Pada definisi coba2 memiliki jumlah baris yang lebih banyak, karena mengikutsertakan nilai NA atau nilai yang hilang pada dataset tersebut. Untuk menghilangkan data NA maka diperlukan perintah "na.omit" sebelum penulisan definisi

coba3<- na.omit(dataku[dataku$day==15 & dataku$month==8 & dataku$dep_time<=2000,])  #Menggunakan cara manual tanpa memasukan data NA

# Jumlah data pada coba3 yang dihitung secara manual masih berbeda dengan jumlah data pada coba yang dihitung secara otomatis
## CARA MENGETAHUI KEGANJILAN DATA
for (i in 1:nrow(coba3)){
  hitung=0
  if (coba$nomor[i] != coba3$nomor[i]){
    print(coba$nomor[i])
    hitung = hitung+1
    break 
  }
}
# Dari filter tersebut diketahui bahwa data pada coba memiliki nilai NA di baris 293378, sedangkan pada coba3 diperintahkan untuk tidak mengikutsertakan nilai NA pada setiap kolomnya,
coba4<-na.omit(filter(dataku, day==15, month==8, dep_time<=2000))         #Menggunakan fitur filter, dengan menghiraukan data NA


## CARA MENGGUNAKAN SLICE() UNTUK MEMOTONG DATA SET
Potong <- slice(dataku, 2:10)                                             #Memotong data dengan fitur slice("dataset", range baris)

## CARA MENGGUNAKAN ARRANGE() UNTUK MENGURUTKAN DATA SET BERDASARKAN 1 PARAMETER ATAU LEBIH SECARA PRIORITAS
dataku2 <- dataku
dataku2 <- arrange(dataku2, year, month, flight)                          #Mengurutkan dataset berdasarkan paramter secara berurutan, year, month, dan flight

## CARA MENGGUNAKAN SELECT() UNTUK MEMILIH DATA SPESIFIK PADA DATA SET
pilih <- select(dataku, nomor, carrier, arr_time)                         #Membuat slicing dataset dengan kolom yang berisikan nomor, carrier, dan arr_time

## MERUBAH NAMA KOLOM DENGAN RENAME()
ganti <- rename(dataku, indeks = nomor)                                   #Merubah nama kolom dengan fungsi rename("nama dataset", "nama kolom baru = nama kolom lama")

## MEMILIH ISI DATA YANG UNIK DENGAN PERINTAH DISTINCT()
unik <- distinct(select(dataku, carrier))                                 #Memilih data yang unik, atau membuat list atas variabel yang berbeda pada dataset

## MENAMBAH KOLOM BARU YANG MERUPAKAN HASIL ALGORITMA BEBERAPA KOLON DENGAN PERINTAH MUTATE()
tambah <- mutate(dataku, kol_baru = arr_delay - dep_delay)             
tambah <- select(tambah, nomor, kol_baru, arr_delay, dep_delay)

## MENAMBAH KOLOM BARU SEPERTI MUTATE() TAPI TIDAK MENAMPILKAN KOLOM LAINNYA DENGAN PERINTAH TRANSMUTE()
khusus <- transmute(dataku, kol_baru = arr_delay - dep_delay, arr_delay, dep_delay)

## MERINGKAS KOLOM DENGAN SUMMARISE()
summarise(dataku, rataan_air_time = mean(air_time, na.rm=TRUE))           #Menghitung ringkasan atas perintah yang dimasukan, na.rm=TRUE, memerintahkan untuk mengindahkan nilai NA pada data tersebut


## MELAKUKAN SAMPLIT DARI DATA SET SECARA ASAK DENGAN SAMPLE_N() DAN SAMPLE_FRAC()
sample_n(dataku, 10)                                                      #Mengambil data sample sebanyak 10 buah dari dataset
sample_frac(dataku, 0,1)                                                  #Mengambil data sample sebanyak 10 persen dari dataset
