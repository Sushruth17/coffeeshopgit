import folium
import pandas as pd
import folium.plugins
import branca
import matplotlib.pyplot as plt, mpld3
import base64
from branca.element import IFrame

data = pd.read_csv('C:/Users/admin/Desktop/data/web-map-master/12.csv', encoding="cp1252")

LOC = list(data['LOCATION'])
ff = list(data['FOOTFALL'])
LAT = list(data['LAT'])
LON = list(data['LON'])
website = list(data['website'])
fg = folium.FeatureGroup('my map')
min = 200
max = 300
m = folium.Map(location=[12.9752848, 77.5070119], zoom_start=10)
# MON = list(data["Mon"])
# TUE = list(data["Tue"])

x=[' ', '']
y=[5,9]
plt.xlabel('MON________________________________________________TUE       ')
plt.ylabel('Sales->')
plt.title('Data')
# plt.bar(x,y)
plt.bar(x,y)
plt.savefig("teettt.png")
vis3= mpld3.save_json(plt.figure(), "teettttttt.html")
n = "teettttttt.html"
html_image = "<!DOCTYPE html><html><body><h2>HTML Image</h2><img src='C:/Users/admin/Desktop/teettt.jpg' alt=\"Girl in a jacket\" width=\"500\" height=\"600\"></body></html>"
bar = "http://127.0.0.1:8898/"


text_file = open("test_image.html", "w")
n = text_file.write(html_image)
text_file.close()





cluster = folium.plugins.MarkerCluster().add_to(m)

for f, lc, lt, ln, w in zip(ff, LOC, LAT, LON, website):

    psale = pd.read_csv('C:/Users/admin/Desktop/data/web-map-master/9.csv')
    prd = psale.to_html(classes='table table-striped table-hover table-condensed table-responsive')
    #html = "<b> Coffee Thagolo nim ayyan dole mooga raghu: </br></b>" + lc + "<br><b></br>For Analysis: <img src='C:/Users/admin/Desktop/teettt.jpg' alt=\"Girl in a jacket\" width=\"100\" height=\"100\"> </b><p><a href=\"C:/Users/admin/PycharmProjects/gm/test_image.html\" target=\"_blank\"</p>>click here</a><br><b></br>Products:</b>" + prd
    #print(html)

    # iframe = branca.element.IFrame(html=html, width=500, height=300)
    # popup = folium.Popup(iframe, max_width=500)
    # start
    resolution, width, height = 75, 7, 3
    encoded = base64.b64encode(open("C:/Users/admin/Desktop/teettt.png", 'rb').read())
    html = '<img src="data:image/png;base64,{}">'.format
    iframe = branca.element.IFrame(html=html(encoded), width=(width * resolution) + 20, height=(height * resolution) + 20)
    popup = folium.Popup(iframe, max_width=500)

    # end

    if f < min:
        folium.Marker(location=[lt, ln], popup=popup,
                      icon=folium.Icon(color='red', icon_color='white', icon='coffee', angle=0, prefix='fa')).add_to(
            cluster)
    elif (f > min) and (f < max):
        folium.Marker(location=[lt, ln], popup=popup,
                      icon=folium.Icon(color='cadetblue', icon_color='white', icon='coffee', angle=0,
                                       prefix='fa')).add_to(cluster)
    else:
        folium.Marker(location=[lt, ln], popup=popup,
                      icon=folium.Icon(color='green', icon_color='white', icon='coffee', angle=0, prefix='fa')).add_to(
            cluster)
m = folium.Map(location=[12.9752848, 77.5070119], zoom_start=11)

m.add_to(cluster)
m.save('testmap4o49.html')
# print(bar)
# mpld3.show()