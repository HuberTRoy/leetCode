"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


思路：

0, 0开始走，
right -> down,
down -> left,
left -> up,
up -> right.
每走过一点，将值添加到结果中，走过的点记为 'x'。当四周都是 'x' 或边界时结束。

测试地址：
https://leetcode.com/problems/spiral-matrix/description/

beat 99.10%.

"""
def checkStop(matrix, x, y):
    t = [(x+1, y),
         (x-1, y),
         (x, y+1),
         (x, y-1),
         (x, y)]
    for i in t:
        try:
            if i[1] < 0 or i[0] < 0:
                continue
                
            if matrix[i[1]][i[0]] != 'x':
                return False
        except IndexError:
            continue
    else:
        return True
    
    
class Solution(object):
    def right(self, matrix, x, y, result, stop):
        if checkStop(matrix, x, y):
            return result
        while 1:
            try:
                # matrix
                if matrix[y][x] == 'x':
                    raise IndexError
                result.append(matrix[y][x])
                matrix[y][x] = 'x'
                x += 1

            except IndexError:
                x -= 1
                return self.down(matrix, x, y+1, result, stop)
    
    def down(self, matrix, x ,y, result, stop):
        if checkStop(matrix, x, y):
            return result
        while 1:
            try:
                # matrix
                if matrix[y][x] == 'x':
                    raise IndexError
                result.append(matrix[y][x])
                matrix[y][x] = 'x'
                y += 1
            except IndexError:
                y -= 1
                return self.left(matrix, x-1, y, result, stop)
    
    def left(self, matrix, x, y, result, stop):
        if checkStop(matrix, x, y):
            return result
        while 1:
            try:
                # matrix
                if matrix[y][x] == 'x' or x < 0:
                    raise IndexError
                result.append(matrix[y][x])
                matrix[y][x] = 'x'
                x -= 1
            except IndexError:
                x += 1
                return self.up(matrix, x, y-1, result, stop)        
    
    def up(self, matrix, x, y, result, stop):
        if checkStop(matrix, x, y):
            return result

        while 1:
            try:
                # matrix
                if matrix[y][x] == 'x' or y < 0:
                    raise IndexError
                result.append(matrix[y][x])
                matrix[y][x] = 'x'
                y -= 1
            except IndexError:
                y += 1
                return self.right(matrix, x+1, y, result, stop)             
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        x, y = 0, 0
        
        result = []
        # right -> down
        # down -> left
        # left -> up
        # up -> right
        stop = {}
        return self.right(matrix, 0, 0, result, stop)
