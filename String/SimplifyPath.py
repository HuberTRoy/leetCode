"""
Given an absolute path for a file (Unix-style), simplify it. 

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

给一个 UNIX 风格的文件系统字符串，修剪成标准格式。

思路：
1. 先用正则多斜线变一斜线。
2. 一个用于存放结果的新列表：
    遇到 . 不管，遇到 .. 就弹出尾部的一个，其他的均加入。
3. 最后用 '/' 合并起来。

beat 73%
测试了多次最高是 28ms，和 24ms大致一样，24ms的没用正则，直接 split('/') 然后 判断非空的组成新的。

测试地址：
https://leetcode.com/problems/simplify-path/description/

"""
import re

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = re.sub(r'/+', '/', path)
        if path[-1] == '/':
            path = path[:-1]
        
        path = path.split('/')
        
        new_path = []
        for i in path:
            if i == '..':
                try:
                    new_path.pop()
                    continue
                except:
                    continue
            if i =='.':
                continue
            
            new_path.append(i)
        
        x = '/'.join(new_path)
        if x and x[0] == '/':
            return x
        return '/' + x
