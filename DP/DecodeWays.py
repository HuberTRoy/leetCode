"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

定义 'A-Z' 分别为 '1-26'。
给定一个包含数字的字符串，给出有几种可能的解码办法。

思路：

1. 首先是一个递归的搜索思路，用递归总是很容易想到...
   每次都判断前一个字符和前两个字符是否在 1-26 之中，在的话就分别再开启一次递归。
   到是不会出错，就是效率低，TLE 了。

2. 看了下 Discuss 里的提点：
   使用 Dp。
   Dp 的思考：
       Dp 的子问题是：
          当前这个点能与组成几个。
       那么如何解出该点的子问题呢？
          我一开始的思考是这样：
             "1221"
             dp[0] = 1  1
             dp[1] = 2  1,2  12
             dp[2] = 3  1,2,2 12,2               1,22
             dp[3] = 5  1,2,2,1 12,2,2 1,22,2    1,2,21 12, 21
             每一层的dp都包含一下上一次结果,后面是一位数的部分，若组合起来 < 27 即可组合成...
             不过这个不好弄，而且虽然效率会比递归高，但...也高不到哪里去，肯定不是 Discuss 中的解法。
             emmm，想了一会没想到好办法，去 Discuss 里看了下思路，一下就明白了...
             多的这个组合恰好和 i-2 的进行了组合，这个的子问题解法是基于前面两个子问题的。

       注意处理下 0。

beat 99%.
测试用例：
https://leetcode.com/problems/decode-ways/description/

"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            if 0 < int(s) < 10:

                return 1
            return 0
        
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letters_dict = {str(i):letters[i-1] for i in range(1, 27)}
        dp = []
        if 0 < int(s[0]) < 10:
            dp.append(1)
        else:
            dp.append(0)

        if 10 <= int(s[0]+s[1]) < 27:
            if 0 < int(s[1]) < 10:
                dp.append(2)
            else: 
                dp.append(1)
        else:
            if s[1] != '0':
                dp.append(dp[0])
            else:
                dp.append(0)
                
        for i in range(2, len(s)):
            x = 0
            if s[i] != '0':
                x += dp[i-1]
            
            if s[i-1] != '0':
                if '10' <= s[i-1] + s[i] < '27':

                    x += dp[i-2]
            dp.append(x)

        return dp[-1]
#         self.result = 0
        
#         def makeDecode(rest_str):
#             if not rest_str:
#                 self.result += 1
#                 # result.append(1)
#                 return
            
#             if len(rest_str)>=2:
#                 if rest_str[:2] in letters_dict:
#                     makeDecode(rest_str[2:])
#             if rest_str[:1] in letters_dict:    
#                 makeDecode(rest_str[1:])
        
#         if len(s)>=2:
#             if s[:2] in letters_dict:
#                 makeDecode(s[2:])

#         if s[:1] in letters_dict: 
#             makeDecode(s[1:])

#         return self.result
