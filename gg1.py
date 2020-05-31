import gmaps

gmaps.configure(api_key='AIzaSyBuHC_G8d3kvYYAFE5uk85hA7eyOOs0jVs')

marker_locations = [
    (-34.0, -59.166672),
    (-32.23333, -64.433327),
    (40.166672, 44.133331),
    (51.216671, 5.0833302),
    (51.333328, 4.25)
]

fig = gmaps.figure()
markers = gmaps.marker_layer(marker_locations)
fig.add_layer(markers)
fig