"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

合并 k 个有序链表。

用了最小堆：

把所有的链表节点入堆，然后出堆形成新的链表即可。

依然依靠了内置模块，待自己书写堆。

测试地址：
https://leetcode.com/problems/merge-k-sorted-lists/description/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        a = []
        
        heapq.heapify(a)
        
        for i in lists:
            while i:
                heapq.heappush(a, i.val)
                i = i.next
        if not a:
            return None
        
        root = ListNode(heapq.heappop(a))
        head = root
        
        while a:
            root.next = ListNode(heapq.heappop(a))
            root = root.next
        
        return head

