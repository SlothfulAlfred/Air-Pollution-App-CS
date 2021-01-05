import plotly.express as px
import sys
import os

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)


data_pathlist = ["map\\docs\\canada.txt","map\\docs\\usa.txt","map\\docs\\mexico.txt"]
image_pathlist = ["map/images/canada_map.png","map/images/usa_map.png","map/images/mexico_map.png"]

from source.helpers.region import Region
from source.helpers.country import Country

i = 0
while i in range(len(data_pathlist)):
    if os.path.isfile(image_pathlist[i]) == False:
        data = open(data_pathlist[i], 'r')
        Map = Country(file = data_pathlist[i])
        map_size = len(Map.regions)
        lat_list = []
        lon_list = []
        em_list = []

        lat_list = [(Map.regions[i].lat) for i in range (map_size)]
        lon_list = [(Map.regions[i].lon) for i in range (map_size)]
        em_list = [(Map.regions[i].emissions) for i in range (map_size)]

        df = em_list

        fig = px.scatter_mapbox(df, lat=lat_list, lon=lon_list,
                        color = em_list, color_continuous_scale=px.colors.sequential.Viridis,
                        size_max=30, zoom=1.5)
        fig.update_layout(mapbox_style="carto-positron")
        fig.write_image(image_pathlist[i])
        fig.to_image(format="png", engine="kaleido")
    i += 1
