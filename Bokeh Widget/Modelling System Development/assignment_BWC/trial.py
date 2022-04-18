from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.io import output_file, show
from bokeh.models import CustomJS, TextInput, RangeSlider
from bokeh.models.widgets import RadioButtonGroup, Slider, Select, Button, Div
from bokeh.io import curdoc

asd = Div(text="<https://www.un-ihe.org/sites/default/files/ihe-delft_logo_black_cyan_reduced_version.png'>")



curdoc().add_root(asd)

# bokeh serve --show trial.py