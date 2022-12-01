from busid import bus_id


class seat(bus_id):

    def __init__(self, seat_num, place, availability: bool, bus_id):
        super().__init__(bus_id=bus_id)
        self.__seat_num = seat_num
        self.__place = place
        self.__availability = availability

    def set_seat_num(self, seat_num):
        self.__seat_num = seat_num

    def set_place(self, place):
        self.__place = place

    def set_availability(self, availability):
        self.__availability = availability

    def get_seat_num(self):
        return self.__seat_num

    def get_place(self):
        return self.__place

    def get_availability(self):
        return self.__availability
