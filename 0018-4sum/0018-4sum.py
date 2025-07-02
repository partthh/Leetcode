class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr=[]
        # dict1={}
        set1=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                dict1=set()
                for k in range(j+1,len(nums)):
                    temp=-(nums[i]+nums[j]+nums[k])+target
                    if temp in dict1 :
                        temp1=[nums[i],nums[j],nums[k],temp]
                        temp1.sort()
                        set1.add(tuple(temp1))
                    dict1.add(nums[k])
        arr1=[list(i) for i in set1]
        return arr1             