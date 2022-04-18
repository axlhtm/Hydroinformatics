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
import Water_Quality as WQ 

##############################
# BACK WATER CURVE
##############################
import Back_Water_Curve as BWC

##############################
# WATER LEVEL AT THE WEIR
##############################
import Water_at_the_Weir as WW

##############################
# SET THE LAYOUT AND OUTPUT FILE 
##############################
tab_WQ      = Panel(child=WQ.WQ_layout, title= "WATER QUALITY")
tab_BWC     = Panel(child=BWC.BWC_layout, title= "BACK WATER CURVE")
tab_WW      = Panel(child=WQ.WQ_layout, title="WATER LEVEL AT THE WEIR")
curdoc().add_root(Tabs(tabs=[tab_WQ, tab_BWC, tab_WW]))

output_file("Modelling_mokcUp.html")

##############################
# RUN SERVER
##############################
# bokeh serve --show Modelling_MockUp.py