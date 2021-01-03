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
data = open(r"gui\docs\canada.txt")

Canada = Country(file = "gui\docs\canada.txt")
df = Canada.regions[0]
df = df.lat()
print(df)

#fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon",     color="peak_hour", size="car_hours",
#                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
#fig.show()

#If this works correctly, the program will open a tab (I'm not sure if the tab has the graph) and generate a png file of the graph at the specified location
