# TresForDataFeeding2025
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pre_order(self, node, path = None):
        '''pre order traversal'''
        if path is None:
            path = []
        if node is None:
            return path
        path.append(node.val)
        self.pre_order(node.left, path)
        return self.pre_order(node.right, path)

    def search(self, root, key):
        if root is None or root.val = None:
            return root
        if root.val and ((root.left and root.left.val == key) or \
                         (root.right and root.right.val == key)):
            return root
        if root.val < key:
            return self.search(root.right, key)

        return self.search(root.left, key)
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root
        parent = self.search(root, key)
        node = parent.right if parent.right == key else parent.left
        if not(node.right or node.left):
            node.val = None
            return root
        parent.val = 

        