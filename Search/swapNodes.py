from collections import deque
from unittest import result

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def swapNodes(indexes, queries):
    # Write your code here
    def create(root, indexes):
        q = deque([root])
        for x, y in indexes:
            temp = q.popleft()
            if x != -1:
                temp.left = Node(x)
                q.append(temp.left)
            if y != -1:
                temp.right = Node(y)
                q.append(temp.right)
        return root
    
    root = Node(1)
    root = create(root, indexes)
    
    def swap(root, k, level, l):
        if root:
            if level%k == 0:
                root.left, root.right = root.right, root.left
        
        swap(root.left, k, level+1, l)
        l.append(root.value)
        swap(root.right, k, level+1, l)
    
    result = []
    for k in queries:
        l = []
        swap(root, k, 1, l)
        result.append(l) 
    return result


indexes = [2, 3, -1, -1, -1, -1]
queries = [1, 1]
swapNodes(indexes, queries)