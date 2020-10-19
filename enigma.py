# You will need to write more classes, which can be done here or in separate files, you choose.
from enigma import *
from traverse import TraverseRotors

if __name__ == "__main__":
    # plugboard = Plugboard()
    #
    # plugboard.add(PlugLead("SZ"))
    # plugboard.add(PlugLead("GT"))
    # plugboard.add(PlugLead("DV"))
    # plugboard.add(PlugLead("KU"))
    # plugboard.add(PlugLead("BY"))
    # plugboard.add(PlugLead("AQ"))
    # plugboard.add(PlugLead("EM"))
    # plugboard.add(PlugLead("HC"))
    # plugboard.add(PlugLead("DF"))
    # plugboard.add(PlugLead("IJ"))
    # plugboard.add(PlugLead("PL"))
    #
    # assert (plugboard.encode("K") == "U")
    # assert (plugboard.encode("A") == "Q")
    # assert (plugboard.encode("P") == "P")
    #
    # rotor = rotor_from_name("I")
    # assert(rotor.encode_right_to_left("A") == "E")
    # assert(rotor.encode_right_to_left("O") == "Y")
    # assert(rotor.encode_right_to_left("S") == "S")
    # assert(rotor.encode_left_to_right("A") == "U")
    # assert(rotor.encode_left_to_right("Q") == "H")
    # assert(rotor.encode_left_to_right("N") == "K")
    #
    # rotorII = rotor_from_name("II")
    # assert(rotorII.encode_right_to_left("A") == "A")
    # assert(rotorII.encode_right_to_left("O") == "M")
    # assert(rotorII.encode_right_to_left("S") == "Z")
    # assert(rotorII.encode_left_to_right("A") == "A")
    # assert(rotorII.encode_left_to_right("Q") == "Q")
    # assert(rotorII.encode_left_to_right("N") == "T")

    traverse_all = TraverseRotors("I II III IV", "B")
    encoded_character_r = traverse_all.traverse_rotors_right_to_left('A')
    encoded_character_ref = traverse_all.traverse_reflector(encoded_character_r)
    encoded_character_l = traverse_all.traverse_rotors_left_to_right(encoded_character_ref)

    print(encoded_character_l)
