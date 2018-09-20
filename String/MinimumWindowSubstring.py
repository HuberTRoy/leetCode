"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


在S中找到包含T所有字符的长度最小的子字符串。
要求在 O(n) 时间复杂度内完成。


思路：
1. emmm.本来是一个 O（n）的但是最后出了点问题...总体思路没错，待改进。passed的了，但效率很低。

首先是 哈希 T .

哈希后的结果放到两个变量里。一个用于对比一个用于删除判断。

返回迭代S：
   如果这个元素存在于 T 中，记录，并在T中删除对应的字符。
      如果此时用于删除的 T 没有了。ok，找出记录的下标的最大与最小。记录为结果。
      用于删除的T没有了也不要停止，继续迭代，此后不断更新重复出现的字符的下标，重复对比此时记录的长度。

为什么可行呢？
S = ADOBE A CODEBANC T = ABC
在这里加一个A进去。

当迭代到ADOBE 时，记录的A = 0 B = 3。此时如果记录的话为 0:3 包含了 A与B.
不管此后与谁重复，只要找里面的最小与最大的下标，即可找到所有想要的值。

这个思路看起来是 O(n) 的。只需迭代一遍，中途就记录几个min，max就可以。

可实际实施起来...
发现这个min与max还不是很好记录...
用堆吧只能很快速的获取一个。
用二叉搜索树吧删除还有点麻烦。
想用红黑吧...还不会写。

到是可以用set暂时代替红黑，喔对，可以用set试试。

啊哈，现在什么都没用，直接用了生成器生成。
以后再试试，先记下来。

下面这个pass了喔。

600+ms beat 7% = =.

测试地址：
https://leetcode.com/problems/minimum-window-substring/description/


"""
from collections import deque
       
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # b = set(t)
        b = {}
        for i in t:
            try:
                b[i] += 1
            except:
                b[i] = 1
        
        a = b.copy()
        
        # [(mins_index, maxs_index), (mins_index, maxs_index), (mins_index, maxs_index)]
        
        x = {}
        mins = ""
        # t_min = 0
        # t_max = 0
        
        for i, d in enumerate(s):
            if d in b:
                try:
                    x[d].append(i)
                except:
                    x[d] = deque([i], maxlen=b[d])
                
                if a.get(d):
                    a[d] -= 1
                    if not a[d]:
                        a.pop(d)

                if not a:
                    values = x.values()
                    if not mins:
            
                        mins = s[min((q[0] for q in values)):max((q[-1] for q in values))+1]
                    else:
                        mins = min(mins, s[min((q[0] for q in values)):max((q[-1] for q in values))+1], key=len)

        if a:
            return ""
        return mins
