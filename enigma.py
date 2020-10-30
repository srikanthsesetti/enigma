import string
from config import *
from run_enigma import *


class PlugLead:
    def __init__(self, mapping):
        self.dict_map = {}
        if self.is_valid_lead(mapping):
            self.dict_map[mapping[0]] = mapping[1]
            self.dict_map[mapping[1]] = mapping[0]

    def encode(self, character):
        if character in self.dict_map:
            return self.dict_map[character]
        else:
            return character

    def is_valid_lead(self, mapping):
        if len(mapping) == 2 and mapping[0] != mapping[1]:
            return True
        elif len(mapping) == 2 and mapping[0] == mapping[1]:
            raise ValueError
        else:
            return False


class Plugboard:
    def __init__(self):
        self.plug_connections = {}
        self.max_plugboard_size = 19

    def is_plugboard_full(self):
        return len(self.plug_connections) >= self.max_plugboard_size

    def encode(self, character):
        if character in self.plug_connections:
            position = string.ascii_lowercase.index(self.plug_connections[character].lower())
            return self.plug_connections[character]
        else:
            position = string.ascii_lowercase.index(character.lower())
            return character

    def add(self, plugs):
        if not self.is_plugboard_full():
            self.plug_connections.update(plugs.dict_map)

    def ten_pairs(self, full_list):
        plug_list = full_list.split()
        for plug in plug_list:
            create_plug = PlugLead(plug)
            self.add(create_plug)


class rotor_from_name:
    def __init__(self, rotor):
        rotor_instance = Config()
        self.named_rotor = rotor_instance.get_rotor(rotor)
        self.a_to_z = rotor_instance.get_rotor('A to Z')

    def encode_right_to_left(self, character):
        # character = self.named_rotor[character]
        # print(f'RTL coded to: {character}')
        for i, item in enumerate(self.a_to_z):
            if item == character:
                return self.named_rotor[i]

    def encode_left_to_right(self, character):
        # character = a_to_z[position]
        for i, item in enumerate(self.named_rotor):
            if item == character:
                # character = rotor[i]
                # print(f'LTR coded to: {a_to_z[i]}')
                return self.a_to_z[i]
