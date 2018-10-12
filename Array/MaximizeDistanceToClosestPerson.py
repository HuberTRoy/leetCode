"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.


Alex 要坐在任意一个 0 上，问坐在哪个点上距离最近的 1是最远的。

思路：
1. 处理好边界
2. 两两相加，用 相加//2 减去前一个，不用后一个减去 相加//2 是因为如果是奇数的话会偏向前一个，偶数无所谓，所以这样做可以少一步判断。

beat :
75%

测试地址：
https://leetcode.com/contest/weekly-contest-88/problems/maximize-distance-to-closest-person/

"""
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        indexes = [i for i in range(len(seats)) if seats[i] == 1]
        x = indexes[0]
        
        if indexes[0] != 0:
            maxes = indexes[0]
        else:
            maxes = 0
            
        for i in range(1, len(indexes)):
            maxes = max((x + indexes[i]) // 2 - x, maxes)
            x = indexes[i]
        
        if indexes[-1] != len(seats):
            maxes = max(len(seats)-indexes[-1]-1, maxes)
        return maxes
