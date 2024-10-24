class Seat:
    def __init__(self, free: bool, occupant: str):
        self.free = free
        self.occupant = occupant 

    #allows the program to assign someone a seat if it's free
    def set_occupant(self):
        if self.free:
            return True
        else:
            return False   

    # remove someone from a seat and return the name of the person 
    # occupying the seat before
    def remove_occupant(self):
        self.free = True
        name = self.occupant
        self.occupant = None
        return name


class Table:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seats = [Seat(True, None) for _ in range(capacity)] #list of Seat objects (size = capacity)

    # returns a boolean (True if a spot is available)
    def has_free_spot(self):
        if self.left_capacity() > 0:
            return True
        else:
            return False
    #places someone at the table
    def assign_seat(self, name):
        if self.has_free_spot():
            for seat in self.seats:
                if seat.set_occupant():
                    seat.free = False
                    seat.occupant = name
                    break
                else:
                    continue
        else: 
            return False
    # returns an integer
    def left_capacity(self):
        count = 0
        for i in self.seats:
            if i.free:
                count += 1
            else: 
                continue
        self.capacity = count
        return self.capacity