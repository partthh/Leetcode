class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        hash1={0:1}
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1-k in hash1:
                count+=hash1[sum1-k]
            if sum1 in hash1:
                hash1[sum1]+=1
            else:
                hash1[sum1]=1
        return count