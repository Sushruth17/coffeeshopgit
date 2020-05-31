from gmplot import gmplot
from tkinter import *

gmap = gmplot.GoogleMapPlotter(12.9738112,77.5460685, 13)
gmap.apikey = 'AIzaSyBuHC_G8d3kvYYAFE5uk85hA7eyOOs0jVs'
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

hidden_gem_lat, hidden_gem_lon = 12.9738112,77.5460685
marker_name = gmap.marker(hidden_gem_lat, hidden_gem_lon,'green')

def button():
    root = Tk()
    root.geometry('100x100')
    btn = Button(root, text='Click me !', bd='5', command=root.destroy)
    btn.pack(side='top')
    root.mainloop()
content = button()
gmap.infowindow(marker_name, content, True)

gmap.draw("C:\\Users\\admin\\\Desktop\\my_map255.html")