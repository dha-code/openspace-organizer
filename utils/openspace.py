import random
import pandas as pd
from collections.abc import Sequence
from table import Table

class Openspace:
    """
    A class which mimics the office setup with tables.
    Each instance has a list of tables and the number of tables

    """
    def __init__(self, capacity: int, number_of_tables: int) -> None:
        """ 
        Constructor which initialises the object

        :param capacity: int with number of seats in each table
        :param number_of_tables :int with tables in the openspace
        :return Openspace object :obj with Tables in an office space
        """
        self.number_of_tables = number_of_tables
        self.capacity = capacity
        self.tables = [Table(capacity) for _ in range(number_of_tables)]
    
    def __str__(self) -> str:
        """
        Returning a string representation of the object instead of the memory adress of the object
        """
        return "An office space with {self.number_of_tables} tables and {self.capacity} seats per table".format(self=self)
    
    def display(self) -> None:
        """
        Function which will display the overlay of the office tables.
        No explicit parameters just the self object 
        """
        count = 1
        for each_table in self.tables:
            print("\n-----------------------------------------------------------------")
            print(f"Table {count} | ",end='')
            count += 1
            for each_seat in each_table.seats:
                print(f"{each_seat.occupant} | ",end='')
        print("\n-----------------------------------------------------------------")
    
    def organize(self, names) -> None:
        """
        Function which will assign each person in the list given a random table.

        :param names: A list of people need to be placed at the tables.
        """
        number_of_spots = self.number_of_tables * self.capacity
        while names and number_of_spots:
            rand_tab = random.randint(0,self.number_of_tables-1)
            if self.tables[rand_tab].has_free_spot():
                self.tables[rand_tab].assign_seat(names[0])
                names.pop(0)
                number_of_spots -= 1

    def store(self, filename: str) -> None:
        """
        Function which will store the table structure.

        :param filename: A string which has the name of the file to save the table layout
        """
        workspace = [[each_seat.occupant for each_seat in each_table.seats] for each_table in self.tables]
        to_save = pd.DataFrame(workspace)
        to_save.to_excel(filename,header=False, index=False)