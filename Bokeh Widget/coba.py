from bokeh.models import Div
from bokeh.io import curdoc

div = Div(text="<img src='myapp/static/foo.png'>")

curdoc().add_root(div)

# bokeh serve --show coba.py