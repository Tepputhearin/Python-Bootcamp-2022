list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
mid = len(list)//2+1
list1 = list[:mid]
list2 = list[mid:]
def encode():
    list1 = list[:mid]
    list2 = list[mid:]
    join1 = "".join(list1)
    join2 = "".join(list2)
    

encode()