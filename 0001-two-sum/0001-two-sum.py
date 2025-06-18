class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr1=[]
        sum1=0
        set1={}
        for i in range(len(nums)):
            set1[nums[i]]=i
        for j in range(len(nums)):
            if target-nums[j] in set1:
                ind=set1[target-nums[j]]
                if j!=ind:
                    arr1.append(j)
                    arr1.append(set1[target-nums[j]])
                    return arr1



            

        