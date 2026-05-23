class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def bt(start):
            ans.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                bt(i+1)
                path.pop()
        
        bt(0)
        return ans