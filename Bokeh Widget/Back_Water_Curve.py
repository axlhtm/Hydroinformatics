from bokeh.plotting import curdoc, figure
from bokeh.layouts import row, column
from bokeh.io import output_file
from bokeh.models import Slider, TextInput, Button, Tabs, Panel, RadioGroup
from bokeh.models.widgets import Slider, Select, Button, Div

import numpy as np
import pandas as pd

##############################
# BACK WATER CURVE
##############################

# LOGO 
logo_source = "<img src='https://www.un-ihe.org/sites/default/files/ihe-delft_logo_black_cyan_reduced_version.png' width=auto height=100>"
logo        = Div(text=logo_source)

#  FRONT END 
## SET THE HEADER 
image_BWC_source = "<img src='https://english.rvo.nl/sites/default/files/2021/03/Deltapark%20Neeltje%20Jans%20header%20themapagina%20water.jpg' width=1390 height=400>"
image_BWC        = Div(text=image_BWC_source)
app_title_BWC    = Div(text="<b> BACK WATER CURVE </b>")
description_BWC  = Div(text="This application helps <b>calculating and analyzing the water profiles for the back water curve phenomenon.</b> All errors and the graphical result will be shown after the calculation is finished.")

## SET THE CHANNEL GEOMETRIC PARAMETER ##### 
sub_div_title_1_BWC  = Div(text="<b>CHANNEL GEOMETRIC PARAMETER")
channel_length_BWC   = TextInput(title="Channel Lentgh (meter):", value="6000")
channel_width_BWC    = TextInput(title="Channel Width (meter):", value="50")
channel_sloope_BWC   = TextInput(title="Channel Sloope :", value="0.001")

## SET THE ROUGHNESS CALCULATION METHOD #####
sub_div_title_2_BWC  = Div(text="<b>HYDRAULICS PARAMETER")
roughness_method_BWC = Select(title="Roughness Coefficient Method:", value="Chezy", options=["Chezy"])
roughness_chz_BWC    = Select(title="Chezy Roughness Coefficient Value:", value="29", options=["29", "37", "42", "49", "73", "100"], visible=True)
discharge_BWC        = TextInput(title="Discharge (meter cubes / seconds):", value="50")
water_depth_BWC      = TextInput(title="Water Depth (meter):", value="3")

## SET THE NUMERICAL METHOD ##### 
sub_div_title_3_BWC  = Div(text="<b>NUMERICAL SOLUTIONS METHOD")
numerical_BWC        = Select(title="Numerical Method:", value="Explicit", options=["Explicit", "Implicit"])
space_step_BWC       = Slider(start=0, end=100, value=10, step=10, title="Space Step (dx) (meter)")
error_val_BWC        = Slider(start=0, end=1, value=0.5, step=.01, title="Error Tollerance")
iteration_num_BWC    = Slider(start=0, end=20, value=5, step=1, title="Maximum Iteration")

## SET THE OUTPUT BUTTON #####
sub_div_title_4  = Div(text="<b>===========================================================================================</b>")
BWC_run_button   = Button(label="Analyze Data", button_type="default")
BWC_clear_button = Button(label="Reset Input")

## SET THE FIGURE AND LAYOUT #####
graph_BWC        = figure(plot_width=700, plot_height=500, title="GRAPHICAL INTERPRETATION")
BWC_layout_left  = column(app_title_BWC, description_BWC, sub_div_title_1_BWC, channel_length_BWC, channel_width_BWC, channel_sloope_BWC, row(column(sub_div_title_2_BWC,roughness_method_BWC, roughness_chz_BWC, discharge_BWC,water_depth_BWC),column(sub_div_title_3_BWC,numerical_BWC,space_step_BWC,error_val_BWC,iteration_num_BWC )))
BWC_layout_right = column(graph_BWC,row(column(BWC_run_button),column(BWC_clear_button)))
BWC_layout       = column(logo, image_BWC,row(BWC_layout_left, BWC_layout_right)) 

# BACK END 
hd_BWC = float(water_depth_BWC.value)
Hw_Exp_BWC = [hd_BWC] # Water height using explicit approach (m)
Hw_Imp_BWC = [hd_BWC] # Water height using implicit approach (m)

