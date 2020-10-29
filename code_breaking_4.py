""""
All known settings are declared upfront
Possible combinations for pluglead A and I will be displayed at the end along with a message which contains the given
crib
Once the possible plugleads and decoded messages are displayed, a quick eyeball check is needed to confirm the
message that makes sense as it is impossible to automate this
You can run this python file to see the results
"""

from run_enigma import *
import itertools

plugboard_pairs = "WP RJ VF HN CG BS"
rotors = "V III IV"
reflector = "A"
ring_settings = "24 12 10"
starting_positions = "S W U"
message = "SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW"
crib = "TUTOR"

possible_a_pairs = ['AD', 'AE', 'AK', 'AL', 'AM', 'AO', 'AQ', 'AT', 'AU', 'AX', 'AZ']
possible_i_pairs = ['ID', 'IE', 'IK', 'IL', 'IM', 'IO', 'IQ', 'IT', 'IU', 'IX', 'IZ']

for a_pair in possible_a_pairs:
    for i_pair in possible_i_pairs:
        if a_pair[1] != i_pair[1]:
            full_plubboard = plugboard_pairs + ' ' + a_pair + ' ' + i_pair
            coded_message = run_enigma(full_plubboard, rotors, reflector, starting_positions, ring_settings, message)
            if crib in coded_message:
                print(f'Found crib in: {coded_message}')
                print(f'Possible missing plugleads are: {a_pair, i_pair}')
