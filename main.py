from island import Island
from character import Enemy, Character, Friend
from item import Item
import time
import random as r

#Naming the islands and describing them

fuschia = Island("Fuschia Village")
fuschia.set_description("A peaceful village by the sea and your home. It's quiet now, but adventure is calling.")

gecko = Island("Gecko Island")
gecko.set_description("A foggy, forest-covered island home to wild beasts and hidden paths. Adventurers often go missing here.")

syrup = Island("Syrup Village")
syrup.set_description("A quiet town with strange activity near the hilltop mansion. Not everything is as peaceful as it seems.")

orange = Island("Orange Town")
orange.set_description("Once a lively port, now reduced to rubble by a mad clown.")

shells = Island("Shells Town")
shells.set_description("A town ruled by a tyrannical Marine captain. Justice has long been forgotten here.")

baratie = Island("Baratie")
baratie.set_description("A floating restaurant with the finest food—and the fiercest brawls on the sea.")

loguetown = Island("Loguetown")
loguetown.set_description("The city where the Pirate King was executed. The Navy watches everyone, and danger hides in plain sight.")

cocoyasi = Island("Cocoyasi Village") 
cocoyasi.set_description("A sunny island ruled by fear. Locals are oppressed by a ruthless pirate crew demanding tribute.")

twincape = Island("Twin Cape")
twincape.set_description("A cliffside lighthouse and the entrance to the Grand Line. An old man watches over a giant, emotional whale.")

#Linking all the islands together

twincape.link_island(fuschia, "north")
fuschia.link_island(twincape, "south")
fuschia.link_island(gecko, "north")
gecko.link_island(fuschia, "south")
gecko.link_island(shells, "north")
shells.link_island(gecko, "south")
shells.link_island(orange, "north")
orange.link_island(shells, "south")
orange.link_island(syrup, "east")
orange.link_island(loguetown, "north")
orange.link_island(baratie, "west")
syrup.link_island(orange, "west")
loguetown.link_island(orange, "south")
baratie.link_island(orange, "east")
baratie.link_island(cocoyasi, "south")
cocoyasi.link_island(baratie, "north")

#Setting characters to different islands

forest_bandit = Enemy("Bush bandit", "Just a typical bandit. Practice your first battle here!")
forest_bandit.set_health(30)
forest_bandit.set_type("light")
gecko.set_enemy(forest_bandit)

usopp = Friend("Usopp", "A tall tale telling sharpshooter")
syrup.set_friend(usopp)

kuro = Enemy("Kuro", "Pretending to be Kaya's butler. Revealed as a pirate plotting to take her fortune")
kuro.set_health(130)
kuro.set_type("heavy")
syrup.set_enemy(kuro)

nami = Friend("Nami", "A clever navigator with a tragic past")
cocoyasi.set_friend(nami)

arlong = Enemy("Arlong", "Ruthless Fishman leader who enslaves the town. Extremely strong")
arlong.set_health(160)
arlong.set_type("heavy")
cocoyasi.set_enemy(arlong)

buggy = Enemy("Buggy the Clown", "A flashy pirate who loves dramatic entrances")
buggy.set_health(110)
buggy.set_type("medium")
orange.set_enemy(buggy)

zoro = Friend("Zoro", "A swordsman imprisoned for protecting a child. Aspires to be in the world's strongest crew")
shells.set_friend(zoro)

morgan = Enemy("Captain Morgan", "A corrupt Marine leader who rules by fear")
morgan.set_health(120)
morgan.set_type("light")
shells.set_enemy(morgan)

sanji = Friend("Sanji", "A chivalrous chef who values food")
baratie.set_friend(sanji)

don_krieg = Enemy("Don Krieg", "A heavily armed pirate warlord with gas attacks and brute force")
don_krieg.set_health(150)
don_krieg.set_type("heavy")
baratie.set_enemy(don_krieg)

smoker = Enemy("Captain Smoker", "A Marine captain wtih smoke powers. Tracks pirates relentlessly")
smoker.set_health(170)
smoker.set_type("heavy")
loguetown.set_friend(smoker)

#Setting items to different islands

