#-----------------------------------------------------------------------------
# Name:        Country Map Generation(python.py)
# Purpose:     Generates a Scatterbox map of a specific country,
#              displaying the emissions data for each province/territory of the country.
#
# References: 	This program uses the NumPy/SciPy style of documentation as found
#				here: https://numpydoc.readthedocs.io/en/latest/format.html with
#				some minor modifications based on Python 3 function annotations
#				(the -> notation).
#
# Author:      Rishabh Tamhane
# Created:     15-Dec-2020
# Updated:     13-Jan-2021
#-----------------------------------------------------------------------------

import plotly.express as px
import os
from region import Region
from country import Country

#Function (country)


def region_map(name):
    i = 0
    name = name.lower()
    map_pathname = ("docs\\" + name + ".txt")
    map_pathname = map_pathname
    image_pathname = ("source/helpers/maps/" + name + "_map.png")
    image_pathname = image_pathname
    if os.path.isfile(image_pathname) == False:
        data = open(map_pathname, 'r')
        Map = Country(file = map_pathname)
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
        fig.write_image(image_pathname)
        fig.to_image(format="png", engine="kaleido")
    i += 1
