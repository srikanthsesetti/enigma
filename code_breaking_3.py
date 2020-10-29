"""
All known settings are declared upfront
This code might take upto a minute due to the number of permutation
All unknown settings will be printed at the end along with the decoded message
You can run this python file to see the results
"""


from run_enigma import *
import itertools

plugboard_pairs = "FH TS BE UQ KD AL"
reflectors = "ABC"
settings_list = [2, 4, 6, 8, 20, 22, 24, 26]
rotors_list = ['II', 'IV', 'BETA', 'GAMMA']
starting_positions = "E M Y"
message = "ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY"
crib = "THOUSANDS"

rotors_per = list(itertools.permutations(rotors_list, 3))
rotor_settings_per = list(itertools.permutations(settings_list, 3))

print('Running...please wait for it to complete')
for reflector in reflectors:
    for rotor_comb in rotors_per:
        rotors = ' '.join(str(x) for x in rotor_comb)
        for rotor_setting in rotor_settings_per:
            rotor_setting = ' '.join(str(y) for y in rotor_setting)
            decoded_message = run_enigma(plugboard_pairs, rotors, reflector, starting_positions, rotor_setting, message)
            if crib in decoded_message:
                print(f'Reflector used in message: {reflector}')
                print(f'rotors used in message: {rotors}')
                print(f'rotor settings used: {rotor_setting}')
                print(f'Full message is: {decoded_message}')
                break
