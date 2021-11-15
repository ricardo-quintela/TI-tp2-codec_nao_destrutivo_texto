import numpy as np
import matplotlib.pyplot as plt
from aux_funcs import *

def readText(filename: str):
    """
    Reads the information from a file and stores it in an array\n

    Args:
        filename: the path of the file to be read

    Returns:
        an array with the read information
    """

    with open(filename, "rb") as f:
        return np.array(list(f.read()))



def main():
    file = readText("project_files\\dataset\\bible.txt")
    print(entropia(file, np.arange(0, 2**8)))

if __name__ == "__main__":
    main()