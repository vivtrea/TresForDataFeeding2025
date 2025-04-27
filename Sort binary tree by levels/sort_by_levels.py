class Node:
    '''node'''
    def __init__(self, L, R, n):
        '''initialize'''
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node, level=0, path=None):
    '''tree level traversal'''
    if path is None:
        path = []
    if node is None:
        return path
    if len(path) <= level:
        path.append([])

    path[level].append(node.value)

    tree_by_levels(node.left, level+1, path)
    tree_by_levels(node.right, level+1, path)

    return [item for sublist in path for item in sublist]
