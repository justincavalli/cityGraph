class City:
    # City Object (vertex) for Island Archipelago (graph)

    def __init__(self, name, population):
        self._name = name
        self._population = population

        # list of cities all the cities connected by an edge (road)
        self._connectedCities = []

    def getName(self):
        return self._name
        
    def addConnection(self, city):
        self._connectedCities.append(city)

    def getPopulation(self):
        return self._population

    def getConnections(self):
        return self._connectedCities

    def __str__(self):
        # format how the City object should be printed
        return self._name + " " + str(self._population) + " " + str(self._connectedCities)
