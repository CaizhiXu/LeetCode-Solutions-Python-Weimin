# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 2: use BST property, O(k) where k is the length of the result
class Solution(object):
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return root.val + self.rangeSumBST(root.left, L, R) \
                    + self.rangeSumBST(root.right, L, R)


# method 1: recursion, without using property of BST O(n)
class Solution1(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        left = self.rangeSumBST(root.left, L, R)
        right = self.rangeSumBST(root.right, L, R)
        val = root.val if root.val >= L and root.val <= R else 0
        return left + right + val
    
