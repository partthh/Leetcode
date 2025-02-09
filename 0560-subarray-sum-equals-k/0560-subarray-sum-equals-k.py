class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        set1={0:1}
        sum1=0
        count=0
        # set1[0]=1
        # remi=0
        for i in range(len(nums)):

            sum1+=nums[i]
            if (sum1-k in set1):
                count+=set1[sum1-k]
            if sum1 in set1:
                set1[sum1]+=1
            else:
                set1[sum1]=1
 
        return count
        