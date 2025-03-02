#Station class for scalability
class Station():
    def __init__(self, name, is_downtime, num_of_sats, maintenance):
        self.__name = name
        self.__is_downtime = is_downtime
        self.__num_of_sats = num_of_sats
        self.__maintenance = maintenance

    #getters
    def getName(self): return self.__name
    def getIsDowntime(self): return self.__is_downtime
    def getNumOfSats(self): return self.__num_of_sats
    def getMaintenance(self): return self.__maintenance


def main() ->None:

    #initialization of stations
    stationA = Station('Station A', False, 0, False)
    stationB = Station('Station B', False, 5, False)

    #testing
    try:
        print(stationA.num_of_sats)
        print(stationB.num_of_sats)
    except:
        print("Values succesfully obfuscated")

    print(stationA.getNumOfSats())
    print(stationB.getNumOfSats())





if __name__ == "__main__":
    main()