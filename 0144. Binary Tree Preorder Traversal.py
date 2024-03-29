# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iteration, stack
class Solution3(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        
        stack = []
        p = root
        while stack or p:
            if p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p = p.right
        
        return res

# recursion, with helper function
class Solution2(object):
    def preorderTraversal(self, root):
        
        res = []
        self.preorderHelper(root, res)
        return res
    
    def preorderHelper(self, root, res):
        if not root:
            return
        res.append(root.val)
        for child in [root.left, root.right]:
            self.preorderHelper(child, res)
        
    
# recursion, no helper function
class Solution1(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        res = [root.val]
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res

