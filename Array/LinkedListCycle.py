"""

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

基本思路：

形成环就是后面的节点中的next指向了前面出现过的节点。
下面这个用了额外空间。

改进：
使用 O(1) 空间的解决方法：
思路是两个指针：
一个每次走一步，另一个每次走两步，若有一个环，那么走两步的与走一步的会在走过这个环的长度后相遇。
相当于两个人跑步，一个每秒跑两米，一个跑一米，绕着100米的圆形跑，100秒过后，一米的这个跑了一圈，二米的这个跑了两圈，但它们相遇了。


测试地址：
https://leetcode.com/problems/linked-list-cycle/description/

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # while head:
        #     if hasattr(head, 'hasVisited'):
        #         return True
            
        #     head.hasVisited = True
        #     head = head.next
        # return False

        if not head:
            return False
        
        two_head = head.next
        
        if not two_head:
            return False
        
        while head != None and two_head != None:
            
            if head == two_head:
                return True
            
            head = head.next
            try:
                two_head = two_head.next.next
            except:
                return False
        
        return False

