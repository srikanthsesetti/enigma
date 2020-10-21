from rotors import *
from reflector import *
import string


class TraverseRotors:
    def __init__(self, rotors_list, reflector, rotor_positions):
        self.rotors_list = rotors_list
        self.reflector = reflector
        self.rotor_positions = rotor_positions
        positioned_a_to_z_list = []
        self.positioned_rotor_list, positioned_a_to_z_list = set_all_rotor_positions(rotors_list, rotor_positions)
        print(self.positioned_rotor_list)
        print(positioned_a_to_z_list)

    def traverse_rotors_right_to_left(self, char):
        position = char[0]
        print(f'position in traverse: {position}')
        character = char[1]
        for each_rotor in reversed(self.positioned_rotor_list):
            traverse = rotor_from_name(each_rotor)
            position, character = traverse.encode_right_to_left(each_rotor, position, character)
        return position, character

    def traverse_reflector(self, char):
        position = char[0]
        character = char[1]
        traverse = ReflectorFromName(self.reflector)
        position, character = traverse.encode_reflector(position, character)
        return position, character

    def traverse_rotors_left_to_right(self, char):
        position = char[0]
        character = char[1]
        for each_rotor in self.positioned_rotor_list:
            traverse = rotor_from_name(each_rotor)
            position, character = traverse.encode_left_to_right(each_rotor, position, character)
        character = chr(65 + position)
        return character

