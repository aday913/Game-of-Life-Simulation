# This file will contain the classes necessary to build a player in Life

class Player(object):
    '''
    This object will contain all the necessary information for each player,
    including the amount of money the person has, their current debt,
    how many life tiles they have, their occupation, their house, and the
    number of people they have in their family!
    '''

    def __init__(self, name):
        self.name = name
        self.cash = 0
        self.debt = 0
        self.lifeTiles = 0
        self.house = None
        self.family = None
    
    def get_cash(self):
        return self.cash

    def get_liftTiles(self):
        return self.lifeTiles

    def addCash(self, amount):
        self.cash += amount
    
    def takeCash(self, amount):
        self.cash -= amount

    