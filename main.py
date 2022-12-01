from bus import bus
from busid import bus_id
from op import op
from seat import seat

at = op()

print("wellcome")
x = input("if you want to book a seat enter 1 \n")
at.check_input_is_empty(x)
at.busses(x)
y = input("pick your bus\n")
at.check_input_is_empty(y)
at.seats(y)
print("-true= available and false= not available-")
z = input("pick your seat ")
at.check_input_is_empty(z)
print(at.booking(z, y))
