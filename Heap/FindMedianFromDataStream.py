"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


找出数据流中的中位数。

这个中位数要求的是排序后的中位数。
1.
    所以最暴力的方法即是：
    1. 每新加一个数据就放到列表尾，然后进行一次排序。
     1.1 当然如果用这个思路到是可以优化，用 O(n) 的搜索确定插入到哪里，插入到列表也是O(n)的操作。
    2. 随后输出 这一步到是 O(1)。
    没写这个的代码，太暴力...
2. 
    基于 1. 的改进，查找我们用二分来代替，这样查找可以降低到 O(log n)，但插入仍然是 O(n)。
    
    输出索引的话就是 O(1) 没什么好说的。

    写了这个的思路，出乎意料的是直接跑赢了 97% 的代码，不过随后几次平均变得低了。
    能跑赢这么多的原因也无非是测试数据过小，小到几乎可以忽略 O(n) 的插入耗时。
    
    这个代码的话很好写：
    一个用于放元素的列表：
    self.stream_data = []

    def addNum(self, num):
        bisect.insort_right(self.stream_data, num)

    def findMdian(self):
        '''
            判断奇偶。
        '''
        pass
3. 
    Discuss 里的思路基本是用到了堆。这个技巧感觉很棒：
    堆的插入和查询都是 O(log n) 级别的，用堆即可克服列表插入的 O(n) 的耗时情况：
    基本骨架是：
        如果我们将一个数据分成左右两部分，那么左边最大和右边最小即为我们找中位的基础元素。
    left         right
    [1,2,3,      4,5,6]

    左边这个符合大顶堆，右边这个则是小顶堆。

    1. 建立一大一小两个堆：
        大顶堆用于存放左边的元素。
        小顶堆用于存放右边的元素。
    2. 要面对的问题是如何在新数据来临时插入：
       1. 若两个堆都为空，那么插入 left 即可。
       2. 若right为空，left不为空：
          >= left[0] 若新数据大于 left[0] 表明应该插入到right里。
          < left[0] 新数据小于 left[0] 应该插入到left，这时要先将left的0弹出放到right里，在插入left。
       3. 都不为空时判断：
          长度相等时：
             > right[0] 表明不需要插入到 left 中，将 right[0] 弹出并插入left，然后插到 right 中即可。
             < right[0] 表明直接插入到 left 中即可。
          不等时：
             left多：
                不大于right[0]
                   left 弹出，加入到 right。
                   新加入的压入 left。
                大于：
                   直接加入 right
             right多：
                 不大于right[0]:
                    直接加入 left.
                 大于:
                    right 弹出，加入到 left。
                    新加入的加入到 right。


测试数据的效率不等：
100ms~500ms 都有跑过...

就巨大量的数据来说：
使用堆应该是最好的选择，每一个操作都是 O(log n) 与 O(1) 级别的。

进阶条件的思考：
1. 如果全部都是 0~100 之间的数据，完全可以建立一个哈希表，以数字为键，新加入的在它的数量上累积，寻找中位也简单。

测试地址：
https://leetcode.com/problems/find-median-from-data-stream/description/


"""
# import bisect
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stream_data_left = []
        heapq.heapify(self.stream_data_left)
        self.stream_data_right = []
        heapq.heapify(self.stream_data_right)


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
#         heapq.heappush(self.stream_data_right, num)
        
#         if len(self.stream_data_right) > len(self.stream_data_left):
#             pop = heapq.heappop(self.stream_data_right)
#             heapq.heappush(self.stream_data_left, -pop)
        if not self.stream_data_left:
            heapq.heappush(self.stream_data_left, -num)
            return
        
        if not self.stream_data_right:
            if num > -self.stream_data_left[0]:
                heapq.heappush(self.stream_data_right, num)
            else:
                pop = heapq.heappop(self.stream_data_left)
                
                heapq.heappush(self.stream_data_right, -pop)
                heapq.heappush(self.stream_data_left, -num)                
            return
        
        if len(self.stream_data_right) == len(self.stream_data_left):
            if num > self.stream_data_right[0]:
                heapq.heappush(self.stream_data_right, num)
                pop = heapq.heappop(self.stream_data_right)
                heapq.heappush(self.stream_data_left, -pop)

            else:
                heapq.heappush(self.stream_data_left, -num)
        elif len(self.stream_data_left) > len(self.stream_data_right):
            if num > self.stream_data_right[0]:
                heapq.heappush(self.stream_data_right, num)
            else:
                heapq.heappush(self.stream_data_left, -num)
                pop = heapq.heappop(self.stream_data_left)
                
                heapq.heappush(self.stream_data_right, -pop)
        else:
            if num < self.stream_data_right[0]:
                heapq.heappush(self.stream_data_left, -num)
            else:
                heapq.heappush(self.stream_data_right, num)
                pop = heap.heappop(self.stream_data_right)
                heapq.heappush(self.stream_data_left, -pop)

        # bisect.insort_right(self.stream_data, num)

    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.stream_data_left) + len(self.stream_data_right)
        if length % 2 == 0:
            return float((-self.stream_data_left[0] + self.stream_data_right[0])) / 2.0
        else:
            return -self.stream_data_left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
