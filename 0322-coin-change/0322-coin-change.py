class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initalize dp array
        # for each n, min( current value, dp[n - coin]+1)

        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] =min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] <= amount else -1