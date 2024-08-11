class Solution(object):
    def canJump(self, nums):
        lennums = len(nums)
        left  = 0
        right = 1
        while left < right and right < lennums:
            rng = range(left, right)
            left = right
            for i in rng:
                if nums[i] + i >= right:
                    right = nums[i] + i + 1
        if right < lennums:
            return False
        else:
            return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        