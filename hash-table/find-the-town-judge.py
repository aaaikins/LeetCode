class Solution:
  def findJudge(self, n, trust):
    num_groups = len(trust)
    trust_map = {}
    list = []

    if n == 1:
      return 1
    for i in range(num_groups):
        list.append(trust[i][0])
        trust_map[trust[i][1]] = trust_map.get(trust[i][1], 0) + 1


    for key, val in trust_map.items():
        if val == n-1 and key not in list:
            return key
    
    return -1