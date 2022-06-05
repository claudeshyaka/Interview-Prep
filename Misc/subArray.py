# Get sub-arrays of an array.

def subArray(l, m):
    
    sub_arr = []
    result = []
    for i in range(1, len(l)+1):
        for j in range(i):
            sub_arr.append(l[j:i])
    
    print("sub array:", sub_arr)

    for i in sub_arr:
        result.append((sum(i) % m))
    print("result:", result)
    return(max(result))

l = [1,2,3]
m = 2
print(subArray(l, m))