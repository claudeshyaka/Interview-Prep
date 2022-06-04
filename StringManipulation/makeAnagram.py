
from collections import Counter

def makeAnagram(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)

    union = ((counter_a - (counter_a & counter_b)) | (counter_b - (counter_a & counter_b)))
    return len(list(union.elements()))

makeAnagram("cde", "abc")