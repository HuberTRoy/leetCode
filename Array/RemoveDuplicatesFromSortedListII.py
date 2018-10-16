"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

这次要把全部的重复都删除。

我的思路是利用标记，过一遍，先把重复的删到剩一个，然后把剩下的一个标记为重复。

然后做一个新的链表。

beat 72%

测试地址：
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/


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
                head.duplicate = True
            else:
                head = head.next
        
        while x:
            if hasattr(x, 'duplicate'):
                x = x.next
            else:
                break      
        
        if not x:
            return None
        
        new = ListNode(x.val)
        x = x.next
        _new = new
        
        while x:
            if hasattr(x, 'duplicate'):
                x = x.next
            else:
                new.next = ListNode(x.val)
                new = new.next
                x = x.next
        return _new
