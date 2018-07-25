"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

经过s1和s2的不断削减组合，最终是否能形成s3.


在最初使用了搜索的递归方法后进行学习DP以及改良，最终beat 85%以上。

思路：
最开始的思路就是搜索，符合条件就开启一个递归，符合条件就开启一个递归，毫不意外的TTL。
当时以为自己用的DP，怎么还会超时了呢。后来学习一下之后，发现自己只是用了一个搜索，而不是DP。

DP的主要任务时找到子问题，通过解决子问题来解决上层问题。还有就是子问题可以有多种解时，保留下来的子问题是哪个。

知道了这个之后，此问题的子问题是 「是否可以组成当前的字符串」。

例：
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s3_0 = s1[0] or s2[0]
s3_1 = for i in s3_0 if s1[1] + i or if s2[0] + i
...

这样直至最后，看是否能够找到，如果其中的一环中出现了空，那么肯定是组不成了。


经过初版的测试后，发现比递归的搜索还要慢很多很多。甚至出现了MLE（内存占用太多）。
最终定位到原因是含有非常多同样的数据。
如这个测试用例：
s1 = aabc s2 = abad s3 = aab....
在判断s3_0时会加入两个可能的结果 
分别是s1 = abc s2 = abad 和 s1 = aabc s2 = bad
这样在s3_1时就会有多个同样的数据
s1 = abc s2 = bad 从s3_0[0][1] 也就是s2中取a.
s1 = abc s2 = bad 从s3_1[0][0] 也就是s1中取a.
这两个最终结果相同，对下一次结果没有影响，只取一个即可。

这仅仅是一个小例子，如果这样的数量过多，会形成非常大的冗余数据，只要出现20次这样的情况就会让最终的列表变成100多W个，而且一个很小的数据量即可达到20次。
但这100多W个所导致的下个结果是同一种，所以我们根本不需要这么多，只保留一个即可。

再思考一下，最初只定位了子问题，没有考虑保留哪些子问题的解，而是全部留下来。现在将缺少的「保留」条件加上。
所以在组成数据时判断是否已经重复即可解决此问题。
这样每次的迭代量变成1+个，基本不会超过4个。
但也有例外，如果 s1 == s2, s3 == s1+s2直接用不加判断的话会耗费大量时间，
如下：
print(Solution().isInterleave('c'*1000, 'c'*1000, 'c'*2000))
大概要半分钟。

因为此时我们制定的子问题规则毫无用处。每一个都可以避开。
或者
s1 == s2, s3 == s1与s2的前一部分相同的部分相加 + 后一部分相同的部分相加。
如 'ccb' 'ccb' 'ccccbb'

Leetcode 中的测试数据并不存在这样的情况。

如果遇到此种情况，可以用DFS来结合，确定一个子问题，一条路走到底，可以完美解决此问题。
不是这种情况下，也可以用DFS结合使用，不过效率差不多，没有此种情况也不需要再重写改写了。


测试用例：
https://leetcode.com/submissions/detail/165737688/

"""

'''
此版本 TTL MLE。
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        """
            recursive.
        """
        
        if len(s3) != len(s1) + len(s2):
            return False
        
        if not s3:
            return True
        
        dp = {}
        
        # s3 index, s1, s2
        for i, d in enumerate(s3):
            if i == 0:
                temp = []
                if s1 and s1[0] == d:
                    temp.append((s1[1:], s2))
                if s2 and s2[0] == d:
                    temp.append((s1, s2[1:]))
                dp[str(i)] = temp
                continue
                
            temp = []
            if dp[str(i-1)]:
                for j in dp[str(i-1)]:
                    s1, s2 = j[0], j[1]
                    if s1 and s1[0] == d:
                        temp.append((s1[1:], s2))
                    if s2 and s2[0] == d:
                        temp.append((s1, s2[1:]))
                    dp[str(i)] = temp
            else:
                return False

            # print(dp)
        try:
            for i in dp[str(len(s3)-1)]:
                if not any(i):
                    return True
            else:
                return False
        except KeyError:
            return False
'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        """
            recursive.
        """
        
        if len(s3) != len(s1) + len(s2):
            return False
        
        if not s3:
            return True
        
        dp = {}
        
        # s3 index, s1, s2
        for i, d in enumerate(s3):
            if i == 0:
                temp = []
                if s1 and s1[0] == d:
                    temp.append((s1[1:], s2))
                if s2 and s2[0] == d:
                    temp.append((s1, s2[1:]))
                dp[str(i)] = temp
                continue
                
            temp = []
            if dp[str(i-1)]:
                for j in dp[str(i-1)]:
                    s1, s2 = j[0], j[1]
                    if s1 and s1[0] == d:
                        if (s1[1:], s2) not in temp:
                            temp.append((s1[1:], s2))
                    if s2 and s2[0] == d:
                        if (s1, s2[1:]) not in temp:
                            temp.append((s1, s2[1:]))
                    dp[str(i)] = temp
            else:
                return False
            # print(len(dp[str(i-1)]))
            del dp[str(i-1)]

            # print(dp)
        try:
            for i in dp[str(len(s3)-1)]:
                if not any(i):
                    return True
            else:
                return False
        except KeyError:
            return False

print(Solution().isInterleave('c'*500+'d', 'c'*500+'d', 'c'*1000+'dd'))