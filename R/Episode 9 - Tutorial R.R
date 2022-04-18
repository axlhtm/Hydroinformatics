## FILE CSV
# CARA MEMBUKA FILE CSV EKSISTING 
baru <- read.csv('kapal_titanic.csv')
class(baru)
head (baru)
tail(baru)

# CARA MEMBUAT FILE CSV BARU
write.csv(baru, 'data_kapal_titanic_baru.csv')
read.csv('data_kapal_titanic_baru.csv')

################################################

## FILE EXCEL
# Install dan aktifkan 2 library, readxl dan xlsx, melalui tab "PACKAGES"
library(readxl)
library(xlsx)

# CARA MEMBUKA FILE XLSX 
excel_sheets('dataexcel.xlsx')
excelbaru <- read_excel('dataexcel.xlsx', sheet = 'Sheet1')
exceldua <- read_xlsx('dataexcel.xlsx', sheet = 'Sheet1')

# CARA MEMBUAT FILE XLSX BARU
write.xlsx(excelbaru, 'outputexcel.xlsx')
read.xlsx('outputexcel.xlsx', sheetName = 'Sheet1')
