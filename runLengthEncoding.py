#https://www.geeksforgeeks.org/run-length-encoding-python/

def encode(message) -> str:
    """
    Encode a string with run-length encoding\n

    Args:
        message: the message to encode

    Returns:
        the encoded string
    """
    encoded_message = ""
    i = 0

    while (i <= len(message) - 1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message) - 1):
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message += str(count) + ch
        i = j + 1
    return encoded_message


def decode(message) -> str:
    """
    Decodes a run-length encoded string\n

    Args:
        message: the string to decode

    Returns:
        the decoded string
    """

    decoded_message = ""

    #iterate through the message to decode each sequence of run-length
    i = 0
    while i < len(message):
        #if the char is not a digit it cant be decoded
        if message[i] == '\n' or message[i] == '\r':
            decoded_message += '\n'
            i += 1
            continue

        length = message[i]
        for k in range(i + 1, len(message)):
            if not message[k].isdigit():
                break
            length += message[k]
            i += 1

        #construct a string length times with the given char
        for j in range(int(length)):
            decoded_message += message[i+1]

        #go to the next symbol
        i += 2

    return decoded_message


if __name__ == "__main__":
    # Provide different values for message and test your program
    encoded_message = encode("ABBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCAB")
    print(encoded_message)
    print(decode(encoded_message))
