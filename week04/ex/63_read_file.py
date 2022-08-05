def read_file(string):
    import os
    if os.path.exists(f"D:/New Folder/Test2/a/{string}") is True:
        op = open(f"D:/New Folder/Test2/a/{string}", mode='r')
        op_read = op.readline()
        return op_read
    elif os.path.exists(f"D:/New Folder/Test2/a/{string}") is False:
        print("Invalid FILENAME")
        return


print(read_file("Yes.txt"))