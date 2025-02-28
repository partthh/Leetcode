class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashset={0:1}
        count=0
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1-k in hashset:
                count+=hashset[sum1-k]
            if sum1 in hashset:
                hashset[sum1]+=1
            else:
                hashset[sum1]=1
        return count
        