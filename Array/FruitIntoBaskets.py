"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

1. Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
2. Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


对于每一个 i，都会产生 tree[i] 类型的水果。有两个篮子，每个篮子只能放一种类型，但同类型的不限次数。
问最多能摘的水果数量。


思路:
1. 一开始用的回溯法：

用两个变量表示篮子，都有水果时就追加。
第三种类型的出现时就进行回溯，回到上一个水果的点再次进行判断。

效率上最差就算 O(n²) 吧。
反正没passed就是了，90个里过了80个..

 1.2. 有个要注意的点：回溯的点选择：
     [1,0,6,6,4,6]

在 tree[2] (6) 这个点，出现了 1,0,6 三种类型，开始回溯，回溯的点是 0, 6 (1, 2) 。
在 tree[4] (4) 这个点，出现了 0,6,4 三种类型，开始回溯，回溯的点需要是 6, 4 (2, 4) 这个6是相邻的第一次出现的点。

---

2. O(n) 的进阶：
对于每一个点来说可以存储一些属性来取消回溯：
     [1,0,6,6,4,6]

count: 这个点可采集到的两种类型的水果数量。
repeat_count: 相邻的同类型水果数量。
capacity: 篮子里的水果类型。
self-value: 这个点可以采集的水果类型。

那么对于下一个点，只需要判断：
1. 是不是同类型：
    同类型 repeat_count 和 count 都 + 1.
   不是看2.
2. 是不是在篮子里：
    是则只把 count + 1 ，同时 repeat_count 和 self-value 更新为1与此点的类型。
   不是看3.。
 2.1 篮子没满，没满就 count + 1 重置 self-value repeat_count 并在 capacity 加上 这个点。

3. 这一步是出现了不在篮子里的第三种水果类型，出现之后：
   count repeat_count capacity 和 self-value 全部重置。
   count 为上一个点的 repeat_count + 1
   repeat_count 为 1
   capacity 重置为 上一个 点的 self-value + 现在的 self-value
   self_value 就此点的值。

最后输出 max count即可。

这个passed. 784ms.

测试链接：
https://leetcode.com/contest/weekly-contest-102/problems/fruit-into-baskets/

"""
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # [{count, repeat_count, capacity, self-value}, ]
        tree_seed = [
                        {'count': 1, 'repeat_count': 1, 'capacity': set([tree[0]]), 'self_value': tree[0]}
                    ]
        
        for i in range(1, len(tree)):
            prev = tree_seed[i-1]
            
            # repeat self_value
            if tree[i] == prev.get('self_value'):
                tree_seed.append({'count': prev.get('count') + 1,
                                 'repeat_count': prev.get('repeat_count') + 1,
                                 'capacity': prev.get('capacity'),
                                 'self_value': tree[i]})
                continue
            
            # already into basket but cannot beside each other.
            
            if tree[i] in prev.get('capacity'):
                tree_seed.append({'count': prev.get('count') + 1,
                                 'repeat_count': 1,
                                 'capacity': prev.get('capacity'),
                                 'self_value': tree[i]})
                continue     
            
            # != but can taken into basket.
            if len(tree_seed[i-1].get('capacity')) == 1:
                new = prev.get('capacity')
                new.add(tree[i])
                
                tree_seed.append({'count': prev.get('count') + 1,
                                 'repeat_count': 1,
                                 'capacity': new,
                                 'self_value': tree[i]})
                continue
                
            # Found Third-fruit.
            new = set()
            new.add(tree[i])
            new.add(tree[i-1])
            tree_seed.append({'count': tree_seed[i-1].get('repeat_count') + 1,
                             'repeat_count': 1,
                             'capacity': new,
                             'self_value': tree[i]})    
        return max(tree_seed, key=lambda x: x['count']).get('count')
            
#         maxes = 0
#         one = None
#         two = None
#         count = 0
#         # for index in range(len(tree)):
#         index = 0
#         length = len(tree)
        
#         while index < length:
            
#             i = tree[index]
#             if one is None:
#                 one = i
#                 count += 1
#                 index += 1
#                 continue
                
#             if i == one:
#                 count += 1
#                 index += 1
#                 continue
                
#             if two is None:
#                 two = i
#                 count += 1
#                 index += 1
#                 continue
            
#             if i == two:
#                 count += 1
#                 index += 1
#                 continue
            
#             maxes = max(maxes, count)
#             count = 1
#             one = tree[index-1]
#             two = None

#             for t in range(index-2, -1, -1):
#                 if tree[t] == one:
#                     index = t+1
#                 else:
#                     break
#         else:
#             maxes = max(maxes, count)
            
        # return maxes
