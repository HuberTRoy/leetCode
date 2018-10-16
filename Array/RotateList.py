"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


旋转链表。 k 非负。

k 超过链表的最大长度也可。

思路：

过一遍链表长度，k % length 取个模，防止 k 超级大。

之后 slow fast 两个，fast 先走 k 个，然后 slow 与 fast 同时走，走到最后 slow.next 即为从后到前 k 个的起点。

剩下的就是把原来的尾置换到前。

下面这个可以优化下，不过就测试来说已经可以了。

beat 100%
24ms ~ 36ms

测试地址：
https://leetcode.com/problems/rotate-list/description/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not k or not head:
            return head
        
        def getLength(node):
            length = 0
            
            while node:
                node = node.next
                length += 1
            
            return length
        
        length = getLength(head)
        k = k % length

        slow = head
        fast = head
        
        while k > 0:
            fast = fast.next
            
            k -= 1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        rotate_head = slow.next
        
        if not rotate_head:
            return head
        
        slow.next = None
        
        _rotate_head = rotate_head
        while _rotate_head.next:
            _rotate_head = _rotate_head.next
        
        _rotate_head.next = head
        
        return rotate_head
        