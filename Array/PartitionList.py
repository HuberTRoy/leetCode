"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

无脑怼。

beat:
99%.

测试地址：
https://leetcode.com/problems/partition-list/description/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        all_nodes = []
        
        while head:
            all_nodes.append(head.val)
            head = head.next
        
        less_nodes = []
        greater_nodes = []
        
        for i in all_nodes:
            if i < x:
                less_nodes.append(i)
            else:
                greater_nodes.append(i)
        
        if less_nodes:
            less_head = ListNode(less_nodes[0])
        
        head = less_head if less_nodes else None
        
        for i in less_nodes[1:]:
            less_head.next = ListNode(i)
            less_head = less_head.next
        
        if greater_nodes:
            greater_head = ListNode(greater_nodes[0])
        
        _head = greater_head if greater_nodes else None
        
        for i in greater_nodes[1:]:
            greater_head.next = ListNode(i)
            greater_head = greater_head.next
        
        if head:
            less_head.next = _head
        
            return head
        return _head
        