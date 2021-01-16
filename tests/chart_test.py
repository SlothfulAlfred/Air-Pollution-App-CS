#-------------------------------------------------
# Name:       chart_test.py
# Purpose:    tests the functions of pie_chart.py and
#             bar_chart.py using the unittest module
#
# Author:     Alfred Mikhael
# Date:       16-01-2021
#-------------------------------------------------
import unittest
import source.helpers.pie_chart as pie
import source.helpers.bar_chart as bar
import matplotlib.pyplot as plt
from source.helpers.country import Country

class Test_Pie_Chart(unittest.TestCase):
    def setUp(self):
        global cntry
        f = open('chart_data.txt', 'w')
        f.write("Country One\n")
        f.write("Region One, 1.00, 2.00, 3.00\n" + "Region Two, 199.99, 44.88, 153.888\n")
        f.write('\n')
        f.close()
        cntry = Country('chart_data.txt')

    def tearDown(self):
        pass

    def test_pie_chart_regions_params(self):
        chart = pie.create_pie_regions(5)
        self.assertEqual(chart, False)
        chart = pie.create_pie_regions([])
        self.assertEqual(chart, False)

    def test_pie_chart_regions(self):
        countries = cntry
        chart = pie.create_pie_regions(countries)
        self.assertEqual(chart, True)

    def test_bar_chart_regions_params(self):
        chart = bar.create_bar_regions(3535)
        self.assertEqual(chart, False)
        chart = bar.create_bar_regions([])
        self.assertEqual(chart, False)

    def test_bar_chart_regions(self):
       countries = cntry
       chart = bar.create_bar_regions(countries)
       self.assertEqual(chart, True)

if __name__ == '__main__':
    unittest.main()
    
