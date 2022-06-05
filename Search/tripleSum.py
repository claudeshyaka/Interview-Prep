
def tripleSum(a, b, c):
    count_p = 0
    count_q = 0
    count = 0
    sorted_a = sorted(set(a))
    sorted_b = sorted(set(b))
    sorted_c = sorted(set(c))
    
    for q in sorted_b:
        while count_p < len(sorted_a) and q >= sorted_a[count_p]:
            count_p += 1
                    
        while count_q < len(sorted_c) and q >= sorted_c[count_q]:
            count_q += 1
    
        count += count_p*count_q
    
    return count

a = [1, 4, 5]
b = [2, 3, 3]
c = [1, 2, 3]
print(tripleSum(a, b, c))