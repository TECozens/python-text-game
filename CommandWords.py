#TODO import
import sys
import Game
import Player 
class CommandWords():
    # TODO Run this in a loop
    # Calls input. If user input consists of 1 or more words and these belong to the validComands then it returns them in a tuple.
    def __init__(self, player, game):
        self.game = game
        self.player = player

        self.known_commands = {
            'exit': self.game._exit,
            'help': self.game._help,
            'go': self.game.player._go,
            'look': self.game.player.look,
            'pick': self.game.player.pick,
            'inventory': self.game.player.get_inventory,
            'drop': self.game.player.drop
        }  

        # Array of go sub commands, used by go
        self.go_direction = {
            'north': self.game.player._go_north,
            'east': self.game.player._go_east,
            'south': self.game.player._go_south,
            'west': self.game.player._go_west
        }

    def get_commands(self):
        return self.known_commands
    
    def get_isCommandWord(self):
        for commands in self.known_commands:
            print(commands)
    
    # TODO Compare Sub Commands List with Args
    def getCommand(self):
        user_input = input('>>')
        (command_input, args) = self.parse_command(user_input)  # Splits user input to compare with main commands and sub commands
        if command_input in self.known_commands:    # Check for user input in dicts, if true then it executes command from the dict
            return self.known_commands[command_input](args)
                
        else: #Validation for user input, propmts user
            print( 'Unknown command {}, try one of these instead:'.format(command_input))
            print( '\n'.join(self.known_commands.keys()))

    # Mathod for parsing command, if it gets "command" returns ("command",None)
    # if "command arg1 arg2" returns ("command", "arg1 arg2")
    @staticmethod
    def parse_command(string):
        string = str(string).lower()
        index = string.find(' ')
        if index < 0:
            return (string, None)

        return (string[:index], string[index+1:])


    