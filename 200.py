class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        numOfIslands = 0
        
        #BFS
        for p in range(m):
            for q in range(n):
                if grid[p][q] == "1":
                    #grid[p][q] is land
                    grid[p][q] = "0" #marked as visited (water)
                    expansion = [(p, q)]
                    while expansion != []:
                        (i, j) = expansion.pop(0)
                        if i - 1 >= 0 and grid[i - 1][j] == "1":
                            grid[i - 1][j] = "0"
                            expansion.append((i - 1, j))
                        if i + 1 <= m - 1 and grid[i + 1][j] == "1":q
                            grid[i + 1][j] = "0"
                            expansion.append((i + 1, j))
                        if j - 1 >= 0 and grid[i][j - 1] == "1":
                            grid[i][j - 1] = "0"
                            expansion.append((i, j - 1))
                        if j + 1 <= n - 1 and grid[i][j + 1] == "1":
                            grid[i][j + 1] = "0"
                            expansion.append((i, j + 1))
                    numOfIslands += 1
        return numOfIslands
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        