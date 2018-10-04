"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

1. A straight forward solution using O(mn) space is probably a bad idea.
2. A simple improvement uses O(m + n) space, but still not the best solution.
3. Could you devise a constant space solution?

若某点为 0 则此行与此列均设为0。

关键字：
1. 坐标去重。
2. 坐标标记。
3. 利用原来的空间进行标记。

1. 先说去重，去重是我想到的第一种思路：
利用set的O(1) 特性去去重，将坐标转换为字符串，然后在转换回去。

这个的效率正如 进阶的 1 所说，O(mn) 空间，bad idea.

能 beat 20% 左右。

2. 坐标标记
   x     x
x [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]

只需要标记 x 和 y一整行即可，也正如进阶 2 所说，空间 O(m+n)，good but not best.
用这个已经可以beat 94%

3. 主要在于四角，稍后在更。


测试地址：
https://leetcode.com/problems/set-matrix-zeroes/description/

"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # x
        raw_length = len(matrix[0])
        # y
        column_length = len(matrix)
        
        # O(mn) 第一版.
        # {"12", "23", "34"}

#         zero_xy = set()
        
#         def makeXY(x, y):
#             xy = set()
#             x = str(x)
#             y = str(y)
#             for i in range(raw_length):
#                 xy.add(','.join([str(i), y]))
            
#             for i in range(column_length):
#                 xy.add(','.join([x, str(i)]))
                
#             return xy
        
#         for y in range(column_length):
#             for x in range(raw_length):
#                 if matrix[y][x] == 0:
#                     zero_xy.update(makeXY(x, y))

#         for i in zero_xy:
#             t = i.split(',')
#             matrix[int(t[1])][int(t[0])] = 0

#         第二版 O(M+N)
#         raw = []
#         column = []
        
#         for y in range(column_length):
#             for x in range(raw_length):
#                 if matrix[y][x] == 0:
#                     raw.append(x)
#                     column.append(y)
                    
#         for x in raw:
#             for y in range(column_length):
#                 matrix[y][x] = 0
        
#         for y in column:
#             for x in range(raw_length):
#                 matrix[y][x] = 0