log_pose = Item("Log Pose")
log_pose.set_description("A special compass that stores the location of each island. It allows travel through the Grand Line.")
twincape.set_item(log_pose)

#Setting different requirements for different islands

syrup.requirements = ["Zoro"]
orange.requirements = ["Zoro"]
baratie.requirements = ["Zoro", "Usopp"]
cocoyasi.requirements = ["Zoro", "Usopp", "Sanji"]
loguetown.requirements = ["Zoro", "Usopp", "Sanji", "Nami"]
twincape.requirements = ["Zoro", "Usopp", "Sanji", "Nami"]

#Setting the game out

current_island = fuschia
dead = False
player_health = 100
crew = []
bag = []

#Game introduction

print("You are a young pirate, setting sail from the quiet village of Fuschia Village in the East Blue with a dream that reaches as far as the Grand Line.")
time.sleep(3.0)
print("Armed with nothing but determination, you begin your journey through the unpredictable seas telling everybody you will be...")
time.sleep(2.0)
print("The King of the Pirates!")
time.sleep(1)
print("Your adventure begins now.")
time.sleep(1.5)
print("Type help at any time to view commands.")
time.sleep(1.5)

# While the user is alive, the game will not end

while dead == False:
    random = r.random()
    print("\n")
    current_island.get_details()
    inhabitant = current_island.get_enemy()
    crewmate = current_island.get_friend()
    item = current_island.get_item()
    if inhabitant is not None:
        inhabitant.describe()
    if inhabitant == None and crewmate is not None:
        crewmate.describe()

# Chance of spawn for eating

    if "Sanji" not in crew:
        if random > 0.75:
            print("A restaurant nearby opened up. Type 'eat' in order to heal!")
            heal = 30
    else:
        if random > 0.6:
            print("Your chef, Sanji, has made you some food. Type 'eat in order to heal!")
            heal = 50
    print("Health: " + str(player_health) + "/100")
    command = input("> ")

# Commands that may be used in the game

    if command.lower() == "help":
        print("""eat = Heals your character. ensure a restaurant has opened up or your cook has made you some food!
recruit = Used to recruit friends into your crew
inspect = Look around the island you are currently on to see if there is anything you may pick up
              
fight = Used to engage in combat with enemies
WHILE IN COMBAT
hit = To hit an enemy using a light, medium or heavy attack
dodge = To dodge an enemy attack and as a result, receiving a damage multiplier
run = Only to be used in special cases. It could save your life once
              
travel = Used to move across islands
WHILE TRAVELLING
'north', 'south', 'east', 'west' = To travel to islands located in the different directions""")
        input("Press enter to continue ")

# Eating in the game to replenish health

    elif command.lower() == "eat" and random > 0.5 and "Sanji" not in crew:
        player_health += heal
        print("You healed 30 health")
        if player_health > 100:
            player_health = 100
    elif command.lower() == "eat" and random > 0.25 and "Sanji" in crew:
        player_health += heal
        print("You healed 50 health")
        if player_health > 100:
            player_health = 100

