import unittest
import country


class Test_Country(unittest.TestCase):
    def setUp(self):
        inp = open("input.txt.", 'w')
        inp.write("Country One\n")
        inp.write("Region One, 1.00, 2.00, 3.00\n" + "Region Two, 199.99, 44.88, 153.888\n")
        inp.write('\n')
        inp.close()
        global cntry 
        cntry = country.Country("input.txt")

    def tearDown(self):
        pass

    def test_country_initializaiton(self):    
        self.assertEqual(cntry.name, "Country One")
        self.assertEqual(len(cntry.regions), 2)

    def test_country_methods(self):
        self.assertEqual("Country One", cntry.getName())
        self.assertEqual(200.99, cntry.getEmissions())
        self.assertEqual(["Region One", "Region Two"], [x for x in cntry.getRegions()])

if __name__ == "__main__":
    unittest.main()
