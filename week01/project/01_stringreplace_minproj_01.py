Para = input("Please input a paragraph:\n")
search = input("Please input a Search String:\n")
if search.isdecimal():
    count_pos = Para.count(search)
    print(f"There are {count_pos} occurrences")
else:
    beg = search[:-len(search) + 1]
    end = search[1:]
    beg_upper = beg.upper()
    up_beg_search = beg_upper + end
    count_pos = Para.count(search) + Para.count(up_beg_search)
    print(f"There are {count_pos} occurrences")