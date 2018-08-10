"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

思路：

已知条件：
每一行以及每一列都是升序排列的。
左上角是整个里面最小的。
右下角是整个里面最大的。
右上角是整行中最大的，但是是整列中最小的。
左下角是整列里最大的，整行里最小的。


1. 直接遍历，O(klogn)，每一行都用二分法，有些无脑，但有效。
passed，不过效率低，只beat了 7% 左右。

2. 基于上面的分析，应该是可以减少一些不必要的搜索的。
左下角是整列里最大的，如果target小于它则不必搜索这一整行，用二分法搜索这一列。
然后脱去这层
[
  [1,     4,  7, 11, 15],
  [2,     5,  8, 12, 19],
  [3,     6,  9, 16, 22],
  [10,   13, 14, 17, 24],

  [18, 21, 23, 26, 30]
]
此时同样的思路搜索13，若target大于则不必搜索这一列，直接搜这一行即可。

[
  [1,     4,     7, 11, 15],
  [2,     5,     8, 12, 19],
  [3,     6,     9, 16, 22],

  [10,   13, 14, 17, 24],

  [18, 21, 23, 26, 30]
]

直到搜索到右上角。

这样的效率也是 O(nlogn).

不出所料，比上个稍微好了那么一点点....

3. 基于上面的分析：
可以不用搜索，直接点对点。

搜了18，这个点，如果target比它大，那么就在这一行继续走，走到21，如果比它大那就继续在这一行走，到了23，
如果比它小就搜这一列，这样搜到row或column的尽头，有就是有，没有就是没有。
效率最差是 O(m+n)。

Good, beat 82%.

测试用例：
https://leetcode.com/problems/search-a-2d-matrix-ii/description/

"""
class Solution(object):
    def binarySearch2(self, rawList, target):
        split = len(rawList) // 2
        
        left = rawList[:split]
        right = rawList[split:]
        
        if not left and not right:
            return False
        
        if left and left[-1] == target:
            return True
        
        if right and right[0] == target:
            return True
        
        if len(left) > 1 and left[-1] > target:
            return self.binarySearch2(left, target)
        
        if len(right) > 1 and right[0] < target:
            return self.binarySearch2(right, target)
        
        return False

    def searchMatrix(self, matrix, target):

        if not any(matrix):
            return False

        # column + row -
        column, row = 0, len(matrix) - 1
        column_length = len(matrix[0])

        while row >= 0 and column < column_length:

            if matrix[row][column] == target:
                return True

            if matrix[row][column] > target:
                row -= 1
            else:
                column += 1

        return False

    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """

    #     if not any(matrix):
    #         return False

    #     # column + row -
    #     column, row = 0, len(matrix) - 1
    #     column_length = len(matrix[0])
    #     while row >= 0 and column < column_length:
    #         """
    #             left bottom to right top.
    #         """
    #         if matrix[row][column] == target:
    #             return True

    #         # search column.
    #         if matrix[row][column] > target:
    #             if self.binarySearch2([i[column] for i in matrix[:row]], target):
    #                 return True

    #         # search row.
    #         else:
    #             if self.binarySearch2(matrix[row][column+1:], target):
    #                 return True

    #         row -= 1
    #         column += 1

    #     return False

    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
        
    #     if not any(matrix):
    #         return False
        
    #     for i in matrix:
    #         if i[0] == target:
    #             return True
            
    #         if i[0] < target:
    #             if self.binarySearch2(i, target):
    #                 return True
        
    #     return False
