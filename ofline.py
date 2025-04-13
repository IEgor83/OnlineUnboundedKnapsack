class UnboundedOfflineKnapsack:
    def __init__(self, capacity=10):
        self.capacity = capacity

    def _fill_knapsack(self, weights, values=None):
        n = len(weights)
        dp = [0] * (self.capacity + 1)

        for c in range(self.capacity + 1):
            for i in range(n):
                if weights[i] <= c:
                    if values:
                        dp[c] = max(dp[c], dp[c - weights[i]] + values[i])
                    else:
                        dp[c] = max(dp[c], dp[c - weights[i]] + weights[i])
        return dp[self.capacity]

    def unbounded_knapsack(self, weights, values):
        return self._fill_knapsack(weights, values)

    def unbounded_knapsack_simple(self, weights):
        return self._fill_knapsack(weights)
