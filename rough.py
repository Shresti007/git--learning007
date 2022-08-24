name = "Jessa29Roy"

size = len(name)
i = 0
while i < len(name):
    if name[i].isdecimal():
        break
    else:
        print(name[i], end =" ")
    i += 1

    