def oneEditReplace(str1, str2):
    foundDifference = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if foundDifference:
                return False
            foundDifference = True
    return True

def oneEditInsert(str1, str2):
    index1 = 0
    index2 = 0
    
    while index2 < len(str2) and index1 < len(str1):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 = index2 + 1
        else:
            index1 = index1 + 1
            index2 = index2 + 1
    return True

def oneEditAway(str1, str2):
    if len(str1) == len(str2):
        return oneEditReplace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return oneEditInsert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return oneEditInsert(str2, str1)
    else:
        return False
    
print(oneEditAway("ple", "pale"))
print(oneEditAway("pale", "pales"))
print(oneEditAway("bale", "pale"))
print(oneEditAway("bae", "pale"))
