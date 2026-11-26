def twoStrings(s1, s2):
    for x in s1:
        if x in s2:
            return 'YES'
    return 'NO'


                                           
print(twoStrings('hello', 'world'))
print(twoStrings('hi', 'world'))
