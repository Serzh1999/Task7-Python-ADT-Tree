class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)
    else:
        # Otherwise recur down the tree
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
 
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
def search(root, key):
    # Base Case: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)
 
    # Key is smaller than root's key
    return search(root.left, key)

# Create the root node
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Search for a specific key in the tree
result = search(r, 60)
if result is not None:
    print("Key is present in tree")
else:
    print("Key is not present in tree")