class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)
        def Check(s:str):
            return s == s[::-1]
        def bt(start: int):
            if start == n:
                ans.append(path[:])
                return 
            for end in range(start, n):
                sub = s[start:end + 1]
                if Check(sub):
                    path.append(sub)
                    bt(end+1)
                    path.pop()
        bt(0)
        return ans