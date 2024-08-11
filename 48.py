class Solution(object):
    def rotate(self, matrix):
        length = len(matrix)
        for i in range(length // 2):
            for j in range(length - 1 - i * 2):
                matrix[i][i + j], matrix[i + j][length - 1 - i], matrix[length - 1 - i][length - 1 - i - j], matrix[length - 1 - i - j][i] = matrix[length - 1 - i - j][i], matrix[i][i + j], matrix[i + j][length - 1 - i], matrix[length - 1 - i][length - 1 - i - j]

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        