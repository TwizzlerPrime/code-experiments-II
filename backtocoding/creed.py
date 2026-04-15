import random

again = False #used to determine if the player can attack again.
magicstr=0 #player must unlock a spell to gain magic strength.
stats = {
    "player_health":100,
    "player_energy":50,
    "player_coins":10,
    "physicalstr":20,
    "player_shield_health":0,
    "magicstr":0
}

def display_status(stats):
    print("Health: ", stats["player_health"])
    print("Energy: ", stats["player_energy"])
    print("Coins: ", stats["player_coins"])
    print("Physical Strength: ", stats["physicalstr"])
    print("Shield Health: ", stats["player_shield_health"])
    print("Magic Strength: ", stats["magicstr"])

inventory = {
    "healing_spell": False,
    "stun_enchantment": False,
    "Luminescentkatana": False,
    "shield": False,
}
def check_inventory(inventory):
    print("\n--- Your Inventory ---")
    for item, owned in inventory.items():
        status = "Owned" if owned else "Not Owned"
        print(f"{item}: {status}")
    print("----------------------\n")

def attack(target, attacker_stats, attacker_name="You", show_result=True): # currently revamping combat system to be more flexible.
    damage = attacker_stats["physicalstr"]
    if "health" in target:
        target["health"] -= damage
        if target["health"] < 0:
            target["health"] = 0  # Prevent negative health
    else:
        print("Target has no health attribute!")
        return
    if show_result:
        print(f"{attacker_name} attack for {damage} damage! {target.get('name', 'Target')} now has {target['health']} HP.")
    if inventory["stun_enchantment"] and random.random() < 0.5:
        target["stunned"] = True
        print(f"{target.get('name', 'Target')} is stunned!")
    if target["health"] <= 0 and "name" in target:
        print(f"{target['name']} has been defeated!")

def defend(defender_stats, target,):
    
    if  defender_stats["player_shield_health"] > 0:
        print(f"You raise your shield. Blocking {target['name']}'s attack!")
        time.sleep(2)
    
        if random.random() < 0.5:
            print(f"Parry successful!\n Deal {defender_stats["physicalstr"]} damage to {target['name']}.")
            target["health"] -= defender_stats["physicalstr"]
            defended = True
            time.sleep(1)
        else:
            print("Parry failed. Shield takes 10 damage.")
            defender_stats["player_shield_health"] -= target["damage"]
            if defender_stats["player_shield_health"] <= 0:
                print("Your shield is broken!")
                defender_stats["player_shield_health"] = 0
            defended = True
    else:
        print("You don't have a shield or it is broken! Cannot defend.")
        time.sleep(2)
        display_status(defender_stats)

def magic(attacker_stats, targets, primary_index=0): #Parameters for magic attack function are in blue.
    if attacker_stats["player_energy"] < 30:
        print("Not enough energy to use magic.")
        return
    if attacker_stats["player_energy"] >= 30:
        attacker_stats["player_energy"] -= 30
        primary_target = targets[primary_index]
        print(f"You cast poison cloud on {primary_target['name']} for {attacker_stats['magicstr']} damage!")
        primary_target["health"] -= attacker_stats["magicstr"]
    
    for i, target in enumerate(targets): #For every target in the targets list:
        if i != primary_index and target.get("health") > 0:
            target["health"] -= attacker_stats["magicstr"] // 2
            print(f"{target['name']} takes {attacker_stats['magicstr'] // 2} damage.")



print("Welcome to Creed, a not-so welocoming place.")
import time
time.sleep(2)
print("You must fight your way through the Tower to escape.")
time.sleep(1)
while True:
    choice=str(input("Do you want to escape?")).lower()
    if choice == "yes":
        print("You prepare yourself for the journey ahead, and start to head down.")
        time.sleep(1)
        break
    elif choice == "no":
        print("You let yourself be trapped, indefinitely.")
        time.sleep(1)
        exit()
    else:
        print("You must choose: yes or no")
        time.sleep(1)

