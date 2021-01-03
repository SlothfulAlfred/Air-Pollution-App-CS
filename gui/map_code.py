import plotly.express as px
import sys
import os
import datetime

print(datetime.datetime.now())
print(os.getcwd())
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
print(os.getcwd())
# do you need sys and os? also why are you printing the cwd

from source.helpers.region import Region
from source.helpers.country import Country
data = open(r"map\\docs\\usa.txt")

# you don't need to use a kwarg here since file is the only argument that is needed
Canada = Country(file = "map\\docs\\usa.txt") 
canada_size = len(Canada.regions)
# you don't need to declare these first you can do everything during the list comprehension 
lat_list = []
lon_list = []
em_list = []

i = 0 # this variable is not necessary 
# why not iterate through the list directly instead of iterating through a range of subscripts then accessing the list
# i.e [region.lat for region in Canada.regions]
lat_list = [(Canada.regions[i].lat) for i in range (canada_size)] 
lon_list = [(Canada.regions[i].lon) for i in range (canada_size)]
em_list = [(Canada.regions[i].emissions) for i in range (canada_size)]

df = em_list

fig = px.scatter_mapbox(df, lat=lat_list, lon=lon_list,
                        color = em_list, color_continuous_scale=px.colors.cyclical.IceFire,
                        size_max=30, zoom=1.5)
fig.update_layout(mapbox_style="carto-positron")
fig.show()
fig.write_image("map/images/usa_map.png")
fig.to_image(format="png", engine="kaleido")
print("Done at",datetime.datetime.now())
