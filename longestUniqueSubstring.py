import functools

def isUnique(str):
    used = '' 
    for i in range(len(str)):
        if str[i] in used:
            return False
        used += str[i]
    return True

def substrings(str):
    """.
    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    """
    subs = []
    for i in range(len(str)):
        for j in range(i, len(str)+1):
            subs.append(str[i:j])
    return subs

print(max(list(filter(isUnique, substrings("bbbbb"))), key=len)) 
