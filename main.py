"""
This is simulation of an interactive program to run and encode/decode messages using Enigma machine
Once you start running this program you'll be asked a series of settings that are required to run Enigma
If you wish to end the program at any time simply type quit

"""
from interactive_console import *


if __name__ == "__main__":
    enigma = RunInteractiveEnigma()
    coded_message = enigma.run_interactive_enigma()
    print(f'Coded message is: {coded_message}')