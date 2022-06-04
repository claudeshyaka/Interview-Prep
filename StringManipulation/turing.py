def reverseString(text):
    index = -1
    n = len(text)
    l = list(text)
    # Loop from last index until half of the index    
    for i in range(n-1, n//2, -1):
 
        # match character is alphabet or not        
        if l[i].isalpha():
            temp = l[i]
            while True:
                index += 1
                if l[index].isalpha():
                    l[i] = l[index]
                    l[index] = temp
                    break
    return ''.join(l)

print(reverseString("z<*zj"))