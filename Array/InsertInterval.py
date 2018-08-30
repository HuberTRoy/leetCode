"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


与 Merge Array 思路上是一样的，本以为用同样的代码会导致 TLE，不过也 Pass 了，beat 74%.

C扩展的排序就是快，不用排序的思路：
这个只会部分重叠，所以目标是找到head和end的点：
[[1,2],[3,5],[6,7],[8,10],[12,16]]  [4, 8]
head 找最后一个大于的。
end 则找第一个小于的。
比如 4 对比 1, 3，6后，那么确定 head 为 3. [3, 5]
    8  对比 2, 5, 7 后找到 10。  [8, 10]

测试地址：
https://leetcode.com/problems/insert-interval/description/

"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, _sentences, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        _sentences.append(newInterval)
        
        _sentences = sorted(_sentences, key=lambda x: x.start)

        if not _sentences:
            return []

        result = []

        head = _sentences[0].start
        tail = _sentences[0].end
        length = len(_sentences)
        for x in range(1, length):
            i = _sentences[x]
            if tail >= i.start:
                tail = max(tail, i.end)
            else:
                result.append([head, tail])
                head = i.start
                tail = i.end

        result.append([head, tail])
        return result

