"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

 

Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.


给定一个由 '0' 和 '1' 组成的字符串，把它变成单调递增的字符串。返回最少的改变次数。

思路：
从左向右走过一遍，把找到的 1 变成 0。
从右向左过一遍，把找到的 0 变成 1。

最后过一遍，找到相加最少的一个点即可（可能不止一个）。

测试地址：
https://leetcode.com/contest/weekly-contest-107/problems/flip-string-to-monotone-increasing/

"""

class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        x = [0] if S[0] == '0' else [1]
        
        # left to right
        # 1 -> 0
        for i in range(1, len(S)):
            if S[i] == '1':
                x.append(x[-1]+1)
            else:
                x.append(x[-1])
        
        # right to left
        # 0 -> 1
        S = S[::-1]
        y = [0] if S[0] == '1' else [1]
        for i in range(1, len(S)):
            if S[i] == '0':
                y.append(y[-1]+1)
            else:
                y.append(y[-1])
        
        y.reverse()
        
        return min([i+j for i,j in zip(x,y)]) - 1

