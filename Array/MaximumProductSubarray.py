"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

给一个数组，找出其中连续的子数组中，相乘最大的一组。

这个算法和 maximum subarray 很相似，那个每个点的状态是 负数的话就可以断开，这个的话不行。

但也是一样的，一开始的思路是遇到负数不断开，遇到负数会乘原来的数，然后把自己加进去也作为因子。

1.
看下面注释掉的写法。这种写法对于负数并不多的可以很有效。但对付负数较多的则力不从心。

184个测试跑到183个就TLE了。

2. 
基于 1. 的改进，1. 中主要是会一直加一直加，导致最差将时间复杂度升高到 O(n²)。
但对于每个点来说其实只需要保留两种状态：
第一种个状态是其中的最大值，还有一个是最小值。
[2, -5, -2, -4, 3]
这个例子中，-2 这个点若按 1. 中的写法积累下来应为 [20, 10, -2]。但10是没有必要的，-5*-2显然是没有 2*-5*-2大，而且即使后面无论是什么数都不可能出现正数 
-5*-2 * x > 2*-5*-2*x的情况。
x在正数的情况下不可能大于 2x。
当x是负数时也基本不会用到它，因为求的是最大值，后面只有出现另一个负数才会相乘得正，x*-y 也不可能大于 2x*-y 的。

所以2算是给1做了剪枝。

这个算法还不错，40ms，前面的也都是基于同样的思路，只保存最大最小。
效率 O（n）。
看了 Discuss 好像也都是这个写法。

测试地址：
https://leetcode.com/problems/maximum-product-subarray/discuss/


"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxes = nums[0]
        currentNums = [[nums[0]]]
        
        for i in range(1, len(nums)):
            x = nums[i]
            temp = [x*j for j in currentNums[i-1]]
            
            minx = min(x, min(temp))
            maxx = max(x, max(temp))
            
            currentNums.append([minx, maxx])
            maxes = max(maxes, maxx)           
        
        return maxes

        # maxes = nums[0]
        # currentNums = [[nums[0]]]

#         for i in nums[1:]:
#             if not currentNums:
#                 currentNums.append(i)
#                 maxes = max(maxes, i)
#                 continue
                
#             if i == 0:
#                 currentNums = []
#                 maxes = max(maxes, i)

#                 continue
            
#             for j in range(len(currentNums[:])):
#                 t = currentNums[j]
#                 if t != 0:        
#                     currentNums[j] = t*i
#                     if i < 0 or t*i < 0:
#                         currentNums.append(i)
#                 else:
#                     currentNums.append(i)
                    
#             maxes = max(maxes, max(currentNums))
        
#         return maxes
