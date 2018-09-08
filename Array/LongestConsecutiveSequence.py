"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


给定一个数组，返回里面最长的连续子序列。
[100, 4, 200, 1, 3, 2]

需要 O(n) 的时间复杂度。


第一种思路：
排序 + 遍历。
虽然很明显时间复杂度不是 O(n)。Python 的底层用的应该是一个优化过的归并排序，
所以排序时间复杂度基本为 O(nlogn)。

不过很容易写出来，对于Python 来说c++内置的排序效率无疑非常高效。
这种方法的话，平均 28ms 在 Python 里 beat 65%。

第二种思路：
用堆代替排序。构建堆的时间复杂度是 O(n)，这个就算了，底层堆构建自己暂时不会写，等能自己写出稳定的堆再来补上。


第三种思路：

在 Discuss 里找到的：

首先set一遍nums，也就是对应的哈希一遍。

之后迭代nums，然后在set里找n+1,n+2,n+3...直到不存在的一个，记下最大长度。
不过只有这样是不行，对于在一条递增链上的数个数，就会寻找数次。
[100, 200, 1, 4, 3, 2]

100, 200 都没什么事。

1, 4, 3, 2

1 会查询4次。
3 会查询1次。
2 会查询2次。

但除了 1 之外，都没必要查询。

要减少这些没必要的查询，要找到的是 *最小* 这个点。既然是最小，那么n-1肯定是不在这个里面的。
所以可以利用这个条件来减少不必要的查询数量。

不要小看这个操作，如果最长的有10000个数。那么无用的子查询会有 10000 的阶加 50005000 次。

写一下。

ok, 这个更高效，提高了4 ms。

第四种思路：
也是在 Discuss 里找到的：
来日再战。


We will use HashMap. The key thing is to keep track of the sequence length and store that in the boundary points of the sequence. For example, as a result, for sequence {1, 2, 3, 4, 5}, map.get(1) and map.get(5) should both return 5.

Whenever a new element n is inserted into the map, do two things:

See if n - 1 and n + 1 exist in the map, and if so, it means there is an existing sequence next to n. Variables left and right will be the length of those two sequences, while 0 means there is no sequence and n will be the boundary point later. Store (left + right + 1) as the associated value to key n into the map.
Use left and right to locate the other end of the sequences to the left and right of n respectively, and replace the value with the new length.
Everything inside the for loop is O(1) so the total time is O(n). Please comment if you see something wrong. Thanks.

public int longestConsecutive(int[] num) {
    int res = 0;
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    for (int n : num) {
        if (!map.containsKey(n)) {
            int left = (map.containsKey(n - 1)) ? map.get(n - 1) : 0;
            int right = (map.containsKey(n + 1)) ? map.get(n + 1) : 0;
            // sum: length of the sequence n is in
            int sum = left + right + 1;
            map.put(n, sum);
            
            // keep track of the max length 
            res = Math.max(res, sum);
            
            // extend the length to the boundary(s)
            // of the sequence
            // will do nothing if n has no neighbors
            map.put(n - left, sum);
            map.put(n + right, sum);
        }
        else {
            // duplicates
            continue;
        }
    }
    return res;
}


"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numx = set(nums)
        
        maxes = 0
        
        for i in nums:
            if i-1 not in numx:
                x = i
                currentMaxes = 1
                while 1:
                    if x+1 in numx:
                        x += 1
                        currentMaxes += 1
                        continue
                    else:
                        maxes = max(maxes, currentMaxes)
                        break
        return maxes

        # sorted.
        # if not nums:
        #     return 0
        
        # nums.sort()
        
        # currentNums = nums[0]
        # result = []
        # currentMax = 1
        
        # for i in nums[1:]:
        #     if i == currentNums + 1:
        #         currentMax += 1
        #         currentNums = i
        #     elif i == currentNums:
        #         pass
        #     else:
        #         result.append(currentMax)
        #         currentMax = 1
        #         currentNums = i
        # result.append(currentMax)
        
        # return max(result)

