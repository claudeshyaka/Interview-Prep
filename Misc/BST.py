class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def _insert(self, new_val, node):
        if node.value < new_val:
            if node.right is not None:
                self._insert(new_val, node.right)
            else:
                node.right = Node(new_val)
        else:
            if node.left is not None:
                self._insert(new_val, node.left)
            else:
                node.left = Node(new_val)

    def insert(self, new_val):
        if self.root is None:
            self.root = Node(new_val)
        else:
            self._insert(new_val, self.root)


    def _search(self, find_val, node):
        if node is None:
            return False
        if node.value == find_val:
            return True
        elif node.value < find_val:
            return self._search(find_val, node.right)
        else:
            return self._search(find_val, node.left)
            
    def search(self, find_val):
        return self._search(find_val, self.root)

    # print the in-order traveral of the binary search tree.
    def _printInorder(self, node):
        if node:
            self._printInorder(node.left)
            print(node.value)
            self._printInorder(node.right)
    
    def printInorder(self):
        self._printInorder(self.root)
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

tree.printInorder()