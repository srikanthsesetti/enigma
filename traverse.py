from rotors import *
from reflector import *
import string
from multiple_rotors import *


class TraverseRotors:
    def __init__(self, rotors_list, reflector, rotor_positions):
        self.reflector = reflector

        self.positioned_a_to_z_list = []
        self.positioned_rotor_list = []
        multiple_rotors = MultipleRotors()
        all_rotors_info, all_a_to_z_info = multiple_rotors.create_multiple_rotors(rotors_list)
        self.positioned_rotor_list, self.positioned_a_to_z_list = \
            multiple_rotors.set_multiple_rotor_positions(all_rotors_info, all_a_to_z_info, rotor_positions)

    def traverse_rotors_right_to_left(self, position, character):
        # turn the right rotor before encoding
        turn_right_rotor = SingleRotor()
        self.positioned_rotor_list[-1], self.positioned_a_to_z_list[-1] = turn_right_rotor.turn_rotor\
            (self.positioned_rotor_list[-1], self.positioned_a_to_z_list[-1])

        for each_rotor, each_a_to_z in zip(reversed(self.positioned_rotor_list), reversed(self.positioned_a_to_z_list)):
            # check if the rotor is on notch

            traverse = rotor_from_name()
            position, character = traverse.encode_right_to_left(each_rotor, each_a_to_z, position, character)
        return position, character

    def traverse_reflector(self, position, character):
        traverse = Reflector()
        named_reflector, reflector_a_to_z = traverse.get_reflector(self.reflector)
        position, character = traverse.encode_reflector(named_reflector, reflector_a_to_z, position, character)
        return position, character

    def traverse_rotors_left_to_right(self, position, character):
        for each_rotor, each_a_to_z in zip(self.positioned_rotor_list, self.positioned_a_to_z_list):
            traverse = rotor_from_name()
            position, character = traverse.encode_left_to_right(each_rotor, each_a_to_z, position, character)
        character = chr(65 + position)
        return character

