class Solution(object):
    def maxArea(self, height):
        length = len(height)
        if length == 2:
            if length[0] >= length[1]:
                return length[1]
            else:
                return length[0]
        else:#length > 2
            if length % 2 == 0:#even length
                a
            else:#odd length
                halflen = length // 2
                lefthalf = height[:halflen + 1]
                righthalf = height[halflen:]
                leftmax = maxArea(self, lefthalf)
                rightmax = maxArea(self, righthalf)
                lefthalfmax = float('-inf')
                for i in range(half):
                    if lefthalfmax < height[i] * (half - i)
        """
        :type height: List[int]
        :rtype: int
        """
        