"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


给定一个字符串 s 和 非空字符串 p。 找到所有 p 在 s 中的变位词，将变位词开始部分的索引添加到结果中。

字符串包含的字符均为小写英文字母。

结果的顺序无关紧要。


思路：
看到标的是个 easy .. 估计数据不会很大，直接 sorted(s[i:i+len(p)]) == sorted(p) 判断了..
结果是 TLE。

好吧，只能认真思考下了。

想到的是利用动态规划，还有点回溯的味道。

子问题为：
当前点加上之前的点是否覆盖了全部的p。

若全部覆盖了，则返回 i - len(p) + 1 的开始索引，同时，将 s[i - len(p) + 1] 处的字符添加到 dp 的判断点中。
这样做可以扫描到这种情况：
s = ababab
p = ab
循环这种。

若没有存在于最后一个dp中，那么先判断是否有重复：
1. 如果在 p 中，但不在上一个子问题的需求解里。
 2. 如果与最前面的一个字符发生了重复。
   3. 如果与之前的一个字符不同。
满足这三个条件那么可以无视这个重复的字符。
比如这样：
s = abac
p = abc

这样相当于把重复的一个 a 忽略掉了。
同时还要判断是否它的前一个是否一致，一致的话就不能单纯的忽略了。

s = abaac / aabc
p = abc

没有满足的上述三个条件，那么重新复制一份原始子问题，然后将当前字符判断一下，继续下一个循环即可。

beat 99% 84ms
测试地址：
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

2018/10/27 修正：

上次分析后是有不足的，可以AC只是因为这个题的测试用例很少。

问题出在上面分析的 2. 和 3. 中，
重新梳理下：
若没有存在于最后一个dp中，那么先判断是否有重复：
1. 如果在 p 中，但不在上一个子问题的需求解里。
  2. 此时要找一个合适的 ·复活点·，直接上例子吧

s "cbdbcae"
   cbd    b 当出现第二个 b 时，b不与之前分析后所找到的 c 相同，那么可以判定为要从 b 这个点开始复活了，但如果是的话那就找不到了。
   要复活的点是 从 b 之前的一个 d。 也就是复活点要在重复的那个字符后面开始，那么我们要做的就是把在它之前的字符给加回来。
p "abcde"

待学习 Discuss 滑动窗口。

"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        # p = sorted(p)
        if not s:
            return []
        _p = {}
        
        for i in p:
            try:
                _p[i] += 1
            except:
                _p[i] = 1
        
        result = []
        
        x = _p.copy()
        if s[0] in _p:
            x[s[0]] -= 1
            if not x[s[0]]:
                x.pop(s[0])
                
        dp = x
        if not dp:
            return [i for i in range(len(s)) if s[i] == p]
        
        for i in range(1, len(s)):
            if s[i] in dp:
                t = dp
                t[s[i]] -= 1
                if not t[s[i]]:
                    t.pop(s[i])
                
                if not t:
                    result.append(i-len(p)+1)
                    x = {}
                    _t = s[i-len(p)+1]
                    x[_t] = 1

                    dp = x
            else:
                if s[i] in _p:
                    if s[i] != s[i-len(p)+sum(dp.values())]:
                        for t in s[i-len(p)+sum(dp.values()):i]:
                            if t == s[i]:
                                break
                            try:
                                dp[t] += 1
                            except:
                                dp[t] = 1
                    continue

                x = _p.copy()
                if s[i] in x:
                    x[s[i]] -= 1
                    if not x[s[i]]:
                        x.pop(s[i])
                dp = x

        return result


# 下面这个代码有瑕疵。
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        # p = sorted(p)
        if not s:
            return []
        _p = {}
        
        for i in p:
            try:
                _p[i] += 1
            except:
                _p[i] = 1
        
        result = []
        
        x = _p.copy()
        if s[0] in _p:
            x[s[0]] -= 1
            if not x[s[0]]:
                x.pop(s[0])
                
        dp = x
        if not dp:
            return [i for i in range(len(s)) if s[i] == p]
        
        for i in range(1, len(s)):
            if s[i] in dp:
                t = dp
                t[s[i]] -= 1
                if not t[s[i]]:
                    t.pop(s[i])
                
                if not t:
                    result.append(i-len(p)+1)
                    x = {}
                    _t = s[i-len(p)+1]
                    x[_t] = 1

                    dp = x
            else:
                if s[i] in _p and s[i] != s[i-1] and s[i] == s[i-len(p)+sum(dp.values())]:
                    continue
                x = _p.copy()
                if s[i] in x:
                    x[s[i]] -= 1
                    if not x[s[i]]:
                        x.pop(s[i])
                dp = x

        return result
