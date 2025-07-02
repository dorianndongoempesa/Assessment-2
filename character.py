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
        self.player_health = 100

#Set the health of the enemy
    def set_health(self, health):
        self.health = health

#Set the type of enemy
    def set_type(self, type):
        self.type = type

#Fight with this character

    def fight(self, attack):
        while self.health > 0 and self.player_health > 0:
            if attack == "light" and self.type == "light":
                self.player_damage = r.randint(3, 15)
                print("You dealt " + self.player_damage + " to " + self.name)
                self.health -= self.player_damage
                enemy_damage = r.randint(1, 5)
                print(self.name + " dealt " + enemy_damage + " to you")
            elif attack == "medium" and self.type == "light":
                random = r.random(0.0, 1.0)
                if random > 0.25:
                    self.player_damage = r.randint(16, 30)
                    print("You dealt " + self.player_damage + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your medium attack!")
                enemy_damage = r.randint(1, 5)
                print(self.name + " dealt " + enemy_damage + " to you")
            elif attack == "heavy" and self.type == "light":
                random = r.random(0.0, 1.0)
                if random > 0.5:
                    self.player_damage = r.randint(31, 50)
                    print("You dealt " + self.player_damage + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your heavy attack!")
                enemy_damage = r.randint(1, 5)
                print(self.name + " dealt " + enemy_damage + " to you")
            if attack == "light" and self.type == "medium":
                self.player_damage = r.randint(2, 10)
                print("You dealt " + self.player_damage + " to " + self.name)
                self.health -= self.player_damage
                enemy_damage = r.randint(5, 10)
                print(self.name + " dealt " + enemy_damage + " to you")
            elif attack == "medium" and self.type == "medium":
                random = r.random(0.0, 1.0)
                if random > (1/3):
                    self.player_damage = r.randint(11, 20)
                    print("You dealt " + self.player_damage + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your medium attack!")
                enemy_damage = r.randint(5, 10)
                print(self.name + " dealt " + enemy_damage + " to you")
            elif attack == "heavy" and self.type == "medium":
                random = r.random(0.0, 1.0)
                if random > (2/3):
                    self.player_damage = r.randint(21, 30)
                    print("You dealt " + self.player_damage + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your heavy attack!")
                enemy_damage = r.randint(5, 10)
                print(self.name + " dealt " + enemy_damage + " to you")
            elif attack == "light" and self.type == "heavy":
                self.player_damage = r.randint(1, 7)
                print("You dealt " + self.player_damage + " to " + self.name)
                self.health -= self.player_damage
                enemy_damage = r.randint(10, 15)
                print(self.name + " dealt " + enemy_damage + " to you")
            elif attack == "medium" and self.type == "medium":
                random = r.random(0.0, 1.0)
                if random > (0.4):
                    self.player_damage = r.randint(8, 15)
                    print("You dealt " + self.player_damage + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your medium attack!")
                enemy_damage = r.randint(10, 15)
                print(self.name + " dealt " + enemy_damage + " to you")
            elif attack == "heavy" and self.type == "heavy":
                random = r.random(0.0, 1.0)
                if random > (0.6):
                    self.player_damage = r.randint(16, 22)
                    print("You dealt " + self.player_damage + " to " + self.name)
                    self.health -= self.player_damage
                else:
                    print("You missed your heavy attack!")
                enemy_damage = r.randint(10, 15)
                print(self.name + " dealt " + enemy_damage + "to you")
        if self.health <= 0 and self.player_health > 0:
            Enemy.enemies_to_defeat -= 1
            return True, self.player_health
        elif self.health > 0 and self.player_health <= 0:
            return False, self.player_health

#Steal from this Character

    def steal(self):
        print("You steal from " + self.name)

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def pat(self):
        print(self.name + " pats you back!")
