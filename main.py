from island import Island
from character import Enemy, Character, Friend
from item import Item

#Naming the islands and describing them

fuschia = Island("Fuschia Village")
fuschia.set_description("A peaceful village by the sea and your home. It's quiet now, but adventure is calling.")

gecko = Island("Gecko Island")
gecko.set_description("A foggy, forest-covered island home to wild beasts and hidden paths. Adventurers often go missing here.")

syrup = Island("Syrup Village")
syrup.set_description("A quiet town with strange activity near the hilltop mansion. Not everything is as peaceful as it seems.")

orange = Island("Orange Town")
orange.set_description("Once a lively port, now reduced to rubble by a mad clown and his minions.")

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

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry... Hanggrry")
harry.set_weakness("vegemite")
fuschia.set_character(harry)

#Setting items to different islands

torch = Item("torch")
torch.set_description("A light for the end of the tunnel")
gecko.set_item(torch)
bag = []

current_island = fuschia
dead = False
while dead == False:
    print("\n")
    current_island.get_details()
    inhabitant = current_island.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
            current_island = current_island.travel(command)
    elif command == "talk":
        #Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        #Check whether the character is an enemy using isinstance()
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            #Fight with the inhabitant, if there is one
            print("Would you like to do a heavy, medium or light attack?")
            attack_weight = input()
            if attack_weight.lower() in ["heavy", "medium", "light"]:
                while inhabitant.fight(attack_weight) == True:
                    print("Bravo, hero you won the fight!")
                    current_island.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you are the King of the Pirates!")
                        dead = True
                else:
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You cannot attack this way.")
        else:
            print("There is no one here to fight with.")
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                    inhabitant.pat()
        else:
            print("There is no one here to pat :(")
    elif command == "take":
        if current_island.item is not None:
            print("You put the " + current_island.item() + " in your bag")
            bag.append(current_island.item())
            current_island.set_item(None)
        else:
            print("There is no item for you to take here")