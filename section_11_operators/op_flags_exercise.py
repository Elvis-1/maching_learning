"""
The flags will correspond to audio processing algorithms.

For each flag that is set when the function is called, print an appropraite message

For example:

process_audio(Flags.L | Flags.S)

prints:

Making louder ...
De-essing ...

use the bitwise & operator to do this.

Next, if you have'nt already done this, refactor your program so that it makes use of a dictionary containing flags and corresponding texts. Use a loop together with the dictionary to process the flags

"""

def printb(value):
    print(f"{value:08b}")

class Flags:
    LOUDER = L = 1
    DENOISE = N = 2
    DEESS = S = 4
    NORMALIZE = O = 8
    REMOVECLICKS = R = 18




