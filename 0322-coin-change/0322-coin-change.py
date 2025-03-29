class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # intialize dp array
        # base case 0 coins yield 0 sum
        # induction case n sum is yielded by [(n-val) +1] coins where val is any of our coins

        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin]+1)

        return dp[amount] if dp[amount] <= amount else -1 