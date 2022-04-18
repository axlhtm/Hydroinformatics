## PENGGUNAAN BOOLEAN TRUE & FALSE
# AND (dan) --> & --> hanya TRUE jika semua statement adalah TRUE
x <- 100
x<200 & x>50 #TRUE
x<200 & x>120 #FALSE
x<200 & x>50 & x>120 #FALSE
x<200 & x>50 & x<300 #TRUE

# OR (atau) --> | --> hanya TRUE jika salah satu statement adalah TRUE
y <- 200
y<300 | y<150 #TRUE
y>300 | y<150 #FALSE
y<300 | y<150 | y==25 #TRUE
y>300 | y<150 | y==25 #FALSE

# NOT (tidak/negasi) --> !
TRUE #Benar
!TRUE #Pernyataan terbalik
!(x==100) #FALSE karena pernyataan tebalik
!(x==20) #TRUE karena pernyataan terbalik
!!(y==200) #TRUE karena pernyataan terbaliknya ada 2. Negatif * Negatif.
!!!(y==200) # FALSE karena pernyataan terbalik ada 3. Negatif * Negatif * Negatif.

## PENGGUNAAN BOOLEAN DALAM DATA FRAME
df <- iris
View(df)
df[df$Sepal.Width>3.1,] #Menampilkan data df yang memiliki nilai Sepal Width lebih dari 3.1
df[df$Sepal.Width==3.1,] #Menampilkan data df yang memiliki nilai Sepal Width sama dengan 3.1
df[df$Sepal.Width==3.1, 'Species'] #Menampilkan data df yang memiliki nilai Sepal Width sama dengan 3.1 pada kolom ke 5 atau kolom Species
df[df$Sepal.Width==3.1 & df$Sepal.Length>6, ] #Menampilkan data df yang memiliki nilai Sepal Width sama dengan 3.1 dan memiliki nilai Sepal Length lebih dari 6
df[df$Sepal.Width==3.1 | df$Sepal.Length>6, ] #Menampilkan data df yang memiliki nilai Sepal Width sama dengan 3.1 atau memiliki nilai Sepal Lengeth lebih dari 6
df[df$Sepal.Width!=3.1,] #Menampilkan data df yang tidak memiliki nilai Sepal Width sebesar 3.1
