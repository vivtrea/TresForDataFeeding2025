class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# Pre-order traversal
def pre_order(node, path = None):
    if path is None:
        path = []
    if node is None:
        return path
    path.append(node.data)
    pre_order(node.left, path)
    return pre_order(node.right, path)
# In-order traversal
def in_order(node):
    return []

# Post-order traversal
def post_order(node):
    return []

