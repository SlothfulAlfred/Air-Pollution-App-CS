import unittest
import source.helpers.region

class Test_Region(unittest.TestCase):
    def setUp(self):
        inp = open("input.txt", 'w')
        inp.write("Sinnoh Region, 1000000, -100, -190\n")
        inp.write("Jotoh Region, 0.01, 0.00, 0.43\n")
        inp.write("Unova, 25.0, 30.0, 30.0")
        inp.close()

    def test_region_init(self):
        with open("input.txt", 'r') as f:
            global m 
            m = []
            q = f.readline().strip(' \n').split(',')
            while (len(q) > 1):
                m.append(region.Region(q[0], q[1], q[2], q[3]))
                q = f.readline().strip(' \n').split(',')

        self.assertEqual(m[0].name, "Sinnoh Region")
        self.assertEqual(m[1].emissions, 0.01)
        self.assertEqual((m[2].lat, m[2].lon), (30.0, 30.0))

    def test_region_methods(self):
        self.assertEqual(m[2].getName(), "Unova")
        self.assertEqual(m[2].getEmissions(), 25.0)
        self.assertEqual(m[1].getCoordinates(), (0.00, 0.43))
                
if __name__ == '__main__':
    unittest.main()
