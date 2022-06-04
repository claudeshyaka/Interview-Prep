def CountSort(arr):
    output = [0 for p in range(len(arr))]
    count = [0 for q in range(10)]

    for i in range(0, len(arr)):
        count[arr[i]] += 1
    print("Count -> ", count)

    for j in range(1, 10):
        count[j] += count[j-1]
    print("cum count ->", count)

    for k in range(len(arr)-1, -1, -1):
        output[count[arr[k]]-1] = arr[k]
        print(count[arr[k]]-1, ":", output[count[arr[k]-1]])
        count[arr[k]] -= 1
    print(count)
    print(output)


    for l in range(0, len(arr)):
        arr[l] = output[l]

    return arr    

arr = [2, 3, 4, 2, 3, 6, 8, 4, 5]
print(CountSort(arr))