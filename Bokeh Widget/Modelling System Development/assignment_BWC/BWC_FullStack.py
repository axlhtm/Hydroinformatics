from bokeh.plotting import curdoc, figure
from bokeh.layouts import row, column
from bokeh.io import output_file
from bokeh.models import Slider, TextInput, Button
from bokeh.models.widgets import RadioButtonGroup, Slider, Select, Button, Div, PreText

import numpy as np
import pandas as pd


##############################
# BACK WATER CURVE 
##############################

#  FRONT END
##### SET THE HEADER #####
main_menu        = RadioButtonGroup(labels=["Back Water Curve", "Sugawara Tank", "Free Flow Equations"], active=0)
app_title        = Div(text="<b> BACK WATER CURVE </b>")
description      = Div(text="This application helps <b>calculating and analyzing the water profiles for the back water curve phenomenon.</b> All errors and the graphical result will be shown after the calculation is finished.")

##### SET THE CHANNEL GEOMETRIC PARAMETER ##### 
sub_div_title_1  = Div(text="<b>CHANNEL GEOMETRIC PARAMETER")
channel_length   = TextInput(title="Channel Lentgh (meter):", value="6000")
channel_width    = TextInput(title="Channel Width (meter):", value="50")
channel_sloope   = TextInput(title="Channel Sloope :", value="0.001")

##### SET THE ROUGHNESS CALCULATION METHOD #####
sub_div_title_2  = Div(text="<b>HYDRAULICS PARAMETER")
roughness_method = Select(title="Roughness Coefficient Method:", value="Chezy", options=["Chezy"])
roughness_chz    = Select(title="Chezy Roughness Coefficient Value:", value="29", options=["29", "37", "42", "49", "73", "100"], visible=True)
discharge        = TextInput(title="Discharge (meter cubes / seconds):", value="50")
water_depth      = TextInput(title="Water Depth (meter):", value="3")

##### SET THE NUMERICAL METHOD ##### 
sub_div_title_3  = Div(text="<b>NUMERICAL SOLUTIONS METHOD")
numerical        = Select(title="Numerical Method:", value="Explicit", options=["Explicit", "Implicit"])
space_step       = Slider(start=0, end=100, value=10, step=10, title="Space Step (dx) (meter)")
error_val        = Slider(start=0, end=1, value=0.5, step=.01, title="Error Tollerance")
iteration_num    = Slider(start=0, end=20, value=5, step=1, title="Maximum Iteration")

##### SET THE OUTPUT BUTTON #####
sub_div_title_4  = Div(text="<b>===========================================================================================</b>")
output_button_1  = Button(label="Analyze Data", button_type="default")
output_button_2  = Button(label="Export Chart Result")
output_button_3  = Button(label="Reset Input")

##### SET THE FIGURE #####
graph            = figure(plot_width=700, plot_height=500, title="Back Water Curve")

##############################
######## THE BACK END ########
##############################

hd = float(water_depth.value)
Hw_Exp = [hd] # Water height using explicit approach (m)
Hw_Imp = [hd] # Water height using implicit approach (m)

def computate() : 
    if numerical.value == "Explicit" : 
    #def explicit() : # Explicit calculation method 
        graph.renderers = []
        b  = float(channel_width.value)  
        L  = float(channel_length.value)
        S0 = float(channel_sloope.value) 
        C  = float(roughness_chz.value) 
        Q  = float(discharge.value)
        hd = float(water_depth.value)
        dx = float(space_step.value)

        ##### Set the Numerical Parameter #####
        maxcom = int (L/dx) + 1 
        x1     = [0 ] # Distance iteration
        Hw_Exp = [hd] # Water height using explicit approach (m)
        Hg_Exp = [0 ] # Ground height (m)
        Wl_Exp = [hd] # Water level using explicit approach (m) 

        for i in range (1,maxcom):
            x1.append     (x1[i-1] + dx)
            Hg_Exp.append (i * dx * S0)
            Hw_Exp.append (Hw_Exp[i-1] + dx * (((Q**2 / (C**2 * Hw_Exp[i-1]**3 * b**2))-S0)))
            Wl_Exp.append (Hw_Exp[i] + Hg_Exp[i])

        graph.varea(x=x1, y1=Hg_Exp, y2=Wl_Exp)
        
    else : 
    #def implicit() : # Implicit calculation method
        graph.renderers = []
        b  = float(channel_width.value)  
        L  = float(channel_length.value)
        S0 = float(channel_sloope.value) 
        C  = float(roughness_chz.value) 
        Q  = float(discharge.value)
        hd = float(water_depth.value)
        dx = float(space_step.value)
        er = float(error_val.value)
        MI = float(iteration_num.value)

        ##### Set the Numerical Parameter #####
        maxcom = int (L/dx) + 1
        x2     = [0 ] # Distance iteration 
        Hw_Imp = [hd] # Water height using implicit approach (m)
        Hg_Imp = [0 ] # Ground height (m)
        Wl_Imp = [hd] # Water level using implicit approach (m)
        A = Q**2/(C**2*b**2) 

        for i in range(1,maxcom):
            htriR = Hw_Imp[i-1] #m
            x2.append(i*dx)
            Hg_Imp.append(S0 * i * dx)
            j = 0
            er = 10

            while er > 0.01:
                if j > MI:
                    break
                else:
                    RHS   = A / htriR ** 3 - S0
                    htril = dx * RHS + Hw_Imp[i-1]
                    er = abs(htril-htriR)
                    htriR = htril
                    j += 1

            Hw_Imp.append(htril)
            Wl_Imp.append(Hw_Imp[i]+Hg_Imp[i])
        #return(x2,Hw_Imp,Hg_Imp,Wl_Imp)

        graph.varea(x=x2, y1=Hg_Imp, y2=Wl_Imp)
    
def save_output() : 
    if numerical.value == "Explicit" : 
        df = pd.DataFrame(Hw_Exp).T
        df.to_excel(excel_writer = "BWC_Explcit_Output.xlsx")
    else : 
        df = pd.DataFrame(Hw_Imp).T
        df.to_excel(excel_writer = "BWC_Implicit_Output.xlsx")

##### SET THE CALCULATION METHOD #####
output_button_1.on_click(computate)
output_button_2.on_click(save_output)

##############################
######### INTEGRATION ########
##############################

output_file("BWC_FullStack.html")
curdoc().add_root(column(main_menu, app_title, description,sub_div_title_1, channel_length, channel_width, channel_sloope, row(column(sub_div_title_2,roughness_method, roughness_chz, discharge,water_depth),column(sub_div_title_3,numerical,space_step,error_val,iteration_num )),column(sub_div_title_4),column(graph), row(column(output_button_1),column(output_button_2))))

##### RUN SERVER #####
# bokeh serve --show BWC_FullStack.py