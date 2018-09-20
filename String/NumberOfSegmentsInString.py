"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

深刻的体会到了什么是，当我要用正则解决一个问题时，那么就有了两个问题。
cry= =.

其实本来用不着正则的。

就是根据空白分割，然后统计数量，没什么难度。O(n).

Python中可以直接 len(s.split()).

测试用例：
https://leetcode.com/problems/number-of-segments-in-a-string/description/

"""
import re

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s.strip():
            return 0
        
        result = re.split(r'\s+', s)
        
        return len(result)
