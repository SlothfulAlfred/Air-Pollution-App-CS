#-------------------------------------------------
# Name:       pie_chart.py
# Purpose:    To create a pie chart displaying the relative 
#             percentage of greenhouse gasses emitted by each 
#             region
#
# Author:     Alfred Mikhael
# Date:       4-12-2020
# References: MatPlotLib documentation was taken from
#             https://matplotlib.org/3.1.1/gallery/
#             pie_and_polar_charts/pie_features.html
#-------------------------------------------------
import matplotlib as plt
import region
import country

def create():
  # list ojects to store the labels that will be used when creating the pie chart
  labels = []
  # Filling temp with the region names
  for x in country.countries:
    temp = x.getRegions()
    labels += temp

  # Empty list to store the relative percentages
  sizes = []
  # Calculating the total greenhouse emissions of North America
  total = 0
  for x in country.countries:
    x += x.getEmissions()
  # Calculating the relative percentage of total
  for x in country.countries:
    for i in x.regions:
      sizes[i] = i.getEmissions() / total
  
  # Creating subplots
  chart = plt.subplots()
  # Initialzing pie chart  
  chart.pie(sizes, labels)
  chart.axis('equal')

  chart.show()


if __name__ == '__main__':
  create()
