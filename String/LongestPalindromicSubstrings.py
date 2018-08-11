"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

最长的回文子串。
1. 本来想用正则的，发现正则不重复搜。

sorted(re.findall(r'((?P<letter>.{1}).*(?P=letter))', "abacab"), key=lambda x: len(x[0]))

unpassed, wrong answer.

2. 回文串的定义是，翻转过来也相同，也就是从中间分开，从各自的中间开始走，到各自的头相同就对了。

思路：
 "cbbd"
 遍历一遍，找到所有字符的位置，放到hash中。

 {"c": [0], "b": [1, 2], "d": [3]}

 若有一个大于len() 1的，就开始判断:
   1. 判断从大到小。
   1.1 制造从大到小的字典{2: [(1, 3), (2, 4)]} 可以用itertools.combinations()
 。

 若全不大于，返回s[0].

效率有点低...大概率 TLE.

WTF, passed，而且还 beat 33%!

"""
import itertools

class Solution(object):

    # beat 33%
    def longestPalindrome(self, s):

        if len(s) <= 1:
            return s
        
        # {"c": [0], "b": [1, 2], "d": [3]}
        s_dict = {}
        for i, d in enumerate(s):
            try:
                s_dict[d].append(i)
            except KeyError:
                s_dict[d] = [i]
        # print(s_dict)
        
        # {2: [(1, 3), (2, 4)]}
        value_dict = {}

        for i in s_dict:
            if len(s_dict[i]) >= 2:
                for j in self.makeCombinations(s_dict[i]):
                    try:
                        value_dict[j[1]-j[0]].append(j)
                    except KeyError:
                        value_dict[j[1]-j[0]] = [j]
        # print(value_dict)
        for i in sorted(value_dict, reverse=True):
            for j in value_dict[i]:
                x = s[j[0]:j[1]+1] 
                if x == x[::-1]:
                    return x

        return s[0]



    def makeCombinations(self, split_list):

        return itertools.combinations(split_list, 2)

    # wrong
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     # if len(s) == 1:
    #     #     return s
        
    #     findall = re.findall(r'((?P<letter>.{1}).*(?P=letter))', s)
    #     print(findall)
    #     for i in sorted(findall, reverse=True, key=lambda x: len(x[0])):
    #         if i[0] == i[0][::-1]:
    #             return i[0]
        
    #     if not s:
    #         return ""
    #     return s[0]

s = Solution()

print(s.longestPalindrome("babad"*200))
