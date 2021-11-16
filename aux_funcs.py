import numpy as np
import matplotlib.pyplot as plt

def ocorrencias(data: np.ndarray, alfa: np.ndarray, zeros: bool = True) -> dict:
    """
    Counts how many alphabet items are in data\n
    Args:
        data: the datastream
        alfa: The alphabet (set of symbols)
        zeros: whether the array has zeros or not

    Returns:
        the occurrences of each symbol of the alphabet in the datastream
    """
    d=data.flatten()

    #if the function is called with zeros set to true the a dictionary contaioning all the items from the alfabet is created
    if zeros:
        ocorrencias = dict.fromkeys(alfa, 0)
    else:
        ocorrencias = {}

    for element in d:
        if element not in ocorrencias:
            ocorrencias[element] = 0
        ocorrencias[element] += 1

    return ocorrencias


def probability(p: np.ndarray, a: np.ndarray, zeros: bool = False) -> np.ndarray:
    """
    Calculates the probability of occurrence of each symbol\n

    Args:
        p: the array to search for symbols
        a: the alphaber
        zeros: whether the array contains null values or not

    Returns:
        an array with the probability of occurence of each symbol
    """

    ocr=ocorrencias(p, a, zeros)
    ocr= list(ocr.values())
    ocr= np.array(ocr)
    prob = ocr / p.flatten().shape[0]

    return prob


def entropia(p: np.ndarray, a: np.ndarray) -> float:
    """Calculates the entropy of an information source.\n

    Entropy: theoretical minimum limit for the average number of bits needed to encode a symbol.

    Args:
        p: The source of information (sound, text, image, etc.)
        a: The alphabet (set of symbols)

    Returns:
        The entropy of the information source.
    """

    prob = probability(p, a)

    return -np.sum(prob * np.log2(prob))


def anlzFt(p: np.ndarray, a: np.ndarray, filename: str):
    """Analyzes a source of information and determines the occurrence of each of the symbols
     of an alphabet.

    A bar graph showing the occurrence of each symbol is displayed.

    Args:
        p: The source of information (sound, text, image, etc.)
        a: The alphabet (set of symbols)
    """

    ocr = ocorrencias(p, a)

    #plot the graph
    plt.figure(1)
    plt.bar(ocr.keys(),ocr.values())
    plt.title(filename)
    plt.savefig(filename + ".png")


def readText(filename: str) -> np.ndarray:
    """
    Reads the information from a file and stores it in an array\n

    Args:
        filename: the path of the file to be read

    Returns:
        an array with the read information
    """

    try:
        with open(filename, "rb") as f:
            return np.array(list(f.read()))
    except:
        print("Erro! Ficheiro não encontrado!")
        raise FileNotFoundError


def saveData(filename: str, data: str):
    """
    Saves the given data on a text file in the same directory as the filename\n

    Args:
        filename: the path of the file
        data: the data to store in the text file
    """
    #get the directory of the file
    filename = filename.replace("\\", "/")
    try:
        filename = filename[0:-filename[::-1].index("/")] + "data.txt"
    except:
        filename = "data.txt"

    with open(filename, "a") as f:
        f.write("\n" + data)
