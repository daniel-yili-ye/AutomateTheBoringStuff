import random
numberOfStreaks = 0

coin = ["H", "T"]
htlist = []

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    current = random.choice(coin)
    htlist.append(current)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    if current == "T":
        streakCounter += 1
        if streakCounter >= 6:
            numberOfStreaks += 1
    else:
        streakCounter = 0

print ("Chance of streak: %s%%" % (numberOfStreaks / 100))