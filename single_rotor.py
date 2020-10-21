from config import *


class SingleRotor:
    def __init__(self):
        self.rotor_instance = Config()

    def get_single_rotor(self, name):
        if name == 'I':
            i = self.rotor_instance.get_rotor(name)
            i_a_to_z = self.rotor_instance.get_rotor('A to Z')
            return i, i_a_to_z
        elif name == 'II':
            ii = self.rotor_instance.get_rotor(name)
            ii_a_to_z = self.rotor_instance.get_rotor('A to Z')
            return ii, ii_a_to_z
        elif name == 'III':
            iii = self.rotor_instance.get_rotor(name)
            iii_a_to_z = self.rotor_instance.get_rotor('A to Z')
            return iii, iii_a_to_z
        elif name == 'IV':
            iv = self.rotor_instance.get_rotor(name)
            iv_a_to_z = self.rotor_instance.get_rotor('A to Z')
            return iv, iv_a_to_z
        elif name == 'V':
            v = self.rotor_instance.get_rotor(name)
            v_a_to_z = self.rotor_instance.get_rotor('A to Z')
            return v, v_a_to_z
        elif name == 'beta':
            beta = self.rotor_instance.get_rotor(name)
            beta_a_to_z = self.rotor_instance.get_rotor('A to Z')
            return beta, beta_a_to_z
        elif name == 'gamma':
            gamma = self.rotor_instance.get_rotor(name)
            gamma_a_to_z = self.rotor_instance.get_rotor('A to Z')
            return gamma, gamma_a_to_z

    def set_single_rotor_position(self, rotor, a_to_z, rotor_position):
        char_index = a_to_z.index(rotor_position)  # get the index value for the character from a to z
        rotor = rotor[char_index:] + rotor[: char_index]
        rotor_a_to_z = a_to_z[char_index:] + a_to_z[: char_index]
        return rotor, rotor_a_to_z
