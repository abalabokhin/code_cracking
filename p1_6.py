def compressString(str1):
    cStr = ""
    if len(str1) <= 2:
        return str1

    i = 0
    for j in range(1, len(str1)):
        if str1[i] != str1[j]:
            cStr += (str1[i] + str(j-i))
            i = j

    cStr += (str1[i] + str(len(str1)-i))

    if len(cStr) >= len(str1):
        return str1

    return cStr

print(compressString("a"))
print(compressString("aa"))
print(compressString("ab"))
print(compressString("aaabbbcdddddddddddddddddddddddddd"))
print(compressString("ab"))
print(compressString("ab"))
