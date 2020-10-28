from traverse import *
from plugboard import *


def run_enigma(ten_pairs, rotors, reflector, initial_rotor_positions, initial_rotor_settings, message):
    ten_pairs = ten_pairs.upper()
    rotors = rotors.upper()
    reflector = reflector.upper()
    initial_rotor_positions = initial_rotor_positions.upper()
    initial_rotor_settings = initial_rotor_settings.upper()
    message = message.upper()

    coded_message = ""
    plugboard = Plugboard()
    plugboard.ten_pairs(ten_pairs)
    traverse_rotors = TraverseRotors(rotors, reflector, initial_rotor_positions, initial_rotor_settings)

    for char in message:
        print(f'character to be encoded: {char}')
        plugboard_initial_position, plugboard_encoded_initial = plugboard.encode(char)
        rtl_position, encoded_character_rtl = traverse_rotors.traverse_rotors_right_to_left(plugboard_initial_position, plugboard_encoded_initial)
        ref_position, encoded_character_ref = traverse_rotors.traverse_reflector(rtl_position, encoded_character_rtl)
        encoded_character_ltr = traverse_rotors.traverse_rotors_left_to_right(ref_position, encoded_character_ref)
        plugboard_end_position, plugboard_encoded_end = plugboard.encode(encoded_character_ltr)
        coded_message += plugboard_encoded_end
    return coded_message
