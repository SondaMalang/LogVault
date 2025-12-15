class Node:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        else:
            self.recursive_insert(self.root, value)

    def recursive_insert(self, current_node, value):

        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:  
                self.recursive_insert(current_node.left, value)
             
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.recursive_insert(current_node.right, value)
        
# Test Code
tree = BinarySearchTree()
tree.insert(50)
tree.insert(25) # Should go to Left of 50
tree.insert(75) # Should go to Right of 50

# ... (after inserting 75)

print("Inserting 10...")
tree.insert(10) # Should go Left of 50 -> Left of 25

# CHECK DEEP LEVEL
# If your bug is fixed, 50.left should still be 25
print(f"Level 1 Left: {tree.root.left.value}") 

# And 25.left should be 10
print(f"Level 2 Left: {tree.root.left.left.value}")

# Print the results
print(f"Root: {tree.root.value}")
print(f"Left: {tree.root.left.value}")
print(f"Right: {tree.root.right.value}")