# CARA MENGGUNAKAN LOOP 
# Menulis kata "Hello" sejumlah 5 kali secara manual 
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# Menulis kata "Hello" sejumlah 5 kali secara otomatis menggunakan while loop
i=1
while(i<=5){
  print("Hello")
  i=i+1
}
 
# Menuliskan angka "1-10" dengan menggunakan while loop
a=1
while(a<=10){
  print(a)
  a=a+1
}

# Menuliskan bilangan genap dari 1 sampai dengan 10
b=1
while(b<=10){
  if(b%%2==0){
    print(b)
  }
  b=b+1
}

# Menuliskan bilangan ganjil dari 1 sampai dengan 10
c=0
while(c<=10){
  if(!c%%2==0){
    print(c)
  }
  c=c+1
}

####################################################
# CARA MENGGUNAKAN FOR LOOP
for (i in 1:10){           #pilihan huruf 'i' dan angka pacuan adalah bebas 
  print(i)                 #perintah apapun
}

for(coba in 0:10){
  print(paste('Index sekarang adalah = ', i))
}

for (l in 1:10){           #Mengiterasi l dalam rentang 1 sampai dengan 10
  for (m in 1:l){          #Setiap iterasi l berjalan, menginterasi nilai m
    cat(m)                 #cat itu print tanpa spasi (enter)
  }
  cat("\n")                #cat('\n') bertujuan untuk enter
}

# Mengiterasi variabel
isi <- c(3,6,9,23)
hasil <- 0
for (i in isi){
  hasil <- hasil+i
  print(i)
  print(paste('hasilnya adalah =' , hasil))
}

kotak <- list(isi, mtcars, 89.17)
for (a in kotak){
  print(a)
}

for(i in isi){
  print('cetak')
}

for (i in 1:length(isi)){
  print('cetak')
}

length(mtcars)           #Memperlihatkan jumlah kolom pada suatu data set, mtcars
nrow(mtcars)             #Memperlihatkan jumlah baris pada suatu data set, mtcars
ncol(mtcars)             #Memperlihatkan jumlah kolom pada suatu data set, mtcars

for (i in 1:length(mtcars)){
  print('cetak')
}

for (i in 1:nrow(mtcars)){
  print('cetak')
}
 
for (i in 1:nrow(mtcars)){
  print(i)
}















