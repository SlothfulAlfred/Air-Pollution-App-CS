#-----------------------------------------------------------------------------
# Name:        Continent Map Generation(python.py)
# Purpose:     Generates a Scatterbox map of North America,
#              displaying the emissions data for each country.
#
# References: 	This program uses the NumPy/SciPy style of documentation as found
#				here: https://numpydoc.readthedocs.io/en/latest/format.html with
#				some minor modifications based on Python 3 function annotations
#				(the -> notation).
#
# Author:      Rishabh Tamhane
# Created:     06-Jan-2021
# Updated:     07-Jan-2021
#-----------------------------------------------------------------------------

import plotly.express as px
import os
from source.helpers.region import Region
from source.helpers.country import Country

def continent_map():
    '''
    Generates a Scatterbox map of North America, displaying the emissions data for each country.
    '''
    countries = os.listdir('docs')          #List of pathways to countries' data
    i=0
    for i in range(len(countries)):
        countries[i] = str("docs/" + countries[i])          #Appends "docs/" to each element of the list (ensures correct pathways are found)


    #Data Order for All Lists: Canada, USA, Mexico
    image_pathname = ("source/images/continent_map.png")        #List of pathway for the final map

    country_list = []        #List of all countries (contains Country objects)
    lon_list = []         #List of longitudes of the countries' geographic centres
    em_list = []        #List of emissions of CO2 (Mt, 2018) of each country

    i = 1
    if os.path.isfile(image_pathname) == False:       #Checks if the map has already been generated
        while i < len(countries):
            open(countries[i], 'r')         #Loads up a specific country, reads data from countries entry
            Map = Country(file=countries[i])
            country_list.append(Map)        #Adds Country object to country_list
            i = i + 1

        #Save emissions, latitude and longitude data to seperate arrays
        em_list = [country_list[x].getEmissions() for x in range(len(country_list))]        #getEmissions function gets the total emissions of a country
        lat_list = [country_list[x].lat for x in range(len(country_list))]
        lon_list = [country_list[x].lon for x in range(len(country_list))]

        #Generates map
        fig = px.scatter_mapbox(data_frame=em_list, lat=lat_list, lon=lon_list,
                                color=em_list, color_continuous_scale=px.colors.sequential.Bluered,
                                color_continuous_midpoint = 700, range_color = (0,1700),
                                size_max=100, zoom=1.5)
        fig.update_layout(mapbox_style="carto-positron")        #Sets map style
        fig.to_image(format="png", engine="kaleido")
        fig.write_image(image_pathname)         #Exports map
