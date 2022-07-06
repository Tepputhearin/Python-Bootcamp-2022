def search_in_tuple(tup,search):
    for i in range(len(tup)):
        if search == tup[i]:
            return f"Element found at index: {i}"
    else:
        return "Element not found in the tuple"
print(search_in_tuple((20,15,10,30),10))