from traverse import *
from plugboard import *


def run_enigma(ten_pairs, rotors, reflector, initial_rotor_positions, initial_rotor_settings, message):
    ten_pairs = ten_pairs.upper()
    rotors = rotors.upper()
    reflector = reflector.upper()
    # print(f'rotor positions: {initial_rotor_positions}')
    initial_rotor_positions = initial_rotor_positions.upper()
    initial_rotor_settings = initial_rotor_settings.upper()
    message = message.upper()

    coded_message = ""
    plugboard = Plugboard()
    plugboard.ten_pairs(ten_pairs)
    traverse_rotors = TraverseRotors(rotors, reflector, initial_rotor_positions, initial_rotor_settings)

    for char in message:
        # print(f'character to be encoded: {char}')
        plugboard_initial_position, plugboard_encoded_initial = plugboard.encode(char)
        rtl_position, encoded_character_rtl = traverse_rotors.traverse_rotors_right_to_left(plugboard_initial_position, plugboard_encoded_initial)
        ref_position, encoded_character_ref = traverse_rotors.traverse_reflector(rtl_position, encoded_character_rtl)
        encoded_character_ltr = traverse_rotors.traverse_rotors_left_to_right(ref_position, encoded_character_ref)
        plugboard_end_position, plugboard_encoded_end = plugboard.encode(encoded_character_ltr)
        coded_message += plugboard_encoded_end
    return coded_message


def run_interactive_enigma():
    ten_pairs = input("Enter up to 10 plug lead combinations with a space between each combination. \n"
                      "For example, AG EN")
    split_pairs = ten_pairs.upper().split()
    while len(split_pairs) > 10:
        ten_pairs = input("You can only enter upto 10 plug lead combinations")
        split_pairs = ten_pairs.split()
    ten_pairs = ten_pairs.upper()

    rotors = input("Enter 3 or 4 rotors to use")
    split_rotors = rotors.upper().split()
    while (len(split_rotors) != 3) and (len(split_rotors) != 4):
        rotors = input("You can only enter 3 or 4 rotors to use")
        split_rotors = rotors.split()
    rotors = rotors.upper()

    reflector = input("Enter the reflector to use")
    while len(reflector) > 1:
        reflector = input("You can only enter one reflector to use")
    reflector = reflector.upper()

    initial_rotor_positions = input("Enter initial rotor positions")
    split_positions = initial_rotor_positions.upper().split()
    while len(split_positions) != len(split_rotors):
        initial_rotor_positions = input("You can only enter same number of initial rotor positions as the rotors")
        split_positions = initial_rotor_positions.split()
    initial_rotor_positions = initial_rotor_positions.upper()

    initial_rotor_settings = input("Enter initial rotor settings")
    split_settings = initial_rotor_settings.upper().split()
    while len(split_settings) != len(split_rotors):
        initial_rotor_settings = input("You can only enter same number of initial rotor settings as the rotors")
        split_settings = initial_rotor_settings.split()
    initial_rotor_settings = initial_rotor_settings.upper()

    message = input("Enter the message to encode")
    message = message.upper()

    coded_message = run_enigma(ten_pairs, rotors, reflector, initial_rotor_positions, initial_rotor_settings, message)
    return coded_message
