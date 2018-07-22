"""
合并两个排序过的数组。

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
基本就是你走一步我走一步，一人一个指向。

O(n)
测试用例：
https://leetcode.com/problems/merge-two-sorted-lists/description/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = cur = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next
            
        cur.next = l1 or l2
        
        return head.next
