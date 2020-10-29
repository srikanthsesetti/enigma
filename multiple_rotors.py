from single_rotor import *


class MultipleRotors:
    def __init__(self):
        self.all_rotors_info = []
        self.all_a_to_z_info = []
        self.all_rotor_notches = []
        self.rotors_moved = []
        self.rotor_offsets = []

    def create_multiple_rotors(self, rotors_list):
        # print(f'from create multiple rotors rotor list: {rotors_list}')
        rotors_list = rotors_list.split()
        # print(f'from create multiple rotors rotor list: {rotors_list}')
        for each_rotor in rotors_list:
            # print(f'each rotor: {each_rotor}')
            single_rotor = SingleRotor()
            rotor, rotor_a_to_z, rotor_notch = single_rotor.get_single_rotor(each_rotor)
            self.all_rotors_info.append(rotor)
            self.all_a_to_z_info.append(rotor_a_to_z)
            self.all_rotor_notches.append(rotor_notch)
            self.rotors_moved.append(False)
            self.rotor_offsets.append(0)
        return self.all_rotors_info, self.all_a_to_z_info, self.all_rotor_notches, self.rotors_moved, self.rotor_offsets

    def set_multiple_rotor_settings(self, all_rotors_info, rotor_settings):
        # print(f'rotor settings: {rotor_settings}')
        rotor_settings = rotor_settings.split()
        # print(f'rotor settings: {rotor_settings}')
        # print(len(all_rotors_info))
        set_rotor_info = []
        for i in range(len(all_rotors_info)):
            single_rotor = SingleRotor()
            rotor_info = single_rotor.set_single_rotor_setting(all_rotors_info[i], rotor_settings[i])
            set_rotor_info.append(rotor_info)
        return set_rotor_info

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

    def set_multiple_rotor_notches(self, positioned_rotor_list, positioned_a_to_z_list, rotor_notch_list, rotor_moved):
        # print('Check if rotors are on notches')
        if len(positioned_rotor_list) == 3:
            # print(positioned_a_to_z_list)
            if rotor_notch_list[-1] != '' and positioned_a_to_z_list[-1][0] == rotor_notch_list[-1]:
                # print('right rotor on notch')
                if rotor_notch_list[1] != '' and positioned_a_to_z_list[1][0] == rotor_notch_list[1]:
                    # print('middle rotor on notch')
                    # turn the left rotor
                    # print('turn left rotor')
                    turn_left_rotor = SingleRotor()
                    positioned_rotor_list[0], positioned_a_to_z_list[0] = \
                        turn_left_rotor.turn_rotor(positioned_rotor_list[0], positioned_a_to_z_list[0])
                    rotor_moved[0] = True
                # print('turn middle rotor')
                # now turn the middle rotor
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[1], positioned_a_to_z_list[1] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[1], positioned_a_to_z_list[1])
                rotor_moved[1] = True

            elif rotor_notch_list[1] != '' and positioned_a_to_z_list[1][0] == rotor_notch_list[1]:
                # print('right rotor is not on notch but middle rotor on notch')
                # print('turn left rotor')
                # turn the left rotor
                turn_left_rotor = SingleRotor()
                positioned_rotor_list[0], positioned_a_to_z_list[0] = \
                    turn_left_rotor.turn_rotor(positioned_rotor_list[0], positioned_a_to_z_list[0])
                rotor_moved[0] = True
                # print('now turn middle rotor')
                # now turn the middle rotor
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[1], positioned_a_to_z_list[1] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[1], positioned_a_to_z_list[1])
                rotor_moved[1] = True

            elif rotor_notch_list[1] != '' and positioned_a_to_z_list[0][0] == rotor_notch_list[0]:
                # print('right and middle rotors are not on notch but left on notch')
                # print('turn left rotor')
                # turn the left rotor
                turn_left_rotor = SingleRotor()
                positioned_rotor_list[0], positioned_a_to_z_list[0] = \
                    turn_left_rotor.turn_rotor(positioned_rotor_list[0], positioned_a_to_z_list[0])
                rotor_moved[0] = True

            # print('turn right rotor')
            # turn the right rotor before encoding
            turn_right_rotor = SingleRotor()
            positioned_rotor_list[-1], positioned_a_to_z_list[-1] = \
                turn_right_rotor.turn_rotor(positioned_rotor_list[-1], positioned_a_to_z_list[-1])
            rotor_moved[-1] = True
            return positioned_rotor_list, positioned_a_to_z_list, rotor_notch_list
        else:
            if rotor_notch_list[-1] != '' and positioned_a_to_z_list[-1][0] == rotor_notch_list[-1]:
                # print('right rotor on notch')
                if rotor_notch_list[-2] != '' and positioned_a_to_z_list[-2][0] == rotor_notch_list[-2]:
                    # print('second from right rotor on notch')
                    # now turn the third from right rotor.
                    turn_middle_rotor = SingleRotor()
                    positioned_rotor_list[-3], positioned_a_to_z_list[-3] = \
                        turn_middle_rotor.turn_rotor(positioned_rotor_list[-3], positioned_a_to_z_list[-3])
                # now turn the second from right rotor
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[-2], positioned_a_to_z_list[-2] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[-2], positioned_a_to_z_list[-2])
            elif rotor_notch_list[-2] != '' and positioned_a_to_z_list[-2][0] == rotor_notch_list[-2]:
                # print('second from right rotor on notch')
                # now turn the third from right rotor.
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[-3], positioned_a_to_z_list[-3] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[-3], positioned_a_to_z_list[-3])
                # now turn the second from right rotor
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[-2], positioned_a_to_z_list[-2] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[-2], positioned_a_to_z_list[-2])
            elif rotor_notch_list[-3] != '' and positioned_a_to_z_list[-3][0] == rotor_notch_list[-3]:
                # print('third from right rotor on notch')
                # now turn the third from right rotor.
                turn_middle_rotor = SingleRotor()
                positioned_rotor_list[-3], positioned_a_to_z_list[-3] = \
                    turn_middle_rotor.turn_rotor(positioned_rotor_list[-3], positioned_a_to_z_list[-3])

            # turn the right rotor before encoding
            turn_right_rotor = SingleRotor()
            positioned_rotor_list[-1], positioned_a_to_z_list[-1] = \
                turn_right_rotor.turn_rotor(positioned_rotor_list[-1], positioned_a_to_z_list[-1])
            return positioned_rotor_list, positioned_a_to_z_list, rotor_notch_list
