"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

这个我的思路是：

1. 先把前 k 个数取出来，然后排序一组，不排序一组。
2. 排序的一组作为查找使用。 不排序的一组作为删除增加会用。
3. 这里也可以使用堆代替排序，红黑树应该最好不过了。
4. 这里使用排序过的列表是为了能够使用二分法，从而达到 log n 级别的查找和后续添加。
   但同时因为即使在 log n级别查找到要添加删除的位置，进行列表的添加和删除仍然是一个 O(n) 级别的事情...
   所以使用堆或者红黑树是最好的，添加和删除都是 log n 级别的。

5. sorted list 主要是进行获取最大与删除冗余，这里使用二分法来删除冗余。
6. unsorted list 用于知道要删除和添加的都是哪一个。

beat 31% 176ms.

测试地址：
https://leetcode.com/problems/sliding-window-maximum/description/


"""
from collections import deque
import bisect

class Solution(object):
    def find_bi(self, nums, target):
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid            
        
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        x = nums[:k]
        y = sorted(x)
        x = deque(x)
        
        maxes = max(x)
        result = [maxes]
        
        for i in nums[k:]:
            pop = x.popleft()
            x.append(i)
            
            index = self.find_bi(y, pop)
            y.pop(index)
            
            bisect.insort_left(y, i)
            
            result.append(y[-1])
        return result
        