import folium
from IPython.display import display
LDN_COORDINATES = (51.5074, 0.1278)
myMap = folium.Map(location=LDN_COORDINATES, zoom_start=12)
display(myMap)