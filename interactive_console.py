import sys
from run_enigma import *
from validation import *


class RunInteractiveEnigma:
    def __init__(self):
        self.ten_pairs = ""
        self.rotors = ""
        self.reflector = ""
        self.initial_rotor_positions = ""
        self.initial_rotor_settings = ""
        self.message = ""

    def get_plugboard_pairs(self):
        self.ten_pairs = input("Enter up to 10 plug lead combinations with a space between each combination. \n "
                               "For example, AG EN")
        while not are_valid_plugleads(self.ten_pairs):
            self.ten_pairs = input("Please provide maximum 10 valid plugs; "
                                   "a plug can connect to just one other plug and cannot connect to itself")

    def get_rotors(self):
        self.rotors = input("Enter 3 or 4 rotors to use from: I II III IV V BETA GAMMA with a space between each rotor")
        while not are_valid_rotors(self.rotors):
            self.rotors = input("You can only enter 3 or 4 rotors to use from: I II III IV V BETA GAMMA")

    def get_reflector(self):
        self.reflector = input("Enter the reflector to use from: A B C")
        while not is_valid_reflector(self.reflector):
            self.reflector = input("You can only enter one reflector to use from: A B C")

    def get_rotor_positions(self):
        self.initial_rotor_positions = input("Enter initial rotor positions as alphabets with a "
                                             "space between each position")
        while not are_valid_rotor_positions(self.initial_rotor_positions, self.rotors):
            self.initial_rotor_positions = input("You can only enter same number of initial rotor positions "
                                                 "as the rotors and positions can only be alphabets")

    def get_rotor_settings(self):
        self.initial_rotor_settings = input("Enter initial rotor settings as numbers from "
                                            "1 to 26 with a space between each ")
        while not are_valid_rotor_settings(self.initial_rotor_settings, self.rotors):
            self.initial_rotor_settings = input("You can only enter same number of initial rotor settings "
                                                "as the rotors and each setting should be a number from 1 to 26")

    def get_message_to_encode(self):
        self.message = input("Enter the message to encode")
        while not is_valid_message(self.message):
            self.message = input("You can only enter the message in alphabets. Spaces and numbers are not allowed")

    def run_interactive_enigma(self):
        coded_message = run_enigma(self.ten_pairs, self.rotors, self.reflector, self.initial_rotor_positions,
                                   self.initial_rotor_settings, self.message)
        return coded_message

# name = ""
# while len(name) > 0: # user must enter a name at least 1 character long to proceed
#     name = input('Enter your name, or type quit to exit ')
#     if name.lower() == "quit":
#         sys.exit() # when the user enters exit, exit the program

