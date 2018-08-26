"""
Contest 1:

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50


测试地址：
https://leetcode.com/contest/weekly-contest-99/problems/surface-area-of-3d-shapes/

每个叠起来的正方体面数有
6 * x - 2 * (x-1)个。
确定好上下左右每个被覆盖的面减去即可。


"""

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        result = 0
        
        lengthY = len(grid)
        lengthX = len(grid[0])
        
        for i in range(lengthY):
            for j in range(lengthX):
                if grid[i][j] != 0:
                    temp_result = 6 * grid[i][j] - 2 * (grid[i][j] - 1)
                    left = min(grid[i][j-1], grid[i][j]) if j-1 >= 0 else 0
                    right = min(grid[i][j+1], grid[i][j]) if j+1 <= lengthX-1 else 0
                    up = min(grid[i-1][j], grid[i][j]) if i-1 >= 0 else 0
                    down = min(grid[i+1][j], grid[i][j]) if i+1 <= lengthY-1 else 0
                    result += (temp_result - sum([left, right, up, down]))
        return result
