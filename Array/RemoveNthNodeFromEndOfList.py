"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

给一个链表和一个n，删除从后数第n个节点。

n总是有效的。

进阶条件是一次性完成。

一开始的想法是总得先知道长度，然后才能倒数第n个吧。
所以一开始用的列表，Python 中的列表非常适合做这个操作。
O(n) 遍历，然后剩下的索引操作就是 O(1) 了。

失误的是，考虑到了如果删除的是head，但是写的话没写成 head.next，写成了 list_node[1]，
这样在链表中只有一个节点的时候就出错了...

本题算是失败了。2 pass.

效率上是 28ms。

看了25ms的写法，感觉非常聪明。
以前总是想，这样的必须得先过一遍知道长度才能做其他的事吧。
这个的写法是，用一条像是绳子一样的。
|----------|
slow     fast

让fast走n步。
然后fast和slow一起走，等fast.next是None，也就是到头了。那么slow就是要删除的点的前一个了。
直接把slow.next与slow.next.next结合就达标了。
如果走了n步后fast直接是None了。那么说明删除的节点是head，那么返回 head.next就好了。

不过这个提交了两次也是 28ms..
但是这个思路是真的棒。

关键词：
绳子。

测试地址：
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/



"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        my_head = my_trail = head
        for i in range(n):
            my_head = my_head.next
        
        if not my_head:
            return head.next
        
        while my_head.next:
            my_head = my_head.next
            my_trail = my_trail.next
        
        my_trail.next = my_trail.next.next
        
        return head
#         list_node = []
#         my_head = head
#         while my_head:
#             list_node.append(my_head)
#             my_head = my_head.next
        
#         if n == len(list_node):
#             try:
#                 return list_node[1]
#             except:
#                 return None
            
#         if n == 1:
#             list_node[-2].next = None
#             return list_node[0]
        
#         list_node[-(n+1)].next = list_node[-(n-1)]
        
#         return list_node[0]