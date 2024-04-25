#This file is the publix map that takes in the aisle information and stores it in one map variable.

from Aisle import *

class PublixMap:
    def __init__(self):
        self.map = {}

    def add_section(self, aisle):
        self.map[aisle.get_aisle()] = aisle #adds aisle to dictionary

           