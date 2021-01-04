#-------------------------------------------------
# Name:       bar_chart.py
# Purpose:    To create a bar chart displaying the relative 
#             percentage of greenhouse gasses emitted by each 
#             region
#
# Author:     Alfred Mikhael
# Date:       4-01-2021
#-------------------------------------------------

import Classes.country
import matplotlib.pyplot as plt
import random

def create_bar_regions(countries):
    '''
    A function that creates a bar charts of regions in given countries

    parameters
    ----------------------
    countries: list
        a list of the Country objects that should be represented in the graph

    returns
    -------------------
    True: 
        if the bar graph is succesfully created
    False
        if no countries are given or if not given a list
    '''
    
   # breaks out of function if it is empty or parameter is not a list
    if countries == []:
        return False
    if type(countries) != list:
        return False

    # list ojects to store the labels that will be used when creating the bar chart
    labels = []
    # Filling temp with the region names
    for x in countries:
      temp = x.getRegions()
      labels += temp

    # Empty list to store the relative percentages
    sizes = []

    # Calculating the total greenhouse emissions of the given countries
    total = 0
    for x in countries:
      total += x.getEmissions()
        
    # Calculating the percentage emitted by each region
    for x in countries:
      for i in x.regions:
        sizes.append(i.getEmissions() * 100/ total)


    # cleaning up tiny values so as to not crowd the graph
    other_emissions = 0
    index = len(labels) - 1
    while index >= 0:
        if sizes[index] < 1.2:
            other_emissions += sizes[index]
            del sizes[index]
            del labels[index]
        index -= 1
    labels.append("Other States")
    sizes.append(other_emissions)

    # Initializing labels and sorting   
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, sizes)]
    sizes, labels = zip(*sorted(zip(sizes, labels), reverse=True, key=lambda x: x[0]))
    # creating a list of x positions for the bars
    pos = [(i*1.3) for i in range(len(labels))]

    # Creating the bar graph
    # creating the main figure
    fig = plt.figure()
    # adding the chart as a subplot
    chart = fig.add_subplot(1, 1, 1)
    # initalizing horizontal bargraph on subplot
    chart.barh(pos, sizes, height=1.0)
    # setting the tick labels
    chart.set_yticks(pos)
    chart.set_yticklabels(labels)
    # ensuring that text can always be read
    # if this is not called, the labels might not 
    # fit on the screen
    fig.tight_layout()
    return True


if __name__ == '__main__':
    us = Classes.country.Country('USA.txt')
    countries = [us]
    if create_bar_regions(countries):
        plt.show()
