from bokeh.io import output_notebook, show
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool
from bokeh.plotting import gmap, figure
from numpy import size

output_notebook()

api_key = 'AIzaSyBuHC_G8d3kvYYAFE5uk85hA7eyOOs0jVs'
map_options = GMapOptions(lat=47.1839600, lng= 6.0014100, map_type="satellite", zoom=8, scale_control=True)

hover=HoverTool(tooltips=[("(x,y)","($x,$y)")])

tools=[hover, 'lasso_select','tap']

p = gmap(api_key, map_options, title="your_title", plot_height=600, plot_width=1000, tools=tools)
p.axis.visible = False
p.legend.click_policy='hide'

your_source = ColumnDataSource(data=dict(lat=12.9738112, lon=77.5460685, size = 13))

p.circle(x="lon",y="lat",size=size, fill_color="purple",legend = "your_legend", fill_alpha=0.2, line_alpha=0, source=your_source)
show(p)