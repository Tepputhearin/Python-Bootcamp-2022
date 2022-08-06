def append_file(filename):
    from datetime import datetime
    lists = []
    write = open(f"D:/New Folder/Test2/b/{filename}", 'w')
    while True:
        now = datetime.now()
        log = now.strftime("%d/%m/%Y %H:%M:%S")
        user = input("$:")
        if user == "EXIT":
            break
        else:
            lists.append(f"[{log}] {user} ")
    wr = write.writelines(lists)
    write.close()
    read = open(f"D:/New Folder/Test2/b/{filename}", 'r')
    re = read.readline()
    print(re)
    return


append_file("add.txt")