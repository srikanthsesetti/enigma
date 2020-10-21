class Config:
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
