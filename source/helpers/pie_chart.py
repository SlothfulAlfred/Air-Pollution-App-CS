#-------------------------------------------------
# Name:       pie_chart.py
# Purpose:    To create a pie chart displaying the relative 
#             percentage of greenhouse gasses emitted by each 
#             region
#
# Author:     Alfred Mikhael
# Date:       4-12-2020
# References: MatPlotLib documentation was taken from
#             https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html
#-------------------------------------------------
import matplotlib.pyplot as plt
From .country import Country


def create_pie_regions(countries):
    '''
    A function that creates a pie charts of the regions in given countries

    parameters
    ----------------------
    countries: list
        a list of the Country objects that should be represented in the graph

    returns
    -------------------
    True: 
        if the piechart is succesfully created
    False
        if no countries are given or if not given a list
    '''
    # breaks out of function if it is empty
    if countries == []:
        return False
    if type(countries) != list:
        return False
    # list ojects to store the labels that will be used when creating the pie chart
    labels = []
    # Filling temp with the region names
    for x in countries:
      temp = x.getRegions()
      labels += temp

    # Empty list to store the relative percentages
    sizes = []

    # Calculating the total greenhouse emissions of North America
    total = 0
    for x in countries:
      total += x.getEmissions()

    # Calculating the relative percentage of total
    for x in countries:
      for i in x.regions:
        sizes.append(i.getEmissions() * 100/ total)

    # cleaning up tiny values so as to not crowd the legend
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

    # Creating the pie chart and the legend
    figure, chart = plt.pie(sizes, radius=1, center=(10, 0))
    plt.legend(figure, labels, loc='center left', fontsize=6, bbox_to_anchor=(-0.3, 0.51))
    return True


def create_pie_countries(countries):
    '''
    A function that creates a pie charts of given countries

    parameters
    ----------------------
    countries: list
        a list of the Country objects that should be represented in the graph

    returns
    -------------------
    True: 
        if the piechart is succesfully created
    False
        if no countries are given or if not given a list
    '''

    # breaks out of function if it is empty
    if countries == []:
        return False
    if type(countries) != list:
        return False

    # list of labels
    labels = [country.name for country in countries]

    # Calculating the total greenhouse emissions of North America
    total = sum(country.getEmissions() for country in countries)

    # list of relative percentages
    sizes = [(x.getEmissions() * 100/total) for x in countries]

    # cleaning up tiny values so as to not crowd the legend
    other_emissions = 0
    index = len(labels) - 1
    while index >= 0:
        if sizes[index] < 1.2:
            other_emissions += sizes[index]
            del sizes[index]
            del labels[index]
        index -= 1

    if other_emissions > 0:
        labels.append("Other States")
        sizes.append(other_emissions)

    # Initializing labels and sorting   
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, sizes)]
    sizes, labels = zip(*sorted(zip(sizes, labels), reverse=True, key=lambda x: x[0]))

    # Creating the pie chart and the legend
    figure, chart = plt.pie(sizes, radius=1, center=(10, 0))
    plt.legend(figure, labels, loc='center left', fontsize=6, bbox_to_anchor=(-0.25, 0.91))
    return True

if __name__ == '__main__':
    us = Country('USA.txt')
    ca = Country('Canada.txt')
    me = Country('Mexico.txt')
    countries = [us]
    continent = [us, ca, me]
    if create_pie_regions(countries):
        # plt.show()
        if create_pie_countries(continent):
            plt.show()
