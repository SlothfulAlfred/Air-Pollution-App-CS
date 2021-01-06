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


# 1. You're missing inline comments and you're missing documentation for your function
#
# 2. If you're taking a Country object as a parameters, why on Earth, the Moon, Mars, Jupiter,
#    Venus, Galactus, the Milky Way, and Andromeda are you initializing a new Country object?
#    Do you have a vendetta against efficient code or are you just doing this as a joke? Have you 
#    ever thought what would happen if we decided to change the format of the file names to something
#    like 'usa_data.txt'? Then his entire function would throw an error. Also since you got rid of 
#    the use of indices inside of your list comprehension, why are you still keeping the map_size
#    variable? Are you really saying that the reason why I suggested that you take a Country 
#    object as a parameter was so that you could use country.name? Is that an insult to my
#    intelligence or yours? If all you wanted was the name then it would've been faster to just
#    take a string as a parameter like you were doing before. The entire method is flawed here.
#
# 3. You haven't changed the color scale yet. Make sure to change/remove that soon.
#
# 4. Finally, I'm not sure how this works, but, shouldnt't you convert the map to an 
#    image before you write it? Just make sure that those last two lines are in the 
#    right order. 

def region_map(country):
    name = country.name
    name = name.lower()
    map_pathname = ("docs\\" + name + ".txt")
    image_pathname = ("source/helpers/images/" + name + "_map.png")

    if os.path.isfile(image_pathname) == False:
        data = open(map_pathname, 'r')
        Map = Country(file=map_pathname)
        map_size = len(Map.regions)

        lat_list = [x.lat for x in Map.regions]
        lon_list = [x.lon for x in Map.regions]
        em_list = [x.emissions for x in Map.regions]

        fig = px.scatter_mapbox(data_frame=em_list, lat=lat_list, lon=lon_list,
                                color=em_list, color_continuous_scale=px.colors.sequential.Viridis,
                                size_max=30, zoom=1.5)

        fig.update_layout(mapbox_style="carto-positron")
        fig.write_image(image_pathname)
        fig.to_image(format="png", engine="kaleido")
