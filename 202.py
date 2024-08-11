class Solution(object):
    def isHappy(self, n):
        orbit = set()
        nextNum = n
        while (nextNum not in orbit):
            orbit.add(nextNum)
            temp = 0
            while nextNum > 0:
                digit = nextNum % 10
                temp += (digit * digit)
                nextNum /= 10
            nextNum = temp
        return (1 in orbit)
        """
        :type n: int
        :rtype: bool
        """
        