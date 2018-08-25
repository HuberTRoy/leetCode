"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28


思路：
直接DP。子问题：
经过当前点的路径一共有多少条。
由于只能向右或者向下且不可返回，每一个点的路径可由左和右的点的路径数相加得来。
边界：
无则为0。

1 1 1
1 2 3

初始化一个 x * x 的列表，并将0, 0设置为1。
之后将每个点的路径数等于左+上。
效率为O(mn)。

2
数学方法暂且跳过。

测试地址：
https://leetcode.com/problems/unique-paths/description/

beat 100%.

"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        _map = [[0 for _ in range(m)] for _ in range(n)]
        # _map[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                x = _map[i-1][j] if i - 1 >= 0 else 0
                y = _map[i][j-1] if j - 1 >= 0 else 0
                
                if x + y == 0:
                    _map[i][j] = 1
                else:
                    _map[i][j] = x + y
                
        return _map[n-1][m-1]

