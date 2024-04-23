from Aisle import *

class PublixMap:
    def __init__(self):
        self.map = {}

    def add_section(self, aisle):
        self.map[aisle.get_aisle()] = aisle

           