print("As you head down the tower, you see a chest, a chipped dagger, and a door to the next room.")
time.sleep(1)
while True:
    choice2=str(input("What do you do? (open chest, take dagger, open door)")).lower()
    if choice2 == "open chest":
        print("The chest contains a shield, 20 coins, and a silver sword!")
        time.sleep(1)
        stats["player_coins"]+=20
        print("You got 20 coins!")
        stats["player_shield_health"]=50
        stats["physicalstr"]=20
        inventory["shield"]=True
        display_status(stats)
        break
    elif choice2 == "take dagger":
        print("You grab the dagger, and it feels heavy, and blunt.")
        time.sleep(1)
        stats["physicalstr"]=15
        display_status(stats)
        break
    elif choice2 == "open door":
        print("You ignore the loot and go to the next room.")
        stats["physicalstr"]=5
        time.sleep(1)
        display_status(stats)
        break
    else:
        print("Why are you idle? (open chest, take dagger, open door)")

print("You enter the next room, with a Baron awaiting you")
time.sleep(2)
baron_stats = {
    "name": "Baron",
    "health":50,
    "damage":20
}
while baron_stats["health"] > 0 and stats["player_health"] > 0:
    choice3=str(input("He pulls out his longsword and takes a stance! What will you do? (attack,defend,)")).lower()
    

    if stats["player_health"] <= 0:
            print("You have been defeated by the Baron!")
            break
    defended = False

    
    if choice3 == "attack":
        attack(attacker_stats=stats, target=baron_stats,)
    
    elif choice3 == "defend" and stats["player_shield_health"] > 0:
        defend(defender_stats=stats, target=baron_stats,)  

    
    else:
        print("Choose to attack or defend!")
        continue

    if not defended and again == False and baron_stats["health"] > 0:
        print(f"The Baron attacks you for {baron_stats['damage']} damage!")
        time.sleep(1)
        stats["player_health"] -= baron_stats["damage"]
        display_status(stats)
    
    if stats["player_health"] <= 0:
            print("You have been defeated by the Baron!")
            break
    
    
    
    if baron_stats["health"] <= 0:
        print("The Baron falls to the ground, dropping a mysterious book.")
        time.sleep(1)
        print("You pick up the book, illuminating the room.")
        time.sleep(3)
        print ("Your hands glow green, and you can manifest poison, but it takes energy..")
        time.sleep(2)
        print ("You gain 25 magic strength and 100 coins!")
        stats["magicstr"]=25    
        stats["player_energy"]+=25
        stats["player_coins"]+=100
        display_status(stats)
        break


print("With your new magic powers in hand, you head to the next room.")
time.sleep(2)
print("This room comes with ethereal sounds, and a.. glowing chestplate?")
time.sleep(3)
while True:
    choice4=str(input("What will you do? (take chestplate, explore room)")).lower()
    if choice4 == "take chestplate":
        print("You put on the chestplate, and feel a surge of energy! You feel as if you can't take it off..")
        time.sleep(1)
        stats["player_health"]+=50
        display_status(stats)
        break
    elif choice4 == "explore room":
        print("You ignore the chestplate and explore the room for something else.")
        time.sleep(3)
        display_status(stats)
        break
    else:
        print("Choose wisely! (take chestplate, explore room)")

if stats["player_shield_health"] <= 0:
    print("Behind the chestplate, you find a smithing table, and make yourself a shield.")
    stats["player_shield_health"]=50
    display_status(stats)

elif stats["player_shield_health"] > 0:
    print(" Behind the chestplate, you find a smithing table and repair your shield.")
    stats["player_shield_health"]=50
    display_status(stats) 

