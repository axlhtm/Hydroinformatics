# CARA MENGGUNAKAN LOGIKA IF, ELSE, ELSE IF

# CARA MENGGUNAKAN LOGIKA IF
if (kondisi I){
  perintah yang diinginkan apabila kondisi I terpenuhi
  }

(Contoh 1 Kondisi dengan 1 Perintah)
x <- 100
if (x>50){
  print('nilai x lebih besar dari 50')
  }


# CARA MENGGUNAKAN LOGIKA ELSE 
if (kondisi I){
  perintah yang diinginkan apabila kondisi I terpenuhi
} else {
  perintah lainnya apabila kondisi I tidak terpenuhi
}

(Contoh 1 Kondisi dengan 2 Perintah)
y <- 200
if (y<100){
  print('nilai y lebih kecil daripada 100')
} else {
  print ('nilai y lebih besar daripada 100')
}


# CARA MENGGUNAKAN LOGIKA ELSE IF 
if (kondisi I){
  perintah yang diinginkan apabila kondisi I terpenuhi
} else if (kondisi II){
  perintah yang diiinginkan apabila kondisi II terpenuhi
} else if (kondisi III){
  perintah yang diinginkan apabila kondisi III terpenuhi
} else if (kondisi IV) {
  perintah yang diinginkan apabila kondisi IV terpenuhi
} else {
  perintah yang diinginkan apabila semua kondisi tidak terpenuhi
}

(Contoh kondisi dan perintah bertingkat)
z <- 300
if (z<50){
  print('nilai z lebih kecil daripada 50')
} else if (z<100){
  print('nilai z lebih kecil daripada 100')
} else if (z<150){
  print('nilai z lebih kecil daripada 150')
} else if (z<200){
  print('nilai z lebih kecil daripada 200')
} else if (z<250){
  print ('nilai z lebih kecil daripada 250') 
} else {
  print ('nilai z lebih besar atau sama daripada 300')
}

a <- 400
if (a>0 & a<10){
  print('nilai a adalah satuan')
} else if (a>9 & a<100){
  print('nilai a adalah puluhan')
} else if (a>99 & a<1000){
  print('nilai ada adalah ratusan')
} else {
  print('nilai a tidak dapat didenisikan')
}

(Contoh kondisi dan perintah bertingkat menggunakan negasi)
b <- 500
if (b>600){
  print('maka nilai b adalah genap')
} else if (b!=50){
  print('nilai b bukan sebesar 50')
} else {
  print('nilai b tidak dapat didefiniskan')
}