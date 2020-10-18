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
            return self.plug_connections[character]
        else:
            return character

    def add(self, plugs):
        if not self.is_plugboard_full():
            self.plug_connections.update(plugs.dict_map)


class Rotors:
    def __init__(self):
        self.beta = ('L', 'E', 'Y',	'J', 'V', 'C', 'N',	'I', 'X', 'W', 'P',	'B', 'Q', 'M', 'D',	'R', 'T', 'A', 'K',	'Z',
                     'G', 'F', 'U',	'H', 'O', 'S')
        self.gamma = ('F', 'S', 'O', 'K', 'A', 'N', 'U', 'E', 'R', 'H', 'M', 'B', 'T', 'I', 'Y', 'C', 'W', 'L', 'Q',
                      'P', 'Z', 'X', 'V', 'G', 'J', 'D')
        self.i = ('E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P',
                  'A', 'I', 'B', 'R', 'C', 'J')
        self.ii = ('A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N',
                   'P', 'Y', 'F', 'V', 'O', 'E')
        self.iii = ('B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A',
                    'K', 'M', 'U', 'S', 'Q', 'O')
        self.iv = ('E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G',
                   'K', 'D', 'C', 'M', 'W', 'B')
        self.v = ('V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J',
                  'Q', 'O', 'F', 'E', 'C', 'K')
        self.a = ('E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S',
                  'P', 'I', 'K', 'H', 'G', 'D')
        self.b = ('Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z',
                  'C', 'W', 'V', 'J', 'A', 'T')
        self.c = ('F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U', 'Q',
                  'S', 'B', 'N', 'M', 'H', 'L')
        self.a_to_z = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    def get_rotor(self, name):
        if name == 'beta':
            return self.beta
        if name == 'gamma':
            return self.gamma
        if name == 'I':
            return self.i
        if name == 'II':
            return self.ii
        if name == 'III':
            return self.iii
        if name == 'IV':
            return self.iv
        if name == 'V':
            return self.v
        if name == 'A':
            return self.a
        if name == 'B':
            return self.b
        if name == 'C':
            return self.c
        if name == 'A to Z':
            return self.a_to_z


class rotor_from_name():
    def __init__(self, name):
        self.rotor_instance = Rotors()
        self.named_rotor = self.rotor_instance.get_rotor(name)
        self.a_to_z = self.rotor_instance.get_rotor('A to Z')

    def encode_right_to_left(self, char):
        for i, item in enumerate(self.a_to_z):
            if item == char:
                return self.named_rotor[i]

    def encode_left_to_right(self, char):
        for i, item in enumerate(self.named_rotor):
            if item == char:
                return self.a_to_z[i]


# You will need to write more classes, which can be done here or in separate files, you choose.

if __name__ == "__main__":
    plugboard = Plugboard()

    plugboard.add(PlugLead("SZ"))
    plugboard.add(PlugLead("GT"))
    plugboard.add(PlugLead("DV"))
    plugboard.add(PlugLead("KU"))
    plugboard.add(PlugLead("BY"))
    plugboard.add(PlugLead("AQ"))
    plugboard.add(PlugLead("EM"))
    plugboard.add(PlugLead("HC"))
    plugboard.add(PlugLead("DF"))
    plugboard.add(PlugLead("IJ"))
    plugboard.add(PlugLead("PL"))

    assert (plugboard.encode("K") == "U")
    assert (plugboard.encode("A") == "Q")
    assert (plugboard.encode("P") == "P")

    rotor = rotor_from_name("I")
    assert(rotor.encode_right_to_left("A") == "E")
    assert(rotor.encode_right_to_left("O") == "Y")
    assert(rotor.encode_right_to_left("S") == "S")
    assert(rotor.encode_left_to_right("A") == "U")
    assert(rotor.encode_left_to_right("Q") == "H")
    assert(rotor.encode_left_to_right("N") == "K")