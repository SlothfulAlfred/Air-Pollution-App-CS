#-------------------------------------------------
# Name:       bar_chart.py
# Purpose:    To create a bar chart displaying the relative 
#             percentage of greenhouse gasses emitted by each 
#             region
#
# Author:     Alfred Mikhael
# Date:       4-01-2021
#-------------------------------------------------

from .country import Country
import matplotlib.pyplot as plt


def create_bar_regions(count):
    '''
    A function that creates a bar chart of regions in a given country

    parameters
    ----------------------
    countries: Country
        the Country objects that should be represented in the graph

    returns
    -------------------
    True: 
        if the bar graph is succesfully created
    False
        if not given a Country object
    '''
    # breaks out of function if it is empty or parameter is not a list
    if type(count) != Country:
        return False

    # list ojects to store the labels that will be used when creating the bar chart
    labels = count.getRegions()

    # total emissions across the country
    # total = count.getEmissions()

    # list to store the relative percentages
    sizes = [i.getEmissions() for i in count.regions]

    # cleaning up tiny values so as to not crowd the graph
    other_emissions = 0
    index = len(labels) - 1
    while index >= 0:
        if sizes[index] < 65:
            other_emissions += sizes[index]
            del sizes[index]
            del labels[index]
        index -= 1
    if other_emissions:
        labels.append("Other States")
        sizes.append(other_emissions)

    # Initializing labels and sorting   
    labels = ['{0} - {1} Mt'.format(i,round(j, 0)) for i,j in zip(labels, sizes)]
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
    chart.set_title(label=f"Carbon Emissions of states in {count.name} in 2018")
    chart.set_xlabel("Equivalent Carbon Emissions (Megatons)")
    # ensuring that text can always be read
    # if this is not called, the labels might not 
    # fit on the screen
    fig.tight_layout()
    # saving the figure as an image
    fig.savefig('source/gui/images/' + count.name + '_bar.png')
    return True

def create_bar_countries(countries):
    '''
    A function that creates a bar charts of given countries

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
    for place in countries:
        if type(place) != Country:
            return False

    # list of labels
    labels = [country.name for country in countries]

    # Calculating the total greenhouse emissions of the given countries
    # total = sum(country.getEmissions() for country in countries)

    # list of relative percentages
    sizes = [country.getEmissions() for country in countries]

    # cleaning up tiny values so as to not crowd the graph
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
    labels = ['{0} - {1} Mt'.format(i, round(j, 0)) for i,j in zip(labels, sizes)]
    sizes, labels = zip(*sorted(zip(sizes, labels), reverse=True, key=lambda x: x[0]))
    # creating a list of x positions for the bars
    pos = [(i*1.3) for i in range(len(labels))]

    # Creating the bar graph
    # creating the main figure
    fig = plt.figure()
    # adding the chart as a subplot
    chart = fig.add_subplot(2, 1, 1)
    # initalizing horizontal bargraph on subplot
    chart.barh(pos, sizes, height=1.0)
    # setting the tick labels
    chart.set_yticks(pos)
    chart.set_yticklabels(labels)
    chart.set_title(f"Carbon Emissions of North American countries in 2018")
    chart.set_xlabel("Equivalent Carbon Emissions (Megatons)")
    # ensuring that text can always be read
    # if this is not called, the labels might not 
    # fit on the screen
    fig.tight_layout()
    # saving the figure as an image
    fig.savefig('source/gui/images/NA_bar.png')
    return True

if __name__ == '__main__':
    us = Country('USA.txt')
    ca = Country('Canada.txt')
    me = Country('Mexico.txt')
    countries = us
    continent = [us, ca, me]
    if create_bar_regions(countries):
        plt.show()
        if create_bar_countries(continent):
            plt.show()
