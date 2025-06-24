class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        max_t = -inf

        for i, t in enumerate(temperatures):
            if t > max_t and stack:
                temp = t
                res[i] = i - stack[-1][1]
            else:
                stack.append([t, i])
        
        return res
