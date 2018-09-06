"""
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].

给定一组有n个数对的数组。每个数对中的第一个数总小于第二个数。

若某数组(c, d) 中的 c > (a, b) 中的 b那么这就可以是一个数对链。现在求最长的数对链。

可以是任意顺序的链接。

第一版思路：
Dp：
由于是任意顺序，要先经过排序，知道哪一个是最小的。
首先按照每个数对的 [1] 进行排序，因为 0总是比1要小的。

dp的子问题：
当前点可与前面的点组成的最大链。
最后输出最大的链。
效率是 O(n²)。

测试通过，beat 20% ~ TLE...

优化：
思考后，经过 [1] 的排序后，第一个肯定是最适合作为首节点，因为没有顺序问题，相当于建立堆一样。
那么剩下的就是在之后的里面挑一个[0]紧挨着第一个的，如此往复。

也就是说：

先进行[1]的排序，选出第一个。在进行[0]的排序，选出大于之前的那个的替换，然后截断再进行[1]的排序。

原始：
[[1,2], [2,3], [3,4]]
进行[1]排序：
[[1,2], [2,3], [3,4]]
选出[1,2]

进行[0]的排序：
[[2,3], [3,4]]
选出 [3, 4]。无剩余项，结束。

更进一步：
进行第一次[1]的排序并取出最适合作为第一个的之后，要做的是取出最适合做第二个的。
1. 最适合做第二个的有一个条件，就是它的[0]必须大于第一个的[1]。
2. 选出第二个后，第三个的对比条件仍是第三个的[0]与第二个的[1]做比较。
3. 第二个与第三个一定也在 [1] 的顺序链中：
第三个(用3表示)可以与第二个(用2表示)结合，也可以与第一个(用1表示)结合，第二个只可以与第一个结合。
1-2-3
2-3
1-3

1[0] < 1[1]
2[0] > 1[1]
2[1] > 2[0]
3[0] > 2[1]
所以
2[0] > 1[0]
3[0] > 2[0]

又因为 3[1]>2[1]>1[1]，所以2一定在1与3之间。

但1与3之间还有其他的数，这些数我们也用2表示，1与3中可能出现的另一种数是 2[0] < 1[1] 的，这种数可以直接抛弃，因为不符合要求。

ok.
基本算是beat 100%，发现前辈们也是用的这种方法。果然不是第一个想到的啊哈哈。

测试地址：
https://leetcode.com/problems/maximum-length-of-pair-chain/description/

"""

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
    # O (nlogn) + O(n)
#         x = sorted(pairs, key=lambda x: x[1])
        
#         mins = x[0]
        
#         maxes = 1
        
#         for i in x:
#             if i[0] > mins[1]:
#                 maxes += 1
#                 mins = i
#         return maxes

    # O(n²)
        pairs.sort(key=lambda x: x[1])
        dp = [1]
        
        currentMaxes = 0
        
        for i in range(1, len(pairs)):
            maxes = max([dp[j]+1 if pairs[i][0] > pairs[j][1] else 1 for j in range(i)])
            dp.append(maxes)
            currentMaxes = max(maxes, currentMaxes)

            
        return currentMaxes

