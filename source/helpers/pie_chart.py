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
from source.helpers.country import Country

def create_pie_regions(count):
    '''
    A function that creates a pie charts of the regions in a given country

    parameters
    ----------------------
    countries: Country
        the Country objects that should be represented in the graph

    returns
    -------------------
    True: 
        if the piechart is succesfully created
    False
        if parameter is not a Country object
    '''
    # Error handling
    if type(count) != Country:
        return False

    # list ojects to store the labels that will be used when creating the pie chart
    labels = count.getRegions()

    # Calculating the total greenhouse emissions of North America
    total = count.getEmissions()

    # Empty list to store the relative percentages
    sizes = [(i.getEmissions() * 100 / total) for i in count.regions]

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

    fig, chart = plt.subplots()
    wedges, dummy = chart.pie(sizes, radius=1, autopct=None)   
    chart.legend(wedges, labels, loc='center left', fontsize=6, bbox_to_anchor=(-0.3, 0.51))
    fig.savefig("source/gui/images/" + count.name + "_pie.png")
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
        if no countries are given, if not given a list, or if the contents of the list
        are not Country objects
    '''

    # breaks out of function if it is empty
    if countries == []:
        return False
    if type(countries) != list:
        return False
    for country in countries:
        if type(country) != Country:
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
    
    # creating subplots
    fig, chart = plt.subplots()
    # creating list of wedges for legend
    wedges, dummy = chart.pie(sizes, radius=1, autopct=None)
    # creating legend and saving figure
    chart.legend(wedges, labels, loc='center left', fontsize=6, bbox_to_anchor=(-0.3, 0.51))
    fig.savefig("source/gui/images/NA_pie.png")
    return True

if __name__ == '__main__':
    us = Country('USA.txt')
    ca = Country('Canada.txt')
    me = Country('Mexico.txt')
    countries = us
    continent = [us, ca, me]
    if create_pie_regions(countries):
        plt.show()
        if create_pie_countries(continent):
            plt.show()
