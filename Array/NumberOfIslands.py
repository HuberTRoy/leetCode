"""
与今日头条的秋招第一题差不多的题：
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

分析看 FootbalFans.py

passed.

测试地址：
https://leetcode.com/problems/number-of-islands/description/

"""
class Solution(object):
    def makeXY(self, x, y):
        return ((x, y-1),
                (x, y+1),
                (x-1, y),
                (x+1, y))
    
    def numIslands(self, court):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        fans_groups = []
        x = 0
        y = 0
        if not court:
            return 0
        
        x_length = len(court[0])
        y_length = len(court)

        def helper(x, y):
            Xy = self.makeXY(x, y)
            for i in Xy:
                try:
                    if i[1] < 0 or i[0] < 0:
                        continue
                        
                    if court[i[1]][i[0]] == '1':
                        court[i[1]][i[0]] = '0'
                        t = helper(i[0], i[1])
                except IndexError:
                    continue
            else:
                return 1


        for y in range(y_length):
            for x in range(x_length):
                if court[y][x] == '1':
                    court[y][x] = '0'
                    fans_groups.append(helper(x, y))



        if not fans_groups:
            return 0

        return len(fans_groups)      

