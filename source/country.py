
class Country():
    '''
    An object that contains a list of associated Region objects (ex. Canada contains provinces/territories)

    Attributes
    ----------------------------------
    regions: list
        contains Region objects associated with the Country object
        defaults to an empty list
    name: string
        Name of the country

    '''
    def __init__(self, name, file = None):
        '''
        '''
        regions = []
        self.name = name
        if file:
            with open(file, 'r') as f:
                self.name = f.readline().strip(' \n')
                while(f.readline() != '\n'):
                    q = f.readline().strip(' \n').split(',')
                    regions.append(Region(q[0], float(q[1]), float(q[2]), float(q[3])))

    def getEmissions(self) -> float:
        return (sum(x.getEmissions() for x in self.regions))

    def getName(self) -> str:
        return self.name

    def getRegions(self) -> str:
        yield (x.getName() for x in self.regions)
