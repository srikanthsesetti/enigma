# Enigma
An interactive console (CLI) is created to demonstrate working Enigma machine

This console takes settings and a message to encode/decode as user input
Once the user enters all the required settings and message, code will run to output a encoded/decoded message

Interactive enigma machine can be started by running the main.py file

Once main.py is run, a prompt is displayed to enter settings. 
As this interactive console takes user input, each setting needs to be validated before passing through the enigma machine. 
To enable this there is a separate validation.py file. 
Each input is sent to be validated. 
If the input is valid then a prompt will be displayed for the next setting. If not, prompt will ask the user to enter the setting again

Once all settings are entered by the user, encoding request is sent to run_enigma class in run_enigma.py file. 
This will send each character in the message through the machine and stores the enocded result until all characters are encoded. 
Once the whole message is encoded the result is returned to the original main.py file.

**Known Issues**
Currently there's an issue with encoding/decoding using a 4 rotor machine.
