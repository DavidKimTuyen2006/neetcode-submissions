class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        return self.tri(n, memo)
    def tri(self, n, memo):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = self.tri(n-1, memo) + self.tri(n-2,memo) + self.tri(n-3,memo)
        return memo[n]
    