class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]  # Last day of travel
        dp = [0] * (n + 1)
        travel_set = set(days)

        for i in range(1, n + 1):
            if i not in travel_set:
                dp[i] = dp[i - 1]  # No travel on this day
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],                    # 1-day pass
                    dp[max(0, i - 7)] + costs[1],           # 7-day pass
                    dp[max(0, i - 30)] + costs[2]           # 30-day pass
                )

        return dp[n]
        