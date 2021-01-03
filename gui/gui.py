import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import sys
import os

print(os.getcwd())
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
print(os.getcwd())

from source.helpers.region import Region
from source.helpers.country import Country
data = open(r"map\docs\canada.txt")

Canada = Country(file = "map\docs\canada.txt")
canada_size = len(Canada.regions)
lat_list = []
lon_list = []
em_list = []

i = 0
while i in range (len(Canada.regions)):
    lat_val = Canada.regions[i]
    lat_val = lat_val.lat
    print(lat_val)
    lat_list.append(lat_val)
    print("Lat:",lat_list[i])
    i = i+1

i = 0
while i in range (len(Canada.regions)):
    lon_val = Canada.regions[i]
    lon_val = lon_val.lon
    print(lon_val)
    lon_list.append(lon_val)
    print("Lon:",lon_list[i])
    i = i+1

i = 0
while i in range (len(Canada.regions)):
    em_val = Canada.regions[i]
    em_val = em_val.emissions
    print(em_val)
    em_list.append(em_val)
    print("EM:",em_list[i])
    i = i+1

df = em_list

fig = px.scatter_mapbox(df, lat=lat_list, lon=lon_list,
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=25, zoom=1.5)
fig.update_layout(mapbox_style="carto-positron")
fig.show()
fig.write_image("map/images/fig1.png")
fig.to_image(format="png", engine="kaleido")



