import gmplot
gmap=gmplot.GoogleMapPlotter(center_lat=12.9738112,center_lng=77.5460685,zoom=12)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

gmap.marker(12.9738112, 77.5460685,title="Merchant_Name")
gmap.draw("C:\\Users\\admin\\\Desktop\\my_maptest.html")