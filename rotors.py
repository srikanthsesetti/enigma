from config import *


class rotor_from_name:
    def __init__(self):
        self.rotor_instance = Config()

    def encode_right_to_left(self, rotor, a_to_z, position, character):
        character = rotor[position]
        for i, item in enumerate(a_to_z):
            if item == character:
                return i, a_to_z[i]

    def encode_left_to_right(self, rotor, a_to_z, position, character):
        for i, item in enumerate(rotor):
            if item == character:
                return i, a_to_z[i]

