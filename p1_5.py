def oneAway (str1, str2):
    lenDiff = len(str1) - len(str2)

    if lenDiff == 0:
        return oneAwayReplacement(str1, str2)
    elif lenDiff == 1:
        return oneAwayAdd(str2, str1)
    elif lenDiff == -1:
        return oneAwayAdd(str1, str2)

    return False

def oneAwayReplacement(str1, str2):
    diffN = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            diffN += 1

    if diffN > 1:
        return False

    return True

def oneAwayAdd(str1, str2):
    # str1 is shorter by 1
    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            j += 1

        return j - i <= 1

assert(oneAway("aa", "ab"))
assert(oneAway("a", "ab"))
assert(oneAway("ab", "b"))
assert(not oneAway("cab", "b"))
assert(oneAway("ac", "abc"))
