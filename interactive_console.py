import sys
from run_enigma import *


class RunInteractiveEnigma:
    def __init__(self):
        self.ten_pairs = ""
        self.rotors = ""
        self.reflector = ""
        self.initial_rotor_positions = ""
        self.initial_rotor_settings = ""
        self.message = ""

    def get_valid_pairs(self):
        self.ten_pairs = input("Enter up to 10 plug lead combinations with a space between each combination. \n"
                          "For example, AG EN")
        split_pairs = self.ten_pairs.split()

        while len(split_pairs) > 10:
            self.ten_pairs = input("You can only enter upto 10 plug lead combinations")
            split_pairs = self.ten_pairs.split()

    def get_valid_rotors(self):
        self.rotors = input("Enter 3 or 4 rotors to use")
        split_rotors = self.rotors.split()
        while (len(split_rotors) != 3) and (len(split_rotors) != 4):
            self.rotors = input("You can only enter 3 or 4 rotors to use")
            split_rotors = self.rotors.split()

    def get_valid_reflector(self):
        self.reflector = input("Enter the reflector to use")
        while len(self.reflector) != 1:
            self.reflector = input("You can only enter one reflector to use")

    def get_valid_rotor_positions(self):
        self.initial_rotor_positions = input("Enter initial rotor positions")
        split_positions = self.initial_rotor_positions.split()
        len_rotors = self.rotors.split()
        while len(split_positions) != len(len_rotors):
            self.initial_rotor_positions = input("You can only enter same number of initial rotor positions as the rotors")
            split_positions = self.initial_rotor_positions.split()

    def get_valid_rotor_settings(self):
        self.initial_rotor_settings = input("Enter initial rotor settings")
        split_settings = self.initial_rotor_settings.split()
        len_rotors = self.rotors.split()
        while len(split_settings) != len(len_rotors):
            self.initial_rotor_settings = input("You can only enter same number of initial rotor settings as the rotors")
            split_settings = self.initial_rotor_settings.split()

    def get_message(self):
        self.message = input("Enter the message to encode")

    def run_interactive_enigma(self):
        self.get_valid_pairs()
        self.get_valid_rotors()
        self.get_valid_reflector()
        self.get_valid_rotor_positions()
        self.get_valid_rotor_settings()
        self.get_message()
        coded_message = run_enigma(self.ten_pairs, self.rotors, self.reflector, self.initial_rotor_positions,
                                   self.initial_rotor_settings, self.message)
        return coded_message

# name = ""
# while len(name) > 0: # user must enter a name at least 1 character long to proceed
#     name = input('Enter your name, or type quit to exit ')
#     if name.lower() == "quit":
#         sys.exit() # when the user enters exit, exit the program

