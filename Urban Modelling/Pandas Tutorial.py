# IMPORT PYTHON LIBRARIES
import pandas as pd 

# IMPORT SENSORS EXCEL FILES AS DATAFRAME
## IMPORT FLOW METERS FILE
xl_fm_apl  = pd.ExcelFile('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Flow Meter/Apollo_NationalaVeche.xls')
fm_apl     = xl_fm_apl.parse('Dataset 1')                                       # Flow meters in Apollo
xl_fm_rn1  = pd.ExcelFile('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Flow Meter/RaduNegru1_Praporgescu.xlsx')
fm_rn1     = xl_fm_rn1.parse('Dataset 1')                                       # Flow meters in Radu Negru 1
xl_fm_rn2  = pd.ExcelFile('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Flow Meter/RaduNegru2_Milcov.xlsx')
fm_rn2     = xl_fm_rn2.parse('Dataset 1')                                       # Flow meters in Radu Negru 2
## IMPORT NOISE SENSORS FILE
xl_ns      = pd.ExcelFile('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Noise Sensors/noise_data.xlsx')
ns_all     = xl_ns.parse('noise_data')                                          # Noise sensors along the network
## IMPORT PRESSURE SENSORS FILE 
xl_ps_pt1  = pd.ExcelFile('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Pressure Sensors/PT1_Buzaului_data.xlsx')
ps_pt1     = xl_ps_pt1.parse('Dataset 1')                                       # Pressure sensors in the Apartment Area Point 1
xl_ps_pt2  = pd.ExcelFile('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Pressure Sensors/PT2_Buzaului_data.xlsx')
ps_pt2     = xl_ps_pt2.parse('Dataset 1')                                       # Pressure sensors in the Apartment Area Point 2
xl_ps_pt3  = pd.ExcelFile('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Pressure Sensors/PT3_Buzaului_data.xlsx')
ps_pt3     = xl_ps_pt3.parse('Dataset 1')                                       # Pressure sensors in the Apartment Area Point 3
xl_ps_pt4  = pd.ExcelFile('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Pressure Sensors/PT4_Buzaului_data.xlsx')
ps_pt4     = xl_ps_pt4.parse('Dataset 1')                                       # Pressure sensors in the Apartment Area Point 4
xl_ps_all  = pd.ExcelFile('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Pressure Sensors/pressure_data_4set.xlsx')
ps_all     = xl_ps_all.parse('Dataset 1')                                       # Pressure sensors in all networks

# DATA PRE-PROCESSING
## FLOW METERS FILE
### SLICING FLOW METERS FILE
fm_apl_aug_jul = fm_apl.set_index('timestamp')['2022-07-01' : '2022-08-31']     # Slicing flow meters in Apollo during period July to August 2022
fm_rn1_aug_jul = fm_rn1.set_index('timestamp')['2022-07-01' : '2022-08-31']     # Slicing flow meters in Radu Negru 1 during period July to August 2022
fm_rn2_aug_jul = fm_rn2.set_index('timestamp')['2022-07-01' : '2022-08-31']     # Slicing flow meters in Radu Negru 2 during period July to August 2022
## NOISE SENSORS FILE
### SLICING NOICE SENSORS FILE
ns_aug_jul = ns_all.set_index('timestamp')['2022-07-01' : '2022-08-31']         # Slicing noise sensors during period July to August 2022
ns_aug_jul_leak = ns_aug_jul.loc[(ns_aug_jul['leak'] == 1)]                     # Slicing noise sensors during period July to August 2022 with leak incident
ns_aug_jul_noleak = ns_aug_jul.loc[(ns_aug_jul['leak'] == 0)]                   # Slicing noise sensors during period July to August 2022 with no leak incident
## PRESSURE SENSORS FILE 
### SLICING PRESSURE SENSORS FILE
ps_pt1_aug_jul = ps_pt1.set_index('t_stamp')['2022-07-01' : '2022-08-31']       # Slicing pressure sensors in the Apartment Area point 1 during period July to August 2022
ps_pt2_aug_jul = ps_pt2.set_index('t_stamp')['2022-07-01' : '2022-08-31']       # Slicing pressure sensors in the Apartment Area point 2 during period July to August 2022
ps_pt3_aug_jul = ps_pt3.set_index('t_stamp')['2022-07-01' : '2022-08-31']       # Slicing pressure sensors in the Apartment Area point 3 during period July to August 2022
ps_pt4_aug_jul = ps_pt4.set_index('t_stamp')['2022-07-01' : '2022-08-31']       # Slicing pressure sensors in the Apartment Area point 4 during period July to August 2022
ps_all_aug_jul = ps_all.set_index('timestamp')['2022-07-01' : '2022-08-31']     # Slicing pressure sensors in all netoworks during period July to August 2022

# DATA PLOTTING
ns_aug_jul_leak.plot.line(y='noise')
ns_aug_jul_noleak.plot.line(y='noise')