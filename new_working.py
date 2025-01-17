import pandas as pd
import folium.plugins
import branca
import matplotlib.pyplot as plt
import base64
import os
import days as d
import gbartest1 as barrrr
import AreaNameMappingDict as ad

img_root_folder = 'res\\img\\'
data_root_folder = 'res\\data\\'
img_default_name_footfall = '_img.png'
img_default_name_sales = '_gplot.png'
data = pd.read_csv(data_root_folder+'data_source.csv', encoding="cp1252")

LOC = list(data['LOCATION'])
#barrrr.getBars(LOC[0]).show()
ff =  list(data['AVGFOOTFALL'])
LAT = list(data['LAT'])
LON = list(data['LON'])
website = list(data['website'])
#fg = folium.FeatureGroup('my map')
min = 200
max = 300
m = folium.Map(location=[20.6112706, 77.7679723], zoom_start=5)
cluster = folium.plugins.MarkerCluster().add_to(m)

#for lc in LOC:
    #file1 = img_root_folder + lc + '_gplot.png'
   # barrrr.getBars(lc).savefig(file1)
   # barrrr.getBars(lc).close()
    #dir_base = os.getcwd()
  #  Filename1 = dir_base + '\\' + file1
  #  encoded = base64.b64encode(open(Filename1, 'rb').read())
  #  html = html(encoded.decode('UTF-8'))

def footfall():
        html = "<img src='data:image/png;base64,{}'></b>".format
        x = ['MON', 'TUE', 'WED', 'THU','FRI', 'SAT', 'SUN']
        y = [mon, tue, wed, thu, fri, sat, sun]
        plt.figure(num=None, figsize=(5.5, 3.5), dpi=80, facecolor='w', edgecolor='k')
        plt.xlabel('DAYS--->')
        plt.ylabel('SALES--->')
        plt.title('Analysis:')
        plt.bar(x, y)
        file = img_root_folder + lc + img_default_name_footfall
        plt.savefig(file)
        plt.close()
        dir_base = os.getcwd()
        Filename = dir_base + '\\' + file
        encoded = base64.b64encode(open(Filename, 'rb').read())
        html = html(encoded.decode('UTF-8'))
        return html

def salesBarPlotter():
    #psale = pd.read_csv(data_root_folder+'shop_menu.csv')
    #prd = psale.to_html(classes='table table-striped table-hover table-condensed table-responsive')
    htmlFootfall=footfall()
    html="<img src='data:image/png;base64,{}'></b>".format

    file1 = img_root_folder + lc + img_default_name_footfall
    bar = barrrr.getBars(lc)
    bar.savefig(file1)
    bar.close()
    dir_base = os.getcwd()
    Filename1 = dir_base + '\\' + file1
    encoded = base64.b64encode(open(Filename1, 'rb').read())
    html = html(encoded.decode('UTF-8'))
    lcMapped = ad.area.get(lc)
    if lcMapped == None:
        lcMapped = lc

    html__ = "<b> Coffee Thago:&nbsp;</b>" + lcMapped + "<br><br><b>Analysis:</b>"
    html__ += html
    html__ += htmlFootfall
    iframe = branca.element.IFrame(html=html__, width=500, height=400)
    popup  = folium.Popup(iframe, max_width=2650)
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

for f, lc, lt, ln, w, mon, tue, wed, thu, fri, sat, \
        sun in zip(ff, LOC, LAT, LON, website, d.MON, d.TUE, d.WED, d.THU, d.FRI, d.SAT, d.SUN):

        salesBarPlotter()


m = folium.Map(location=[20.6112706, 77.7679723], zoom_start=5)

m.add_to(cluster)
m.save("Nmap.html")
