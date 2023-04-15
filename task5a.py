class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def printPreorder(node):
    if node:
        print("-->",node.val, end=" ")
        printPreorder(node.left)
        printPreorder(node.right)

def printInorder(node):
    if node:
        printInorder(node.left)
        print("-->",node.val, end=" ")
        printInorder(node.right)

def printPostorder(node):
    if node:
        printPostorder(node.left)
        printPostorder(node.right)
        print("-->",node.val, end=" ")

# Test
root = Node(2)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
root.right.left = Node(6)
root.left.right = Node(4)
root.left.right.left = Node(5)
root.right.right = Node(8)
print("Preorder: ")
printPreorder(root)
print("\nInorder: ")
printInorder(root)
print("\nPostorder: ")
printPostorder(root)
