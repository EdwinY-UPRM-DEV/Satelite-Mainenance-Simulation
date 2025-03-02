#Station class for scalability
class Station():
    def __init__(self, name: str, is_downtime: bool, num_of_sats: int, maintenance: bool):
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


    #Custom Functions
    def switchingDowntime(self):
        if self.getIsDowntime:
            self.setIsDowntime(False)
        else:
            self.setIsDowntime(True)

    def switchingMaintenance(self):
        if self.getMaintenance():
            self.setMaintenance(False)
        else:
            self.setMaintenance(True)

    def increaseNumOfSats(self, s=None):
        if not s:
            self.setNumOfSats(self.getNumOfSats() + 1)
        else:
            #abs to remove accidental flipping of signs
            self.setNumOfSats(self.getNumOfSats() + abs(s))

    def decreaseNumOfSats(self, s=None):
        if not s:
            self.setNumOfSats(0 if (self.getNumOfSats() - 1) < 0 else self.getNumOfSats() - 1)
        else:
            #abs to remove accidental flipping of signs
            self.setNumOfSats(0 if (self.getNumOfSats() - abs(s)) < 0 else self.getNumOfSats() - abs(s))



def main() ->None:

    #initialization of stations
    stationA = Station('Station A', False, 0, False)
    stationB = Station('Station B', False, 5, False)

    #testing - all OK
    print("Before increase: ", stationA.getNumOfSats())
    stationA.increaseNumOfSats()

    print("Normal Increase: ",stationA.getNumOfSats())
    stationA.increaseNumOfSats(5)
    print("Increase by 5: ",stationA.getNumOfSats())

    stationA.decreaseNumOfSats()
    print("Decrease normal: ", stationA.getNumOfSats())
    stationA.decreaseNumOfSats(2)
    print("Decrease by 2: ",stationA.getNumOfSats())
    stationA.decreaseNumOfSats(20)
    print("Absurd decrease: ", stationA.getNumOfSats())

    









if __name__ == "__main__":
    main()