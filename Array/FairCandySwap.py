"""
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

 

Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]
Example 2:

Input: A = [1,2], B = [2,3]
Output: [1,2]
Example 3:

Input: A = [2], B = [1,3]
Output: [2,3]
Example 4:

Input: A = [1,2,5], B = [2,4]
Output: [5,4]
 

Note:

1 <= A.length <= 10000
1 <= B.length <= 10000
1 <= A[i] <= 100000
1 <= B[i] <= 100000
It is guaranteed that Alice and Bob have different total amounts of candy.
It is guaranteed there exists an answer.


开胃菜。

有两个好盆友，要交换糖果使得他们两个的糖果一样。

输出的结果也是交换的糖果数量而不是下标，所以非常容易写。

设爱丽丝给 x 颗糖，得到 y颗。那鲍勃就给 y 得到 x。

最终是 
1? - x + y = 2? - y + x
2x - 2y = 1? - 2?

x - y = (1? - 2?) / 2


1?即 爱丽丝的初始糖，
2?即 鲍勃的初始糖。

那么首先把 爱丽丝和鲍勃的糖加起来 / 2，然后迭代 爱丽丝的糖，若迭代的这个糖 - 前面计算出来的糖鲍勃有的话返回即可。

要写的话首先把鲍勃的糖哈希一下，这样查找的时间复杂度为 O(1)。

测试地址：
https://leetcode.com/contest/weekly-contest-98/problems/fair-candy-swap/

beat:
100% 44 ms


"""

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        x = (sum(A) - sum(B)) // 2
        b = set(B)        
        for i in A:
            if i - x in b:
                return (i, i-x)
