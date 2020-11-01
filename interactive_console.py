import sys
from run_enigma import *
# from plugboard import *
import string
from validation import *


class RunInteractiveEnigma:
    def __init__(self):
        self.ten_pairs = ""
        self.rotors = ""
        self.reflector = ""
        self.initial_rotor_positions = ""
        self.initial_rotor_settings = ""
        self.message = ""

    def get_valid_plugboard_pairs(self):
        self.ten_pairs = input("Enter up to 10 plug lead combinations with a space between each combination. \n "
                               "For example, AG EN")
        while not self.are_plugleads_valid():
            self.ten_pairs = input("Please provide maximum 10 valid plugs; "
                                   "a plug can connect to just one other plug and cannot connect to itself")

    def get_valid_rotors(self):
        self.rotors = input("Enter 3 or 4 rotors to use from: I II III IV V BETA GAMMA with a space between each rotor")
        while not self.are_valid_rotors():
            self.rotors = input("You can only enter 3 or 4 rotors to use from: I II III IV V BETA GAMMA")

    def get_valid_reflector(self):
        self.reflector = input("Enter the reflector to use from: A B C")
        while not self.is_valid_reflector():
            self.reflector = input("You can only enter one reflector to use from: A B C")

    def get_valid_rotor_positions(self):
        self.initial_rotor_positions = input("Enter initial rotor positions as alphabets with a "
                                             "space between each position")
        while not self.are_valid_rotor_positions():
            self.initial_rotor_positions = input("You can only enter same number of initial rotor positions "
                                                 "as the rotors and positions can only be alphabets")

    def get_valid_rotor_settings(self):
        self.initial_rotor_settings = input("Enter initial rotor settings as numbers from "
                                            "1 to 26 with a space between each ")
        while not self.are_valid_rotor_settings():
            self.initial_rotor_settings = input("You can only enter same number of initial rotor settings "
                                                "as the rotors and each setting should be a number from 1 to 26")

    def get_message_to_encode(self):
        self.message = input("Enter the message to encode")
        while not self.is_valid_message():
            self.message = input("You can only enter the message in alphabets. Spaces and numbers are not allowed")

    def are_plugleads_valid(self):
        split_pairs = self.ten_pairs.split()
        valid = None
        if len(split_pairs) == 0:
            return True
        if len(split_pairs) <= 10:
            for each_plug in split_pairs:
                if PlugLead.is_valid_lead(each_plug.upper()):
                    valid = True
                else:
                    return False
            return valid
        else:
            return False

    def are_valid_rotors(self):
        valid_rotors = ['I', 'II', 'III', 'IV', 'V', 'BETA', 'GAMMA']
        split_rotors = self.rotors.split()
        valid = None
        if (len(split_rotors) == 3) or (len(split_rotors) == 4):
            for each_rotor in split_rotors:
                if each_rotor.upper() in valid_rotors:
                    valid = True
                else:
                    return False
            return valid
        else:
            return False

    def is_valid_reflector(self):
        valid_reflectors = ['A', 'B', 'C']
        if len(self.reflector) == 1 and self.reflector.upper() in valid_reflectors:
            return True
        else:
            return False

    def are_valid_rotor_positions(self):
        valid_positions = string.ascii_uppercase
        split_positions = self.initial_rotor_positions.split()
        rotors = self.rotors.split()
        valid = None
        if len(split_positions) == len(rotors):
            for each_position in split_positions:
                if each_position.upper() in valid_positions:
                    valid = True
                else:
                    return False
            return valid
        else:
            return False

    def are_valid_rotor_settings(self):
        valid_settings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        split_settings = self.initial_rotor_settings.split()
        len_rotors = self.rotors.split()
        valid = None
        if len(split_settings) == len(len_rotors):
            for each_setting in split_settings:
                try:
                    if int(each_setting) in valid_settings:
                        valid = True
                    else:
                        return False
                except ValueError:
                    return False
            return valid
        else:
            return False

    def is_valid_message(self):
        valid_message_characters = string.ascii_uppercase
        valid = True
        for char in self.message:
            if char.upper() in valid_message_characters:
                valid = True
            else:
                return False
        return valid

    def run_interactive_enigma(self):
        coded_message = run_enigma(self.ten_pairs, self.rotors, self.reflector, self.initial_rotor_positions,
                                   self.initial_rotor_settings, self.message)
        return coded_message

# name = ""
# while len(name) > 0: # user must enter a name at least 1 character long to proceed
#     name = input('Enter your name, or type quit to exit ')
#     if name.lower() == "quit":
#         sys.exit() # when the user enters exit, exit the program