print("After your looting, you head down, from the 6th floor to the 5th.")
time.sleep(2)
print("The entrance to the next floor has a strange figure next to it.")
print("Greetings, prisoner. I'm the buisinessman around here. I run, The Table.")
time.sleep(2)
print("The table has lots of teachings and items, but for a small price.")
time.sleep(1)
while True:
    print("The Table includes a healing spell book, a sword stun enchantment, and the Luminescent Katana.")
    time.sleep(1)
    choice5=str(input("Do you want to buy anything? (healing spell, stun enchantment, katana, or leave shop)"))
    if choice5 == "healing spell" and inventory["healing_spell"] == True:
        print("You already have the healing spell!")
        continue
    elif choice5 == "healing spell" and inventory["healing_spell"] == False:
        display_status(stats)
        healchoice=str(input("Are you sure you wish to buy the healing spell for 30 gold?."))
        if stats["player_coins"] < 30:
            print("You don't have enough coins!")
            continue
        elif healchoice == "yes" and stats["player_coins"] >= 30:
            stats["player_coins"]-=30
            print("You buy the healing spell, and learn how to heal yourself.")
        time.sleep(1)
        inventory["healing_spell"]=True
        display_status(stats)
        continue
    
    if choice5 == "stun enchantment" and inventory["stun_enchantment"] == True:
        print("You already have this enchantment!.")
        continue
    elif choice5 == "stun enchantment" and inventory["stun_enchantment"] == False:
        display_status(stats)
        stunchoice=str(input("Are you sure you wish to buy the sword stun enchantment for 50 gold?."))
        time.sleep(3)
        if stats["player_coins"] < 50:
            print("You don't have enough coins!")
            continue
        elif stunchoice == "yes" and stats["player_coins"] >= 50:
            stats["player_coins"]-=50
            print("You buy the sword stun enchantment, and learn how to stun your enemies.")
            inventory["stun_enchantment"]=True
        time.sleep(2)
        display_status(stats)
        continue
    if choice5 == "katana" and inventory["Luminescentkatana"] == True:
        print("You already have the Luminescent Katana!")
        continue
    elif choice5 == "katana" and inventory["Luminescentkatana"] == False:
        display_status(stats)
        katanachoice=str(input("Are you sure you wish to buy the Luminescent Katana for 70 gold?.")).lower()
        if stats["player_coins"] < 70:
            print("You don't have enough coins!")
            continue
        elif katanachoice == "yes" and stats["player_coins"] >= 70:
            stats["player_coins"]-=70
            inventory["Luminescentkatana"]=True
        print("You buy the Luminescent Katana; its razor sharp blade resonates with you..")
        time.sleep(1)
        stats["physicalstr"]=35
        display_status(stats)
        continue
    elif choice5 == "leave shop":
        leavechoice=str(input("Are you sure you want to leave the shop?")).lower()
        if leavechoice == "yes":
            print("You leave the shop, and head to the next room.")
            time.sleep(1)
            display_status(stats)
            break
        elif leavechoice == "no":
            print("You stay in the shop.")
        else:
            print("Well..?: (yes or no)")
            continue
    else:
        print("Choose wisely! (healing spell, stun enchantment, katana)") 



print("After acquiring your new goods, you leave the shop,to an eerie hallway, where 3 henchmen of Galanova await.")
time.sleep(2)
henchmen = [
    {"name": "Henchman 1", "health": 30, "damage": 10, "stunned": False},
    {"name": "Henchman 2", "health": 30, "damage": 10, "stunned": False},
    {"name": "Henchman 3", "health": 30, "damage": 10, "stunned": False}
]
print("This is the guy who beat the Baron? He looks.. weak.")
print()
print("Let's bring his head to Galanova!")
time.sleep(2)

