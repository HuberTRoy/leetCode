"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


想清楚在写。

beat 94%

测试地址：
https://leetcode.com/problems/spiral-matrix-ii/description/

"""
class Solution(object):
        
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        maps = [[0 for i in range(n)] for j in range(n)]
        
        current_value = [i for i in range(1, n*n+1)]
        current_value.reverse()
        
        def makeXY(x, y):
            # up
            # down
            # right
            # left
            return [(x, y-1),
                    (x, y+1),
                    (x+1, y),
                    (x-1, y)]

        def right(x, y):

            while 1:
                if not current_value:
                    return maps
                xy = makeXY(x, y)
                if (y > -1 and x > -1) and (y < n and x < n):
                    if maps[y][x] == 0:
                        maps[y][x] = current_value.pop()
                        y, x = xy[2][1], xy[2][0] 
                    else:
                        # down
                        return down(x-1, y+1)
                else:
                    # down
                    return down(x-1, y+1)

        def down(x, y):

            while 1:
                if not current_value:
                    return maps
                xy = makeXY(x, y)
                if (y > -1 and x > -1) and (y < n and x < n):
                    if maps[y][x] == 0:
                        maps[y][x] = current_value.pop()
                        y, x = xy[1][1], xy[1][0] 

                    else:
                        # left
                        return left(x-1, y-1)
                else:
                    # left
                    return left(x-1, y-1)       
        def left(x, y):

            while 1:
                if not current_value:
                    return maps
                xy = makeXY(x, y)

                if y > -1 and x > -1 and y < n and x < n:
                    if maps[y][x] == 0:
                        maps[y][x] = current_value.pop()
                        y, x = xy[3][1], xy[3][0] 
                    else:
                        # up
                        return up(x+1, y-1)
                else:
                    # up
                    return up(x+1, y-1)  
        def up(x, y):

            while 1:
                if not current_value:
                    return maps
                xy = makeXY(x, y)
                
                if y > -1 and x > -1 and y < n and x < n:
                    if maps[y][x] == 0:
                        maps[y][x] = current_value.pop()
                        y, x = xy[0][1], xy[0][0] 
                    else:
                        # right
                        return right(x+1, y+1)
                else:
                    # right
                    return right(x+1, y+1)              
                
        return right(0, 0)
