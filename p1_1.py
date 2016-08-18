def checkString2(str):
    sorted_str = sorted(str)
    for i in range (0, len(str) - 1):
        if sorted_str[i] == sorted_str[i+1]:
            return False
    return True

def checkString(str):
    #with hash table
    dict = set()
    for c in str:
        if c in dict:
            return False
        dict.add(c)
    return True

assert(not checkString2("aAadr"))
assert(not checkString2("aacdr"))
assert(checkString2("abcdr"))
assert(checkString2(""))
assert(checkString2("aПамbcdr"))
