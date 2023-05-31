class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def deepestBranch(self):
        # Initialize
        path = f"{self.val}"
        longest_path = f"{self.val}"
        depth = 0
        max_depth = 0

        # Recursion function
        def recur(node, path, depth, longest_path, max_depth):
            path += f" --> {node.val}"
            depth += 1

            if node.left:
                longest_path, max_depth = recur(node.left, path, depth, longest_path, max_depth)
            if node.right:
                longest_path, max_depth = recur(node.right, path, depth, longest_path, max_depth)

            if node.left is None and node.right is None:
                if depth > max_depth:
                    max_depth = depth
                    longest_path = path

            return longest_path, max_depth

        if self.left:
            longest_path, max_depth = recur(self.left, path, depth, longest_path, max_depth)
        if self.right:
            longest_path, max_depth = recur(self.right, path, depth, longest_path, max_depth)

        # If Node is external node
        if self.left is None and self.right is None:
            print(f"\nTree's max depth is 0\n{self.val}")
            return self.val, 0

        print(f"\nTree's max depth is {max_depth}\n{longest_path}")
        return longest_path


def printPreorder(node):
    if node:
        print(node.val, "-->", end=" ")
        printPreorder(node.left)
        printPreorder(node.right)

def printInorder(node):
    if node:
        printInorder(node.left)
        print(node.val, "-->", end=" ")
        printInorder(node.right)

def printPostorder(node):
    if node:
        printPostorder(node.left)
        printPostorder(node.right)
        print(node.val,"-->", end=" ")

# BINARY SORT

def insertSort(node,val):
    if node is None:
        return Node(val)
    else:
        if node.val is val:
            return node
        elif node.val < val:
            node.right = insertSort(node.right, val)
        else:
            node.left = insertSort(node.left, val)
    return node



# Test

'''root = Node('Haziman Sairin')
insertSort(root,'Zikri Hakim')
insertSort(root,'Jameel Majdi')
insertSort(root,'Raniya Waleed')
insertSort(root,'Syukri Talib')
insertSort(root,'Saif al-Din')
insertSort(root,'Nuqman Aliff')
insertSort(root,'Abd al-Karim Mumtaz')
insertSort(root,'Kizzy Harriette')
insertSort(root,'Zharif Aiman')
insertSort(root,'Sharifa Harun')
insertSort(root,'Najma Fuad')
insertSort(root,'Amir Su\'ad')
print("Preorder: ")
printPreorder(root)
print("\nInorder: ")
printInorder(root)
print("\nPostorder: ")
printPostorder(root)
printInorder(root)
root.deepestBranch()'''

root = Node(50)
insertSort(root, 30)
insertSort(root, 20)
insertSort(root, 90)
insertSort(root, 40)
insertSort(root, 70)
insertSort(root, 60)
insertSort(root, 80)
insertSort(root, 75)

# printPreorder(root)
printInorder(root)
# printPostorder(root)

root.deepestBranch()
