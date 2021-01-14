def getinfo():
    id = ""
    pn = ""
    valid = False
    while not valid:
        id = input("please enter a vlid id : ")
        if len(id) == 5 and "A" < id[0] < "Z" and id[1:].isnumeric():
            valid = True
    pn = input("ente the preferd name: ")
    concatenated = id + "*" + pn
    return concatenated


value = getinfo()
print(value)
