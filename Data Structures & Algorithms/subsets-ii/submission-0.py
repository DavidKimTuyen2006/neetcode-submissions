class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        nums.sort()
        def backtrack(n, start):
            if len(path) == n:
                ans.append(path.copy())
                return 
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(n, i+1)
                path.pop()

        for i in range(len(nums)+1):
            backtrack(i, 0)
        return ans