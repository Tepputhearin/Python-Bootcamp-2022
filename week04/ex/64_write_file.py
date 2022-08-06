def write_file(filename, content):
    import os
    if os.path.exists(f"D:/New Folder/Test2/a/{filename}") is True:
        while True:
            user = input(f"Are you sure you want to replace <{filename}>?[Y/N]\n")
            if user == "Y":
                wri = open(f"D:/New Folder/Test2/a/{filename}", mode='w')
                wri.write(content)
                return 1
            elif user == "N":
                return 0
            else:
                print("Invalid Option")
    else:
        wri = open(f"D:/New Folder/Test2/a/{filename}", mode='w')
        wri.write(content)
    return 1
write_file("Ha.txt", "Nice to meet you")