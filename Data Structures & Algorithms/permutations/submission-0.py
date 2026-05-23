class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        used = [0]*n
        path = []

        def bt(start):
            if len(path) == n:
                ans.append(path.copy())
                return 
            
            for i in range(n):
                if used[i] == 1:
                    continue
                path.append(nums[i])
                used[i] = 1
                bt(0)
                path.pop()
                used[i] = 0
        bt(0)
        return ans