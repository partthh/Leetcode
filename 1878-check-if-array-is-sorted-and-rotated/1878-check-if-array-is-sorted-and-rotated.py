class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        for i in range(1,len(nums)):
            
            if nums[i-1]>nums[i]:
                count+=1
        if nums[-1]>nums[0]:
            count+=1
            
        print(count)
        if count>=2:
            return False
        else:
            return True