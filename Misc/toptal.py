from collections import Counter
import math
def solution(T, R):
    passed = 0
    counter_test = Counter()

    for k in T:
        if k[len(k)-1].isnumeric():
            counter_test[k[len(k)-1]] = 1
        else:
            counter_test[k[len(k)-2]] = 1           
        
    print("groups", counter_test) 
    for i, j in zip(T, R):
        # print(i, j)
        # print(i[len(i)-1])
        if j == "OK" and i[len(i)-1].isnumeric():
            passed += 1

    score = (passed * 100) / len(counter_test)
    return math.floor(score)

T = ["test1a", "test2", "test1b", "test1c", "test3"]
R = ["Wornf", "OK", "Runtime", "OK", "Time Li"]
print(solution(T, R))

