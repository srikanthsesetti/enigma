from config import *

class ReflectorFromName:
    def __init__(self, name):
        self.reflector_instance = Config()
        self.a_to_z = self.reflector_instance.get_rotor('A to Z')
        self.named_reflector = self.reflector_instance.get_rotor(name)

    def encode_reflector(self, char):
        for i, item in enumerate(self.named_reflector):
            if item == char:
                print(f'char is {char}')
                print(f'encoded to {item} in reflector')
                return self.a_to_z[i]
