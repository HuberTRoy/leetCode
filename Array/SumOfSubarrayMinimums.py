"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
 
给一个数组，返回所有子数组中最小的数之和。

思路：

每个点都有左右两条路：

 3，1 ，2 ，4
 
 left 3 == 0，没有比它大的。
 right 3 == 0，到是有比它大的，但和它不挨着。
 _self = 1,
 left * right = 0,
 
 total = 0 + 0 + 1 + 0

 left 1 == 1，有一个3。
 right 1 == 2，有两个，2,4。
 _self = 1
 
 left * right = 1 * 2 = 2

 total = 1 + 2 + 1 + 2 = 6。 
 
 # 左边和右边最后进行的是相乘。

 对于每个数的左边来说，只要这个数是最小的就可以了。
 对于每个数的右边来说，它必须是唯一最小的才行。
 反过来也行，反正就是只能出现一个。

 3,1,2,1

 对于第一个 1，来说 向右走 1==1，出现了重复。
 这时不能判断为也是一组，因为如果与它组成 1,2,1 那当进行最后一个 1 左边的判断时，还会出现一个 1,2,1。这样就重复了。

---
第一版的代码只能跑通100中的95个例子..
遇到最大值，3W个，直接 TLE 了。

第一版中每个点都需要对所有的其他点重新计算，导致最差会在 O(n²) 。

优化点：
通过子问题来减少判断的次数。

因为要与之连，所以只要有一个不可以，它前面的就不需要在去管了，肯定是不可以的。

3，1 ，2 ，4
left(加上自身):
 [1, 2, 1, 1]
 
3 这个点的 1 由其左边比它大的而来，由于没有，所以只有自己 1.
1 这个点 由其左边比它大的而来，1 + 1 = 2
2 这个点 由其左边比它大的而来，1
4 同样。

right(加上自身) 可以倒过来进行判断:
倒过来之后判断的还是左边，这样比较好写。
4,2,1,3
 [1, 2, 3, 1] reverse [1,3,2,1]

因为加上了自身，所以 left * right 即可：
[1,2,1,1]
[1,3,2,1]
[1,6,2,1]
 3 1 2 4

 3 + 6 + 4 + 4 = 17.

写的时候还需要一个额外变量：

 [4, 2, 1, 3]
 
 这个变量存的是目前的总和：
   最小的数
 [(4,1)]
     个数
 [(2,2)]
 [(1,3)]
 [(1,3),(3,1)]

如果没有的话，又要与原来的一模一样了。


ok, 这次他通过了， 268ms。

测试地址：
https://leetcode.com/contest/weekly-contest-102/problems/sum-of-subarray-minimums/


"""

class Solution(object):

    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        
        # count
        left = []
        right = []

        # (num, count)
        _left = []
        _right = []
        for i in A:
            base = 1
            while _left:
                if i < _left[-1][0]:
                    base += _left[-1][1]
                    _left.pop()
                else:
                    break

            _left.append((i, base))
            left.append(base)

        for i in reversed(A):
            base = 1
            while _right:
                if i <= _right[-1][0]:
                    base += _right[-1][1]
                    _right.pop()
                else:
                    break

            _right.append((i, base))
            right.append(base)

        right.reverse()

        result = 0

        for i in range(len(A)):
            result += A[i] * left[i] * right[i] 

        return result % mod

        # result = 0
        # length = len(A)
        
        # for i in range(length):
        #     _self = 1
        #     left = 0
        #     right = 0
            
        #     for j in range(i-1, -1, -1):
        #         if A[i] < A[j]:
        #             left += 1
        #             continue               
        #         break
                    
        #     for j in range(i+1, length):
        #         if A[i] <= A[j]:
        #             right += 1
        #             continue

        #         break
            
        #     sums = left * right
        #     # print([sums, _self, left, right])
        #     result += (A[i] * sum([sums, _self, left, right]))
        # # print(result)
        # return result % mod
