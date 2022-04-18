 bil <- matrix(1:25, byrow=T, nrow=5)
 bil
 bil+bil
 bil*bil
 bil%*%bil
 1/bil
2/bil 
bil^2

# Slicing and Indexing
# bil[baris, kolom]
bil[1, ]
bil[3, ] 
bil[5, ]
bil[ ,3]
bil[4:5,]
bil[c(2,4),]
bil[c(1,3,4),]
bil[c(1,3,4),c(2,4,5)]
bil[2:5,1:3]
