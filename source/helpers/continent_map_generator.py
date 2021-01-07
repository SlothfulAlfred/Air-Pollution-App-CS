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
# Created:     13-Jan-2021
# Updated:     13-Jan-2021
#-----------------------------------------------------------------------------

import plotly.express as px
import os
from region import Region
from country import Country

# I strongly strongly strongly strongly suggest that you just take a list of Country
# objects here. You should write your code with the mentality that it might need
# to be updated and/or maintained in the future so make it easy for yourself.

# In the PEP-8 standards, inline comments need to be separated from the code by 
# at least 2 indentations (8 spaces). Also you should generally avoid them and 
# opt for block comments which are like what I'm writing now. These are on a 
# separate line and refer to all/most of the code that is on the same indentation as 
# them or in the following block. 

def continent_map():
    '''
    Generates a Scatterbox map of North America, displaying the emissions data for each country.
    '''

    #Data Order for All Lists: Canada, USA, Mexico
    data_pathname = ["docs\canada.txt","docs\\usa.txt","docs\\mexico.txt"] #List of pathways to countries' data
    image_pathname = ("source/helpers/images/continent_map.png") #List of pathway for the final map

    # You should use the new built-in lat and lon attributes in the 
    # Country class. I used these values to create it so the map
    # won't change much.
    #
    # filling out emissions list would be better using list comprehension. 
    
    lat_list = [49.6937, 39.8283, 19.432608] #List of latitudes of the countries' geographic centres
    lon_list = [-96.8441, -98.5795, -99.133209] #List of longitudes of the countries' geographic centres
    em_list = [] #List of emissions of CO2 (Mt, 2018) of each country

    i = 0
    if os.path.isfile(image_pathname) == False: #Checks if the map has already been generated
        while i <= 2:
            
            open(data_pathname[i], 'r') 
            Map = Country(file=data_pathname[i]) #Loads up a specific country, reads data from data_pathname
            emissions = Map.getEmissions() #getEmissions function gets the total emissions of a country
            em_list.append(emissions) #Appends emissions value of country to em_list

            i = i + 1
            
        fig = px.scatter_mapbox(data_frame=em_list, lat=lat_list, lon=lon_list, #Generates map of continent
                                color=em_list, color_continuous_scale=px.colors.sequential.Bluered,
                                color_continuous_midpoint = 700, range_color = (0,1700),
                                size_max=100, zoom=1.5,
                                )

        fig.update_layout(mapbox_style="carto-positron") #Sets map style
        fig.to_image(format="png", engine="kaleido")
        fig.write_image(image_pathname) #Exports map
