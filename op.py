from bus import bus
from seat import seat


class op:
    bus_list: list[bus] = [bus(bus_id=1, location="from gaza to khanyounes"),
                           bus(bus_id=2, location="from khanyounes to gaza"),
                           bus(bus_id=3, location="from Rafah to gaza")]
    seat_list: list[seat] = [seat(bus_id=1, seat_num=1, place="front", availability=True),
                             seat(bus_id=1, seat_num=2, place="mid right", availability=False),
                             seat(bus_id=1, seat_num=3, place="mid left", availability=True),
                             seat(bus_id=1, seat_num=4, place="back right", availability=False),
                             seat(bus_id=1, seat_num=5, place="back lift", availability=True),

                             seat(bus_id=2, seat_num=1, place="front", availability=True),
                             seat(bus_id=2, seat_num=2, place="mid right", availability=True),
                             seat(bus_id=2, seat_num=3, place="mid left", availability=True),
                             seat(bus_id=2, seat_num=4, place="back right", availability=False),
                             seat(bus_id=2, seat_num=5, place="back lift", availability=False),

                             seat(bus_id=3, seat_num=1, place="front", availability=False),
                             seat(bus_id=3, seat_num=2, place="mid right", availability=False),
                             seat(bus_id=3, seat_num=3, place="mid left", availability=True),
                             seat(bus_id=3, seat_num=4, place="back right", availability=True),
                             seat(bus_id=3, seat_num=5, place="back lift", availability=True)]

    def busses(self, x):
        for i in self.bus_list:
            if int(x) == 1:
                print(i.get_bus_id(), i.get_location())
            else:
                print("error")
                exit()

    def seats(self, y):
        for i in self.seat_list:
            if int(i.get_bus_id()) == int(y):
                print(i.get_seat_num(), i.get_place(), i.get_availability())

    def booking(self, z, y):
        for i in self.bus_list:
            if int(i.get_bus_id()) == int(y):
                for i in self.seat_list:
                    if int(i.get_seat_num()) == int(z) and i.get_availability() == True:
                        return "your seat has been booked"
                    else:
                        print("seat is not available")
                        exit()

    @staticmethod
    def check_input_is_empty(*input):
        for item in input:
            if item.isspace() or item == "":
                print("empty input")
                exit()
            else:
                pass
