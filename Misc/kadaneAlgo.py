# Kadane algo

def maxSumSubArray(arr):
    n = len(arr)
    local_max = arr[0]
    global_max = arr[0]
    for i in range(1, n):
        local_max = max(local_max, local_max+arr[i])
        if local_max > global_max:
            global_max = local_max
    return global_max

arr = [1,2,4,5]
print(maxSumSubArray(arr))