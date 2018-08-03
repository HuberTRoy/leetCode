"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

给定两个字符串，判断是否属于相同的模式。

这个没想到什么好办法，就是根据字典进行替换然后对比是否一致。

在Discuss里看到一个 one line 版。

先上自己的思路：

迭代字符串a，如果遇到的是a_d中的字符串，则根据a_d替换，否则将其根据出现的顺序添加到a_d中，
这样做让每个单词根据字符所出现的顺序进行字典替换。

测试用例：

https://leetcode.com/problems/isomorphic-strings/description/
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        """
        这里可以缩写为一个函数，但不需要复用，直接复制粘贴了。
        """
        s_k = 0
        t_k = 0
        s_d = {}
        t_d = {}
        new_s = ''
        new_t = ''
        for i in s:
            if s_d.get(i):
                new_s += s_d.get(i)
            else:
                s_d[i] = str(s_k)
                s_k += 1
        for i in t:
            if t_d.get(i):
                new_t += t_d.get(i)
            else:
                t_d[i] = str(t_k)
                t_k += 1
        
        return new_s == new_t

"""
接下来是one line 版，虽然并不是很高效，但思路不错。
这个问题的核心问题是 重复的数据，如果每个单词都不想同那么也是同一种模式，关键就是找出相同的单词。
zip会将每个部位的单词两两对应。
`zip` `rar`
('z', 'r'), ('i', 'a'), ('p', 'r')
如果两个单词的模式相同，那么一定会出现多组同样的数据，且数量与原单词去重后一致。
t,s与s,t的效果应该是一致的，都不会影响判断。

return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))
"""

"""
第三版：
根据 one line 的思路：
zip可以有效检测分组：
one line 虽然简单易写，不过有3次set，时间复杂度为 O(3n)，set是c++写的所以很快，感觉不出来。

就是把第一版变成了zip的的形式，理论上应该会快的，但实际运行时间与第一版一致。

"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_k = 0
        t_k = 0
        s_d = {}
        t_d = {}
        for i in zip(s, t):
            if s_d.get(i[0]):
                s_k2 = s_d.get(i[0])
            else:
                s_k2 = s_d[i[0]] = str(s_k)
                s_k += 1

            if t_d.get(i[1]):
                t_k2 = t_d.get(i[1])
            else:
                t_k2 = t_d[i[1]] = str(t_k)
                # t_k2 = t_d.get(i[1])
                t_k += 1
                
            if s_k2 != t_k2:
                return False
        return True
