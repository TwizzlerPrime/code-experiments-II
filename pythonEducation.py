#WARNING: This file is NOT meant to be run. Its for the funsies and education heheheha and it will most likely not work.

#Anything not deleted after testing is useful enough to be replicated for further use.
#List Comprehension Example
Modifiers = ("Darkness, Veiled, Empowered, Enchanted")
ModifiersList = Modifiers.split()
ModLength = [len(modifier) for modifier in ModifiersList if modifier != "Enchanted"]

print(ModifiersList)
print(ModLength)
#genrally useful for creating lists from other lists with conditions

#Lambda usage
f = "bonjour"
y = "mes amis!"
greetings = lambda x,y : x + " " + y
print(greetings(f,y))
#Using a lambda function to create a greeting
#Used to create small anonymous functions for short-term use

#Multiple Function Arguments
def foo(first, second, third, *therest):
    print(f"First: {first}")
    print(f"Second: {second}")
    print(f"Third: {third}")
    print(f"And all the rest... {list(therest)}")

#Sets and set commands
#Sets are collections (lists) of non-dublicate items and values
VibeHouseAtt = set(["Devore," "Afialabi", "Adesanya",])  #Defines VibeHouseAtt as a set
TrapHouseAtt = set(["Belal", "Rafiki", "Ezlivi", "Duckii"]) #Defines TrapHouseAtt as a set of people
print(VibeHouseAtt) #Prints them out
print(TrapHouseAtt)
#Set commands
print(VibeHouseAtt.intersection(TrapHouseAtt))  #Checks for common values in both sets
print(VibeHouseAtt.union(TrapHouseAtt))  #Combines both sets into one
print(VibeHouseAtt.difference(TrapHouseAtt))  #Shows values in VibeHouseAtt that are not in TrapHouseAtt
print(VibeHouseAtt.symmetric_difference(TrapHouseAtt))  #Shows values that are in either set but not both

#Partial Functions
#Partial functions allow you to make a new funtion with preset arguments from another function.
#You first need to import the partial function from the functools module.
from functools import partial
#Now let's say we have a function called "powerGauge" which gauges how much power your character has
#from items in their inventory (a dictionary).
inventory = {
    "Sword": 10,
    "Shield": 5,
    "Potion": 2
}
def powerGuage(inventory):
    return sum(inventory.values())
#Now we can create a partial function that always uses the inventory dictionary.
totalPower = partial(powerGuage, inventory)
print(sum(inventory.values()))  #Prints the total power of the inventory
print(totalPower())  #Calls the partial function to get the same result
    
