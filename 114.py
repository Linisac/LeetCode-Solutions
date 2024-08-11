# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        def flattenr(root):
            rootLeft = root.left
            rootRight = root.right
            if rootLeft == None and rootRight == None:
                return (root, root)
            elif rootLeft != None and rootRight == None:
                leftStart, leftEnd = flattenr(rootLeft)
                root.left = None
                root.right = leftStart
                return (root, leftEnd)
            elif rootLeft == None and rootRight != None:
                rightStart, rightEnd = flattenr(rootRight)
                return (root, rightEnd)
            else:
                leftStart, leftEnd = flattenr(rootLeft)
                rightStart, rightEnd = flattenr(rootRight)
                root.left = None
                root.right = leftStart
                leftEnd.right = rightStart
                return (root, rightEnd)
        if root != None:
            flattenr(root)
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        