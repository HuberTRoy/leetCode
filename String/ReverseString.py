"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"

倒序字符串，在 Python 中应该是非常简单的，Python 的字符串支持分片操作。

基本有这么几种方法：
1. 创建新字符串，从后向前迭代，然后与新字符串合并。
2. 直接用分片 [::-1]
3. 转换成列表，然后翻转列表。

经测试 2 和 3的效率差不多，没看源码，底层2应该用的1的思路实现的吧。


测试用例：
https://leetcode.com/problems/reverse-string/description/

"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # return s[::-1]
        return ''.join(reversed(list(s)))
