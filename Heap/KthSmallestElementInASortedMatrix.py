"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.


找到第k小个数。

测试用例：
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/


思路是用了堆：
Python 有内置的堆模块，需要进行研究自写。 2018/08/02待跟进。

堆：
堆是一个完全二叉树，完全二叉树是除了最底层，其他层都是铺满的。
                                   0

                  1                                 2

          3               4                5               6

      7       8       9       10      11      12      13      14

    15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30

堆又分为最大堆与最小堆，最小堆是根节点是整个堆中最小的，最大堆则是最大的。

堆的操作分为：插入，取顶。
大部分情况下插入时的数据都是无序的，所以要保证最大堆与最小堆需要的操作肯定要有上浮与下沉。
上浮：
最小堆中:
如果父节点比自己大则自己上浮。
如果子节点比自己小则自己下沉。
也就是做数据交换，一直上浮或下沉到符合条件为止。

代码待添加...


"""
'''
内置heapq的第一个版本：
运行时间长，但并未TLE.passed...

import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for i in matrix:
            for j in i:
                heapq.heappush(heap, j)
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        return heap[0]
'''

'''
第二个版本：
使用sorted. 每次都根据每个列表的0进行排序，然后取出。直到k=0.
排序时间复杂度为平均为 O(log len(n))。需要进行k次，所以是 O(klog len(n))。
理想情况下应该是最快的，但在书写时sorted在数据量过大时都会重新生成数组，所以导致很慢。
改进版本是直接打散列表，然后一次性sorted,这样的时间复杂度为 O(nlogn),也很容易写，但不想这样。

# 1
原以为会TTL，居然没有，跑了1778ms，也是最慢的。

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        while k:
            # matrix = sorted(matrix, key=lambda x: x[0])
            matrix.sort(key=lambda x: x[0])
            pop = matrix[0][0]
            matrix[0] = matrix[0][1:]
            if not matrix[0]:
                matrix = matrix[1:]
            k -= 1
            
        return pop
'''
'''
基于第二版的改进：
第二版的性能瓶颈应该是在排序时会重新移动大量的元素，如果每次仅对len(n)个元素排序呢？
每次都会for 一遍 len(n)，生成一个新的 列表，列表中的元素是 ([0], index)，然后排序这个列表。
也就是说不在排序原列表，而是排序一个新的列表。
根据index去修正原列表。

这版本TTl.这样排序会导致时间复杂度为(k*len(n)*log len(n))
'''
'''
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        length = len(matrix)
        while k:
            # matrix = sorted(matrix, key=lambda x: x[0])
            # matrix.sort(key=lambda x: x[0])
            
            # 测试用例是Python 2.
            newMatrix = sorted([(matrix[i][0], i)for i in xrange(length)], key=lambda x: x[0])

            pop = matrix[newMatrix[0][1]][0]
            matrix[0] = matrix[newMatrix[0][1]][1:]
            if not matrix[0]:
                matrix = matrix[1:]
            k -= 1
            
        return pop
'''

'''
第四版思路：
基于第二版改进：
第二版每次都只取一个，如果取多个呢？
比如第一次做归并排序时，
我是 [[1]+[2]]+[3]]+[4]]+[5]]+[6]]
而实际上应该是
[[1]+[2]] + [[3]+[4]] + [[5]+[6]]
[[1, 2, 3, 4]] + [[5, 6]]。

如果每次排序后去除t个，需要保证 n[0][-1] < n[1][-1]。
比如
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8。
第二版中每次排序会去除一个最小的。

matrix = [
   [5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 7

matrix = [
   [9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 6

matrix = [
   [10, 11, 13],
   [12, 13, 15]
],
k = 5
---
如果加入一条
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8

# 进入此条的条件是 k > len(matrix[0])

if matrix[0][-1] < matrix[1][0]:
    index1 = len(matrix[0])
    # index2 = 0
    # for t in xrange(matrix[1]):
        # if matrix[1][t] > matrix[0][-1]:
            # index2 = t
            # break

那么此时matrix[0] 将全部去除。k也相应的减去。

还有一种情况是 0[-1] 并不小于 1[0] 
此时需要寻找 0 中小于 1[0]的数。

    for t in xrange(len(matrix[0])-1, -1, -1):
        if matrix[0][t] < matrix[1][0]:
            index1 = t
那么此时将去除maxtrix[0][:t+1], k也减去相应的len.

< len 则退化为第二版。

仍然TLE....
'''
'''
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        while k:
            matrix.sort(key=lambda x: x[0])
            
            if k >= len(matrix[0]):
                if len(matrix) >= 2:
                    if matrix[0][-1] <= matrix[1][0]:
                        index1 = len(matrix[0])
                    else:
                        for t in range(len(matrix[0])-1, -1, -1):
                            if matrix[0][t] <= matrix[1][0]:
                                index1 = t+1
                                break
                                
                    popedMatrix = matrix[0][:index1]
                    matrix[0] = matrix[0][index1:]
                    if not matrix[0]:
                        matrix = matrix[1:]
                    pop = popedMatrix[-1]
                    k -= len(popedMatrix)
                    # print(matrix, index1)
                else:
                    return matrix[0][-1]
            else:
                pop = matrix[0][0]
                matrix[0] = matrix[0][1:]
                if not matrix[0]:
                    matrix = matrix[1:]
                k -= 1
            
        return pop
'''

'''
目前为止，通过的是第一版和第二版，第三和第四基于2的改进都以失败告终。
第四版的性能瓶颈在于，如果1[0]一直小于0[-1] 那么就需要一直迭代，如果恰好每次0中只有[0]比1[0]小，那么就会迭代过多的次数。
从而导致 TLE.

'''
