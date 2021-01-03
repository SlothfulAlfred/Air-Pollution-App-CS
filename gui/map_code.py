import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import sys
import os
# if you are nog going to use json, sys, and os then don't import them

# I don't know what this is supposed to be but if it's unnecessary then delete it

#Sets the file path. 
print(os.getcwd())
path_parent = os.path.dirname(os.getcwd()) #Finds where the file is
os.chdir(path_parent)
print(os.getcwd())

#Imports the two classes used
from source.helpers.region import Region
from source.helpers.country import Country
data = open(r"map\docs\canada.txt") #dataset for the map

#calling the country class imported. Finds the data set to be used
Canada = Country(file = "map\docs\canada.txt")
#variable establishing how large the document is and how many regions there are. Region is a list within country. Each object in the list is of the region class
canada_size = len(Canada.regions)
#setting up lists for lattitude, longitude and emissions
lat_list = []
lon_list = []
em_list = []

# I'm very confused why you used a while loop here? Not that I'm against while loops but even then
# it should be while i < len(Canada.regions). If you were using a for loop it would be 
# for i in range(len(Canada.regions)). Also it would be much much much better if you put 
# this stuff into a function. That way it is generalized and callable. 

#We call the regions list within the Canada object. There is always a Regions object in the list, we then read the latitude value of the object, before appending it to the list and iterating.
i = 0
while i in range (len(Canada.regions)):
    lat_val = Canada.regions[i]
    lat_val = lat_val.lat
    print(lat_val)
    lat_list.append(lat_val)
    print("Lat:",lat_list[i])
    i = i+1

# Secondly, you're using a redundantly long way to fill the lists. One of the best things about python is that it has 
# list comprehension. That means your entire while loop can be condensed into a single line. I'd like you to try it
# first and if you're stuck you can ask me and I'll help out. 
# The general structure for list comprehension is
# name_of_list = [variable (iterable, optional) condition], for example:
#
# numbers = [x for x in range(10)] 
# print(numbers)
# >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# An example with conditions and an iteration:
#
# numbers = [x for x in range(20) if x % 2 == 0]
# print(numbers)
# >> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Hope that helps

#same as the last loop except the longitude value of the object is read instead

i = 0
while i in range (len(Canada.regions)):
    lon_val = Canada.regions[i]
    lon_val = lon_val.lon
    print(lon_val)
    lon_list.append(lon_val)
    print("Lon:",lon_list[i])
    i = i+1
#same as the last loop except the emissions value of the object is read instead
i = 0
while i in range (len(Canada.regions)):
    em_val = Canada.regions[i]
    em_val = em_val.emissions
    print(em_val)
    em_list.append(em_val)
    print("EM:",em_list[i])
    i = i+1

#assigning the data variable that mapbox uses to the list of emission values
df = em_list

# Make sure that you can change the sizes of the markers in plotly express
# otherwise please switch to plotly.graph_objects before you get too 
# invested in this. The documentation is on the scatter mapbox page

#Generate the map as a scatter map. Fig.show is the function that causes it to appear in the users browser
fig = px.scatter_mapbox(df, lat=lat_list, lon=lon_list,
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=25, zoom=1.5)
fig.update_layout(mapbox_style="carto-positron")
fig.show()
#Saves it as a png within the program
fig.write_image("map/images/fig1.png")
fig.to_image(format="png", engine="kaleido")
