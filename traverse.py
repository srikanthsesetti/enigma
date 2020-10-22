from rotors import *
from reflector import *
import string
from multiple_rotors import *


class TraverseRotors:
    def __init__(self, rotors_list, reflector, rotor_positions):
        self.reflector = reflector
        self.positioned_rotor_list = []
        self.positioned_a_to_z_list = []
        self.rotor_notch_list = []

        # create all rotors and notches
        multiple_rotors = MultipleRotors()
        all_rotors_info, all_a_to_z_info, all_rotor_notches = multiple_rotors.create_multiple_rotors(rotors_list)
        self.rotor_notch_list = all_rotor_notches

        # move rotors to the starting positions
        self.positioned_rotor_list, self.positioned_a_to_z_list,  = \
            multiple_rotors.set_multiple_rotor_positions(all_rotors_info, all_a_to_z_info, rotor_positions)

    def traverse_rotors_right_to_left(self, position, character):
        # turn the middle one if right rotor is on notch
        if self.positioned_rotor_list[-1][0] == self.rotor_notch_list[-1]:
            print('third rotor on notch')
            # turn the left rotor if middle rotor is on notch
            if self.positioned_rotor_list[1][0] == self.rotor_notch_list[1]:
                print('middle rotor on notch')
                # turn the left rotor. middle rotor will be turned outside this if statement
                turn_left_rotor = SingleRotor()
                self.positioned_rotor_list[0], self.positioned_a_to_z_list[0] = \
                    turn_left_rotor.turn_rotor(self.positioned_rotor_list[0], self.positioned_a_to_z_list[0])
            # now turn the middle rotor. right rotor will always be turned outside this if statement
            turn_middle_rotor = SingleRotor()
            self.positioned_rotor_list[-2], self.positioned_a_to_z_list[-2] = \
                turn_middle_rotor.turn_rotor(self.positioned_rotor_list[-2], self.positioned_a_to_z_list[-2])

        # turn the right rotor before encoding
        turn_right_rotor = SingleRotor()
        self.positioned_rotor_list[-1], self.positioned_a_to_z_list[-1] = \
            turn_right_rotor.turn_rotor(self.positioned_rotor_list[-1], self.positioned_a_to_z_list[-1])

        for each_rotor, each_a_to_z, each_rotor_notch in zip(reversed(self.positioned_rotor_list), reversed(self.positioned_a_to_z_list), reversed(self.rotor_notch_list)):
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

