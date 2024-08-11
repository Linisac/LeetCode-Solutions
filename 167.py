class Solution(object):
    def twoSum(self, numbers, target):
        length = len(numbers)
        for i in range(0, length - 1):
            diff = target - numbers[i]
            #note that it must hold that diff >= numbers[i]
            #because otherwise diff would have been found in an earlier iteration
            if diff == numbers[i]:
                return [i + 1, i + 2]
            else: #diff > numbers[i]
                left = i + 1
                right = length - 1
                while left <= right:
                    middle = (left + right) / 2
                    if numbers[middle] == diff:
                        return [i + 1, middle + 1]
                    elif numbers[middle] < diff:
                        left = middle + 1
                    else: #numbers[middle] > diff
                        right = middle - 1
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        