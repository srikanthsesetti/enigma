from config import *


class SingleRotor:
    def __init__(self):
        self.rotor_instance = Config()

    def get_single_rotor(self, name):
        if name == 'I':
            i = self.rotor_instance.get_rotor(name)
            i_a_to_z = self.rotor_instance.get_rotor('A to Z')
            i_notch = self.rotor_instance.get_rotor_notch(name)
            return i, i_a_to_z, i_notch
        elif name == 'II':
            ii = self.rotor_instance.get_rotor(name)
            ii_a_to_z = self.rotor_instance.get_rotor('A to Z')
            ii_notch = self.rotor_instance.get_rotor_notch(name)
            return ii, ii_a_to_z, ii_notch
        elif name == 'III':
            iii = self.rotor_instance.get_rotor(name)
            iii_a_to_z = self.rotor_instance.get_rotor('A to Z')
            iii_notch = self.rotor_instance.get_rotor_notch(name)
            return iii, iii_a_to_z, iii_notch
        elif name == 'IV':
            iv = self.rotor_instance.get_rotor(name)
            iv_a_to_z = self.rotor_instance.get_rotor('A to Z')
            iv_notch = self.rotor_instance.get_rotor_notch(name)
            return iv, iv_a_to_z, iv_notch
        elif name == 'V':
            v = self.rotor_instance.get_rotor(name)
            v_a_to_z = self.rotor_instance.get_rotor('A to Z')
            v_notch = self.rotor_instance.get_rotor_notch(name)
            return v, v_a_to_z, v_notch
        elif name == 'BETA':
            beta = self.rotor_instance.get_rotor(name)
            beta_a_to_z = self.rotor_instance.get_rotor('A to Z')
            beta_notch = self.rotor_instance.get_rotor_notch(name)
            return beta, beta_a_to_z, beta_notch
        elif name == 'GAMMA':
            gamma = self.rotor_instance.get_rotor(name)
            gamma_a_to_z = self.rotor_instance.get_rotor('A to Z')
            gamma_notch = self.rotor_instance.get_rotor_notch(name)
            return gamma, gamma_a_to_z, gamma_notch
        else:
            raise ValueError

    @staticmethod
    def set_single_rotor_position(rotor, a_to_z, rotor_position):
        char_index = a_to_z.index(rotor_position)
        rotor = rotor[char_index:] + rotor[: char_index]
        rotor_a_to_z = a_to_z[char_index:] + a_to_z[: char_index]
        return rotor, rotor_a_to_z

    @staticmethod
    def turn_rotor(rotor, a_to_z):
        rotor = rotor[1:] + rotor[: 1]
        rotor_a_to_z = a_to_z[1:] + a_to_z[: 1]
        return rotor, rotor_a_to_z

    @staticmethod
    def encode_right_to_left(rotor, a_to_z, position, character):
        character = rotor[position]
        for i, item in enumerate(a_to_z):
            if item == character:
                return i, character

    @staticmethod
    def encode_left_to_right(rotor, a_to_z, position, character):
        character = a_to_z[position]
        for i, item in enumerate(rotor):
            if item == character:
                return i, character

    @staticmethod
    def set_single_rotor_setting(rotor, position):
        out_rotor = ()
        position = int(position)
        position -= 1
        for char in rotor:
            char_number = ord(char)
            char = chr(((char_number - 65 + position) % 26) + 65)
            out_rotor = out_rotor + (char,)
        out_rotor = out_rotor[-position:] + out_rotor[: -position]
        return out_rotor
