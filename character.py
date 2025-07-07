import random as r

class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

#Describe the character

    def describe(self):
        print(self.name + " is here!")
        print(self.description)

#Set what this character will say when talked to

    def set_conversation(self, conversation):
        self.conversation = conversation

#Talk to this character

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says] " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

#Fight with this character

    def fight(self):
        print(self.name + " doesn't want to fight you")
        return True

class Enemy(Character):
    enemies_to_defeat = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        Enemy.enemies_to_defeat += 1
        self.player_damage = 0
        self.enemy_damage = 0

#Set the health of the enemy
    def set_health(self, health):
        self.health = health

#Get the health of the enemy
    def get_health(self):
        return self.health

#Set the type of enemy
    def set_type(self, type):
        self.type = type

#Fight with this character

    def fight(self, attack):
            if attack == "light" and self.type == "light":
                self.player_damage = r.randint(3, 15)
                print("You dealt " + str(self.player_damage) + " to " + self.name)
                self.health -= self.player_damage
                self.enemy_damage = r.randint(1, 5)
                print(self.name + " dealt " + str(self.enemy_damage) + " to you")
            elif attack == "medium" and self.type == "light":
                random = r.random()
                if random > 0.25:
                    self.player_damage = r.randint(16, 30)
                    print("You dealt " + str(self.player_damage) + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your medium attack!")
                self.enemy_damage = r.randint(1, 5)
                print(self.name + " dealt " + str(self.enemy_damage) + " to you")
            elif attack == "heavy" and self.type == "light":
                random = r.random()
                if random > 0.5:
                    self.player_damage = r.randint(31, 50)
                    print("You dealt " + str(self.player_damage) + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your heavy attack!")
                self.enemy_damage = r.randint(1, 5)
                print(self.name + " dealt " + str(self.enemy_damage) + " to you")
            if attack == "light" and self.type == "medium":
                self.player_damage = r.randint(2, 10)
                print("You dealt " + str(self.player_damage) + " to " + self.name)
                self.health -= self.player_damage
                self.enemy_damage = r.randint(5, 10)
                print(self.name + " dealt " + str(self.enemy_damage) + " to you")
            elif attack == "medium" and self.type == "medium":
                random = r.random()
                if random > (1/3):
                    self.player_damage = r.randint(11, 20)
                    print("You dealt " + str(self.player_damage) + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your medium attack!")
                self.enemy_damage = r.randint(5, 10)
                print(self.name + " dealt " + str(self.enemy_damage) + " to you")
            elif attack == "heavy" and self.type == "medium":
                random = r.random()
                if random > (2/3):
                    self.player_damage = r.randint(21, 30)
                    print("You dealt " + str(self.player_damage) + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your heavy attack!")
                self.enemy_damage = r.randint(5, 10)
                print(self.name + " dealt " + str(self.enemy_damage) + " to you")
            elif attack == "light" and self.type == "heavy":
                self.player_damage = r.randint(1, 7)
                print("You dealt " + str(self.player_damage) + " to " + self.name)
                self.health -= self.player_damage
                self.enemy_damage = r.randint(10, 15)
                print(self.name + " dealt " + str(self.enemy_damage) + " to you")
            elif attack == "medium" and self.type == "heavy":
                random = r.random()
                if random > (0.4):
                    self.player_damage = r.randint(8, 15)
                    print("You dealt " + str(self.player_damage) + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your medium attack!")
                self.enemy_damage = r.randint(10, 15)
                print(self.name + " dealt " + str(self.enemy_damage) + " to you")
            elif attack == "heavy" and self.type == "heavy":
                random = r.random()
                if random > (0.6):
                    self.player_damage = r.randint(16, 22)
                    print("You dealt " + str(self.player_damage) + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your heavy attack!")
                self.enemy_damage = r.randint(10, 15)
                print(self.name + " dealt " + str(self.enemy_damage) + " to you")

#Steal from this Character

    def steal(self):
        print("You steal from " + self.name)

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def pat(self):
        print(self.name + " pats you back!")       