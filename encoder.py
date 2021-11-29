import sys
import numpy as np
from burrowsWheeler import *
from runLengthEncoding import encode, decode
from aux_funcs import *

def main(args):
    if len(args) == 1 or len(args) > 4:
        return

    #get the console arguments
    param = args[1]

    #show help message
    if param == "-help":
        print(
            "=========\n"
            " Encoder\n"
            "=========\n\n"
            "Usage: encoder param origin destination\n\n"
            "Params: -help -> show this message\n"
            "        -e    -> encode a file\n"
            "        -d    -> decode a file\n"
        )
        return

    #get the origin and destination paths
    originPath = args[2]
    destinationPath = args[3]

    #read the file
    try:
        text = readText(originPath, "r")
    except FileNotFoundError:
        print("Erro! " + originPath + " nao existe!")
        return

    #encode the message
    if param == "-e":
        encoder = bwt_encoder()
        encoded_message = encoder.encode(text)
        message = str(encoded_message[0]) + '\n' +  encode(encoded_message[1])

    #decode the message
    elif param == "-d":
        decoder = bwt_decoder()
        message = decoder.decode(decode(text[text.index('\n') + 1:]), int(text[0:text.index('\n')]))

    #write in the destination path the text
    writeFile(destinationPath, message)


if __name__ == "__main__":
    main(sys.argv)