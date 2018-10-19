"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

设计一种结构，支持以下三种操作：

insert(val) 插入一个 val, 若存在则返回 False，否则True.
remove(val) 从中删除一个 val, 若不存在则返回 False，否则True.
getRandom() 返回其中的任意一个数。

以上操作均需在 O(1) 的时间复杂度内完成。

插入 O(1) 的结构一般会用 哈希表，链表，或者在列表尾部插入。
删除 O(1) 的话链表需要查找，即时用到二分也不是 O(1)，列表的话给定确定的下标查找是 O(1) 的。

根据上面的结论，哈希表肯定是要用了，添加删除和查找都是 O(1)，不过哈希表并不能进行 getRandom，或者说不能以 o(1) 时间完成 getRandom。
而上面提到，列表的给定下标的查找是 O(1) 的，并且插入到列表尾的话也是 O(1) 的操作。

所以这里的思路是用两个结构：
在不考虑内存的情况下，
哈希表用于进行一般的查找删除，列表用于找随机。

1. 这样在添加时，哈希表的 key:value 为 val:index。
随后在列表尾添加 val.

2. 删除时，将要删除的元素的下标与列表的最后一个元素互换，删除列表尾和哈希表内的目标元素，
并将 `最后一个元素` 在 `哈希表`中的 `下标` 替换为原本要删除的那个元素的下标。

这里要注意，写的时候若是 先从哈希表中取出目标的下标，然后在从列表尾取出最后一个元素添加的话，要判断下是否是同一个元素，若是同一个则可以不进行替换。


beat:
90%

测试地址：
https://leetcode.com/problems/insert-delete-getrandom-o1/description/


"""
import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_dict = {}
        self.data_list = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.data_dict.get(val) is not None:
            return False
        
        self.data_dict[val] = self.length
        self.length += 1
        self.data_list.append(val)
        
        return True
    
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        if self.data_dict.get(val) is not None:
            x = self.data_dict.pop(val)
            y = self.data_list[-1]
            if y != val:

                self.data_dict[y] = x
            self.data_list[-1], self.data_list[x] = self.data_list[x], self.data_list[-1]
            
            self.data_list.pop()
            self.length -= 1

            return True
        
        return False
        
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        return self.data_list[random.randint(0, self.length-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
