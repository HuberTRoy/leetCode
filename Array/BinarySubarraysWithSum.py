"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

 

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.

pre result + hash 有一个思路一模一样，代码也一模一样的。

测试地址：
https://leetcode.com/contest/weekly-contest-108/problems/binary-subarrays-with-sum/

"""
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        
        dicts = {0:1}
        
        pre = 0
        result = 0
        
        for i in A:
            pre += i
            
            result += dicts.get(pre-S, 0)
            dicts[pre] = dicts.get(pre, 0) + 1
        
        return result
