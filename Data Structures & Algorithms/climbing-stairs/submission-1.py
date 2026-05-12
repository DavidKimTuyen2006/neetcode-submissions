class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self._rec(n, memo)
    def _rec(self, k: int, memo:dict) -> int:
        if k == 1:
            return 1
        if k == 2:
            return 2
        if k in memo:
            return memo[k]
        
        memo[k] = self._rec(k-1,memo) + self._rec(k-2, memo)
        return memo[k]




