def encode():
    userstr = input("Enter the string to encode:\n")
    dict = {'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z','N':'A', 'O':'B', 'P':'Q', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    list = []
    for i in userstr:
        convert = list.append(dict[i])
    print("The endcode text is:","".join(list))
def decode():
    userstr = input("Enter the string to decode:\n")
    dict = {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'Q', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    list = []
    for i in userstr:
        convert = list.append(dict[i])
    print("The decoded text is:","".join(list))
while True:
    userch = input("Press 1 to encode\nPress 2 to decode\n")
    if userch == "1":
        encode()
    elif userch == "2":
        decode()
    usercon = input("Do you want to continue?[Y/N]\n")
    if usercon == "N":
        break