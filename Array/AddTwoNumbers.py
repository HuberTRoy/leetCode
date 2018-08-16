"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


给两个非空的链表，每个节点包含一个整数。数字是以倒序排列的，现在输出两个链表相加得出的新链表。

长度问题：
1. 同长度不需要考虑。
2. 不同长度下，正序意味着
 3421 + 465 = 3421
               465
这种情况最好的方法应该是从后向前，但此题目中给出的就是从后向前，所以也不必考虑这个，
直接给0即可。

思路：
头到尾，对于每一个位来说，最大是 9+9，进位最大是1.

Ok，一遍过，O(n)。
beat 67%.


"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        get_value = self.getRest(l1, l2)
        root = ListNode(get_value[0])
        rest_value = get_value[1]
        l1 = l1.next
        l2 = l2.next

        backup_root = root

        while l1 is not None or l2 is not None:
            
            get_value = self.getRest(l1, l2, rest_value)

            new_node = ListNode(get_value[0])
            rest_value = get_value[1]

            root.next = new_node
            root = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None    
        
        if rest_value:
            root.next = ListNode(rest_value)
        
        return backup_root
        
    def getRest(self, l1, l2, rest=0):
        # return (val, rest)
        # 9+8 (7, 1)
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0

        return ((l1_val + l2_val + rest) % 10, (l1_val + l2_val + rest) // 10)
