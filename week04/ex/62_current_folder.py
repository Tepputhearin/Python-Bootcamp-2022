def current_folder():
    import os
    lists = []
    need = os.listdir()
    for i in range(len(need)):
        if os.path.isfile(need[i]):
            lists.append((need[i],"File"))
        elif os.path.isdir(need[i]):
            lists.append((need[i],"Folder"))
    return lists

print(current_folder())