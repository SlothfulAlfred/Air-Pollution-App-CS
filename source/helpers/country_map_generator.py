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

def region_map(country):
    '''
    Generates a Scatterbox map of a specific country, displaying the emissions data
    for each province/territory of the country.

    Parameters
    -----------------------
    country : non-iterable object
        A Country object, containing latitude, longitude and emissions data for each of its
        stored regions.
    '''
    name = country.name # Uses name of Country object to set paths both of data and final map image
    name = name.lower()
    image_pathname = ("source/helpers/images/" + name + "_map.png")

    if os.path.isfile(image_pathname) == False:

        lat_list = [x.lat for x in country.regions]  #Loads the latitudes for the Country object's regions
        lon_list = [x.lon for x in country.regions]  #Loads the longitudes for the Country object's regions
        em_list = [x.emissions for x in country.regions]  #Loads the emissions data for the Country object's regions

        fig = px.scatter_mapbox(data_frame=em_list, lat=lat_list, lon=lon_list, #Generates map of country
                                color=em_list, color_continuous_scale=px.colors.sequential.Bluered,
                                color_continuous_midpoint=20, range_color=(0, 170),
                                size_max=30, zoom=1.5)

        fig.update_layout(mapbox_style="carto-positron") #Sets map style
        fig.to_image(format="png", engine="kaleido")
        fig.write_image(image_pathname) #Exports map
