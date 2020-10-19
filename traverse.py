from rotors import *
from reflector import *


class TraverseRotors:
    def __init__(self, rotors, reflector):
        self.rotor_list = rotors.split()
        self.reflector = reflector

    def traverse_rotors_right_to_left(self, char):
        for each_rotor in reversed(self.rotor_list):
            traverse = rotor_from_name(each_rotor)
            char = traverse.encode_right_to_left(char)
        return char

    def traverse_reflector(self, char):
        traverse = ReflectorFromName(self.reflector)
        char = traverse.encode_reflector(char)
        return char

    def traverse_rotors_left_to_right(self, char):
        for each_rotor in self.rotor_list:
            traverse = rotor_from_name(each_rotor)
            char = traverse.encode_left_to_right(char)
        return char