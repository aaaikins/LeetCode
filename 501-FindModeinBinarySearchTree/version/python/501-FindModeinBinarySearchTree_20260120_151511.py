# Last updated: 1/20/2026, 3:15:11 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findMode(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10        max_count = 0
11        cur_count = 0
12        prev_val = root.val
13
14        def inorder(node):
15            nonlocal prev_val, cur_count, max_count, res
16
17            if not node:
18                return
19
20            inorder(node.left)
21
22            if node.val == prev_val:
23                cur_count += 1
24            else:
25                cur_count = 1
26                prev_val = node.val
27
28            if cur_count > max_count:
29                max_count = cur_count
30                res = [node.val]
31            elif cur_count == max_count:
32                res.append(node.val)
33
34            inorder(node.right)
35
36        inorder(root)
37        return res
38
39
40            
41
42        