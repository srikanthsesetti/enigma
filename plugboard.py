import string
import sys


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

    @staticmethod
    def is_valid_lead(mapping):
        if len(mapping) == 2 and mapping[0] != mapping[1]:
            return True
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
            return position, self.plug_connections[character]
        else:
            position = string.ascii_lowercase.index(character.lower())
            return position, character

    def add(self, plugs):
        if not self.is_plugboard_full():
            self.plug_connections.update(plugs.dict_map)
        else:
            raise ValueError('Maximum 10 plug leads are allowed to connect')

    def ten_pairs(self, full_list):
        plug_list = full_list.split()
        for plug in plug_list:
            try:
                if PlugLead.is_valid_lead(plug) and not self.is_plugboard_full():
                    create_plug = PlugLead(plug)
                    self.add(create_plug)
                else:
                    raise ValueError
            except ValueError:
                print('Please provide maximum 10 valid plugs; '
                      'a plug can connect to just one other plug and cannot connect to itself')
                sys.exit(1)
