# Tanmay Sonawane CIS 360 Lab 05
# 10/09/24

class BinaryNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def addToTree(k, v):
    # Insert the node in the correct position in the BST
    if k < v.key:
        if v.left is None:
            v.left = BinaryNode(k)
        else:
            addToTree(k, v.left)
    elif k > v.key:
        if v.right is None:
            v.right = BinaryNode(k)
        else:
            addToTree(k, v.right)

def findAllInRange(k1, k2, v):
    if v is None:
        return []
    
    if k1 <= v.key <= k2:
        L = findAllInRange(k1, k2, v.left)
        R = findAllInRange(k1, k2, v.right)
        return L + [v.key] + R
    elif v.key < k1:
        return findAllInRange(k1, k2, v.right)
    elif k2 < v.key:
        return findAllInRange(k1, k2, v.left)

def outputTree(v):
    # Print the node in the format key(left, right)
    if v is None:
        return
    left_key = v.left.key if v.left else 'e'
    right_key = v.right.key if v.right else 'e'
    print(f"{v.key}({left_key},{right_key})", end="; ")
    if v.left:
        outputTree(v.left)
    if v.right:
        outputTree(v.right)

# Main program to construct the BST with a predefined list of integers
def main():
    # Predefined list of integers
    integers = [6, 4, 8, 2, 7, 3, 1]

    # Initialize the root of the BST with the first integer
    root = BinaryNode(integers[0])

    # Insert the rest of the integers into the BST
    for key in integers[1:]:
        addToTree(key, root)

    # Print the tree
    print("The tree is:")
    outputTree(root)
    print(" ")

    integers = [1,2,6,8,33,94,62,4,55,91,622,45,46,10,23,73,16,13,19,7]
    root = BinaryNode(integers[0])
    for key in integers[1:]:
        addToTree(key, root)

    print("The tree is:")
    outputTree(root)
    print(" ")
    
    # Test case 1: Find all elements in range [10, 20]
    print("Elements in range [1, 20] for tree 2:", findAllInRange(1, 20, root))

    # Test case 2: Find all elements in range [5, 15]
    print("Elements in range [30, 100] for tree 2:", findAllInRange(30, 100, root))

# Execute the program
if __name__ == "__main__":
    main()
