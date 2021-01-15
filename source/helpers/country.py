import Classes.region as reg
import logging

# Pointer (more like a file index) to current file position to aid initialization of 
# multiple Country objects

ptr = 0 #Good idea, if its possible see if you can implement it into the Region Class (there are going to be more of them than Country objects)

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
    getEmisssions() -> float #Typo (Emissions)
        Returns the sum of the emissions of the affiliated regions
    getName() -> str #This function feels redundant, as name is a callable attribute
        Returns the name of the country
    getRegions() -> list 
        Returns the names of the affiliated regions as a list
    getCoordinates() -> tuple #This function feels redundant, as the latitude and longitude are callable attributes. Additionally, it seems strange to call them as a tuple, rather than a string or list. Is there any specific advantages to tuples?
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
                    q = f.readline().strip(' \n').split(',') #Very clean, no changes here!
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
        return sum(x.getEmissions() for x in self.regions) #Very clean, no changes here!

    def getName(self) -> str: 
        '''
        returns the name of the country

        Returns
        ----------------------------------
        string
            the name of the country
        '''
        return self.name #Redundant, see methods

    def getRegions(self) -> list:
        '''
        returns a list of the names of the affiliated regions
        
        Returns
        --------------------------------
        list
            a list of the names of the affiliated regions
        '''
        return (x.getName() for x in self.regions) #Very clean, no changes here!

    def getCoordinates(self) -> tuple:
        '''
        returns a tuple of the coordinates

        Returns
        --------------------
        tuple
            coordinates
        '''
        return tuple((self.lat, self.lon)) #Redundant, see methods

