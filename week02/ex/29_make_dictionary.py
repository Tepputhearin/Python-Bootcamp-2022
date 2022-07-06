def make_dictionary(list, tuple):
    dict = {}
    for i in range(len(list)):
        dict[list[i]] = tuple[i]
    return dict
print(make_dictionary([50,10,62], ("Borey", "Thirak", "Dane")))