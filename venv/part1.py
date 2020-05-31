from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(12.9738112,77.5460685, 13)
gmap.apikey = 'AIzaSyBuHC_G8d3kvYYAFE5uk85hA7eyOOs0jVs'
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"


  # ...and so on...
# Polygon
# Scatter points
#e)
content = "'test'"
gmap.infowindow(content,0,0)
# Marker
hidden_gem_lat, hidden_gem_lon = 12.9738112,77.5460685
gmap.marker(hidden_gem_lat, hidden_gem_lon,'red')

# Draw
gmap.draw("C:\\Users\\admin\\\Desktop\\my_map25.html")