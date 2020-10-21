from enigma import *
from traverse import *
from plugboard import *


def run_enigma(ten_pairs, rotors, reflector, initial_rotor_settings, message):
    coded_message = ""
    plugboard = Plugboard()
    plugboard.ten_pairs(ten_pairs) # "HL MO AJ CX BZ SR NI YW DG PK"
    traverse_rotors = TraverseRotors(rotors, reflector, initial_rotor_settings)  # "I II III", "B", "A A A"

    for char in message:
        plugboard_encoded_initial = plugboard.encode(char) # "H"
        # move_right_rotor_by_one = traverse_rotors.move_right_rotor_by_one()
        encoded_character_rtl = traverse_rotors.traverse_rotors_right_to_left(plugboard_encoded_initial)
        encoded_character_ref = traverse_rotors.traverse_reflector(encoded_character_rtl)
        encoded_character_ltr = traverse_rotors.traverse_rotors_left_to_right(encoded_character_ref)
        plugboard_encoded_end = plugboard.encode(encoded_character_ltr)
        coded_message += plugboard_encoded_end
    return coded_message

