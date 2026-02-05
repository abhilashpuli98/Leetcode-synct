# Last updated: 2/5/2026, 7:40:55 AM
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    count+=(len(grid[i])-j)
                    break
        return count