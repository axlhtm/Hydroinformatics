## LATIHAN MANDIRI 
# Gunakan conditionals (if, else, else if) untuk mengurutkan 3 angka dibawah ini mulai dari yang paling kecil ke yang paling besar 

bil <- c(200,100,10)
bil[1]
bil[2]
bil[3]

if (bil[1] < bil[2]){
  A <- bil[1]
  B <- bil[2]
} else{
  A <- bil[2]
  B <- bil[1]
}

if (bil[3] < A){
  C <- B
  B <- A
  A <- bil [3]
} else if(bil[3] > B){
  C <- bil[3]
}

bil.baru <- c(A,B,C)
