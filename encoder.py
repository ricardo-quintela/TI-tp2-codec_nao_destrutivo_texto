import sys
import numpy as np
from burrowsWheeler import *
from runLengthEncoding import encode, decode
from aux_funcs import *

def main(args):
    if len(args) == 1 or len(args) > 5:
        print("Error! Bad arguments!")
        return

    #get the console arguments
    param = args[1]

    #show help message
    if param == "-help":
        print(
            "=========\n"
            " Encoder\n"
            "=========\n\n"
            "Usage: encoder param origin destination query_size\n\n"
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


    # get the query size
    if len(args) == 5:
        try:
            querySize = int(args[4])
        except:
            print("Error! Bad query size!")
            return
    else:
        querySize = len(text)

    #encode the message
    if param == "-e":
        encoder = bwt_encoder()

        message = ""

        #iterate through text step by step
        for i in range(0, len(text), querySize):
            end = i + querySize if i + querySize <= len(text) else len(text)

            encoded_message = encoder.encode(text[i:end])
            message += str(encoded_message[0]) + '\t' +  encode(encoded_message[1]) + '\t'

    #decode the message
    elif param == "-d":
        decoder = bwt_decoder()


        # split the text between tabs (\t)
        text = text.split('\t')[:-1]

        message = ""

        # iterate through the decoded message list
        for i in range(0,len(text),2):
            message += decoder.decode(decode(text[i+1]), int(text[i]))

    #write in the destination path the text
    writeFile(destinationPath, message)


if __name__ == "__main__":
    main(sys.argv)