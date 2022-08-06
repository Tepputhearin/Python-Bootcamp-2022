def delete_file(filename):
    import os
    while True:
        user = input("Are you sure you want to delete <{filename}>?[Y/N]\n")
        if user == "Y":
            if os.path.isfile(f"D:/New Folder/Test2/b/{filename}"):
                remove = os.remove(f"D:/New Folder/Test2/b/{filename}")
                return 1
            elif os.path.isdir(f"D:/New Folder/Test2/b/{filename}"):
                remove = os.rmdir(f"D:/New Folder/Test2/b/{filename}")
                return 1
        elif user == "N":
            return 0
        else:
            print("Invalid Option")

print(delete_file("Nice.txt"))

