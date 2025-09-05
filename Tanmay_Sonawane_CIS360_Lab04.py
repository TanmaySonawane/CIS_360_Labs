# Tanmay Sonawane CIS 360 Lab 04
# 10/02/24
      
class Node:
    def __init__(self, data):
        self.data = data  # This stores the operator or operand
        self.left = None  # Left child
        self.right = None  # Right child

    # Pre-order traversal (root -> left -> right)
    def pre_order_traverse(self):
        print(self.data, end=' ')  # Visit root
        if self.left:
            self.left.pre_order_traverse()
        if self.right:
            self.right.pre_order_traverse()

    # In-order traversal (left -> root -> right)
    def in_order_traverse(self):
        if self.left:
            self.left.in_order_traverse()
        print(self.data, end=' ')  # Visit root
        if self.right:
            self.right.in_order_traverse()

    # Post-order traversal (left -> right -> root)
    def post_order_traverse(self):
        if self.left:
            self.left.post_order_traverse()
        if self.right:
            self.right.post_order_traverse()
        print(self.data, end=' ')  # Visit root

def build_expression_tree(postfix_expr):
    stack = []
    
    # Iterate through each symbol in the postfix expression
    for char in postfix_expr:
        if char.isdigit():  # If it's an operand, create a new node and push to stack
            node = Node(char)
            stack.append(node)
        elif char in "+-*/":  # If it's an operator, pop two nodes and create a new tree
            node = Node(char)
            t1 = stack.pop()  # First popped is the right child
            t2 = stack.pop()  # Second popped is the left child
            node.right = t1
            node.left = t2
            stack.append(node)  # Push the new tree to the stack

    # The remaining node in the stack is the root of the expression tree
    return stack.pop()

# Test the code with postfix expressions

# Postfix expression 1: 
postfix_expr1 = "34+56*78+9/-*"
print(f"postfix expression 1: {postfix_expr1}\n")
tree1 = build_expression_tree(postfix_expr1)

print("Pre-order traversal (prefix):")
tree1.pre_order_traverse()
print("\nIn-order traversal (infix):")
tree1.in_order_traverse()
print("\nPost-order traversal (postfix):")
tree1.post_order_traverse()

# Postfix expression 2: 
postfix_expr2 = "48-91+12*7+/*"
print("")
print("")
print(f"postfix expression 2: {postfix_expr2}")
tree2 = build_expression_tree(postfix_expr2)

print("\n\nPre-order traversal (prefix):")
tree2.pre_order_traverse()
print("\nIn-order traversal (infix):")
tree2.in_order_traverse()
print("\nPost-order traversal (postfix):")
tree2.post_order_traverse()
