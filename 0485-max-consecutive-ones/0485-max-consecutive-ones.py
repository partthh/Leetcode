class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        i=0
        for j in range(len(nums)):
            if (nums[j]==0):
                # maxi=max(maxi,j-i)
                i=j+1
            maxi=max(maxi,j-i+1)
        return maxi

