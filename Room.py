import Item
# TODO import Enemies

class Room():        
    def __init__(self, name, description, room_items):
        self.name = name
        self.room_items = room_items
        self.description = description
        self.rooms_connected = {}

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def is_connected(self, current_room, direction):
        if direction in self.rooms_connected:   #TODO Get the Room from this dict      
            return self.rooms_connected[direction]  

        elif direction not in self.rooms_connected:
            print('This direction doesn\'t exist try a different path!')
            self.get_exits()
            return current_room


    # Define add_connection() function. The function takes as argument one direction: (north,east,west,sount) and a Room. 
    def add_connection(self, room_to_connect, direction):
        self.rooms_connected[direction] = room_to_connect
        
    def get_exits(self):
        for exits in self.rooms_connected:
            print(exits)
    

    # Returns a string containing all the items in the room by name. E.g. toast,keys. Items are separated with comma and at the end there is a full stop.
    def string_all_items(self):
        if False in self.room_items.values():
            return "There are no Items!"
        else:
            print('==>', str(self.room_items), '.')

    

    # Returns a string containing all the connections of the room. 
    # Format of the string should be ==> direction:name_of_room, e.g. south:lab,east:kitchen.
    # Connections are separated with commas, and the last one finishes with full stop.
    def string_all_connections(self):
        print('==>', str(self.rooms_connected), '.')

    # TODO Add an item in the list of items of the room. The items should be of type Item. Returns nothing.   
    def add_item(self,item):
        d = {item: 'Dropped by player'}
        return self.room_items.update(d)
    
    def del_item(self, item):
        del self.room_items[item]

    def add_empty_item_container(self):
        d = {Item: False}
        if not False in self.room_items.values():
            self.room_items.update(d)
        else:
            pass


class Default(dict):
    def __missing__(self, key):
        return key