# If there is an enemy, the only thing you can do is ask for the list of commands or eat. You are not able to do anything else

    elif inhabitant is not None and isinstance(inhabitant, Enemy):
        if command.lower() != "fight":
            print("You are not able to " + command + ". There is an enemy here")
        elif command.lower() == "fight":
            while inhabitant.health > 0 and player_health > 0:
                print("What would you like to do")
                attack_type = input("> ")

                # Attacking an enemy 'hit'

                if attack_type.lower() == "hit":
                    print("Would you like to do a heavy, medium or light attack?")
                    hit_type = input("> ")
                    if hit_type.lower() in ["heavy", "medium", "light"]:
                        inhabitant.fight(hit_type)
                        inhabitant.health -= int(inhabitant.multiplier * inhabitant.player_damage)
                        player_health -= inhabitant.enemy_damage

                        # If you are defeated?

                        if player_health <= 0:
                            print("You are now on 0 health")
                            print(inhabitant.name + " is now on " + str(inhabitant.health) + " health")
                            time.sleep(2)
                            print("You have been defeated")
                            time.sleep(1.5)
                            print("So called...")
                            time.sleep(1)
                            print("King of the Pirates")
                            time.sleep(1.5)
                            dead = True

                        # If you defeat your enemy?

                        elif inhabitant.health <= 0:
                            Enemy.enemies_to_defeat -= 1
                            current_island.set_enemy(None)
                            print("You dealt " + str(int(inhabitant.player_damage * inhabitant.player_damage)) + " to " + inhabitant.name)
                            print(inhabitant.name + " dealt " + str(inhabitant.enemy_damage) + " to you")
                            print("You are now on " + str(player_health) + " health")
                            print(inhabitant.name + " is now on 0 health")
                            print("You have defeated " + inhabitant.name)
                        else:
                            print("You dealt " + str(int(inhabitant.multiplier * inhabitant.player_damage)) + " to " + inhabitant.name)
                            print(inhabitant.name + " dealt " + str(inhabitant.enemy_damage) + " to you")
                            print("You are now on " + str(player_health) + " health")
                            print(inhabitant.name + " is now on " + str(inhabitant.health) + " health")
                    else:
                        print("You cannot attack this way")

                # Dodging an enemy attack. Dodging succesfully rewards the user with a 1.5x damage increase on their next hit
                
                elif attack_type.lower() == "dodge":
                    if inhabitant.dodge() == True:
                        inhabitant.multiplier = 1.5
                    else:
                        inhabitant.multiplier = 1
                        player_health -= inhabitant.enemy_damage

                # Run from a fight.

                elif attack_type.lower() == "run":

                    # Running only works on Captain Smoker. Gives alternative ending.

                    if inhabitant.name == "Captain Smoker":
                        time.sleep(2)
                        print("Smoke fills the alleyways as Smoker closes in. You escape to sea, battered and alone.")
                        time.sleep(2)
                        print("The World Government now has its eye on you - a wanted pirate with no crew to back him up.")
                        time.sleep(1.5)
                        print("The Grand Line will have to wait for now...")
                        time.sleep(1)
                        print("... King of the Pirates!")
                        time.sleep(1)
                        dead = True
                    else:
                        print("Don't be a coward, take him on!")
                else:
                    print("You cannot perform this action in a fight")           
        else:
            print("There is no one here for you to fight with.")

# Travelling around the map in the game

    elif command.lower() == "travel": 
            print("In what direction would you like to travel?")
            direction = input("> ")

            # User must enter an direction that has an island attached to it, ensuring that they have the required crew members to travel to that island

            if direction.lower() in ["north", "south", "east", "west"] and current_island.travel(direction).requirements == [] or crew == current_island.travel(direction).requirements:
                current_island = current_island.travel(direction)
            else:
                print("You cannot move to this island without recruiting other members to your crew.")

# Recruiting other members for your crew in the game

    elif command.lower() == "recruit":
        if inhabitant is not None:
            print("I wouldn't do that if I were you...")
        elif crewmate is not None:
            print("You have recruited " + crewmate.name)
            current_island.set_friend(None)
            crew.append(crewmate.name)
        else:
            print("There is no one here to recruit")

# Inspecting the island in the game to look for any items

    elif command.lower() == "inspect":
        if current_island.item is not None:
            item.describe()
            decision = input("Would you like to pick it up? (yes/no) ")

            # If you accept to pick up the item

            if decision.lower() == "yes":
                print("You put the [" + item.name + "] in your bag")
                bag.append(item.name)
                current_island.set_item(None)

                # Picking up the Log Pose finishes the game. This is the true ending.

                if "Log Pose" in bag:
                    print("With your crew assembled, your ship sails beyond Twin Cape. You grip your Log Pose. Your journey has only begun.")
                    time.sleep(2)
                    print("The Grand Line awaits the future...")
                    time.sleep(1.5)
                    print("... King of the Pirates!")
                    time.sleep(1)
                    dead = True

            # If you deny picking up an item

            elif decision.lower() == "no":
                print("You left the " + item.name + "alone")
            else:
                print("You are unable to complete this action")
        else:
            print("There is no item for you to take here")
    else:
        print("You are unable to perform this action")