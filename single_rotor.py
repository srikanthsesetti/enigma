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
        elif name == 'beta':
            beta = self.rotor_instance.get_rotor(name)
            beta_a_to_z = self.rotor_instance.get_rotor('A to Z')
            beta_notch = self.rotor_instance.get_rotor_notch(name)
            return beta, beta_a_to_z, beta_notch
        elif name == 'gamma':
            gamma = self.rotor_instance.get_rotor(name)
            gamma_a_to_z = self.rotor_instance.get_rotor('A to Z')
            gamma_notch = self.rotor_instance.get_rotor_notch(name)
            return gamma, gamma_a_to_z, gamma_notch

    def set_single_rotor_position(self, rotor, a_to_z, rotor_position):
        char_index = a_to_z.index(rotor_position)
        rotor = rotor[char_index:] + rotor[: char_index]
        rotor_a_to_z = a_to_z[char_index:] + a_to_z[: char_index]
        return rotor, rotor_a_to_z

    def turn_rotor(self, rotor, a_to_z):
        rotor = rotor[1:] + rotor[: 1]
        rotor_a_to_z = a_to_z[1:] + a_to_z[: 1]
        return rotor, rotor_a_to_z

    # def is_rotor_on_notch(self, rotor, rotor_position):
