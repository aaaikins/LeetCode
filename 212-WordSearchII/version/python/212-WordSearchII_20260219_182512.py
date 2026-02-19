# Last updated: 2/19/2026, 6:25:12 PM
1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.word = None
5
6    def addWord(self, word):
7        node = self
8
9        for ch in word:
10            if ch not in node.children:
11                node.children[ch] = TrieNode()
12            node = node.children[ch]
13
14        node.word = word
15
16class Solution:
17    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
18        nRows = len(board)
19        nCols = len(board[0])
20
21        trie = TrieNode()
22
23        for word in words:
24            trie.addWord(word)
25
26        
27        visit = set()
28        results = []
29
30        def dfs(r, c, node):
31            if (r < 0 or r >= nRows) or (c < 0 or c >= nCols) or (r, c) in visit or board[r][c] not in node.children:
32                return
33
34            visit.add((r, c))
35            ch = board[r][c]
36            parent = node
37            node = node.children[ch]
38
39            if node.word:
40                results.append(node.word)
41                node.word = None
42
43            dfs(r + 1, c, node)
44            dfs(r, c + 1, node)
45            dfs(r - 1, c, node)
46            dfs(r, c - 1, node)
47
48            visit.remove((r, c))
49
50            if not node.children:
51                del parent.children[ch]
52
53            
54        
55        for r in range(nRows):
56            for c in range(nCols):
57                dfs(r, c, trie)
58
59        
60        return results
61
62