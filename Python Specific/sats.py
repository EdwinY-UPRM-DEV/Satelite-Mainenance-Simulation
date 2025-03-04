#Satellite class
class Satellite():
    def __init__(self, priority: int, upload_time: float, available: bool, busy_until: float, busy_interval: float, current_sat: str):
        self.__priority = priority
        self.__upload_time = upload_time
        self.__available = available
        self.__busy_until = busy_until
        self.__busy_interval = busy_interval
        self.__current_sat = current_sat

        

#Station class for scalability
class Station():
    def __init__(self, name: str, is_downtime: bool = False, num_of_sats: int = 0, maintenance: bool = False):
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

    def changeName(self, newName):
        if type(newName) == str:
            self.setName(newName)
        else:
            raise "Type must be string"

    def __str__(self):
        return self.getName()
    def __repr__(self):
        return f"Station({self.getName()}, {self.getIsDowntime()}, {self.getNumOfSats()}, {self.getMaintenance()})"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (
            self.getName() == other.getName() and
            self.getIsDowntime() == other.getIsDowntime() and
            self.getNumOfSats() == other.getNumOfSats() and
            self.getMaintenance() == other.getMaintenance()
    )




def main() ->None:

    #Test Cases
    Alpha = Satellite(1, 0.50, True, None, None, None)







if __name__ == "__main__":
    main()