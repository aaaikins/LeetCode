# Last updated: 2/18/2026, 11:42:34 PM
1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.word = None
5    
6    def addWord(self, word):
7        node = self
8        for ch in word:
9            if ch not in node.children:
10                node.children[ch] = TrieNode()
11            node = node.children[ch]
12        node.word = word
13
14class Solution:
15    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
16        # Build a Trie
17        trie = TrieNode()
18
19        for word in words:
20            trie.addWord(word)
21
22        nRows = len(board)
23        nCols = len(board[0])
24
25        results = []
26        visit = set()
27
28        def dfs(r, c, node, word):
29            if (r < 0 or r >= nRows) or (c < 0 or c >= nCols) or board[r][c] not in node.children or (r,c) in visit:
30                return
31
32            visit.add((r, c))
33            node = node.children[board[r][c]]
34            word += board[r][c]
35
36            if node.word:
37                results.append(word)
38                node.word = None
39
40            dfs(r + 1, c, node, word)
41            dfs(r, c + 1, node, word)
42            dfs(r - 1, c, node, word)
43            dfs(r, c - 1, node, word)
44
45            visit.remove((r, c))
46
47        for r in range(nRows):
48            for c in range(nCols):
49                dfs(r, c, trie, "")
50
51        return results