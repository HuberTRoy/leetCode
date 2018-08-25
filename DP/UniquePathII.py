"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

与Unique Path 相比就是多了不通的路，这个和边界处理的效果是一样的。不过不通所使用的数字1，所以预处理一下。

其他的不同之处：

在1中会将 0 0 变为1，但如果此处也直接使用的话会造成下面情况的错误：
[[1]]时预处理为[['x']]，但随后如果不做处理会直接变为path为1，但结果是0。
同样的还有[[1,0]]，[[0,1]]
[0, 1]
[1, 0]

需要注意的点：
1. 只要判断开始/结束点为 1 可以直接返回 0。
2. 如果此点不通则不必进行此点的加减运算。

优化小结：
1. 尽量避免多个判断。
    if x + y == 0 and i + j == 0:
        _map[i][j] = 1
    else:
        _map[i][j] = x + y
每次都需要两次判断，
    if x + y != 0:
        _map[i][j] = x + y
    elif i + j == 0:
        _map[i][j] = 1

改成这样效果是一样的,但减少了每次所必须进行的判断数量。
改动后的效果提升明显：
第一个平均耗时 36ms。
第二个只有 24ms。

2. 先完成后优化。
不要想太多，先完成后在优化速度。
最开始的做法是 两个判断 + 预处理 1 + 只判断入口，走完了再判断出口。

跑通之后，发现可以直接判断出口是不是也为 1。
两个判断也可以缩为1~2个。
预处理1更是不必要。

但如果反过来，我不进行预处理 1，不先写两个判断。做起来是很难的，很多开荒的地方都是模糊的。

现在这个版本已经可以了，还可以优化的地方：
预处理第一横排和竖排，这样可以不需要边界判断，也就会减少3~4个判断数量。


测试地址：
https://leetcode.com/problems/unique-paths-ii/description/

beat 76%

"""


class Solution(object):

    def uniquePathsWithObstacles(self, _map):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        if _map[0][0] == 1:
            return 0
            
        if _map[-1][-1] == 1:
            return 0
            
        
        n, m = len(_map), len(_map[0])

        for i in range(n):
            for j in range(m):
                if _map[i][j] == 1:
                    _map[i][j] = 'x'
                    continue
                    
                x = _map[i-1][j] if i - 1 >= 0 and _map[i-1][j] != 'x' else 0
                y = _map[i][j-1] if j - 1 >= 0 and _map[i][j-1] != 'x' else 0
                
                if x + y != 0:
                    _map[i][j] = x + y
                elif i + j == 0:
                    _map[i][j] = 1

        return _map[n-1][m-1]

    # def uniquePathsWithObstacles(self, _map):
    #     """
    #     :type obstacleGrid: List[List[int]]
    #     :rtype: int
    #     """
        
    #     if _map[0][0] == 1:
    #         return 0
    #     if _map[-1][-1] == 1:
    #         return 0
            
    #     for i, d in enumerate(_map):
    #         for j, d2 in enumerate(d):
    #             if d2 == 1:
    #                 _map[i][j] = 'x'
        
    #     n, m = len(_map), len(_map[0])

    #     for i in range(n):
    #         for j in range(m):
    #             if _map[i][j] == 'x':
    #                 continue
    #             x = _map[i-1][j] if i - 1 >= 0 and _map[i-1][j] != 'x' else 0
    #             y = _map[i][j-1] if j - 1 >= 0 and _map[i][j-1] != 'x' else 0
                
    #             if x + y == 0 and i + j == 0:
    #                 _map[i][j] = 1
    #             else:
    #                 _map[i][j] = x + y

    #     return _map[n-1][m-1]

