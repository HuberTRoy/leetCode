"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...


给一个单链表，将所有的单数节点和双数节点聚合在一块，双数节点跟在单数节点后面。

空间复杂度需要为 O(1) 时间则为 O(n)

思路：

1. 定义两个开头的节点，odd 和 even，用于区分单双。
odd.next 和 even.next 都同时为 .next.next。

不断替换，直到最后，最后不要忘了把 even 连在 odd 后面。

beat:
100%

测试地址：
https://leetcode.com/problems/odd-even-linked-list/description/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd = head
        even = head.next
        even_head = even
        
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            
            odd = odd.next
            even = even.next
            
        odd.next = even_head
        
        return head
        