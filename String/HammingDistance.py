"""
汉明距离：
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

相异的部分就是汉明距离。
应用：
搜索引擎中的搜图：
https://blog.csdn.net/liudongdong19/article/details/80541216
基本思路是：
    将图片转换灰度后会有64级，每级对应一个整数，两两对比整数。也就是取汉明距离。

测试用例：
https://leetcode.com/problems/hamming-distance/description/

思路：
利用异或运算相同取0，相异取1，最后计算出
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return str(bin(x ^ y)).count('1')

