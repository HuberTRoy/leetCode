"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3


删除链表中重复的节点。

一直迭代，若当前 val == next.val，则把 next 与 next.next 相连。

beat 
100%


测试地址：
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/


"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        x = head
        
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return x
