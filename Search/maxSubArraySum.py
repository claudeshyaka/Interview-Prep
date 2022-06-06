# maximum subarray sum modulo m

import bisect

def maximumSum(a, m):

    prefixSum = 0
    maxSum = 0
    sortedPrefixes = []
    n = len(a)

    for i in range(n):
        prefixSum = (prefixSum + a[i]) % m
        maxSum = max(maxSum, prefixSum)

        startIndex = bisect.bisect_right(sortedPrefixes, prefixSum)
        if startIndex < len(sortedPrefixes):
            maxSum = max(maxSum, prefixSum - sortedPrefixes[startIndex] + m)
        bisect.insort(sortedPrefixes, prefixSum)
    return maxSum
 

a = [3,3,9,9,5]
m = 7
print(maximumSum(a, m))