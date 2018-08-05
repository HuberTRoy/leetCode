"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

给定两个链表，判断是否有交叉部分。

分析：

那么，就有了以下4种情况：
 1. 长度相同，有交叉部分。
 2. 长度不同，有交叉部分。
 3. 长度相同，无交叉部分。
 4. 长度不同，无交叉部分。

1. 两个链表，若存在交叉部分则最后至交叉点一定是相同的。
那么倒序判断可以说应该是最高效的，从两个链表的尾部开始，直至找到不同部分或一方为None表示无交叉。
由给定的链表节点可知，这是一只单向链表，所以此思路已经无法在继续进行。 O(n)

2. 另一个思路是根据上面的信息，顺序进行判断，
让长链表一方先走，然后与短的一起走，直至找到相同部分或一方为None表示无交叉，
但我们也不知道长度，只能先遍历一遍找到长度。O(2(m+n))

3. 用的 Python 可以直接利用set()，一个哈希表，来达到O(1)的查找...
所以 原本的做法是，遍历b，然后判断b中的每一个是否在a中存在，存在则返回。这种做法简单粗暴..
但相应的复杂度是O(mn). 

1. 不可行，3.有点无脑。用2.来做一下 

此做法参考了 Discuss 里的高票回答：

反正是要遍历两遍，直接让两个一起走，
要么一起结束：
 1. 有相同返回相同.
 2. 无相同，返回None.

要么一长一短：
 1. 短的肯定是先走完的，然后让短的变成长的。
 2. 短的变成长的之后原本的长的因为走了一段所以变成了较短的，所以会先走完。走的这段距离就是原本我们要求的差值。
 3. 原本的长的再变成短的，一起走完即可。

例：

a = [1, 2, 3, 4]
b = [5, 6, 7]

t = 1
f = 5
t != f
t = 2
f = 6
t != f
t = 3
f = 7
t != f
此时f已经走到的尽头，f替换为a.
t = 4
f = a.head = 1
t != f
此时t已经走到了尽头，t替换为b.
t = b.head = 5
f = 2
此时已经与我们预想的一致了。
a = [1, 2, 3, 4]
b =    [5, 6, 7]

"""
class ListNode(object):
    __slots__ = ('val', 'next')
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        a = headA
        b = headB
        
        if not a or not b:
            return None
        
        while a != b:
            
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        
        return a
