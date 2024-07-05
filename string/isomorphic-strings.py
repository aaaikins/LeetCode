class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        # s_map = {}
        # t_map ={}

        # for i in range(len(s)):
        #     s_map[s[i]] = s_map.get(s[i], 0) + 1
        #     t_map[t[i]] = t_map.get(t[i], 0) + 1

        # return sorted(s_map.values()) == sorted(t_map.values())
        