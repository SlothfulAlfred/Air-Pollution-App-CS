#-------------------------------------------------
# Name:       country.py
# Purpose:    A class that stores information about a country,
#             it's affiliated regions, and it's greenhouse gas emissions
#
# Author:     Alfred Mikhael
# Date:       15-01-2021
#-------------------------------------------------
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
    lat: float
        latitude of the country
    lon: float
        longitutde of the country

    Methods
    -------------------------------
    getEmissions() -> float
        Returns the sum of the emissions of the affiliated regions
    getName() -> str 
        Returns the name of the country 
    getRegions() -> list
        Returns the names of the affiliated regions as a list
    getCoordinates() -> tuple
        Returns a tuple of the coordinates 

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
                first_line = f.readline().strip(' \n').split(',')
                # initialzing attributes
                self.name = first_line[0]
                self.lat = float(first_line[1])
                self.lon = float(first_line[2])

                # initialzing regions list
                q = f.readline().strip(' \n').split(',')
                while(len(q) > 1):
                    self.regions.append(reg.Region(q[0], q[1], q[2], q[3]))
                    q = f.readline().strip(' \n').split(',')
        else:
            logging.error("File not provided")
            raise FileNotFoundError

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
        return [x.getName() for x in self.regions]

    def getCoordinates(self) -> tuple:
        '''
        returns a tuple of the coordinates

        Returns
        --------------------
        tuple
            coordinates
        '''
        return tuple((self.lat, self.lon))



