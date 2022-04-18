# Nominal (Makanan & Minuman)
barang <- c('makanan','minuman','minuman','minuman','makanan','makanan','minuman')
kategori.barang <- factor(barang)

# Ordinal (Memiliki tingkat)
rasa <- c('payah', 'maknyus', 'mantab', 'biasa', 'biasa', 'tidak enak', 'payah')
kategori.rasa <- factor(rasa, ordered=T, levels=c('payah', 'tidak enak', 'biasa', 'mantab', 'maknyus'))                                     

# Contoh Ordinal Kualitas
evaluasi <-c('puas', 'tidak puas', 'sangat puas', 'biasa saja', 'biasa saja', 'puas', 'sangat tidak puas', 'puas')
kategori.evaluasi <- factor(evaluasi, ordered=T, levels=c('sangat tidak puas', 'tidak puas', 'biasa saja', 'puas', 'sangat puas'))
