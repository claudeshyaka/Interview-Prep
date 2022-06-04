
from collections import Counter
def substrCount(s):
    l = []
    count = 0
    ch = None
    n = len(s)
    
    for i in range(n):
        if s[i] == ch:
            count+=1
        else:
            if ch is not None:
                l.append((ch, count))
            ch = s[i]
            count = 1
    l.append((ch,count))

    ans = 0
    for i in l:
        ans += (i[1])*(i[1]+1)//2

    for j in range(1, len(l)-1):
        if l[j-1][0]==l[j+1][0] and l[j][1] == 1:
            ans += min(l[j-1][1], l[j+1][1])
    
    return ans

print(substrCount("aaaa"))