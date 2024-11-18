from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.layouts import column
from bokeh.plotting import figure

# Import the Rust function
from rust_bokeh_app import double_value

# Initialize data source
source = ColumnDataSource(data=dict(x=[0, 1, 2], y=[0, 1, 4]))

# Create a plot
plot = figure(height=400, width=400, title="Rust + Bokeh App")
plot.line("x", "y", source=source, line_width=3)

# Widgets
text_input = TextInput(value="2.0", title="Input Value:")
slider = Slider(start=0, end=10, value=1, step=0.1, title="Multiplier")

# Callback function
def update_data(attr, old, new):
    input_value = float(text_input.value)
    multiplier = slider.value
    new_y = [double_value(x * multiplier) for x in [0, 1, 2]]
    source.data = dict(x=[0, 1, 2], y=new_y)

# Connect widgets to callback
text_input.on_change("value", update_data)
slider.on_change("value", update_data)

# Layout and add to document
layout = column(text_input, slider, plot)
curdoc().add_root(layout)
