"""

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49


给一组数据，返回两组边界中可盛放水最多的一组。

图数据看链接：
https://leetcode.com/problems/container-with-most-water/description/


思路：
1. 一开始是个Dp, O(n²)。当然是TLE...

Dp时的主要难点在于：
无法把当前点作为子问题答案，只能是记录从之前的所有点到此点最大的一组作为子问题。

分析
盛放水有两个决定因素：一个是点到点的距离，另一个是两点中最短的那个的高度。

一开始可能会想的很简单：
记录出最高最远的一个点不就是了？
答案是错误的。
例子中所选的点是：
 0 1 2 3 4 5 6 7 8
[1,8,6,2,5,4,8,3,7]
   ↑             ↑


若是修改一下，把第一个从 1 变为 7。那么应该选 0 和 8 索引处的数。
 0 1 2 3 4 5 6 7 8
[7,8,6,2,5,4,8,3,7]
 ↑               ↑
当记录 7,0 和 8,1 相遇，是记录 7,0 好还是记录 8,1 好呀？
肯定会说当然是记录 7,0 它能提供 7 个呢，8从高度上只多了 1 而已。
这样在部分情况下当然没问题。

还有一种情况：
[7, 15, 13]

这种情况15 比 7 多了 8 点，是否应该记录 15,1 而不是 7,0 呢？

如果记录了 15,1  在 13 处所记录的最大值应为 13 * (2-1) = 13
但是 用 7,0 却可以有 7 * (2-0) = 14 呢。
这种情况下 15 这个点应该用 7,0

但稍加一位：
[7, 15, 13, 12]

这个时候，15 这个点用 15,1 又是最合适的。


所以明朗了，
当前点用哪个取决于它后面的数。
在判断到 15 这个点的时候，如果后面也有一个数，它与 7 的差值*与 15 的距离可以抵消掉 7 的话就可以了。
但是这个写法写起来不光麻烦...而且从效率上好像并无改进，甚至更差，因为不光要把剩下的所有元素迭代一遍，
有时还要判断之前的一些。

2.

通过上面的分析，这个算法肯定不能只从一边想办法。
由此，想到了 Two sum 的一种O(n) 算法:
先排序，
有两个指针从两端开始走，若它们相加大于目标，那么就把右边的指针向前挪一位，反之左边的挪一位。

同样的思路用在这。

用两个指针从两端走，记录下当前的最大值，然后让其中较小的一边移动一位。
为什么移动较小的一个呢：

先来看如果移动较大的一位：
将较大的一位记为 X.
  较小的记为 Y.
那么剩下的数对于Y的那个来说有三种情况：
1. 比X大。 这种情况肯定是不如之前的可放的水多，高度不变的情况下距离变短了。
2. 与X相等。同上。
3. 比X要小。
   如果这个数比X要小，那么对应的也有三种情况：
   1. 比 Y 要小，如果比 Y 小，那么距离和高度同时不如 X, Y。
   2. 与 Y 相等，距离不如 X, Y。
   3. 比 Y 要大，距离不如 X, Y。

所以如果移动较大的一位，剩下的结果只能是要小。没有比它们更大的情况。

所以移动较小的一位，可以找出潜在的上面分析到的，
像 [7, 15, 13, 12] 
是否有可能有 15 - 12 这种情况。

---
最后，再写的时候又发现一个问题：
如果两个数相同的要怎么办呢？

最后得出的结论是：
凉拌！
---
拿错剧本了。

应该是 走哪一边无所谓。
因为只有以下几种情况：
1. 比它们小的，这种情况全部都会小，静静的等着迭代结束就好了。
2. 有一个比它们大的，这种情况同上，分析过了。
3. 有多个比它们大的，只有这种情况才有可能比这一对相同的大。
   而这种情况，先走哪一个都不会对结果有影响，如果有这种情况先走的那个一定会在这个点上等着后走的追上来。


OK:

思路清晰了：
1. 头尾两个指针。
2. 小的要先走。
3. 同样的无所谓。
4. 记录每一步 min(X, Y) * distance.
5. 在头尾相遇时结束，也就是 O(n) 时间复杂度与 O(1) 空间复杂度。

测试链接：
https://leetcode.com/problems/container-with-most-water/description/
beat 95% 40ms。 
---

哇塞，又一个自己想到的好方法，测试通过后在 Discuss 里找到同样的思路的算法。

好像，我还是有点东西的喔。哎嘿嘿。

"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        
        currentMax = 0
        
        while l != r:
            currentMax = max(min(height[r], height[l]) * (r-l), currentMax)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        
        return currentMax
