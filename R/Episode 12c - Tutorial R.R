######### LATIHAN MANDIRI 

for (a in 1:20){
  if (a==10){
    next
  }else if (a==15){
    break
  }
  print(paste("nilai a saat ini adalah", a))
}

for (b in 1:10){
  if (!b==5){
    next
  }else if (b==8){
    break
  }
  print(paste("Nilai b saat ini adalah", b))
}

f <- 0
while (f<=15){
  print(paste("Aku sayang fenina =", f, "kali"))
  f=f+1
}
