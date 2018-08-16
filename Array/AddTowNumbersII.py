"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

这次给定的正序排列的，而且不允许翻转链表。

思路：
先遍历一遍，为短的一个链表填充0。
(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
              ↓
(7 -> 2 -> 4 -> 3) + (0 -> 5 -> 6 -> 4)

之后用递归：
def x(l1, l2):
    # 退出的条件是 l1 和 l2 均为 None.
    # 当然因为事先做了长度相同的处理这里判断一个即可。
    # 返回的是 (rest, ListNode)
    if l1 is None:
        return (0, None)
    
    nextValue = x(l1.next, l2.next)
    
    get_value = getValue(l1, l2, nextValue[0])
    myNode = ListNode(get_value[0])
    myNode.next = nextValue[1]

    return (get_value[1], myNode)

之后在最外层做一次rest判断。
Ok，一遍过，beat 89%.


还有一种方法是不断 * 10，相加后不断 % 10， // 10。
效率都是一样的。

测试地址：
https://leetcode.com/problems/add-two-numbers-ii/description/




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

        l1, l2 = self.getEqualNodes(l1, l2)
        
        # return l1, l2
        result = self._addTwoNumbers(l1, l2)
        if result[0]:
            node = ListNode(result[0])
            node.next = result[1]
            return node
        return result[1]
            
    def _addTwoNumbers(self, l1, l2):
        if l1 is None:
            return (0, None)
        nextValue = self._addTwoNumbers(l1.next, l2.next)
        
        get_value = self.getRest(l1, l2, nextValue[0])
        myNode = ListNode(get_value[0])
        myNode.next = nextValue[1]
        
        return (get_value[1], myNode)
        
        # get_value = self.getRest()
       
    def getEqualNodes(self, l1, l2):
        # Get equal length.
        b_l1 = l1
        b_l2 = l2
        
        while b_l1 is not None and b_l2 is not None:
            b_l1 = b_l1.next
            b_l2 = b_l2.next
        
        if b_l1:
            # l1 is longer than l2
            t_lx = b_l1
            fix_lx = l2
            raw_lx = l1
        else:
            t_lx = b_l2
            fix_lx = l1
            raw_lx = l2
            
        if t_lx:
            root = ListNode(0)
            b_root = root
            t_lx = t_lx.next
            while t_lx:
                node = ListNode(0)
                root.next = node
                root = node
                t_lx = t_lx.next
            root.next = fix_lx
            
            return (raw_lx, b_root)
        return (l1, l2)
        
    def getRest(self, l1, l2, rest=0):
        # return (val, rest)
        # 9+8 (7, 1)
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0

        return ((l1_val + l2_val + rest) % 10, (l1_val + l2_val + rest) // 10)
