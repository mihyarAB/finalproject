from busid import bus_id


class bus(bus_id):

    def __init__(self, bus_id, location):
        super().__init__(bus_id=bus_id)
        self.__location = location

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location
