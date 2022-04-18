from bokeh.plotting import curdoc, figure
from bokeh.layouts import row, column
from bokeh.io import output_file
from bokeh.models import Slider, TextInput, Button
from bokeh.models.widgets import RadioButtonGroup, Slider, Select, Button, Div, PreText

from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.io import output_file, show
from bokeh.models import CustomJS, TextInput, RangeSlider
from bokeh.models.widgets import RadioButtonGroup, Slider, Select, Button, Div

from attr import asdict
from bokeh.models import Div
from bokeh.io import curdoc


logo_source = "<img src='ihelogo.png' width=auto height=100>"
logo        = Div(text=logo_source)

copyright   = Div(text="This modelling software is made by Abdalla, Axel, Irfan")

show(column(logo, copyright))

# bokeh serve --show test.py