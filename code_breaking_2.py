"""
All known settings are declared upfront
Run this python file to see the decoded message and missing ring positions
"""

from run_enigma import *
import itertools
import string

plugboard_pairs = "VH PT ZG BJ EY FS"
reflector = "B"
rotors = "Beta I III"
ring_settings = "23 02 10"
message = "CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH"
crib = "UNIVERSITY"

for i in itertools.permutations(string.ascii_lowercase, 3):
    combination = ' '.join(i)
    decode_message = run_enigma(plugboard_pairs, rotors, reflector, combination, ring_settings, message)
    if crib in decode_message:
        print(f'Missing Ring Positions: {combination.upper()}')
        print(f'Decoded message: {decode_message}')
        break
