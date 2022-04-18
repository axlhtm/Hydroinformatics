# CARA MENGGUNAKAN WHILE LOOP
a <- 0 

while (a<=10){             # Harus ada iterator atau batasan dari kondisi
  print(a)
  a <- a+1                 # a+1 adalah batasan dari kondisi tersebut
}

# CARA MENGGUNAKAN BREAK 
b <- 0 

while(b<=10){
  print(paste('Nilai b saat ini adalah =' ,b))
  if (b==7){
    break
  }
  b=b+1
}

# CARA MENGGUNAKAN NEXT
for (p in 1:10){
  if (p == 4){
    next                   #Apabila p == 4 maka tidak di print dan dilajutkan ke iterasi selanjutnya
}else if (p==8){
    break                  #Apabila p == 8 maka siklus iterasi berhenti
}
print(p)
}
  