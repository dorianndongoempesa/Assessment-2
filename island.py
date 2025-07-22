#My 'room' class, Island
class Island:
    def __init__(self, island_name):
        self.name = island_name
        self.description = None
        self.linked_islands = {}
        self.enemy = None
        self.friend = None
        self.item = None
        self.requirements = []

#Here is a method to set the description of the island:

    def set_description(self, island_description):
        self.description = island_description

#Here is a method to get the description of the island:

    def get_description(self):
        return self.description

#Here is a method to print the description of the island:

    def describe(self):
        print(self.description)

#Here is a method is get the name of the island:

    def set_name(self, island_name):
        self.name = island_name

#Here is a method to get the name of the island:

    def get_name(self):
        return self.name

#Here is a method to set an enemy onto an Island

    def set_enemy(self, new_enemy):
        self.enemy = new_enemy

#Here is a method to get an enemy onto an Island

    def get_enemy(self):
        return self.enemy
    
#Here is a method to set an enemy onto an Island

    def set_friend(self, new_friend):
        self.friend = new_friend

#Here is a method to get an enemy onto an Island

    def get_friend(self):
        return self.friend

#Here is a method used to link the islands together:

    def link_island(self, island_to_link, direction):
        self.linked_islands[direction] = island_to_link

#Here is a method used to link locations within an island together

    def link_location(self, location_to_link):
        self.linked_locations = location_to_link

#Here is a method that displays all the islands linked to the current island object:

    def get_details(self):
        print(self.name)
        print("----------")
        print(self.description)
        for direction in self.linked_islands:
            island = self.linked_islands[direction]
            print(island.get_name() + " is " + direction)

#Here is a method that allows the user to move around the islands:

    def travel(self, direction):
        if direction in self.linked_islands:
            return self.linked_islands[direction]
        else:
            print("You can't go that way")
            return self

#Here is a method to set an item to an Island
    
    def set_item(self, item_name):
        self.item = item_name

#Here is a method to get an item from an Island

    def get_item(self):
        return self.item