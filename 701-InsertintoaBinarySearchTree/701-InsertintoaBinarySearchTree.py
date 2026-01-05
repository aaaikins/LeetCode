# Last updated: 1/5/2026, 3:51:11 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        new_node = TreeNode(val)
10
11        if not root:
12            return new_node
13
14        cur = root
15
16        while cur:
17            if val < cur.val:
18                if cur.left:
19                    cur = cur.left
20                else:
21                    cur.left = new_node
22                    break
23            else:
24                if cur.right:
25                    cur = cur.right
26                else:
27                    cur.right = new_node
28                    break
29
30        return root