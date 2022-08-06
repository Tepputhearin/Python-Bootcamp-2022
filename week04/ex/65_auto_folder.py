def auto_folder(lists):
    import os
    if len(lists) > 0:
        for i in range(len(lists)):
            if os.path.exists(f"D:/New Folder/Test2/a/{lists[i]}") is True:
                while True:
                    user = input(f"Are you sure you want to replace <{lists[i]}>?[Y/N]\n")
                    if user == "Y":
                        op = os.replace(f"D:/New Folder/Test2/a/{lists[i]}",f"D:/New Folder/Test2/a/{lists[i]}")
                        break
                    elif user == "N":
                        break
                    else:
                        print("Invalid option")
            elif os.path.exists(f"D:/New Folder/Test2/a/{lists[i]}") is False:
                op = os.makedirs(f"D:/New Folder/Test2/a/{lists[i]}")
        return 1
    else:
        return 0
print(auto_folder(["f1","f2","f3","f4"]))