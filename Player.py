#TODO import
import Game
import Room
from Item import Item, Warrior_Chestplate, Warrior_Greaves, Warrior_Helmet, Warrior_Leggings, Lost_Blade, Offensive, Consumables, Meteora, Protection
import CommandWords
class Player():
    def __init__(self, name, current_room, game, inventory):
        self.name = name #player's name
        self.current_room = current_room #Players starting room
        self.game = game
        self.inventory = inventory #collection of items the player is carrying
        self.health = 100 #player's current health
        self.can_carry = 250 #maximum weight the player can carry
        self.current_weight = 0

        # Array of go sub commands, used by go
        self.go_direction = {
            'north': self._go_north,
            'east': self._go_east,
            'south': self._go_south,
            'west': self._go_west
        }


    def get_direction(self):
        return self.go_direction

    def get_current_room(self):
        return self.current_room

    def get_name(self):
        return print(self.name)
    
    def set_name(self, player_name):
        self.name = player_name

    def set_current_room(self, new_room):
        self.current_room = new_room
        print('\nYou are now in',self.current_room.get_name(),'\nDescription: ', self.current_room.get_description())

    # Movement handling, will get executed when user types 'go ...' and will split direction to call another function
    def _go(self, args):
        if args is None:    # No argument
            print('\nGo excepts one of these:', ', '.join( self.go_direction.keys()))
            return False

        # Split sub command and arguments
        (command,args) = CommandWords.CommandWords(self.game.player, self.game).parse_command(args)
        if command not in self.go_direction:
            print( '\nGo excepts one of these:', ', '.join( self.go_direction.keys()))
            return False

        if args is not None:
            print( '\nToo many arguments for Go')
            return False

        #Path checking for room the player is in
        self.go_direction[command](args)
        pathchecker = self.current_room.is_connected(self.current_room, command)

        #Changing the Players current room
        self.set_current_room(pathchecker)
        return True

    # Adds an Item to the inventory. Checks that adding the item does not exceed maximum weight and that item is of type Item. If not prints appropriate messages.
    def pick(self, args):
        print(self.current_room.room_items)
        for itemC in list(self.current_room.room_items):       
            if False in self.current_room.room_items.values():
                print("\nThere's nothing to take here!")
            else:
                item_input = input("Pick an Item by typing its name:")
                if item_input != itemC.get_name():
                    print("\nTry this item name once you've typed pick",'(',itemC.get_name(),')')
                    print(item_input)

                if item_input == itemC.get_name():
                    self.add_to_inv(itemC)
                    self.current_room.del_item(itemC)
                    self.current_room.add_empty_item_container()

    
    def add_to_inv(self, item):
        if self.get_weight() + item.get_weight() >= self.can_carry:
            print('\nYou can no longer fit items into your inventory!\n Try to (Drop) something!')
        else:
            print('\nAdded to (inventory)', item.get_name())
            d = {item: 'Found by you'}
            for itemC in list(self.inventory):
                del self.inventory[itemC]
            
            self.inventory.update(d)
            self.current_weight = self.current_weight + item.get_weight()

    

    def _go_north(self, args):
        print('\nYou try going to the North')

    def _go_south(self, args):
        print('\nYou try going to the South')

    def _go_west(self, args):
        print('\nYou try going to the West')

    def _go_east(self, args):
        print('\nYou try going to the East')

    def look(self, args): 
        itemD = self.current_room.room_items
        for itemC in itemD:
            if False in self.current_room.room_items.values():
                print("\nThere is nothing left to find here.\nExits:")
                self.current_room.get_exits()
            else:
                if itemC in itemD:
                    print("You\'ve discovered:\n", '(',itemC.get_name(),')', itemD[itemC],"\nYou see some exits in these directions:")
                    self.current_room.get_exits()
            

    def drop(self, args):
        print(self.inventory)
        for itemC in list(self.inventory):       
            if False in self.inventory.values():
                print("There is nothing to drop")
            else:
                #input the name of item the user wants to drop                
                item_input = input("Drop an item by typing the name of an Item in your Inventory:\n")   
                
                #If the item name is wrong show this
                if item_input != itemC.get_name():  
                    print("Item names are Case sensitive! After (drop) do (Item Name) which is displayed:\n",'(',itemC.get_name(),')')
                
                #If the item name is the same as the input drop the item
                if item_input == itemC.get_name():
                    for isEmpty in list(self.current_room.room_items):
                        if False in self.current_room.room_items.values():
                            self.current_room.del_item(isEmpty)
                            self.current_room.add_item(itemC)
                        
                        self.del_from_inv(itemC) # Item the user has dropped shows
                        self.add_empty_item_container()

                


    def del_from_inv(self, item):
        print('You\'ve dropped', item.get_name())
        self.del_item(item)
        self.current_weight = self.current_weight - item.get_weight()

    # Returns a string containing all the items in the inventory by name. E.g. toast,keys. Items are separated with comma and at the end there is a full stop.
    def get_inventory(self, args):
        if False in self.inventory.values():
            print('\nThere is nothing in your inventory')
        else:
            print('Here are the Items in your inventory:')
            for item in self.inventory:
                print(item.get_name(),',',item.get_description())
            
    def del_item(self, item):
        del self.inventory[item]

    def add_empty_item_container(self):
        d = {Item: False}
        if not False in self.inventory.values():
            self.inventory.update(d)
            

    # Returns an integer with the overall weight of all the items in the inventory.
    def get_weight(self):
        return self.current_weight

