#TODO import
import Player
import Room
from Item import Item, Warrior_Chestplate, Warrior_Greaves, Warrior_Helmet, Warrior_Leggings, Lost_Blade, Offensive, Consumables, Meteora, Protection
import CommandWords
import Enemies
import sys

class Game():
    # Initialise Game
    def __init__(self):
        self.finished = False

    # function that creates all the Rooms of the Game and any Items in them
    def create_rooms(self):
        self.Level_1_A = Room.Room("Introduction:","\nHello and welcome to the start of your new Adventure!, you should try getting to grips with what\'s around here \n\nTry to (look) around. \nFor more info type (help)", {Item: False})
        self.Level_1_B = Room.Room("Hallway","You\'re in a hallway which strays away from the past", {Item: False})
        self.Level_1_C = Room.Room("Warriors Altar", "You\'ve discovered a room with many statues of long forgotten warriors wielding power beyond that of ordinary mankind",{Lost_Blade(): 'A Blade left behind on the Altar'})
        self.Level_2_A = Room.Room("Hollow Forest", "You\'ve discovered a large and open forest, time to venture forth into the wild tangling trees.\nAs you look back you notice that your path has been blocked", {Item: False})
        self.Level_2_B = Room.Room("Forest Passageway", "An open passage through the forest, it seems to be a road.", {Item: False})
        self.Level_1_A.add_connection(self.Level_1_B, 'north')
        self.Level_1_B.add_connection(self.Level_1_A, 'south')
        self.Level_1_B.add_connection(self.Level_1_C, 'north')
        self.Level_1_C.add_connection(self.Level_1_B, 'south')
        self.Level_1_C.add_connection(self.Level_2_A, 'west')
        self.Level_2_A.add_connection(self.Level_2_B, 'west')
        self.Level_2_B.add_connection(self.Level_2_A, 'east')

    def _exit(self,args):
        self.finished = True
        print("Game Over")

    #A nice Ascii art print title for my game
    def title(self):
        print('@@@  @@@   @@@@@@   @@@       @@@        @@@@@@   @@@  @@@  @@@      @@@@@@    @@@@@@   @@@  @@@  @@@')      
        print('@@@  @@@  @@@@@@@@  @@@       @@@       @@@@@@@@  @@@  @@@  @@@     @@@@@@@   @@@@@@@@  @@@  @@@  @@@')               
        print('@@!  @@@  @@!  @@@  @@!       @@!       @@!  @@@  @@!  @@!  @@!     !@@       @@!  @@@  @@!  @@@  @@!')       
        print('!@!  @!@  !@!  @!@  !@!       !@!       !@!  @!@  !@!  !@!  !@!     !@!       !@!  @!@  !@!  @!@  !@!')      
        print('@!@!@!@!  @!@  !@!  @!!       @!!       @!@  !@!  @!!  !!@  @!@     !!@@!!    @!@  !@!  @!@  !@!  @!!')       
        print('!!!@!!!!  !@!  !!!  !!!       !!!       !@!  !!!  !@!  !!!  !@!      !!@!!!   !@!  !!!  !@!  !!!  !!!')       
        print('!!:  !!!  !!:  !!!  !!:       !!:       !!:  !!!  !!:  !!:  !!:          !:!  !!:  !!!  !!:  !!!  !!:')       
        print(':!:  !:!  :!:  !:!   :!:       :!:      :!:  !:!  :!:  :!:  :!:         !:!   :!:  !:!  :!:  !:!  :!:')      
        print('::   :::  ::::: ::   :: ::::   :: ::::  ::::: ::   :::: :: :::      :::: ::   ::::: ::  ::::: ::  :: ::::')  
        print(':   : :   : :  :   : :: : :  : :: : :   : :  :     :: :  : :       :: : :     : :  :    : :  :   : :: : :')
        print('\nGame by Cardiff University Student: C1843439\n')                                                                                                                          
            

    #Everything plays within this method when input is called.
    def play(self):
        #My Game's Title
        self.title()

        #Some instantiations
        self.player = Player.Player("No Name", self.Level_1_A, self, {Item: False})
        self.parser = CommandWords.CommandWords(self.player, self)
        self.player.set_name(input("You welcome yourself within a dark abyss.\nLost, perhaps you should define who you are with a name: "))
        
        #Intro Print
        print(self.Level_1_A.get_name(), self.Level_1_A.get_description())
        
        # allows input feedback loop
        while self.finished == False:
            self.parser.getCommand() #Text to Function Parser takes input as Tuple and then splits it for each command and sub command, increasing complexity

    def _help(self, args):
        print("Here are some commands that may be of use to you in-game.")
        for key in self.parser.known_commands:
            print(key)

#This is a main method used to call game and get input
if __name__ == "__main__":
    game = Game()
    game.create_rooms()
    game.play()
