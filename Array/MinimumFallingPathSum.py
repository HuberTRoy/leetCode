"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

 

Note:

1. 1 <= A.length == A[0].length <= 100
2. -100 <= A[i][j] <= 100



从上到下，每下层元素可以选择位于它之上的 左中右 三个元素。

直接 Dp 思路：
从第二层开始，每个元素都选择位于它之上的三个元素中最小的一个元素。
最后输出最后一层中最小的元素即可。

测试地址：
https://leetcode.com/contest/weekly-contest-108/problems/minimum-falling-path-sum/

"""
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        for y in range(1, len(A)):
            for x in range(len(A[0])):
                a = A[y-1][x-1] if x-1 >= 0 else float('inf')
                b = A[y-1][x+1] if x+1 < len(A[0]) else float('inf')
                
                A[y][x] += min(A[y-1][x], a, b)
        
        return min(A[-1])
