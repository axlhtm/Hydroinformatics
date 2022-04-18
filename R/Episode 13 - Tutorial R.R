## BELAJAR MENGGUNAKAN FUNGSI DI R 

coba <- function(){
  print('Ini adalah fungsi coba')
  print('ini adalah baris ke 2')
}

coba()

fungsi.baru <- function(a='maju'){
  print(paste('Parameter yang saya masukan adalah =', a))
}

fungsi.baru('OKE')
fungsi.baru(12)

fungsi.baru2 <- function(a){
  print(paste('Parameter yang saya masukan adalah ='))
}

fungsi.baru()


jumlah <- function(a,b){
  return(a+b)              #Gunakan return jika kita butuh nilainya nanti, setelah command return maka semua perintah dibawahnya akan diabaikan
  print('Coba cetak garis ini')
}

jumlah(10,20)
isi <- jumlah(10,20)
isi

baru <- function(num){
  if (num<10){
    print('A')
    return(T)
    print('coba 1')
  } else {
    print('b')
    return (F)
    print('coba 2')
  }
}

keranjang <- baru(2)

lagi <- function(a,b,c){
  print(paste('Saya',a,'adalah seorang ahli data science'))
  print(paste('Perkalian antara' ,b, 'dengan' ,c, '=',b*c))
  return(b*c)
}

lagi('Anton',20,3)
kotak <- lagi('Anton',20,3)


## PERBEDAAN PRINT DAN RETURN
hebat <- function(a,b){
  return(a+b)
  return(a*b)                #Apabila terdapat 2 return secara bersamaan, maka yang digunakan adalah return yang pertama
}

hebat2 <- function(a,b){
  print(a+b)
  print(a*b)                 #Apabila terdapat 2 print secara bersamaan, maka yang digunakan adalah print yang terakhir
}

balok1 <- hebat(2,3)
balok2 <- hebat2(2,3)
