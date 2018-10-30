"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


图看链接：
https://leetcode.com/problems/trapping-rain-water/description/

思路：
1. 这里想到用单调栈来做，给的例子基本上是单调递减，然后有一个不符合的就开始处理。

不过随之而来的遇到的第一个不合理的地方：
           |
|          |
|  |    |  |  
-----------
2 1  0 1  3

在 2 1 0 之后，出现了第一个不是单调递增的值，1，然后开始处理，处理之后得到值 1（1-0）。可是用后面的 3 能装更多的水。

2. 对上面问题的修复是片面的：
    我的想法是再开始判断单调递增，直到不合理的出现。这样修复后可以处理这一类问题，不过随之而来的又一个新的问题：


|               |
|           |   |
|  |     |  | | |
|  |  |  |  | | | 
------------------
4  2  1  2  3 2 4

显然用两边的 4 可以装更多的水，但用之前的单调递增+单调递减是不能达到这样的效果的。

3. 基于 2 的再改进。
   两次思考问题都过于局限，只看到了眼前的一点。
   这次的改进依然基于单调栈，遇到非单调递减的值，不会直接清空已经存储的点，而是全部覆盖记录。

   比如 
   4 2 1 2 当遇到第二个 2 时，会进行 2-1 2-2 的记录，留下 4，因为 4此时是 > 2 的，若是 2 1 4 就没必要保留了。
   所以放置一个用于覆盖记录的列表。

   result = [0] * length

   每次非单调递减后就执行一次 stack[0] - i 与最小值的差覆盖，这样覆盖到最后结果就会是正确的。

例：
 4  2  1  2  3  2  4
[0, 0, 0, 0, 0, 0, 0]
 0  1  2  3  4  5  6

第一次单调递减打破后：
会执行一次 0 - 3 的判断。
[0, 0, 1, 0, 0, 0, 0]

此时栈中剩余的是记录 4 的下标 0 和 记录第二个2的下标 3。

第二次单调递减打破后：
会执行一次 0 - 4 的判断
[0, 0, 1, 0, 0, 0, 0] -> [0, 1, 2, 1, 0, 0, 0]

此时栈中剩余的是 0 和 4

第三次打破后：
会执行一次 0 - 6 的判断
[0, 1, 2, 1, 0, 0, 0] -> [0, 2, 3, 2, 1, 2, 0]

这样的时间复杂度 最差是 O(n²) 最好是 O(n)。

beat 
0% 
太慢，待改进。


测试地址：
https://leetcode.com/problems/trapping-rain-water/description/

"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = [0]

        i = 1
        length = len(height)
        result = [0] * length
        
        while i < length:
            if height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                mins = min(height[stack[0]], height[i])
                index = 0
                for j in xrange(stack[0], i):
                    _ = mins - height[j]

                    if _ > 0 and _ > result[j]:
                        result[j] = _
                
                if height[stack[0]] <= height[i]:
                    stack = []
                else:
                    stack = [stack[0]]
                
                stack.append(i)
                i += 1

        return sum(result)
        