def make_list(*args):
    list = []
    for i in range(len(args)):
        list.append(args[i])
    return list
print(make_list(21,"Hello",45))