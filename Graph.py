import City

class Graph:

    def __init__(self):
        self._myGraph = {}
        self._setupGraph()


    def _setupGraph(self):
        # Create graph by reading in the two text files
        
        cityPop = open('city_population2.txt', 'r')
        roadNet = open('road_network2.txt', 'r')

        while True:
            line = cityPop.readline()

            if not line:
                break
            else:
                str = line.split(" : ")
                name = str[0]
                population = int(str[1])

                # Create a City object to act as a vertex in the graph
                self._myGraph[name] = City.City(name, population)

        while True:
            line = roadNet.readline()

            if not line:
                break
            else:
                str = line.split(" : ")
                outgoing = str[0]
                incoming = str[1].replace("\n", "")

                # for each end (city) of the edge, add the other as a connection
                self._myGraph[outgoing].addConnection(self._myGraph[incoming])
                self._myGraph[incoming].addConnection(self._myGraph[outgoing])

    def BFS(self, vertex):
        # list of all vertices in the island
        visited = []
        # explore one level at a time in BFS
        level = [vertex]

        while len(level) > 0:
            for connection in level.pop().getConnections():
                if connection not in visited:
                    # mark as visited and add to the next level to explore
                    level.append(connection)
                    visited.append(connection)
        
        return visited

    def mapIslands(self):
        # list of cities visited
        visitedCities = []
        # list of islands(list)
        islands = []
        numIslands = 0
        for city in self._myGraph.values():
            # head of a new tree/island
            if city not in visitedCities:
                numIslands += 1
                currIsland = self.BFS(city)
                visitedCities.extend(currIsland)
                islands.append(currIsland)
        
        return islands

    def outputNumIslands(self):
        # print the number of islands in the archipelago
        print("There are", len(self.mapIslands()), "islands in the archipelago.")
    
    def outputPopulations(self):
        islands = self.mapIslands()
        islandNum = 1

        # loop through each city in each island
        for island in islands:
            pop = 0
            for city in island:
                # add up the population of every city in the island
                pop += city.getPopulation()
            print("The population of island number", islandNum, "is", pop)
            islandNum += 1

    def minimumPath(self, city1, city2):
        # to find the minimum path, do BFS again returning the level number
        # when city2 is found

        if(city1 == city2):
            print("The two cities are the same. No highways are needed")
            return
        
        # list of all vertices in the island
        visited = []
        # explore one level at a time in BFS
        level = [self._myGraph[city1]]
        
        levelNum = 1

        while len(level) > 0:
            for connection in level.pop().getConnections():
                if(connection.getName() == city2):
                    # if we reach city2 then return the level as minimum number of highways
                    print("The minimum amount of highways between", city1, "and", city2, "is", levelNum)
                    return
                elif connection not in visited:
                    # mark as visited and add to the next level to explore
                    level.append(connection)
                    visited.append(connection)
            # increase the levelNum
            levelNum += 1

        # never reached city2 so there is no connection
        print(city2, "could not be reached from", city1)

            
        