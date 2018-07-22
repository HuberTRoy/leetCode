"""
Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

测试用例：
https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

整体思路：
获取出x和y轴的最大值，然后逐个遍历。

时间复杂度 O(mn)。

"""

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid[0])
        
        # Get line max.
        line_dict = {str(index):max(data) for index, data in enumerate(grid)}
        # Get column max.
        column_dict = {str(index):max((grid[index2][index] for index2 in range(len(grid)))) for index in range(length)}
        
        total_increases = 0
        
        for index, line in enumerate(grid):
            for index2, cell in enumerate(line):
                total_increases += min([line_dict[str(index)], column_dict[str(index2)]]) - cell
        
        return total_increases