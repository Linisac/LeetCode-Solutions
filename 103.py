# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        def fun(root, ltor):
            leftResult = rightResult = []
            if root.left != None:
                leftResult = fun(root.left, not ltor)
            if root.right != None:
                rightResult = fun(root.right, not ltor)
            result = [[root.val]]
            lenLeftResult = len(leftResult)
            lenRightResult = len(rightResult)
            for i in range(max(lenLeftResult, lenRightResult)):
                if i >= lenLeftResult:
                    result.append(rightResult[i])
                elif i >= lenRightResult:
                    result.append(leftResult[i])
                else: #i < lenLeftResult and i < lenRightResult
                    if i % 2 == 0:
                        result.append((leftResult[i] + rightResult[i]) if (not ltor) else (rightResult[i] + leftResult[i]))
                    else:
                        result.append((leftResult[i] + rightResult[i]) if ltor else (rightResult[i] + leftResult[i]))
            return result
        if root != None:
            return fun(root, True)
        else:
            return []
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        