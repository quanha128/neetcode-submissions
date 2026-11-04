class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, paths, remain):
            # base case
            if remain == 0:
                res.append(list(paths))
                return
            elif remain < 0:
                return
            
            for i in range(start, len(nums)):
                # choice
                paths.append(nums[i])

                # explore
                backtrack(i, paths, remain-nums[i])

                # reset
                paths.pop()
        backtrack(0, [], target)
        return res