def ticket(passenger_type):
    fare = 50
    passenger_type = passenger_type.upper().strip()
    if passenger_type == "A":
        fare = 50
    elif passenger_type == "S":
        fare = 45
    elif passenger_type == "C" or passenger_type == "E":
        fare = 25
    return fare


p = input("passenger type [A]dult, [S]tudent, [C]hild, [E]lder -> ")
print(ticket(p))
