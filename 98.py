# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        #fun(root) returns a triple (whether_root_is_valid, min_val_of_root, max_val_of_root)
        def fun(root):
            minVal = maxVal = root.val
            leftIsValid = True
            leftMin = leftMax = 0 #0 is dummy initial value
            rightIsValid = True
            rightMin = rightMax = 0 #0 is dummy initial value
            if root.left != None:
                leftIsValid, leftMin, leftMax = fun(root.left)
                minVal = leftMin
            if root.right != None:
                rightIsValid, rightMin, rightMax = fun(root.right)
                maxVal = rightMax
            return ((root.left == None or (leftIsValid and leftMax < root.val)) and
            (root.right == None or (rightIsValid and rightMin > root.val)), minVal, maxVal)
        return fun(root)[0]
        """
        :type root: TreeNode
        :rtype: bool
        """
        