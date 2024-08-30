class Solution:
    def minOperations(self, n: int) -> int:
        dp = {0: 0}

        # Iterate through all numbers from 1 to n
        for i in range(1, n + 1):
            # Initialize the minimum number of operations for the current number
            min_ops = float('inf')

            # Try adding or subtracting each power of 2 from the current number
            for j in range(0, int(math.log2(i)) + 1):
                power_of_two = 2**j
                if i - power_of_two >= 0 and dp.get(i - power_of_two, float('inf')) < min_ops:
                    min_ops = dp[i - power_of_two] + 1
                if i + power_of_two <= n and dp.get(i + power_of_two, float('inf')) < min_ops:
                    min_ops = dp[i + power_of_two] + 1

            # Store the minimum number of operations for the current number
            dp[i] = min_ops

        # Return the minimum number of operations for the given number
        return dp[n] - 1



        