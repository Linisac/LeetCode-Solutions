# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        tree = TreeNode(postorder.pop())
        pos = inorder.index(tree.val)
        leftSublistIn = inorder[:pos]
        rightSublistIn = inorder[pos + 1:]
        lenOfLeftSublistIn = len(leftSublistIn)
        leftSublistPost = postorder[:lenOfLeftSublistIn]
        rightSublistPost = postorder[lenOfLeftSublistIn:]
        if leftSublistIn != []:
            tree.left = self.buildTree(leftSublistIn, leftSublistPost)
        if rightSublistIn != []:
            tree.right = self.buildTree(rightSublistIn, rightSublistPost)
        return tree
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        