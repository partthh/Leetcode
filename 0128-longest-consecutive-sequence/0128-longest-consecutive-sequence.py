class Solution(object):
    def longestConsecutive(self,nums):
        s1=set()
        # cnt=
        cnt=0
        longest=0
        for i in range(len(nums)):
            s1.add(nums[i])
        for i in nums:
            x=i
            if x-1 not in s1:
                cnt=1
                while x+1 in s1:
                    x+=1
                    cnt+=1
                longest=max(longest,cnt)
        return longest