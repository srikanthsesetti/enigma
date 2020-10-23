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

    # def set_multiple_rotor_settings(self, all_rotors_info):


    def set_multiple_rotor_notches(self, positioned_rotor_list, positioned_a_to_z_list, rotor_notch_list):
        if len(positioned_rotor_list) == 3:
            if rotor_notch_list[-1] != '' and positioned_rotor_list[-1][0] == rotor_notch_list[-1]:
                print('right rotor on notch')
                if rotor_notch_list[1] != '' and positioned_rotor_list[1][0] == rotor_notch_list[1]:
                    print('middle rotor on notch')
                    # turn the left rotor
                    turn_left_rotor = SingleRotor()
                    positioned_rotor_list[0], positioned_a_to_z_list[0] = \
                        turn_left_rotor.turn_rotor(positioned_rotor_list[0], positioned_a_to_z_list[0])
                    # now turn the middle rotor
                    turn_middle_rotor = SingleRotor()
                    positioned_rotor_list[1], positioned_a_to_z_list[1] = \
                        turn_middle_rotor.turn_rotor(positioned_rotor_list[1], positioned_a_to_z_list[1])

            elif rotor_notch_list[1] != '' and positioned_rotor_list[1][0] == rotor_notch_list[1]:
                print('right rotor is not on notch but middle rotor on notch')
                # turn the left rotor
                turn_left_rotor = SingleRotor()
                positioned_rotor_list[0], positioned_a_to_z_list[0] = \
                    turn_left_rotor.turn_rotor(positioned_rotor_list[0], positioned_a_to_z_list[0])
                # now turn the middle rotor
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[1], positioned_a_to_z_list[1] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[1], positioned_a_to_z_list[1])

            elif rotor_notch_list[1] != '' and positioned_rotor_list[0][0] == rotor_notch_list[0]:
                print('right and middle rotors are not on notch but left on notch')
                # turn the left rotor
                turn_left_rotor = SingleRotor()
                positioned_rotor_list[0], positioned_a_to_z_list[0] = \
                    turn_left_rotor.turn_rotor(positioned_rotor_list[0], positioned_a_to_z_list[0])

            # turn the right rotor before encoding
            turn_right_rotor = SingleRotor()
            positioned_rotor_list[-1], positioned_a_to_z_list[-1] = \
                turn_right_rotor.turn_rotor(positioned_rotor_list[-1], positioned_a_to_z_list[-1])
            return positioned_rotor_list, positioned_a_to_z_list, rotor_notch_list
        else:
            if rotor_notch_list[-1] != '' and positioned_rotor_list[-1][0] == rotor_notch_list[-1]:
                print('right rotor on notch')
                if rotor_notch_list[-2] != '' and positioned_rotor_list[-2][0] == rotor_notch_list[-2]:
                    print('second from right rotor on notch')
                    if rotor_notch_list[-3] != '' and positioned_rotor_list[-3][0] == rotor_notch_list[-3]:
                        print('third from right rotor on notch')
                        # now turn the third from right rotor.
                        turn_middle_rotor = SingleRotor()
                        positioned_rotor_list[-3], positioned_a_to_z_list[-3] = \
                            turn_middle_rotor.turn_rotor(positioned_rotor_list[-3], positioned_a_to_z_list[-3])
                        # now turn the second from right rotor
                        turn_middle_rotor = SingleRotor()
                        positioned_rotor_list[-2], positioned_a_to_z_list[-2] = \
                            turn_middle_rotor.turn_rotor(positioned_rotor_list[-2], positioned_a_to_z_list[-2])
            elif rotor_notch_list[-2] != '' and positioned_rotor_list[-2][0] == rotor_notch_list[-2]:
                print('second from right rotor on notch')
                if rotor_notch_list[-3] != '' and positioned_rotor_list[-3][0] == rotor_notch_list[-3]:
                    print('third from right rotor on notch')
                    # now turn the third from right rotor.
                    turn_middle_rotor = SingleRotor()
                    positioned_rotor_list[-3], positioned_a_to_z_list[-3] = \
                        turn_middle_rotor.turn_rotor(positioned_rotor_list[-3], positioned_a_to_z_list[-3])
                    # now turn the second from right rotor
                    turn_middle_rotor = SingleRotor()
                    positioned_rotor_list[-2], positioned_a_to_z_list[-2] = \
                        turn_middle_rotor.turn_rotor(positioned_rotor_list[-2], positioned_a_to_z_list[-2])
            elif rotor_notch_list[-3] != '' and positioned_rotor_list[-3][0] == rotor_notch_list[-3]:
                print('third from right rotor on notch')
                # now turn the third from right rotor.
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[-3], positioned_a_to_z_list[-3] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[-3], positioned_a_to_z_list[-3])

            # turn the right rotor before encoding
            turn_right_rotor = SingleRotor()
            positioned_rotor_list[-1], positioned_a_to_z_list[-1] = \
                turn_right_rotor.turn_rotor(positioned_rotor_list[-1], positioned_a_to_z_list[-1])
            return positioned_rotor_list, positioned_a_to_z_list, rotor_notch_list
