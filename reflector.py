from config import *

class Reflector:
    def __init__(self):
        self.reflector_instance = Config()

    def get_reflector(self, name):
        if name == 'A':
            reflectora = self.reflector_instance.get_rotor(name)
            reflectora_a_to_z = self.reflector_instance.get_rotor('A to Z')
            return reflectora, reflectora_a_to_z
        elif name == 'B':
            reflectorb = self.reflector_instance.get_rotor(name)
            reflectorb_a_to_z = self.reflector_instance.get_rotor('A to Z')
            return reflectorb, reflectorb_a_to_z
        elif name == 'C':
            reflectorc = self.reflector_instance.get_rotor(name)
            reflectorc_a_to_z = self.reflector_instance.get_rotor('A to Z')
            return reflectorc, reflectorc_a_to_z

    def encode_reflector(self, named_reflector, reflector_a_to_z, position, character):
        character = named_reflector[position]
        print(f'Reflector coded to: {character}')
        return position, character


