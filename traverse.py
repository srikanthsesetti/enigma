from reflector import *
import string
from multiple_rotors import *
from single_rotor import *


class TraverseRotors:
    def __init__(self, rotors_list, reflector, rotor_positions, rotor_settings):
        self.reflector = reflector
        self.positioned_rotor_list = []
        self.positioned_a_to_z_list = []
        self.rotor_notch_list = []
        self.rotor_moved =[]
        self.rotor_offsets = []

        # create all rotors and notches
        multiple_rotors = MultipleRotors()
        all_rotors_info, all_a_to_z_info, all_rotor_notches, self.rotor_moved, self.rotor_offsets = \
            multiple_rotors.create_multiple_rotors(rotors_list)
        self.rotor_notch_list = all_rotor_notches

        # ring settings for all rotors
        set_rotor_info = multiple_rotors.set_multiple_rotor_settings(all_rotors_info, rotor_settings)

        # move rotors to the starting positions
        self.positioned_rotor_list, self.positioned_a_to_z_list,  = \
            multiple_rotors.set_multiple_rotor_positions(set_rotor_info, all_a_to_z_info, rotor_positions)

    def traverse_rotors_right_to_left(self, position, character):
        # move the rotors if they are on notches
        rotor_notches = MultipleRotors()
        self.positioned_rotor_list, self.positioned_a_to_z_list, self.rotor_notch_list =\
            rotor_notches.set_multiple_rotor_notches(self.positioned_rotor_list, self.positioned_a_to_z_list,
                                                     self.rotor_notch_list, self.rotor_moved)

        # now traverse each rotor right to left
        for each_rotor, each_a_to_z, each_rotor_notch in zip(reversed(self.positioned_rotor_list),
                                                             reversed(self.positioned_a_to_z_list),
                                                             reversed(self.rotor_notch_list)):
            traverse = SingleRotor()
            position, character = traverse.encode_right_to_left(each_rotor, each_a_to_z, position, character)
        return position, character

    def traverse_reflector(self, position, character):
        traverse = Reflector()
        named_reflector, reflector_a_to_z = traverse.get_reflector(self.reflector)
        position, character = traverse.encode_reflector(named_reflector, reflector_a_to_z, position, character)
        return position, character

    def traverse_rotors_left_to_right(self, position, character):
        if len(self.positioned_rotor_list) == 3:
            # add offset and traverse left most rotor
            offset = ord(self.positioned_a_to_z_list[0][0]) - 65
            char_number = ord(character)
            character = chr(((char_number + offset - 65) % 26) + 65)
            for i, item in enumerate(self.positioned_rotor_list[0]):
                if item == character:
                    position = i

            # traverse middle rotor
            character = self.positioned_a_to_z_list[1][position]
            for i, item in enumerate(self.positioned_rotor_list[1]):
                if item == character:
                    position = i

            # traverse right rotor
            character = self.positioned_a_to_z_list[2][position]
            for i, item in enumerate(self.positioned_rotor_list[2]):
                if item == character:
                    position = i

            # take the position of the character from right rotor and find the character in A to Z
            character = chr(65 + position)
            return character

        elif len(self.positioned_rotor_list) == 4:
            # add offset and traverse left most rotor
            offset = ord(self.positioned_a_to_z_list[0][0]) - 65
            char_number1 = ord(character)
            character = chr(((char_number1 + offset - 65) % 26) + 65)
            for i, item in enumerate(self.positioned_rotor_list[0]):
                if item == character:
                    position = i

            # traverse second from left rotor
            character = self.positioned_a_to_z_list[1][position]
            for i, item in enumerate(self.positioned_rotor_list[1]):
                if item == character:
                    position = i

            # traverse second rotor from right
            character = self.positioned_a_to_z_list[2][position]
            for i, item in enumerate(self.positioned_rotor_list[2]):
                if item == character:
                    position = i

            # traverse right rotor
            character = self.positioned_a_to_z_list[3][position]
            for i, item in enumerate(self.positioned_rotor_list[3]):
                if item == character:
                    position = i

            # take the position of the character from right rotor and find the character in A to Z
            character = chr(65 + position)
            return character