def compute_BWC() : 
    if numerical_BWC.value == "Explicit" : 
    #def explicit() : # Explicit calculation method 
        graph_BWC.renderers = []
        b_BWC  = float(channel_width_BWC.value)  
        L_BWC  = float(channel_length_BWC.value)
        S0_BWC = float(channel_sloope_BWC.value) 
        C_BWC  = float(roughness_chz_BWC.value) 
        Q_BWC  = float(discharge_BWC.value)
        hd_BWC = float(water_depth_BWC.value)
        dx_BWC = float(space_step_BWC.value)

        ##### Set the Numerical Parameter #####
        maxcom_BWC = int (L_BWC/dx_BWC) + 1 
        x1_BWC     = [0 ] # Distance iteration
        Hw_Exp_BWC = [hd_BWC] # Water height using explicit approach (m)
        Hg_Exp_BWC = [0 ] # Ground height (m)
        Wl_Exp_BWC = [hd_BWC] # Water level using explicit approach (m) 

        for i in range (1,maxcom_BWC):
            x1_BWC.append     (x1_BWC[i-1] + dx_BWC)
            Hg_Exp_BWC.append (i * dx_BWC * S0_BWC)
            Hw_Exp_BWC.append (Hw_Exp_BWC[i-1] + dx_BWC * (((Q_BWC**2 / (C_BWC**2 * Hw_Exp_BWC[i-1]**3 * b_BWC**2))-S0_BWC)))
            Wl_Exp_BWC.append (Hw_Exp_BWC[i] + Hg_Exp_BWC[i])

        graph_BWC.varea(x=x1_BWC, y1=Hg_Exp_BWC, y2=Wl_Exp_BWC)
        
    else : 
    #def implicit() : # Implicit calculation method
        graph_BWC.renderers = []
        b_BWC  = float(channel_width_BWC.value)  
        L_BWC  = float(channel_length_BWC.value)
        S0_BWC = float(channel_sloope_BWC.value) 
        C_BWC  = float(roughness_chz_BWC.value) 
        Q_BWC  = float(discharge_BWC.value)
        hd_BWC = float(water_depth_BWC.value)
        dx_BWC = float(space_step_BWC.value)
        er_BWC = float(error_val_BWC.value)
        MI_BWC = float(iteration_num_BWC.value)

        ##### Set the Numerical Parameter #####
        maxcom_BWC = int (L_BWC/dx_BWC) + 1
        x2_BWC     = [0 ] # Distance iteration 
        Hw_Imp_BWC = [hd_BWC] # Water height using implicit approach (m)
        Hg_Imp_BWC = [0 ] # Ground height (m)
        Wl_Imp_BWC = [hd_BWC] # Water level using implicit approach (m)
        A_BWC      = Q_BWC**2/(C_BWC**2*b_BWC**2) 

        for i in range(1,maxcom_BWC):
            htriR = Hw_Imp_BWC[i-1] #m
            x2_BWC.append(i*dx_BWC)
            Hg_Imp_BWC.append(S0_BWC * i * dx_BWC)
            j_BWC = 0
            er_BWC = 10

            while er_BWC > 0.01:
                if j_BWC > MI_BWC:
                    break
                else:
                    RHS   = A_BWC / htriR ** 3 - S0_BWC
                    htril = dx_BWC * RHS + Hw_Imp_BWC[i-1]
                    er_BWC = abs(htril-htriR)
                    htriR = htril
                    j_BWC += 1

            Hw_Imp_BWC.append(htril)
            Wl_Imp_BWC.append(Hw_Imp_BWC[i]+Hg_Imp_BWC[i])
        #return(x2,Hw_Imp,Hg_Imp,Wl_Imp)

        graph_BWC.varea(x=x2_BWC, y1=Hg_Imp_BWC, y2=Wl_Imp_BWC)
    
def clear_output_BWC() : 
    graph_BWC.renderers = []


## SET THE CALCULATION METHOD
BWC_run_button.on_click(compute_BWC)
BWC_clear_button.on_click(clear_output_BWC)