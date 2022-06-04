
def alternatingCharacters(s):
    cnt = 0
    x = ""
    for i in s:
        x += i
        if len(x) >= 2:
            print(x)
            if x[len(x)-2] == i:
                cnt+=1
    return cnt

s = "AAABBB"
print(alternatingCharacters(s))
