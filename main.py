from aux_funcs import *
import sys


def main(args):

    #get the file name
    if len(args) < 2:
        filename = input("Escreva o nome do ficheiro>>>")
    elif len(args) > 2:
        return
    else:
        filename = args[1]

    #calculate entropy and read the graph
    try:
        file = readText("%s" % (filename))
    except:
        return

    saveData(filename, "------------------\n%s\nEntropia: %s" % (filename, entropia(file, np.arange(0, 2**8))))
    anlzFt(file, np.arange(0, 2**8), filename)

if __name__ == "__main__":
    main(sys.argv)
