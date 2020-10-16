import unittest
from Item import Item, Warrior_Chestplate, Warrior_Greaves, Warrior_Helmet, Warrior_Leggings, Lost_Blade, Offensive, Consumables, Meteora, Protection
import Player
import Room
import Game
import CommandWords
import sys
#TODO import 

class TestCode(unittest.TestCase):
    def test_room_correct(self):
        a = Room.Room("a", "room a", {Lost_Blade})
        b = Room.Room("b","b room", {Item: False})
        a.add_connection(b, "west")
        self.assertEqual(a.is_connected(b, "west"), b.rooms_connected.values() == "west")
        print(">>>>> ","pass test_room_correct")
        
    def test_room_nodirection(self):
        a = Room.Room("a","a room", {Item: False})
        b = Room.Room("b","b room", {Item: False})
        a.add_connection(b, "blue")
        assert "blue" is not a.rooms_connected.values()
        print(">>>>> ","pass test_room_nodirection")
        
    def test_room_noroom(self):
        a = Room.Room("a","a room", {Item: False})
        a.add_connection("west","cat") 
        assert "cat" is not a.rooms_connected.values()
        print(">>>>> ","pass test_room_noroom")
        
    def test_show_connections(self):
        a = Room.Room("a","a room", {Item: False})
        b = Room.Room("b","b room", {Item: False})
        c = Room.Room("c","c room", {Item: False})
        a.add_connection("west",b) 
        a.add_connection("east",c)        
        self.assertEqual(a.string_all_connections(),"west:b,east:c.","Should be west:b,east:c. Format of the string should be ==> direction:name_of_room. \n Connections are separated with commas, and the last one finishes with full stop.")
        print(">>>>> ","pass test_show_connections")
        
    def test_item_not_in_room(self):
        game = Game.Game()
        a = Room.Room("a", "room a", {Item: False})
        alex = Player.Player("alex", a, game, {Item: False})
        
        self.assertEqual(alex.get_weight,0,"Should be 0")
        print(">>>>> ","pass test_item_not_in_room")        
        
    def test_item_carrying(self):
        game = Game.Game()
        a = Room.Room("a", "room a", {Lost_Blade: 'Blade Left behind for item pick test'})
        alex = Player.Player("alex", a, game, {Item: False})    
        game.player = alex
        alex.pick(alex.pick)
        self.assertEqual(alex.get_weight(),20,"Should be 20")
        print(">>>>> ","pass test_item_carrying")

TestCode().test_item_carrying()