while stats["player_health"] > 0 and any(h["health"] > 0 for h in henchmen):
    print("\nThe henchmen surround you!")
    time.sleep(1)
    print(f"Your health: {stats['player_health']}")
    
    stunned = False
    
    for i, h in enumerate(henchmen):
        if h["health"] > 0:
            print(f"{i + 1}. {h['name']} - Health: {h['health']} {'(Stunned)' if h['stunned'] else ''}")

    swarmchoice=str(input("What will you do? (attack, defend, magic)")).lower()
    defended = False
    
    if swarmchoice == "attack":
        target = int(input("Choose your target (1, 2, or 3): ")) - 1
        if 0 <= target < len(henchmen) and henchmen[target]["health"] > 0:
            defended = False
            attack(henchmen[target], stats, show_result=True)
            time.sleep(2)
                        
        
            
    
    elif swarmchoice == "defend":
        print("You raise your shield, and the henchmen attack!")
        for h in henchmen:
            if h["health"] > 0:
                defend(defender_stats=stats, target=h)
                time.sleep(1)
            
        
        else:
            print("You fail to parry the attack! Your shield takes damage!")
            stats["player_shield_health"] -= 10
            time.sleep(2)    
            display_status(stats)
            defended = True


    if swarmchoice == "magic" and stats["player_energy"] > 0:
        target = int(input("choose your primary target (1, 2 or 3):")) - 1
        if 0 <= target < len(henchmen) and henchmen[target]["health"] > 0:
            magic(attacker_stats=stats, targets=henchmen, primary_index=i)
            time.sleep(3)
            print()
            display_status(stats)
            
        else:
            print ("Not enough energy!")
            time.sleep2
            print()
            display_status(stats)
            time.sleep(2)
            
            if henchmen[target]["health"] <= 0:
                print(f"{henchmen[target]['name']} has been defeated!")
                time.sleep(1)
            else:
                print(f"{henchmen[target]['name']} has {henchmen[target]['health']} health left.")

        if not defended:
            for i, h in enumerate(henchmen):
                if h["health"] > 0 and not h.get("stunned", False):
                    print(f"{h['name']} attacks you for {h['damage']} damage!")
                    stats["player_health"] -= h["damage"]
                    time.sleep(1)
                elif h.get("stunned", False):
                    print(f"{h['name']} is stunned and can't attack!")
                    h["stunned"] = False 

    if all (h["health"] <= 0 for h in henchmen):
        print("All the henchmen have been defeated!")
        time.sleep(1)
        print("After looting them, you feel Galanova's eerie presence.")
        time.sleep(2)
        print("You earned 50 coins and a health restore!")
        stats["player_coins"] += 50
        stats["player_health"] = 100
        display_status(stats)
        break  
import time
time.sleep(3)
print("Galanova speaks.")
print("\n\033[1mYou are the vermin who defeated my.. vermin..\033[0m")
time.sleep(3)
print("\033[1mThere's only so much your underdeveloped subordiantes can do.\033[0m")
time.sleep(2)
print("\033[1mI will grace you with my presence, and end your insignificant life.\033[0m")
time.sleep(2)
print("You prepare yourself for a new, more powerful threat.")
print("Before that though, the Table appears before you.")


print("\n Yes, it is I, again, here to bring you offers from the Table.")
print("You'll have to pay, obviously; I mean you could be stomped by Galanova...")
shopchoice = input("Will you buy anything? (Yes/No)").lower()
if shopchoice == "yes":
    while True:
        print("Great! Here's what I got:")
        time.sleep(0.5)
        print("1. Acid coating spell - 40 coins")
        print("2. Thorns Armour enchantment - 60 coins")
        print("3. Vampirism - 30 coins")
        
        print("And some other options:")
        print("4. Check Inventory")
        print("5. Check balance")
        print("6. Leave Shop")
        choice6 = input("What would you like to do? (1-6)").lower()
        if choice6 == "1" and stats["player_coins"] >= 40:
            if not inventory.get("acid_coating_spell"): 
                input("The Acid coating spell gives your physical weapons a toxin DOT and corrosive effect for 2 turns." \
                "are you sure you wish to buy it? (yes/no)").lower()
                    
                stats["player_coins"] -= 40
                inventory["acid_coating_spell"] = True
                print("You now have the Acid Coating Spell!")
            else:
                print("You already have the Acid Coating Spell!")
            if inventory.get("acid_coating_spell"):
                print("You already have the Acid Coating Spell!")
                
                
                
            



   
        
    
    
            
    
        
