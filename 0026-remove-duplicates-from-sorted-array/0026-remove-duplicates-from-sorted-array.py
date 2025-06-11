class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set1={}
        pos=0
        for i in range(len(nums)):
            if nums[i] not in set1:
                set1[nums[i]]=1
                nums[pos]=nums[i]
                pos+=1
        return len(set1)
            