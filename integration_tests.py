from run_enigma import *

assert(run_enigma("", "I II III", "B", "A A A", "01 01 01", "s") == "J")
assert(run_enigma("", "I II III", "B", "A A A", "01 01 01", "A") == "B")
assert(run_enigma("", "IV V Beta", "B", "A A A", "14 09 24", "H") == "Y")
assert(run_enigma("", "I II III", "B", "a a V", "01 01 01", "D") == "O")
assert(run_enigma("", "I II III", "B", "a e V", "01 01 01", "D") == "Z")
assert(run_enigma("", "I II III", "B", "a e V", "01 01 01", "F") == "W")
assert(run_enigma("", "I II III", "B", "a e V", "01 01 01", "HELLO") == "VDXRE")
assert(run_enigma("", "I II III", "B", "a e A", "01 01 01", "H") == "I")
assert(run_enigma("", "I II III", "B", "G G G", "01 01 01", "H") == "J")
assert(run_enigma("", "I II III", "B", "Q E V", "02 02 02", "L") == "Z")
assert(run_enigma("", "I II III", "B", "Q E V", "02 02 02", "Y") == "B")
assert(run_enigma("", "I II III", "B", "Q E V", "01 01 01", "A") == "L")
assert(run_enigma("", "I II III", "B", "b e V", "01 01 01", "H") == "N")
assert(run_enigma("", "I II III", "B", "A A Z", "01 01 01", "A") == "U")
assert(run_enigma("HL MO AJ CX BZ SR NI YW DG PK", "I II III", "B", "A A Z", "01 01 01", "HELLOWORLD") == "RFKTMBXVVW")
assert(run_enigma("", "I II III", "B", "Q E V", "4 1 1", "A") == "S")
assert(run_enigma("", "I II III", "B", "Q E V", "6 1 1", "A") == "J")
assert(run_enigma("", "I II III", "B", "Q E V", "6 1 1", "TIOAHHWPGC") == "HELLOWORLD")
assert(run_enigma("", "I II III", "B", "Q E V", "10 2 1", "H") == "T")
assert(run_enigma("", "I II III", "C", "Q E V", "07 11 15", "Z") == "M")
assert(run_enigma("", "IV I II III", "C", "A A A A", "1 1 1 1", "Z") == "V")
assert(run_enigma("", "I II III IV", "C", "Q E V Z", "07 11 15 19", "Z") == "V")
print(run_enigma("AB CD EF GG IJ KL MN OP QR ST", "I II III IV", "C", "Q E V Z", "07 11 15 19", "A"))
