"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

与 1 差不多，不过这次有重复。
进阶条件里问：
1. 如果是已排序的可以怎么优化？
2. 如果 数组1 比 数组2 要小，哪个算法好些？
3. 如果 数组2 在硬盘里排过序，但内存不足以一次性全部读取该怎么做？

我的思路是：
1. 先排序。
2. 之后设置两个指针。

若 1与2相同，则将结果添加到最终结果的列表中，1和2各+1。
若 1比2要大，那么表示2向后走还有可能遇到和1相同的数字，所以2 +1。
否则 1 +1。直到有一个到了末尾。

这个思路的话，进阶的1和3直接可以包含进去。
2的话，Discuss 里的其他方法基本上是用 哈希表。 1和2哈希，然后取个数较小的交集，这种方法在数组较小的时候要比上面提到的思路快。

排序后的思路：

beat 100% 24ms.

测试地址：
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/


"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
    
    
        nums1.sort()
        nums2.sort()
        
        _n1 = 0
        _n2 = 0
        
        _n1_length = len(nums1)
        _n2_length = len(nums2)
        
        while _n1 < _n1_length and _n2 < _n2_length:
            if nums1[_n1] == nums2[_n2]:
                result.append(nums1[_n1])
                _n1 += 1
                _n2 += 1
            
            elif nums1[_n1] < nums2[_n2]:
                _n1 += 1
            else:
                _n2 += 1
        
        return result       