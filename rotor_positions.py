from rotors import *


def set_all_rotor_positions(rotors, rotor_positions):
    rotor_list = rotors.split()
    rotor_positions = rotor_positions.split()
    positioned_rotor_list = []
    for i in range(len(rotor_list)):
        rotor_i = rotor_from_name(rotor_list[i])
        positioned_rotor = rotor_i.set_rotor_position(rotor_positions[i])
        positioned_rotor_list.append(positioned_rotor)
    return positioned_rotor_list
