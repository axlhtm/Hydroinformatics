#  ============================================================================
#  EXAMPLE - HOW TO EXTRACT FEATURES FROM TIME DOMAIN
#  ============================================================================

#  IMPORT PYTHON LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  LOAD THE AUDIO SIGNAL FILE
'The CSV file contains data from 2 sensors. Sensor A is stored in column A, while sensor B is in column B'
df = pd.read_csv("G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/Sensor Sample/Case1_1000.csv")
signal = df.iloc[:, -2].values # Extract signal from sensor A to array

#  DISPLAY THE AUDIO FILE 
plt.plot(signal)
plt.xlabel("Number of samples")
plt.ylabel("Amplitude")
plt.title("Row vibration signal")

#  SIGNAL FEATURES EXRACTION USING DEF FUNCTION
## Time Domain
def get_mean_acceleration(signal, frame_size, hop_length): # 
    mean = []
    for i in range(0, len(signal), hop_length):
        current_mean = np.sum(signal[i:i+frame_size])/frame_size
        mean.append(current_mean)
    return mean

