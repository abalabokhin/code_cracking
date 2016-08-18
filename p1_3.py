def changeString(str, len):
    wsn = 0
    for i in range (0, len):
        if str[i] == ' ':
            wsn += 1

    i = len -1
    j = len + 2 * wsn - 1

    while i != j:
        if str[i] != ' ':
            str[j] = str[i]
        else:
            str[j] = "0"
            str[j-1] = '2'
            str[j-2] = '%'
            j -= 2

        j-=1
        i-=1

    return "".join(str)

assert(changeString("", 0) == "")
assert(changeString(list("   "), 1) == "%20")
assert(changeString(list("20 123     "), 7) == "20%20123%20")

