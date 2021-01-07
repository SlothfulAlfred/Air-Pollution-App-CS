import unittest
from Classes.country import Country


class Test_Country(unittest.TestCase):
    def setUp(self):
        global cntry, cntry_two 
        # writing dummy data to file
        inp = open("input.txt.", 'w')
        inp.write("Country One, 20, 30\n")
        inp.write("Region One, 1.00, 2.00, 3.00\n" + "Region Two, 199.99, 44.88, 153.888\n")
        inp.write('\n')
        inp.close()
        inp_two = open('input_two.txt', 'w')
        inp_two.write("Country Two, 40, 50\n")
        inp_two.write("Region Three, 2.33, 3.44, 35.5\n" + "Region Four, 355.5, 89.9, 99.99\n")
        inp_two.write('\n')
        inp_two.close()
        # initializing objects
        cntry = Country("input.txt")
        cntry_two = Country('input_two.txt')

    def tearDown(self):
        pass

    def test_country_initializaiton(self):    
        self.assertEqual(cntry.name, "Country One")
        self.assertEqual(len(cntry.regions), 2)
        self.assertEqual(cntry.lat, 20)
        self.assertEqual(cntry.lon, 30)

    def test_country_methods(self):
        self.assertEqual("Country One", cntry.getName())
        self.assertEqual(200.99, cntry.getEmissions())
        self.assertEqual(["Region One", "Region Two"], [x for x in cntry.getRegions()])
        self.assertEqual(cntry.getCoordinates(), (20, 30))

    def test_country_multiple_initialization(self):
        self.assertEqual(cntry_two.name, "Country Two")
        self.assertEqual(len(cntry_two.regions), 2)
        self.assertEqual(cntry_two.lat, 40)
        self.assertEqual(cntry_two.lon, 50)


if __name__ == "__main__":
    unittest.main()
