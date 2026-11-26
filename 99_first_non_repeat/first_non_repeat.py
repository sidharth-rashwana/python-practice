def non_repeat_m1(s:str):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] +=1

    s = sorted(d.items(),key=lambda x:x[1])
    return s[0]


def non_repeat_m2(s:str):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] +=1

    for k,v in d.items():
        if v == 1:
            return k
    return None

print(non_repeat_m1("swiss"))                               
print(non_repeat_m2("swiss"))