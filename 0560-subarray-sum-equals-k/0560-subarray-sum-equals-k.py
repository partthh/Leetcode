class Solution(object):
    def subarraySum(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash1={}
        sum1=0
        count=0
        for i in range(len(arr)):
            sum1+=arr[i]
            if sum1==k:
                count+=1
            if sum1-k in hash1:
                # maxi=max(maxi,length)
                count+=hash1[sum1-k]

            if sum1 not in hash1:
                hash1[sum1]=1
            # if hash1[sum1] not in 
            else:
                hash1[sum1]=hash1[sum1]+1
        return count
        