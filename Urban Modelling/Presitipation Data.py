# HOW TO KNOW MAXIMUM DAILY PRECITIPATION RATE 

## IMPORT CSV FILE WITHOUT PYTHON LIBARIRES 
with open("G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Urban Modelling/AHUH1.csv","r") as fin :
    text = fin.read() 
lines = text.split('\n')

# LOOP THROUGHT ELEMETN IN THE FIRST LINE 
rain = []

for val in lines[1:]:
    out = val.split(",")
    if len(out) >=2:
        if out[1] =="NA":
            out[1]=0
        v = float(out[1])    
    rain.append(v)

# By here, I have an array (list) of numbers.
# I need to sum each consecutive 24 numbers 
nb = int(len(rain)/24)                                                         # Numbers of Block (24 Hours Cycle)
dailyrain = []                                                                 # Empty array for daily rain
                                                               
for day in range(nb) :                                                         # Loop for grouping 24 hours data in 1 block 
    sum = 0.0
    for hour in range(24): 
        sum = sum + rain [day * 24 + hour]
    dailyrain.append(sum)

max_dr = max(dailyrain)                                                        # Maximum Daily Presitipation
print(max_dr)