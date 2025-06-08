class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1={}
        maxi=0
        count=0
        for i in nums:
            if i in set1:
                set1[i]+=1
                maxi=max(maxi,set1[i])
            else:
                set1[i]=1
                maxi=max(maxi,set1[i])
        # print(set1)
        # print(maxi)
        for key,value in set1.items():
            if value==maxi:
                count+=value
        return count
        
        