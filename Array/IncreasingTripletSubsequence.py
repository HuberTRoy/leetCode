"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false

给一个数组，若里面存在 arr[i] < arr[j] < arr[k] 且 0 <= i < j < k <= n-1，则返回True。
否则False.

要求 O(n)时间以及O(1) 空间。 


对于 i 的规则是尽量小。首先确定为第一个，之后若出现比它小的，则确定为这个否则确定为 j。
对于 j 的规则依然是尽量小，但要大于i。

思考时有可能出现的陷阱：

1. 有比 i 小的就替换，那要是 arr[100] < i，那前面的99个确定没有符合条件的吗？
   还要基于 j，i的判断条件是，若比 i 小则替换为 i，若比 i 大则与 j 比较，与 j 比较遵循同样的规则。

2. 有无可能出现在 j 之前有 3 个小于 j 的递增序列呢？
   不可能：
      一个数在 j 之前有两种状态：
         比 j 大或与 j 相等。
         若比 j 小则替换为 j 了。
    在 j 之后也不可能，若这个数比 j 小则会替换为 j。

3. 那么有没有可能出现第一个 j 与第二个 j 之间存在 3 个这样的递增序列呢？
   也是不可能的：
       若比 j 大则直接返回了。
       若比 j 小或等则替换。

所以按此规则：
1. i 之前不可能存在 3 个递增序列。
2. i - j 这段也不可能存在 3 个递增序列。
3. j - k 这段也不可能存在 3 个递增序列。

o(n) o(1)
     只有 4 个变量。

beat 100%

测试地址：
https://leetcode.com/problems/increasing-triplet-subsequence/description/

"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) < 3:
            return False
        
        one = None
        two = None
        for i, d in enumerate(nums):
            if one:
                if d <= one[1]:
                    one = (i, d)
                    continue
                    
                if two:
                    if d <= two[1]:
                        two = (i, d)
                    else:
                        return True
                else:
                    two = (i, d)
            else:
                one = (i, d)
        return False



