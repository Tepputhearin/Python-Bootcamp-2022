def dict_values(dict):
    for i in dict:
        jo = " ".join(dict[i])
        print(f"{i}: {jo}\n******")
    return
print(dict_values({120:("Visal", "Borey", "Sovann"), 130:("Hout","Mouyleng", "Pidor"), 140:("Nary", "Misora", "Masaki")}))
