from single_rotor import *


class MultipleRotors:
    def __init__(self):
        self.all_rotors_info = []
        self.all_a_to_z_info = []
        self.all_rotor_notches = []

    def create_multiple_rotors(self, rotors_list):
        rotors_list = rotors_list.split()
        for each_rotor in rotors_list:
            single_rotor = SingleRotor()
            rotor, rotor_a_to_z, rotor_notch = single_rotor.get_single_rotor(each_rotor)
            self.all_rotors_info.append(rotor)
            self.all_a_to_z_info.append(rotor_a_to_z)
            self.all_rotor_notches.append(rotor_notch)
        return self.all_rotors_info, self.all_a_to_z_info, self.all_rotor_notches

    def set_multiple_rotor_positions(self, all_rotors_info, all_a_to_z_info, all_rotor_positions):
        all_rotor_positions = all_rotor_positions.split()
        positioned_rotor_list = []
        positioned_a_to_z_list = []
        for i in range(len(all_rotors_info)):
            single_rotor = SingleRotor()
            positioned_rotor, positioned_a_to_z = single_rotor.set_single_rotor_position(all_rotors_info[i],
                                                                                         all_a_to_z_info[i],
                                                                                         all_rotor_positions[i])
            positioned_rotor_list.append(positioned_rotor)
            positioned_a_to_z_list.append(positioned_a_to_z)
        return positioned_rotor_list, positioned_a_to_z_list

    def set_multiple_rotor_notches(self, positioned_rotor_list, positioned_a_to_z_list, rotor_notch_list):
        if len(positioned_rotor_list) == 3:
            print(f'length is: {(len(positioned_rotor_list))}')
            if positioned_rotor_list[-1][0] == rotor_notch_list[-1]:
                print('third rotor on notch')
                if positioned_rotor_list[1][0] == rotor_notch_list[1]:
                    print('middle rotor on notch')
                    # turn the left rotor. middle rotor will be turned outside this if statement
                    turn_left_rotor = SingleRotor()
                    positioned_rotor_list[0], positioned_a_to_z_list[0] = \
                        turn_left_rotor.turn_rotor(positioned_rotor_list[0], positioned_a_to_z_list[0])
                # now turn the middle rotor. right rotor will always be turned outside this if statement
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[-2], positioned_a_to_z_list[-2] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[-2], positioned_a_to_z_list[-2])
            # turn the right rotor before encoding
            turn_right_rotor = SingleRotor()
            positioned_rotor_list[-1], positioned_a_to_z_list[-1] = \
                turn_right_rotor.turn_rotor(positioned_rotor_list[-1], positioned_a_to_z_list[-1])
            return positioned_rotor_list, positioned_a_to_z_list, rotor_notch_list
        else:
            print(f'length is: {(len(positioned_rotor_list))}')
            if positioned_rotor_list[-1][0] == rotor_notch_list[-1]:
                print('right rotor on notch')
                if positioned_rotor_list[-2][0] == rotor_notch_list[-2]:
                    print('second from right rotor on notch')
                    if positioned_rotor_list[-3][0] == rotor_notch_list[-3]:
                        print('third from right rotor on notch')
                        # turn the left rotor. third from right rotor will be turned outside this if statement
                        turn_left_rotor = SingleRotor()
                        positioned_rotor_list[0], positioned_a_to_z_list[0] = \
                            turn_left_rotor.turn_rotor(positioned_rotor_list[0], positioned_a_to_z_list[0])
                    # now turn the third from right rotor.
                    # second from right rotor will always be turned outside this if statement
                    turn_middle_rotor = SingleRotor()
                    positioned_rotor_list[-3], positioned_a_to_z_list[-3] = \
                        turn_middle_rotor.turn_rotor(positioned_rotor_list[-3], positioned_a_to_z_list[-3])
                # now turn the second from right rotor. right rotor will always be turned outside this if statement
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[-2], positioned_a_to_z_list[-2] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[-2], positioned_a_to_z_list[-2])
            # turn the right rotor before encoding
            turn_right_rotor = SingleRotor()
            positioned_rotor_list[-1], positioned_a_to_z_list[-1] = \
                turn_right_rotor.turn_rotor(positioned_rotor_list[-1], positioned_a_to_z_list[-1])
            return positioned_rotor_list, positioned_a_to_z_list, rotor_notch_list
