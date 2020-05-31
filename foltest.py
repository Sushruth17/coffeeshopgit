import folium
import pandas as pd
import folium.plugins

data = pd.read_csv('C:/Users/admin/Desktop/testmap2/web-map-master/6.csv', encoding="cp1252")

LOC = list(data['LOCATION'])
ff = list(data['FOOTFALL'])
LAT = list(data['LAT'])
LON = list(data['LON'])
website = list(data['website'])
fg = folium.FeatureGroup('my map')
a = 200
b = 300
m = folium.Map(location=[12.9752848, 77.5070119], zoom_start=11)
marker_cluster = folium.plugins.MarkerCluster().add_to(m)
#locationlist = pd.read_csv('C:/Users/admin/Desktop/testmap2/web-map-master/6.csv', encoding="cp1252")
for lt, ln in zip(LAT, LON):
    folium.Marker(lt, ln).add_to(marker_cluster)

for f, lc, lt, ln, w in zip(ff, LOC, LAT, LON, website):
    if f < a:
        fg.add_child(folium.Marker(location=[lt, ln],
                                   popup="<b> Coffee Thago:</br></b>" + lc + "<br><b></br>For Analysis: </b><a href=" + w + ">click here</a>",
                                   icon=folium.Icon(color='red', icon_color='white', icon='coffee', angle=0,
                                                    prefix='fa')))
    elif (f > a) and (f < b):
        fg.add_child(folium.Marker(location=[lt, ln],
                                   popup="<b> Coffee Thago:</br></b>" + lc + "<br><b></br>For Analysis: </b><a href=" + w + ">click here</a>",
                                   icon=folium.Icon(color='cadetblue', icon_color='white', icon='coffee', angle=0,
                                                    prefix='fa')))
    else:
        fg.add_child(folium.Marker(location=[lt, ln],
                                   popup="<b> Coffee Thago:</br></b>" + lc + "<br><b></br>For Analysis: </b><a href=" + w + ">click here</a>",
                                   icon=folium.Icon(color='green', icon_color='white', icon='coffee', angle=0,
                                                    prefix='fa')))
m = folium.Map(location=[12.9752848, 77.5070119], zoom_start=11)

m.add_child(fg)
m