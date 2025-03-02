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

    #setters
    def setName(self, newName) -> None:  self.__name = newName
    def setIsDowntime(self, newDownTime) -> None:  self.__is_downtime = newDownTime
    def setNumOfSats(self, newNumOfSats) -> None:  self.__num_of_sats = newNumOfSats
    def setMaintenance(self, newMaintenance) -> None:  self.__maintenance = newMaintenance



    def switchingDowntime(self):
        if self.getIsDowntime:
            self.setIsDowntime(False)
        else:
            self.setIsDowntime(True)





def main() ->None:

    #initialization of stations
    stationA = Station('Station A', False, 0, False)
    stationB = Station('Station B', False, 5, False)

    #testing - all OK

    print(stationA.getIsDowntime(), stationA.getName())
    stationA.setIsDowntime(True)
    stationA.setName('Station C')
    print(stationA.getIsDowntime(), stationA.getName())
    stationA.switchingDowntime()
    print(stationA.getIsDowntime())






if __name__ == "__main__":
    main()