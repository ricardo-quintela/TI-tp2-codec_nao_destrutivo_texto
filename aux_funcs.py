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
        filename: the name to appear in the title of the graph
    """

    ocr = ocorrencias(p, a)

    #plot the graph
    plt.figure(1)
    plt.bar(ocr.keys(),ocr.values())
    plt.title(remFolderName(filename))
    plt.xlabel("Symbol")
    plt.ylabel("Occurrences")
    plt.savefig(filename + ".png")


def readText(filename: str, read_type: str = "rb") -> np.ndarray:
    """
    Reads the information from a file and stores it in an array\n

    Args:
        filename: the path of the file to be read
        read_type: binary or normal

    Returns:
        an array with the read information
    """

    try:
        with open(filename, read_type) as f:
            if read_type == 'r':
                return f.read()

            l = list(f.read())
            l.append(0)

            return np.array(l)

    except:

        print("Erro! Ficheiro não encontrado!")
        raise FileNotFoundError

    return None


def writeFile(path: str, text: str):
    """
    Writes the given text on a given file\n

    Args:
        path: the path of the file to write on
        text: the text to write on the file
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

    except:
        print("Erro! Impossivel abrir o ficheiro!")
        return

    print("Texto codificado com sucesso!")



def remFolderName(filename: str) -> str:
    """
    Removes the folder name from the path
    Args:
        filename: the path of the file

    Returns:
        only the name of the file without the folder path
    """
    p = getFolder(filename)[::-1]
    return filename[-filename[::-1].index(p):]


def group(data: np.ndarray) -> np.ndarray:
    """
    Groups the items in the datastream in pairs\n

    Args:
        data: the datastream

    Returns:
        the datastream with its items grouped
    """
    d = data.flatten()

    grouped = np.zeros((round(d.shape[0] / 2, 0),), int) # o grupo de items tem de ter metade do tamanho

    index = 0
    for i in range(0,d.shape[0],2):
        grouped[index] = d[i] << 8 | d[i+1] #shift 8 bits para a direita e depois adiciona o numero uqe queremos agrupar, ou logico
        index += 1

    if grouped.shape[0] % 2 != 0:
        grouped[-1] = d[-1]

    return grouped


def getFolder(filename: str) -> str:
    """
    Returns the folder on which the given path is stored
    Args:
        filename: the path of the file

    Returns:
        the folder of the same given file
    """
    filename = filename.replace("\\", "/")

    try:
        filename = filename[0:-filename[::-1].index("/")]
    except:
        filename = ""

    return filename


def saveData(filename: str, data: str):
    """
    Saves the given data on a text file in the same directory as the filename\n

    Args:
        filename: the path of the file
        data: the data to store in the text file
    """
    #get the directory of the file

    filename = getFolder(filename) + "data.txt"


    with open(filename, "a") as f:
        f.write("\n" + data)