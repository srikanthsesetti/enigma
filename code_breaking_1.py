"""
All known settings are declared upfront
Run this python file to see the details of the reflector used and the decoded message
"""

from run_enigma import *

plugboard_pairs = "KI XN FL"
reflectors = "ABC"
crib = "SECRETS"
rotors = "Beta Gamma V"
ring_settings = "04 02 14"
starting_positions = "M J M"
message = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"

for reflector in reflectors:
    decoded_message = run_enigma(plugboard_pairs, rotors, reflector, starting_positions, ring_settings, message)
    if crib in decoded_message:
        print(f'Reflector: {reflector}')
        print(f'Decoded message:  {decoded_message}')
        break
