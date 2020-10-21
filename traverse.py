from rotors import *
from reflector import *


class TraverseRotors:
    def __init__(self, rotors_list, reflector, rotor_positions):
        self.rotors_list = rotors_list
        self.reflector = reflector
        self.rotor_positions = rotor_positions
        self.positioned_rotor_list = set_all_rotor_positions(rotors_list, rotor_positions)

    def traverse_rotors_right_to_left(self, char):
        # move right hand side rotor by 1
        for each_rotor in reversed(self.positioned_rotor_list):
            traverse = rotor_from_name(each_rotor)
            char = traverse.encode_right_to_left(each_rotor, char)
        return char

    def traverse_reflector(self, char):
        traverse = ReflectorFromName(self.reflector)
        char = traverse.encode_reflector(char)
        return char

    def traverse_rotors_left_to_right(self, char):
        for each_rotor in self.positioned_rotor_list:
            traverse = rotor_from_name(each_rotor)
            char = traverse.encode_left_to_right(each_rotor, char)
        return char

