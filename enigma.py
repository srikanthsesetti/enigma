# You will need to write more classes, which can be done here or in separate files, you choose.
from run_enigma import *

if __name__ == "__main__":
    # plugboard = Plugboard()
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

    # ten_pairs = input("Enter up to 10 plug lead combinations")
    # split_pairs = ten_pairs.upper().split()
    # while len(split_pairs) > 10:
    #     ten_pairs = input("You can only enter upto 10 plug lead combinations")
    #     split_pairs = ten_pairs.split()
    # ten_pairs = ten_pairs.upper()
    #
    # rotors = input("Enter 3 or 4 rotors to use")
    # split_rotors = rotors.upper().split()
    # while (len(split_rotors) != 3) and (len(split_rotors) != 4):
    #     rotors = input("You can only enter 3 or 4 rotors to use")
    #     split_rotors = rotors.split()
    # rotors = rotors.upper()
    #
    # reflector = input("Enter the reflector to use")
    # while len(reflector) > 1:
    #     reflector = input("You can only enter one reflector to use")
    # reflector = reflector.upper()
    #
    # initial_rotor_settings = input("Enter initial rotor settings")
    # split_settings = initial_rotor_settings.upper().split()
    # while len(split_settings) != len(split_rotors):
    #     initial_rotor_settings = input("You can only enter same number of initial rotor settings as the rotors")
    #     split_settings = initial_rotor_settings.split()
    # initial_rotor_settings = initial_rotor_settings.upper()
    #
    # message = input("Enter the message to encode")
    # message = message.upper()

    # coded_message = run_enigma(ten_pairs, rotors, reflector, initial_rotor_settings, message)
    # print(f'Coded message is: {coded_message}')

    """ setting default values
    Delete at the end
    """

    coded_message1 = run_enigma("HL MO AJ CX BZ SR NI YW DG PK", "I II III", "B", "A A Z", "01 01 01", "HELLOWORLD")
    # print(f'Coded message is: {coded_message1}')
    print(coded_message1 == 'RFKTMBXVVW')

    #
    coded_message2 = run_enigma("PC XZ FM QA ST NB HY OR EV IU", "IV V Beta I", "A", "E Z G P", "18 24 03 05", "BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI")
    print(f'Coded message is: {coded_message2}')

    # coded_message3 = run_enigma("AT LU NR IG", "III II I GAMMA", "A", "V E Q J", "4 24 17 7", "AAAAAAAAAAAAAAAAAAAAAA")
    # print(f'Coded message is: {coded_message3}')

    # coded_message4 = run_enigma("", "I II III", "B", "A A A", "01 02 03", "AAAAAAAAAAAAAAAAAAAAAA")
    # # print(f'Coded message is: {coded_message4}')
    # print(coded_message4 == 'GGFEBRZUOENGGILYLOVDLB')
