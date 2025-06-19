class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ele=nums[0]

        arr=[]
        if not nums:
            return []
        count=0
        count1=0
        ele=None
        ele1=None
        for i in range(len(nums)):
            if ele==nums[i]:
                count+=1
            elif ele1==nums[i]:
                count1+=1
            elif count==0:
                count+=1
                ele=nums[i]
            elif count1==0:
                count1+=1
                ele1=nums[i]
            else:
                count-=1
                count1-=1
        count2=0
        count3=0
        for i in nums:
            if i==ele:
                count2+=1
            elif i==ele1:
                count3+=1
            
        if count2>(len(nums)//3):
            arr.append(ele)
        if count3>(len(nums)//3):
            arr.append(ele1)
        return arr