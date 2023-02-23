import folium
import pandas as pd

# m = folium.Map(location=[45.5236, -122.6750])
m = folium.Map(
    location=[22.5236, 122.6750],
    zoom_start=4,
    tiles="./tiles/{z}/{x}_{y}.png",
    attr="Mapbox attribution",
)

# define the URL for tile server and get the proper size of the image, this example shows China
# URL = "http://webrd04.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scale=1&style=7"

# m = folium.Map(
#     location=[45.523, -122.675],
#     zoom_start=4,
#     tiles=URL,
#     attr="Mapbox attribution",
# )
# Create your Folium map object

# Save the html and render it using the Selenium webdriver.
m.save('map.html')
