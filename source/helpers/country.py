import .region as reg
import logging

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

    Methods
    -------------------------------
    getEmisssions() -> float
        Returns the sum of the emissions of the affiliated regions
    getName() -> str
        Returns the name of the country
    getRegions -> list
        Returns the names of the affiliated regions as a list

    '''
    def __init__(self, file = None):
        '''
        Constructor to initialize a country object and it's corresponding region objects

        Parameters
        --------------------------------
        file: string
            the name of the input file that will be used to initialize the objects
            defaults to None
        
        Raises
        ----------------------------------
        FileNotFoundError
            If no file is provided
        '''
        self.regions = []
        if file:
            with open(file, 'r') as f:
                self.name = f.readline().strip(' \n')
                q = f.readline().strip(' \n').split(',')
                while(len(q) > 1):
                    self.regions.append(reg.Region(q[0], q[1], q[2], q[3]))
                    q = f.readline().strip(' \n').split(',')
        else:
            raise FileNotFoundError(logging.log("File not provided"))

    def getEmissions(self) -> float:
        '''
        returns the emissions of the country

        Returns
        -----------------------------
        float
            sum of the emissions of the afilliated regions
        '''
        return sum(x.getEmissions() for x in self.regions)

    def getName(self) -> str:
        '''
        returns the name of the country

        Returns
        ----------------------------------
        string
            the name of the country
        '''
        return self.name

    def getRegions(self) -> list:
        '''
        returns a list of the names of the affiliated regions
        
        Returns
        --------------------------------
        list
            a list of the names of the affiliated regions
        '''
        return (x.getName() for x in self.regions)

