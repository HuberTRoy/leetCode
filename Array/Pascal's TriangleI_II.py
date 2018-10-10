"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

帕斯卡三角。

图看链接：
https://leetcode.com/problems/pascals-triangle/description/

顺着思路来即可。

I
测试地址：
https://leetcode.com/problems/pascals-triangle/description/

II
测试地址：
https://leetcode.com/problems/pascals-triangle-ii/description/

II 中的要求是返回最后一个，且空间为 O(K)。下面这个空间不是 O(k) 不过只要修改一下即可。

"""
# I
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        
        for i in range(1, numRows+1):
            x = [0 for j in range(i)]
            x[0] = 1
            x[-1] = 1
            for j in range(1, i-1):
                x[j] = result[-1][j] + result[-1][j-1]
            
            result.append(x)
        
        return result

# II
 class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        
        for i in range(1, numRows+2):
            x = [0 for j in range(i)]
            x[0] = 1
            x[-1] = 1
            for j in range(1, i-1):
                x[j] = result[-1][j] + result[-1][j-1]
            
            result.append(x)
        
        return result[-1]
