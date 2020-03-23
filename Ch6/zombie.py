import zombiedice
import random

"""
1. A bot that, after the first roll, randomly decides if it will continue or stop
2. A bot that stops rolling after it has rolled two brains
3. A bot that stops rolling after it has rolled two shotguns
4. A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
5. A bot that stops rolling after it has rolled more shotguns than brains
"""

class MyZombie_1:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            r = (random.randint(0,1))
            if r == 0:
                diceRollResults = zombiedice.roll()
            else:
                break

class MyZombie_2:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MyZombie_3:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MyZombie_4:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            for i in range(4):
                if shotgun < 2:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break
            break

class MyZombie_5:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotgun > brains:
                break # roll again
            else:
                diceRollResults = zombiedice.roll()

zombies = (
    MyZombie_1(name='Random'),
    MyZombie_2(name='Stop at 2 Brains'),
    MyZombie_3(name='Stop at 2 Shotguns'),
    MyZombie_4(name='Roll 4 Times'),
    MyZombie_5(name='Stop at SmB')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)