"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

给一个非空字符串和一个包含单词的非空字典。判断是否能用字典里的单词组合成给定的字符串。

思路：
Dp:
从0开始，若此分隔存在于给定字典中，则可以断开。

s = "leetcode", wordDict = ["leet", "code"]

leetcode
  l e e t c o d e 
T F F F F F F F F 

leet
s[0:0+4] in wordDict

s[0+4] = True

  l e e t c o d e 
T F F F T F F F F 
        当搜索到这里时会再次进行重复的搜索。


---
emmm, 写法待改进。
这个写法思路一样，不过效率会低。

beat 3%.

测试地址：
https://leetcode.com/problems/word-break/description/

"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
            
        dp = [True] + [False] * len(s)

        for i in range(len(s)):
            for j in range(i+1):
                if dp[j] == True:
                    for x in wordDict:
                        if x == s[j:j+len(x)]:
                            dp[j+len(x)] = True 

        return dp[-1]
