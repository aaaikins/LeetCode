# Last updated: 1/5/2026, 3:58:07 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9
10        new_node = TreeNode(val)
11
12        if not root:
13            return new_node
14
15        cur = root
16
17        while True:
18            if val < cur.val:
19
20                if not cur.left:
21                    cur.left = new_node
22                    return root
23
24                cur = cur.left
25
26            else:
27
28                if not cur.right:
29                    cur.right = new_node
30                    return root
31
32                cur = cur.right
33