"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

strStr() 等同于 Python 中的 find()

想要通过直接：
```
str.find()
```
直接 beat 100%...

测试用例：
https://leetcode.com/problems/implement-strstr/description/

自己的实现思路：

记录两者len，needle的长度大于haystack，则一定不存在 -1.
接下来遍历 haystack 若此时剩余长度小于 needle 则一定不存在 -1.
若[0]与[0]相同，则进一步进行对比，一样则返回下标，不一样则继续。

built-in 20ms
myself 24ms
考虑到built-in 是 c++，这样效率也基本一致了。

"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # bulit-in 20ms
        # return haystack.find(needle)
        
        # myself
        if not needle:
            return 0
        
        # 24ms.
        lengthHaystack = len(haystack)
        lengthNeedle = len(needle)
        
        if lengthNeedle > lengthHaystack:
            return -1
        
        if lengthNeedle == lengthHaystack:
            return 0 if haystack == needle else -1
        
        for i, d in enumerate(haystack):
            if lengthHaystack - i < lengthNeedle:
                return -1
            
            if d == needle[0]:
                if haystack[i:i+lengthNeedle] == needle:
                    return i
        
