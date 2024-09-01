class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1<<len(nums)):
            sublist = []
            for j in range(len(nums)):
                if (i&(1<<j)):
                    sublist.append(nums[j])
            ans.append(sublist.copy())
        return ans
        