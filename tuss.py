# import gmplot package
import gmplot

# GoogleMapPlotter return Map object
# Pass the center latitude and
# center longitude
gmap1 = gmplot.GoogleMapPlotter(30.3164945,
                                78.03219179999999, 13 )

gmap1.apikey = "AIzaSyBuHC_G8d3kvYYAFE5uk85hA7eyOOs0jVs"
# Pass the absolute path
gmap1.marker(30.318107,78.034381, 'cornflowerblue')

gmap1.draw("C:\\Users\\admin\\\Desktop\\map11ttstt.html")
