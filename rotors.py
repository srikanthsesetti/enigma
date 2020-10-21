from config import *


class rotor_from_name:
    def __init__(self, name):
        self.rotor_instance = Config()
        self.named_rotor = self.rotor_instance.get_rotor(name)
        self.a_to_z = self.rotor_instance.get_rotor('A to Z')

    def encode_right_to_left(self, rotor, position, character):
        print(f'position in encode rtl: {position}')
        character = rotor[position]
        for i, item in enumerate(self.a_to_z):
            if item == character:
                print(f'char encode rtl is {character}')
                print(f'encoded to {item} in right to left')
                return i, self.a_to_z[i]

    def encode_left_to_right(self, rotor, position, character):

        for i, item in enumerate(rotor):
            if item == character:
                print(f'char in encode ltr is {character}')
                print(f'encoded to {item} in left to right')
                return i, self.a_to_z[i]

    def set_rotor_position(self, char):
        """ Sets position of each rotor
        Takes the character the rotor needs to be set to
        """
        print(char)
        out_rotor = ()
        char_index = self.a_to_z.index(char)  # get the index value for the character from a to z
        # for i in range(len(self.named_rotor)):
        #     character = self.named_rotor[i]  # for each character in the rotor
        #     i_ord = ord(character)  # get the ord value of the character
        #     if (i_ord >= 65) and (i_ord <= 90):
        #         character = chr(((i_ord - 65 + char_index) % 26) + 65)  #
        #     out_rotor.append(character)

        # for i in self.named_rotor:
        #     character = self.named_rotor[(self.named_rotor.index(char) + 1) % 26]
        #     out_rotor.append(character)
        out_rotor = self.named_rotor[char_index:] + self.named_rotor[: char_index]
        self.a_to_z = self.a_to_z[char_index:] + self.a_to_z[: char_index]
        return out_rotor, self.a_to_z


def set_all_rotor_positions(rotors_list, rotor_positions):
    rotor_list = rotors_list.split()
    rotor_positions = rotor_positions.split()
    positioned_rotor_list = []
    positioned_a_to_z_list = []
    for i in range(len(rotor_list)):
        rotor_i = rotor_from_name(rotor_list[i])
        positioned_rotor, positioned_a_to_z = rotor_i.set_rotor_position(rotor_positions[i])
        positioned_rotor_list.append(positioned_rotor)
        positioned_a_to_z_list.append(positioned_a_to_z)
    return positioned_rotor_list, positioned_a_to_z_list
