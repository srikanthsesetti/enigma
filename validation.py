from plugboard import *
import string


def are_valid_plugleads(ten_pairs):
    split_pairs = ten_pairs.split()
    valid = None
    if len(split_pairs) == 0:
        return True
    if len(split_pairs) <= 10:
        for each_plug in split_pairs:
            if PlugLead.is_valid_lead(each_plug.upper()):
                valid = True
            else:
                return False
        return valid
    else:
        return False


def are_valid_rotors(rotors):
    valid_rotors = ['I', 'II', 'III', 'IV', 'V', 'BETA', 'GAMMA']
    split_rotors = rotors.split()
    valid = None
    if (len(split_rotors) == 3) or (len(split_rotors) == 4):
        for each_rotor in split_rotors:
            if each_rotor.upper() in valid_rotors:
                valid = True
            else:
                return False
        return valid
    else:
        return False


def is_valid_reflector(reflector):
    valid_reflectors = ['A', 'B', 'C']
    if len(reflector) == 1 and reflector.upper() in valid_reflectors:
        return True
    else:
        return False


def are_valid_rotor_positions(initial_rotor_positions, rotors):
    valid_positions = string.ascii_uppercase
    split_positions = initial_rotor_positions.split()
    rotors = rotors.split()
    valid = None
    if len(split_positions) == len(rotors):
        for each_position in split_positions:
            if each_position.upper() in valid_positions:
                valid = True
            else:
                return False
        return valid
    else:
        return False


def are_valid_rotor_settings(initial_rotor_settings, rotors):
    valid_settings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    split_settings = initial_rotor_settings.split()
    len_rotors = rotors.split()
    valid = None
    if len(split_settings) == len(len_rotors):
        for each_setting in split_settings:
            try:
                if int(each_setting) in valid_settings:
                    valid = True
                else:
                    return False
            except ValueError:
                return False
        return valid
    else:
        return False


def is_valid_message(message):
    valid_message_characters = string.ascii_uppercase
    valid = True
    for char in message:
        if char.upper() in valid_message_characters:
            valid = True
        else:
            return False
    return valid
