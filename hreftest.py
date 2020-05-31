import folium
import pandas as pd
import folium.plugins
import branca
import matplotlib.pyplot as plt, mpld3
import base64
from branca.element import IFrame
import os

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

x=[' ', '']
y=[6,9]
plt.xlabel('MON________________________________________________TUE       ')
plt.ylabel('Sales->')
plt.title('Data')
plt.bar(x,y)
plt.savefig("teettt.png")
text_file = open("test_image.html", "w")

html_image = "<!DOCTYPE html><html><body><h2>HTML Image</h2><img src='file:///C:/Uss/admin/Desktop/teettt.jpger' alt=\"Girl in a jacket\" width=\"500\" height=\"600\"></body></html>"
n = text_file.write(html_image)
text_file.close()

#from bs4 import BeautifulSoup
#import re
#import urllib3
#url = "C:\s1txt.html"
#page = urllib3.urlopen(url)
#soup = BeautifulSoup(page.read())

from bs4 import BeautifulSoup

#html = '''<a href="file:///C:/Users/admin/Desktop/1/s1txt.html">next</a>
#<span class="class"><a href="another_url">later</a></span>

html = '''<b> Coffee <br></b><a href="s1txt.html" target=\"_blank\"</p>click here</a>
'''

soup = BeautifulSoup(html,features="html.parser")
features="html.parser"

for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])

cluster = folium.plugins.MarkerCluster().add_to(m)

for f, lc, lt, ln, w in zip(ff, LOC, LAT, LON, website):

    psale = pd.read_csv('C:/Users/admin/Desktop/data/web-map-master/9.csv')
    prd = psale.to_html(classes='table table-striped table-hover table-condensed table-responsive')
    #wrc =  ""
    #html="<img src='data:image/png;base64,{}'></b>".format
    #html= "<b> Coffee Thago:</br></b><br><b></br>For Analysis: </b><a href="+https://www.instagram.com/"target="_blank"+>click here</a>"
    html = "<b> Coffee <br></b><a href=C:/Users/admin/Desktop/1/s1txt.html target=\"_blank\"</p>>click here</a>"
    #html = "<b> Coffee <br></b><a href=file:///C|/Users/admin/Desktop/1/s1txt.html target=\"_blank\"</p>>click here</a>"
    #html = "<b> Coffee <br></b><a href="+str(soup)+" target=\"_blank\"</p>click here</a>"
    #html = "<b> Coffee <br></b><a href=\"file:///C:/Users/admin/Desktop/1/s1txt.html" target=\"_blank\"</p>click here</a>"
    #html = "<b> Coffee <br></b><a href="https://www.instagram.com/?hl=en/" target="_blank">click here</a>"
    file =  'teettt.png'
    dir_base = os.getcwd()
    Filename = dir_base + '\\' + file
    encoded = base64.b64encode(open(Filename, 'rb').read())
    iframe = branca.element.IFrame(html=html, width=500, height=300)
    popup  = folium.Popup(iframe, max_width=2650)

    if f < min:
        folium.Marker(location=[lt, ln], popup=popup,
                      icon=folium.Icon(color='red', icon_color='white', icon='coffee', angle=0, prefix='fa')).add_to(cluster)
    elif (f > min) and (f < max):
        folium.Marker(location=[lt, ln], popup=popup,
                      icon=folium.Icon(color='cadetblue', icon_color='white', icon='coffee', angle=0,
                                       prefix='fa')).add_to(cluster)
    else:
        folium.Marker(location=[lt, ln], popup=popup,
                      icon=folium.Icon(color='green', icon_color='white', icon='coffee', angle=0, prefix='fa')).add_to(cluster)
m = folium.Map(location=[12.9752848, 77.5070119], zoom_start=11)

m.add_to(cluster)
m.save("S1.html")