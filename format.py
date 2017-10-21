class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0

        visited = []
        
        def getMaxArea(i, j):
            print(i, j)
            if [i, j] not in visited and i>=0 and i<=len(grid)-1 and j>=0 and j<=len(grid[0])-1:
                visited.append([i, j])
                if grid[i][j] == 1:
                    # if i == 0:
                    print(True)
                    return 1 + getMaxArea(i+1, j) + getMaxArea(i-1, j) + getMaxArea(i, j+1) + getMaxArea(i, j-1)
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                current = getMaxArea(grid[i][j])
                if current > maxArea:
                    maxArea = current
                    
        return maxArea