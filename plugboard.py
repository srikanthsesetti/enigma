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
        print(f'char is {character}')
        if character in self.plug_connections:
            print(f'encode in plugboard to {self.plug_connections[character]}')
            return self.plug_connections[character]
        else:
            print(f'No connection so returning {character}')
            return character

    def add(self, plugs):
        if not self.is_plugboard_full():
            self.plug_connections.update(plugs.dict_map)

    def ten_pairs(self, full_list):
        plug_list = full_list.split()
        for plug in plug_list:
            create_plug = PlugLead(plug)
            self.add(create_plug)
