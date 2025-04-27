class Node:
    '''node'''
    def __init__(self, data):
        '''initialize'''
        self.data = data
        self.left = None
        self.right = None
        
# Pre-order traversal
def pre_order(node, path = None):
    '''pre order traversal'''
    if path is None:
        path = []
    if node is None:
        return path
    path.append(node.data)
    pre_order(node.left, path)
    return pre_order(node.right, path)
# In-order traversal
def in_order(node, path = None):
    '''in order traversal'''
    if path is None:
        path = []
    if node is None:
        return path
    in_order(node.left, path)
    path.append(node.data)
    return in_order(node.right, path)

# Post-order traversal
def post_order(node, path = None):
    '''post order traversal'''
    if path is None:
        path = []
    if node is None:
        return path
    post_order(node.left, path)
    post_order(node.right, path)
    path.append(node.data)
    return path
