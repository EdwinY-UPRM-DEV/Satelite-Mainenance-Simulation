class Station():
    def __init__(self, name, downtime_link_active, num_of_sats, maintenance):
        self.name = name
        self.downtime_link_active = downtime_link_active
        self.num_of_sats = num_of_sats
        self.maintenance = maintenance

def main() ->None:

    stationA = Station('Station A', False, 0, False)
    stationB = Station('Station B', False, 0, False)




if __name__ == "__main__":
    main()