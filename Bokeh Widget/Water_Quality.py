from tkinter.filedialog import askdirectory
from bokeh.plotting import curdoc, figure
from bokeh.layouts import row, column
from bokeh.io import output_file
from bokeh.models import Slider, TextInput, Button, Tabs, Panel, RadioGroup
from bokeh.models.widgets import Slider, Select, Button, Div

import numpy as np
import pandas as pd

##############################
# GROUND WATER RESERVOIR 
##############################

#  FRONT END 
## LOGO 
logo_source = "<img src='https://www.un-ihe.org/sites/default/files/ihe-delft_logo_black_cyan_reduced_version.png' width=auto height=100>"
logo        = Div(text=logo_source)

## SET THE HEADER 
image_WQ_source = "<img src='https://english.rvo.nl/sites/default/files/2021/03/Deltapark%20Neeltje%20Jans%20header%20themapagina%20water.jpg' width=1390 height=400>"
image_WQ        = Div(text=image_WQ_source)
app_title_WQ    = Div(text="<b>WATER QUALITY</b>")
description_WQ  = Div(text="This application helps <b>calculating and analyzing the water quality phenomenon.</b> Explicit, implicit, and combined methods are being used during the calculation. All errors and the graphical result will be shown after the calculation is finished.")

## SET THE GEOMETRIC PARAMETER #####
sub_div_title_1_WQ  = Div(text="<b>TANK AND CONTAMINANT PARAMETER")
contaminant_WQ      = TextInput(title="Contaminant in a tank (gram / liter):", value="13")
degradation_WQ      = TextInput(title="Degradation Rate:", value="0.6")
total_time_WQ       = TextInput(title="Total computation time (days):", value="12")

## SET THE NUMERICAL METHOD ##### 
sub_div_title_2_WQ  = Div(text="<b>NUMERICAL SOLUTIONS METHOD")
numerical_WQ        = Select(title="Numerical Method:", value="Explicit", options=["Explicit", "Implicit", "Combined"])
time_step_WQ        = Slider(start=0, end=5, value=0.5, step=0.1, title="Time Step (dt) (seconds)")
sub_div_title_3_WQ  = Div(text="<b>SHOW THE ANALYTICAL EQUATION")
analytical_WQ       = Select(title="Analytical Equation:", value="Yes", options=["Yes", "No"])


## SET THE OUTPUT BUTTON #####
sub_div_title_4  = Div(text="<b>===========================================================================================</b>")
WQ_run_button   = Button(label="Analyze Data", button_type="default")
WQ_clear_button = Button(label="Reset Input")

## SET THE FIGURE AND LAYOUT #####
graph_WQ        = figure(plot_width=700, plot_height=500, title="GRAPHICAL INTERPRETATION")
WQ_layout_left  = column(app_title_WQ, description_WQ, row(column(sub_div_title_1_WQ, contaminant_WQ, degradation_WQ, total_time_WQ),column(sub_div_title_2_WQ, numerical_WQ, time_step_WQ,sub_div_title_3_WQ, analytical_WQ)))
WQ_layout_right = column(graph_WQ,row(column(WQ_run_button),column(WQ_clear_button)))
WQ_layout       = column(logo, image_WQ,row(WQ_layout_left, WQ_layout_right)) 

# BACK END 
def compute_WQ() :
    graph_WQ.renderers = [] 
    A0_WQ   = float(contaminant_WQ.value)                                      # Initial Concentration in Containment B at time t=0 (g/l)
    k1_WQ   = float(degradation_WQ.value)                                      # Degradation Rates of 1 (day^-1)
    T_WQ    = float(total_time_WQ.value)                                       # Total Time (days)
    dt_WQ   = float(time_step_WQ.value)                                        # Time Step (seconds)
    maxcom_WQ = int(T_WQ/dt_WQ) + 1 
    t_WQ      = [0]                                                            # Time Itteration
    A_Exp_WQ  = [A0_WQ]                                                        # List of calculate A using Explicit Approach
    A_Imp_WQ  = [A0_WQ]                                                        # List of calculate A using Implicit Approach
    A_Ana_WQ  = [A0_WQ]                                                        # List of calculate A using Analytical Approach

    for i in range (1,maxcom_WQ) : 
        t_WQ.append(t_WQ[i-1] + dt_WQ)
        A_Exp_WQ.append(A_Exp_WQ[i-1] * (1 - dt_WQ * k1_WQ))
        A_Imp_WQ.append(A_Imp_WQ[i-1] / (1 + dt_WQ * k1_WQ))
        A_Ana_WQ.append(A0_WQ * (2.718 ** (-1 * k1_WQ * t_WQ[i])))

    if numerical_WQ.value == "Explicit" : 
        graph_WQ.line(x=(t_WQ), y1=(A_Exp_WQ))
        graph_WQ.line(x=(t_WQ), y2=(A_Ana_WQ))

    elif numerical_WQ.value == "Implicit" : 
        graph_WQ.line(x=(t_WQ), y1=(A_Imp_WQ))
        graph_WQ.line(x=(t_WQ), y2=(A_Ana_WQ))

    elif numerical_WQ.value == "Combined" : 
        graph_WQ.line(x=(t_WQ), y1=(A_Exp_WQ))
        graph_WQ.line(x=(t_WQ), y2=(A_Imp_WQ))
        graph_WQ.line(x=(t_WQ), y3=(A_Ana_WQ))

def clear_output_WQ() : 
    graph_WQ.renderers = []

## SET THE CALCULATION METHOD
WQ_run_button.on_click(compute_WQ)
WQ_clear_button.on_click(clear_output_WQ)