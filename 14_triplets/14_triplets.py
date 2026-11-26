a = [3, 5, 7]
b = [3, 6]
c = [4, 6, 9]


def triplets(a, b, c):
                                           
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    print(a, b, c)

    count = 0                                         

                                                    
    for q in b:
                                                                       
        count_a = len([p for p in a if p <= q])

                                                                       
        count_c = len([r for r in c if r <= q])

                                                     
        count += count_a * count_c

    return count


print(triplets(a, b, c))
