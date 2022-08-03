def message_converter(message):
    character = []
    hex_deci = []
    for i in range(len(message)):
        char = message[i:i+1]
        char = ord(char)
        character.append(char)
    for j in range(len(character)):
        hexa = hex(character[j])
        hex_deci.append(hexa[2:])
    new = "".join(hex_deci)
    newer = new.upper()
    print(newer)
    return





message_converter("Hello")