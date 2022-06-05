

from attr import has


def pairs(k, arr):
    count = 0
    # initialize dictionary for lookup
    hashmap = {}

    for i in arr:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    for i in arr:
        temp = i + k
        if temp in hashmap:
            count += hashmap[temp]
    return count

arr = [1, 5, 3, 4, 2]
k = 2
print(pairs(k, arr))