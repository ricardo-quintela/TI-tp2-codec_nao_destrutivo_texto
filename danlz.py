from aux_funcs import *
import numpy as np
import sys


def main(args):

    #exit if not enough params
    if len(args) != 2:
        return

    #show help message
    if args[1] == "-help":
        print("============\n"
              "    HELP    \n"
              "============\n"
              "Usage: danlz PATH\n\n"
              "PATH: the path of the file to be analyzed\n"
             )
        return

    #store the filename
    filename = args[1]

    #read the text in the path
    try:
        file = readText(filename)
    except FileNotFoundError:
        print("Erro! " + filename + " nao existe!")
        return


    #analyze the data with the correct coding
    saveData(filename, "------------------\n%s\nEntropia: %s" % (remFolderName(filename), entropia(file, np.arange(0, 2**8))))
    anlzFt(file, np.arange(0, 2**8), filename)

if __name__ == "__main__":
    main(sys.argv)