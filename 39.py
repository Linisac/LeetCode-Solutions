class Solution(object):
    def combinationSum(self, candidates, target):
        if target < 0:
            return []
        elif target == 0:
            return [[]]
        else:
            #target > 0:
            result = []
            for i in range(len(candidates)):
                result.extend([[candidates[i]] + x for x in self.combinationSum(candidates[i:], target - candidates[i])])
            return result
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        