#sample: On July 16, 1969, the Apollo 11 spacecraft launched from the Kennedy Space Center in Florida. Its mission was to go where no human being had gone before—the moon! The crew consisted of Neil Armstrong, Michael Collins, and Buzz Aldrin. The spacecraft landed on the moon in the Sea of Tranquility, a basaltic flood plain, on July 20, 1969. The moonwalk took place the following day. On July 21, 1969, at precisely 10:56 EDT, Commander Neil Armstrong emerged from the Lunar Module and took his famous first step onto the moon’s surface. He declared, “That’s one small step for man, one giant leap for mankind.” It was a monumental moment in human history
while True:
    Para = input("Please input a paragraph:\n")
    search = input("Please input a Search String:\n")
    beg = search[:-len(search) + 1]
    end = search[1:]
    beg_upper = beg.upper()
    up_beg_search = beg_upper + end
    if search.isdecimal():
        count_pos = Para.count(search)
        print(f"There are {count_pos} occurrences")
    else:
        count_pos = Para.count(search) + Para.count(up_beg_search)
        print(f"There are {count_pos} occurrences")
    while True:
        replace = input("Do you want to replace the text[Y/N]?\n")
        if replace == "Y" or replace == "y":
            replace = input("Please input a replacement string:\n")
            num_re = int(input("How many occurrences do you want to replace?\n"))
            num_re2 = num_re - Para.count(up_beg_search)+1
            Para_re = Para.replace(search , replace, num_re2)
            Para_re2 = Para_re.replace(up_beg_search, replace, Para.count(up_beg_search))
            print(f"{num_re} words has be replaced from the paragraph")
            print(Para_re2)
            break
        elif replace == "N" or replace == "n":
            replace = input("Oh!you don't like to replace,Do you want check again[Y/N]?\n")
            if replace == "N" or replace == "n":
                break
            else:
                print("Please give proper input")
        else:
            if replace != "Y" or replace != "y" or replace != "n" or replace != "N":
                print("Please give proper input")
    break
