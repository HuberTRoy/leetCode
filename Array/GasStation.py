"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.


给两个数组：
一个 gas 一个 cost，gas 是所包含的气，cost 则是要花费的气。

问如果能从某个站点开始行使完一圈，那么开始的点在哪。

思路：

如果 sum(gas) < sum(cost)，那么一定是不可能跑完全程的。

注意事项里说过只存在一个解决方法。

那么既然全程的气是足够的，那么一定有一个点可以开始。
1. 从头到尾，若 gas - cost 有剩余，那么是一个潜在的点，此时继续向下进行并记录 rest gas，若之后某站 gas 不够了，那之前记录的点就不是。
2. 此时重新开始，重复 1. 即可。

beat 66%。

测试地址：
https://leetcode.com/problems/gas-station/description/


"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        rest = 0
        station = None
        
        for i in range(len(gas)):
            if rest + gas[i] - cost[i] >= 0:
                rest = rest + gas[i] - cost[i]
                if station is None:
                    station = i
            else:
                rest = 0
                station = None

        return station
        