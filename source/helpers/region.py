#-------------------------------------------------
# Name:       region.py
# Purpose:    A class that stores information about
#             the greenhouse gas emissions and the coordinates
#             of a given region
#
# Author:     Alfred Mikhael
# Date:       15-01-2021
#-------------------------------------------------

class Region():
    """
    An object that contains the air pollution data and the geocoordinates of a certain area / region

    Attributes
    -----------------------------
    name: string
        The name of the region
    emissions: float
        Greenhouse gas emissions in 2018 measured in megatonnes of CO2
    lat: float
        Latitudinal coordinates of region
    lon: float
        Longitudinal coordinates of region

    Methods
    ---------------------------
    getEmissions() -> float
        returns the greenhouse gas emissions of the region in 2018
    getCoordinates() -> tuple
        returns the latitude and longitude of the region as a tuple
    getName() -> string
        returns the name of the region
    
    """

    def __init__(self, name, em = 0.00, lat = -82.8628, lon = 135.0000):
        '''
        Constructor to initialize a region object

        Parameters
        -----------------------
        name: string
            The name of the region

        em: float
            the annual greenhouse emissions of a region in megatonnes of CO2
            defaults to zero if nothing is input

        lat: float
            the latitudinal coordinates of a region
            defautls to the latitude of Antarctica

        lon: float
            the longitudinal coordinates of a region
            defaults to the longitude of Antarctica

        Raises
        ----------------------
        ValueError
            If the emissions are below zero 
        '''
        if float(em) < 0.00:
            raise ValueError("Cannot have negative emissions")
        self.emissions = float(em)
        self.lat = float(lat)
        self.lon = float(lon)
        self.name = name


    def getEmissions(self) -> float:
        '''
        returns yearly greenhouse gas emissions
        
        Returns
        ----------------------
        float:
            yearly greenhouse gas emissions
        '''
        return self.emissions


    def getCoordinates(self) -> tuple:
        '''
        returns the coordinates of the region

        Returns
        -----------------------
        tuple:
            latitude and longitude coordinates of the region
        '''
        return (self.lat, self.lon)

    def getName(self) -> str:
        '''
        returns the name of the region

        Returns 
        ----------------------------
        string:
            the name of the region
        '''
        return self.name

