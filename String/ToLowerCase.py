"""
将所有字符转换成小写字符。
Python 自带此函数。

若要自己写的话，我想到的是一个是建立起哈希表。
{'A': 'a'....}
这样查表，时间复杂度是 O(n)。

还有可以利用ASCII。
ord('a')
97
chr('A')
65
中间差了32个。

"""

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()
