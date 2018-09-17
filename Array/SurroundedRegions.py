"""

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.


给一个二维数组里面是 'X' 和 'O'，所有并未连着任何边界的 'O' 都变成 'X' 即可。
X X X X
X X O O
X O X X
X X X X
变形后为
X X X X
X X O O
X X X X
X X X X

思路：
1. 一开始用递归，迭代每一个点，把里面所有的和带边界的 O 及其相邻的找出来，把不相邻的 和 相邻的 分别放到两个坐标列表里，然后进行 'O' 'X' 的分配..
  这个思路和写法都没问题... 无奈的是测试数据过大会导致超过最大递归深度，而且比较慢。
  放弃。

2. 这个思路沿用上一个的思路，只不过这次所做的是只迭代四周的即可。 因为不与四周的 'O' 相邻的是不需要在一开始就变得。
所以只迭代找出四周的 'O' 并用递归把它的邻居们都变成另一个字符，或者存坐标也可以。

之后迭代原地图，然后把是标识的变回 'O'，原来是 'O' 的变成 'X' 即可。

效率 O(row*column)

测试链接：
https://leetcode.com/problems/surrounded-regions/description/

beat 40%~60%.
时间上可以通过一些细节做优化，能提升数毫秒，不过就此题来说没有必要，前面的基本都是这个思路。


"""
class Solution(object):
    def makeAround(self, x, y):
        # if x - 1 >= 0 and y - 1 >= 0 and x + 1 < x_maxes and y + 1 < y_maxes:
            # return True
            # right left down up
        return [(y, x-1),
                (y, x+1),
                (y-1, x),
                (y+1, x)]
        # return False
        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #     return board
        
        if not board:
            x_length = 0
        else:
            x_length = len(board[0])
        y_length = len(board)
        
        def translate_o_to_e(x, y):
            # pass
            # coordinate = self.makeAround(x, y)
            # if coordinate:
            for i in self.makeAround(x, y):
                if i[0] >= 0 and i[1] >= 0 and i[0] < y_length and i[1] < x_length:
                    if board[i[0]][i[1]] == "O":
                        board[i[0]][i[1]] = "E"
                        translate_o_to_e(i[1], i[0])

        # up down
        e_coordinate = []
        for i in range(x_length):
            if board[0][i] == 'O':
                board[0][i] = 'E'
                translate_o_to_e(i, 0)

            if board[y_length-1][i] == "O":
                board[y_length-1][i] = 'E'
                translate_o_to_e(i, y_length-1)

        # left right
        for i in range(y_length):
            if board[i][0] == 'O':
                board[i][0] = 'E'
                translate_o_to_e(0, i)

            if board[i][x_length-1] == 'O':
                board[i][x_length-1] = 'E'
                translate_o_to_e(x_length-1, i)

        for y in range(y_length):
            for x in range(x_length):
                if board[y][x] == 'E':
                    board[y][x] = 'O'
                elif board[y][x] == 'O':
                    board[y][x] = 'X'
                    
#         e_coordinate = []
#         for y in range(y_length):
#             for x in range(x_length):
#                 if board[y][x] == 'O':
#                     coordinate = self.makeAround(x, y, x_length, y_length)
#                     if not coordinate:
#                         board[y][x] = 'E'
#                         e_coordinate.append((y, x))
#                     else:
#                         for i in coordinate:
#                             if board[i[0]][i[1]] == 'E':
#                                 board[y][x] = 'E'
#                                 e_coordinate.append((y, x))
#                                 break
#                         else:
#                             board[y][x] = 'X'

#         for i in e_coordinate:
#             board[i[0]][i[1]] = 'O'        
#         def found_o(y, x):
#             result = []
#             coordinate = self.makeAround(x, y, x_length, y_length)
            
#             if not coordinate:
#                 return False, result
            
#             for i in coordinate:
#                 if board[i[0]][i[1]] == 'O':
#                     board[i[0]][i[1]] = 'E'
#                     x = found_o(i[0], i[1])
                    
#                     result.append(i)
#                     result.extend(x[1])
                    
#                     if not x[0]:
#                         return False, result
                    
                    
#             return True, result
        
#         o_coordinate = []
#         x_coordinate = []
#         for y in range(y_length):
#             for x in range(x_length):
#                 if board[y][x] == 'O':
#                     x = found_o(y, x)
#                     if x[0]:
#                         x_coordinate.extend(x[1])
#                     else:
#                         o_coordinate.extend(x[1])
                        
#         # print(o_coordinate)
#         for i in o_coordinate:
#             board[i[0]][i[1]] = 'O'
#         # print(x_coordinate)
#         for i in x_coordinate:
#             # print(i)
#             board[i[0]][i[1]] = 'X'
                # coordinate = self.makeAround(x, y, x_length, y_length)
        
                # if coordinate:
                    # board[y][x] = 'X'