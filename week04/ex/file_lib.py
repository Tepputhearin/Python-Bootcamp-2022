class FileLib:
    def inspect(self):
        import os
        path = os.getcwd()
        if os.path.isfile(path):
            print("It is a file")
        elif os.path.isdir(path):
            print("It is a folder")
        else:
            print("Doesn't exist")
        return
    def current_path(self):
        import os
        o = os.getcwd()
        print(o)
        return
    def read(self, filename):
        import os
        if os.path.exists(f"D:/New Folder/Test2/a/{filename}") is True:
            op = open(f"D:/New Folder/Test2/a/{filename}", mode='r')
            op_read = op.readlines()
            op.close()
            print(op_read)
            return
        elif os.path.exists(f"D:/New Folder/Test2/a/{filename}") is False:
            print("Invalid FILENAME")
            return
    def write(self, filename, content):
        import os
        if os.path.exists(f"D:/New Folder/Test2/a/{filename}") is True:
            while True:
                user = input(f"Are you sure you want to replace <{filename}>?[Y/N]\n")
                if user == "Y":
                    wri = open(f"D:/New Folder/Test2/a/{filename}", mode='w')
                    wri.write(content)
                    wri.close()
                    return 1
                elif user == "N":
                    return 0
                else:
                    print("Invalid Option")
        else:
            wri = open(f"D:/New Folder/Test2/a/{filename}", mode='w')
            wri.write(content)
            wri.close()
        return 1
    def append(self, filename):
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
        read.close()
        return
    def remove(self,filename):
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
    def create_folder(self, folder_list):
        import os
        if len(folder_list) > 0:
            for i in range(len(folder_list)):
                if os.path.exists(f"D:/New Folder/Test2/a/{folder_list[i]}") is True:
                    while True:
                        user = input(f"Are you sure you want to replace <{folder_list[i]}>?[Y/N]\n")
                        if user == "Y":
                            op = os.replace(f"D:/New Folder/Test2/a/{folder_list[i]}", f"D:/New Folder/Test2/a/{folder_list[i]}")
                            break
                        elif user == "N":
                            break
                        else:
                            print("Invalid option")
                elif os.path.exists(f"D:/New Folder/Test2/a/{folder_list[i]}") is False:
                    op = os.makedirs(f"D:/New Folder/Test2/a/{folder_list[i]}")
            return 1
        else:
            return 0