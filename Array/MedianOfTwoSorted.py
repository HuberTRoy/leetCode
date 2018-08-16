"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

 

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

求两个列表合并后的中位数。

时间复杂度要求O(log (m+n))

1. 直接sorted后取中位，时间复杂度为O((m+n)log(m+n))。
2. 不用全部排序，本质上是一个求第k(s)小的数。 时间复杂度(O( (m+n)/2 ))还是没到要求的 O(log (m+n))，此版beat 43%~56%。 
# 打印真的是很慢，只打印一条很小的数据2.方法就会只能beat 7%..

3. 最后是 O(Log(m+n)) 的思路：
求第k小的数的时候，有一种方法是每次去除 k // 2 个数，剩余 < 1个时就找到了最终要找的数。
a = [1, 2, 4, 6]
b = [3, 5, 7, 9]

此时的 k 为 8 // 2 = 4.
k//2 = 2

则对比 a与b的第2个数也是下标为2-1哪个较小，较小的一组去除。然后循环即可。

因为是排过序的列表，不论哪一个列表中，去除 k//2 个数都不会去除目标。

因为只有k的一半，又是排过序的，假设a[k//2]<b[k//2]：
1. 去除的值只有k的一半，
2. 选择的是较小的那一组，那么组合起来：
b[:k//2-1] + a[:k//2] + b[k//2-1]
前两者无论如何都是比 b[k//2] 要小的，所以要么第k小的数是 b[k//2]，要么不是，去除a[:k//2]一点问题都没有。

需要注意的问题：
1. 若k//2大于某一个列表时，此时调整为所大于的列表的长度，不可能出现两个列表同时都小于的情况，
   除非写错了否则不可能 len(a)+len(b) // 4 > len(a)还 > len(b)
   a / 4 + b / 4 = a时 b / 4 = 3a / 4 -> b = 3a，3b/4 = 9a/4，所以 b/4 + a/4则不可能也大于b。
2. 奇数在取k时向上取整。
3. k//2向下取整。

这样每次去除的是k的一半，所以时间复杂度为O(log(k)) -> O(log((m+n)//2)) 符合要求。

beat 75%，前面的25%都是用的sorted，C扩展的sorted效率是最高的，也就是第一版，基本上是100%，但是这是作弊行为= =。

测试地址：
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

"""
class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        length = len(nums1) + len(nums2)
        if length <= 2:
            return sum(nums1+nums2) / length 
        raw_length = length
        
        length = length // 2

        if raw_length % 2 != 0:
            length += 1
            
        while length > 1:

            reduce_value = length // 2
            if nums1:
                if reduce_value > len(nums1):
                    reduce_value = len(nums1)
            if nums2:
                if reduce_value > len(nums2):
                    reduce_value = len(nums2)
                
            nums1_k_value = nums1[reduce_value-1] if nums1 else float('inf')
            nums2_k_value = nums2[reduce_value-1] if nums2 else float('inf')

            if nums1_k_value < nums2_k_value:
                nums1 = nums1[reduce_value:]
            else:
                nums2 = nums2[reduce_value:]

            length -= reduce_value


        result = sorted(nums1[:2] + nums2[:2])
        if raw_length % 2 != 0:
            return result[0]

        return sum(result[:2]) / 2 
                

    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
        
    #     length = len(nums1) + len(nums2)
    #     if length <= 2:
    #         return sum(nums1+nums2) / length 
    #     raw_length = length
    #     length = length // 2
    #     # Get kth minium number(s).
    #     if raw_length % 2 == 0:
    #         get = [length, length-1]
    #     else:
    #         get = [length]
        
    #     index_nums1 = 0
    #     index_nums2 = 0
    #     total_nums = 0
    #     result = []

    #     while get:
    #         if index_nums1 == len(nums1):
    #             x = nums2[index_nums2]
    #             index_nums2 += 1
    #         elif index_nums2 == len(nums2):
    #             x = nums1[index_nums1]
    #             index_nums1 += 1
    #         else:
    #             if nums1[index_nums1] < nums2[index_nums2]:
    #                 x = nums1[index_nums1]
    #                 index_nums1 += 1
    #             else:
    #                 x = nums2[index_nums2]
    #                 index_nums2 += 1
            
    #         if get[-1] == total_nums:
    #             result.append(x)
    #             get.pop()
        
    #         total_nums += 1
            
    #     return sum(result) / len(result) 

    # sorted.
    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
        
    #     list3 = nums1 + nums2
    #     list3.sort()
        
    #     return self.median(list3)
        
    # def median(self, nums):
        
    #     length = len(nums)
    #     if length % 2 == 0:
    #         return (nums[(length // 2)-1] + nums[length // 2]) / 2
        
    #     return nums[length // 2]