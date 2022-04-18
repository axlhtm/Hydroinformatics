from bokeh.plotting import curdoc, figure
from bokeh.layouts import row, column
from bokeh.io import output_file
from bokeh.models import Slider, TextInput, Button
from bokeh.models.widgets import RadioButtonGroup, Slider, Select, Button, Div, PreText

number_1   = TextInput(title="Number 1", value="500")
number_2   = TextInput(title="Number 2", value="100")

result      = PreText(text="""Please click to compute velocity""",width=500, height=100)
add_button  = Button(label="Add (+)", button_type="success")
min_button  = Button(label="Minus (-)", button_type="success")

def add() : 
    A1 = float(number_1.value)
    A2 = float(number_2.value)
    value_add = A1 + A2
    result.text =str(value_add)
add_button.on_click(add)

def minus() : 
    A1 = float(number_1.value)
    A2 = float(number_2.value)
    value_minus = A1 + A2 
    result.text = str(value_minus)
min_button.on_click(minus)


curdoc().add_root(column(number_1, number_2, add_button, min_button, result))

# bokeh serve --show Calculator.py
# http://localhost:5006/myapp