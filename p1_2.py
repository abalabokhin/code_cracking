#no unicode with array
def isPerm(str1, str2):
    if len(str1) != len(str2):
        return False
    dict = [0] * 256
    for c in str1:
        dict[ord(c)] += 1

    for c in str2:
        num = ord(c)
        dict[num] -= 1
        if dict[num] < 0:
            return False

    return True

assert(isPerm("", ""))
assert(not isPerm("a", "b"))
assert(isPerm("aab", "baa"))
assert(not isPerm("aab", "bab"))
assert(not isPerm("a", "ab"))
assert(isPerm("П", "a"))
