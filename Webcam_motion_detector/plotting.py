from motion_detector import df

from bokeh.plotting import figure
from bokeh.io import show,output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")

df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = {'x': df["Start"],'y': df["End"]}
source=ColumnDataSource(data=cds)

p = figure(x_axis_type="datetime",height=100,width=500, sizing_mode='scale_width',title="Motion Graph")
p.yaxis.minor_tick_line_color = None

hover = HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])

q = p.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="green",source=source)

output_file("Graph.html")
show(p)