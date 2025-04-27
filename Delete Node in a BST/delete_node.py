class Solution(object):
    '''solution'''
    def get_successor(self, curr):
        '''get succesor'''
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr

    def deleteNode(self, root, key):
        '''delete node with a given key'''
        if root is None:
            return root
        if root.key > key:
            root.left = self.deleteNode(root.left, key)
        elif root.key < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            succ = self.get_successor(root)
            root.key = succ.key
            root.right = self.deleteNode(root.right, succ.key)

        return root
