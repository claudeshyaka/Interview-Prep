def solution(A, S):
    # write your code in Python 3.6
    subarray = []
    result = 0
    for i in range(1, len(A)):
        for j in range(i):
            if A[j:i] not in subarray:
                subarray.append(A[j:i])

    print(subarray)
    # l = list(subarray)
    for k in subarray:
        m = sum(k)/len(k)
        print (m)
        if m == S:
            result+=1
    return result

print(solution([2,1,3], 2))