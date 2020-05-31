import pandas as pd
import folium.plugins
import branca
import matplotlib.pyplot as plt
import base64
import os
import days as d
import gbartest1 as barrrr

img_root_folder = 'res\\img\\'
data_root_folder = 'res\\data\\'
img_default_name = '_img.png'
data = pd.read_csv(data_root_folder+'data_source.csv', encoding="cp1252")

LOC = list(data['LOCATION'])
#barrrr.getBars(LOC[0]).show()
ff = list(data['AVGFOOTFALL'])
LAT = list(data['LAT'])
LON = list(data['LON'])
website = list(data['website'])
#fg = folium.FeatureGroup('my map')
min = 200
max = 300
m = folium.Map(location=[20.6112706, 77.7679723], zoom_start=5)
cluster = folium.plugins.MarkerCluster().add_to(m)

for f, lc, lt, ln, w, mon, tue, wed, thu, fri, sat, sun in zip(ff, LOC, LAT, LON, website, d.MON, d.TUE, d.WED, d.THU, d.FRI,d. SAT,d.SUN):

    psale = pd.read_csv(data_root_folder+'shop_menu.csv')
    prd = psale.to_html(classes='table table-striped table-hover table-condensed table-responsive')
    html="<img src='data:image/png;base64,{}'></b>".format
    x = ['MON', 'TUE', 'WED', 'THU','FRI', 'SAT', 'SUN']
    y = [mon, tue, wed, thu, fri, sat, sun]
    plt.figure(num=None, figsize=(5.5, 3.5), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('DAYS--->')
    plt.ylabel('SALES--->')
    plt.title('Analysis:')
    plt.bar(x, y)
    file =  img_root_folder + lc + img_default_name
    plt.savefig(file)
    plt.close()
    dir_base = os.getcwd()
    Filename = dir_base + '\\' + file
    encoded = base64.b64encode(open(Filename, 'rb').read())
    html = html(encoded.decode('UTF-8'))
    html__ = "<b> Coffee Thago:&nbsp;</b>" + lc + "<br><br><b>Products:</b>" + prd
    html__ = html__+html
    iframe = branca.element.IFrame(html=html__, width=500, height=400)
    popup  = folium.Popup(iframe, max_width=2650)
    print(barrrr.getBars(lc))
    barrrr.getBars(lc).show()
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
m = folium.Map(location=[20.6112706, 77.7679723], zoom_start=5)

m.add_to(cluster)
m.save("Cmap.html")
