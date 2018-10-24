"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

O (n log n) 用归并排序比较好。

难点在于常量空间复杂度...

暂不解决这个问题，再回顾下归并排序。

归并排序的核心思路是分治，将大问题分成小问题，再将已经解决的小问题不断合并成一个解决方案。

所以归并排序的话先分割，进行对半分割即可。

_left = list[:middle]
_right = list[middle:]

分割成 _left 和 _right 后，要做的是归并。

merge_sort(_left, _right)

这里就归并用到底不做剪枝优化了。

merge_sort
的关键词是：
1. _left 和 _right 分别挑剩余的最小的合并到一个集合里。
2. 若 _left 耗尽，直接合并 _right。
3. _right 同理。

def merge_sort(_left, _right):
    _l_index = 0
    _r_index = 0

    _l_length = len(l)
    _r_length = len(r)

    while _l_i < _l_l and _r_i < _r_l:
        if l[_l_i] < r[_r_l]:
            l[_l_i]
            _l_i += 1
        else:
            r
    
    if _l_i == _l_l:
        extend _r

    if _r_i == _r_l:
        extend _l

    return result


这是最原始的 split ，后面要扩展一下才能用。
def split(list):

    _left = list[:middle]
    _right = list[middle:]

    return merge_sort(_left, _right)

在初次分割之后，_left 和 _right 确实分成了两份，但都是未经过排序的，直接用merge_sort的话是不行的（这里展开思考的话，会想到另一种排序——堆排序）。

我们需要对_left和_right分别再次进行 分割-合并。

def split(list):

    _left = split(list[:middle])
    _right = split(list[middle:])

    return merge_sort(_left, _right)

写到这里还有点问题，这样会无限分割下去，在加一个判断用于结束递归。

def split(list):
    if len(list) <= 1:
        return list

    _left = split(list[:middle])
    _right = split(list[middle:])

    return merge_sort(_left, _right)

元素<=1个时就可以返回了。

   [1, 2, 4, 5]
   left  ↓  right
  [1, 2]   [4, 5]
left↓right left↓right
 [1] [2]   [4] [5]
到这里
不在分割 [1] [2] 分别返回，然后执行了
merge_sort([1], [2])
merge_sort([4], [5])

然后再返回...


beat:
84%
测试地址：
https://leetcode.com/problems/sort-list/description/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lists = []
        
        while head:
            lists.append(head.val)
            head = head.next
        
    
        def merge_sort(l, r):
            
            _l = 0
            _r = 0
            
            _l_length = len(l)
            _r_length = len(r)
            
            result = []
            
            while _l < _l_length and _r < _r_length:
                if l[_l] < r[_r]:
                    result.append(l[_l])
                    _l += 1
                else:
                    result.append(r[_r])
                    _r += 1
                    
            if _l == _l_length:
                while _r < _r_length:
                    result.append(r[_r])
                    _r += 1
            else:
                while _l < _l_length:
                    result.append(l[_l])
                    _l += 1
            
            return result
        
        def split(l):
            if len(l) <= 1:
                return l
            
            _l = split(l[:len(l)//2])
            _r = split(l[len(l)//2:])
            
            return merge_sort(_l, _r)
        
        lists = split(lists)
        
        if not lists:
            return None
        
        head = ListNode(lists[0])
        
        _head = head
        
        for i in lists[1:]:
            head.next = ListNode(i)
            head = head.next
        
        return _head
        