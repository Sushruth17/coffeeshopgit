import gmaps
import json
import requests
countries_string = requests.get(
    "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
).content
countries = json.loads(countries_string)
gmaps.configure(api_key="AI...")
fig = gmaps.figure()
geojson = gmaps.geojson_layer(countries)
fig.add_layer(geojson)
fig