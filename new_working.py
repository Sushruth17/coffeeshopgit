import pandas as pd
import folium.plugins
import branca
import matplotlib.pyplot as plt
import base64
import os
import gbartest1 as barrrr
import AreaNameMappingDict as ad
import sqltestdb as sdb

img_root_folder = 'res\\img\\'
data_root_folder = 'res\\data\\'
img_default_name_footfall = '_img.png'
img_default_name_sales = '_gplot.png'
data = pd.read_csv(data_root_folder+'data_source.csv', encoding="cp1252")
locDictKey = ad.area.keys()
print("value---->",locDictKey)

LAT = []
LON = []
ff = []
MON = []
TUE = []
WED = []
THU = []
FRI = []
SAT = []
SUN = []
for area in locDictKey:
    locDetails = sdb.getLocationDetails(area)
    LAT.append(locDetails.get('LAT'))
    LON.append(locDetails.get('LON'))
    ff.append(locDetails.get('AVGFOOTFALL'))
    MON.append(locDetails.get('MON'))
    TUE.append(locDetails.get('TUE'))
    WED.append(locDetails.get('WED'))
    THU.append(locDetails.get('THU'))
    FRI.append(locDetails.get('FRI'))
    SAT.append(locDetails.get('SAT'))
    SUN.append(locDetails.get('SUN'))

#print("LAT DETAILS ____________>",LAT)
#print("LON DETAILS ____________>",LON)
LOC = list(locDictKey)
#print("listLOC-------------------------------------------->",LOC)
#barrrr.getBars(LOC[0]).show()
#ff =  list(data['AVGFOOTFALL'])
#LAT = list(data['LAT'])
#LON = list(data['LON'])
#website = list(data['website'])
#fg = folium.FeatureGroup('my map')
min = 200
max = 300
m = folium.Map(location=[20.6112706, 77.7679723], zoom_start=5)
cluster = folium.plugins.MarkerCluster().add_to(m)

def footfall(lc):
    html = "<img src='data:image/png;base64,{}'></b>".format
    x = ['MON', 'TUE', 'WED', 'THU','FRI', 'SAT', 'SUN']
    y = [mon, tue, wed, thu, fri, sat, sun]
    plt.figure(num=None, figsize=(5.5, 3.5), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('DAYS -->')
    plt.ylabel('FOOTFALL -->')
    plt.title('Footfall:',fontweight='bold')
    plt.bar(x, y)
    absolutePathFootFall = img_root_folder + lc + img_default_name_footfall
    plt.savefig(absolutePathFootFall)
    plt.close()
    dir_base = os.getcwd()
    Filename = dir_base + '\\' + absolutePathFootFall
    try:
        encoded = base64.b64encode(open(Filename, 'rb').read())
        html = html(encoded.decode('UTF-8'))
    except:
        lcMapped = ad.area.get(lc)
        if lcMapped == None:
            lcMapped = lc
        html = "<!DOCTYPE html><html><head><title></title> \
                </head><body><p style=font-family:calibri>No {} data for {} </p></body></html>".format('footfall',lcMapped)
        print("Exception while opening file for FootFall")

    return html

def salesBarPlotter(lc):

    htmlFootfall=footfall(lc)
    htmlSales="<img src='data:image/png;base64,{}'></b></br></br></br>".format
    absolutePathSales = img_root_folder + lc + img_default_name_sales

    bar = barrrr.getBars(lc)
    if bar != None:
        bar.savefig(absolutePathSales)
        bar.close()
    dir_base = os.getcwd()
    Filename1 = dir_base + '\\' + absolutePathSales
    try:
        encoded = base64.b64encode(open(Filename1, 'rb').read())
        htmlSales = htmlSales(encoded.decode('UTF-8'))
    except:
        lcMapped = ad.area.get(lc)
        if lcMapped == None:
            lcMapped = lc
        htmlSales = "<!DOCTYPE html><html><head><title></title> \
                    </head><body><p style=font-family:calibri>No {} data for {} </p></body></html>".format('sales',lcMapped)
        print("Exception while opening file for Sales")
    lcMapped = ad.area.get(lc)
    if lcMapped == None:
        lcMapped = lc

    mainHTML = "<b><p style=font-family:calibri> Coffee Thago:&nbsp;</b>" + lcMapped + "<br><br><b>Analysis:</p></b>"
    #print("Im htmlsale - > " ,htmlSales)
    if htmlSales!= None:
        mainHTML += htmlSales
        #print("Im htmlFootfall - > ", htmlFootfall)
    if htmlFootfall!= None:
        mainHTML += htmlFootfall
    #print("html --- >>>",htmlSales)
    iframe = branca.element.IFrame(html=mainHTML, width=500, height=400)
    mainHTML = None
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

for f, lc, lt, ln, mon, tue, wed, thu, fri, sat, \
        sun in zip(ff, LOC, LAT, LON, MON, TUE, WED, THU, FRI, SAT, SUN):

        salesBarPlotter(lc)


m = folium.Map(location=[20.6112706, 77.7679723], zoom_start=5)

m.add_to(cluster)
m.save("Nmap.html")
