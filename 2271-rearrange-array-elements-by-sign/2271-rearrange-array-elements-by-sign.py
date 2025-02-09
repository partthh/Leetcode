class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1=[]
        l2=[]
        for i in range(len(nums)):
            if nums[i]>0:
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        pos=1
        pos1=0
        while len(l1)!=len(nums):
            
            l1.insert(pos,l2[pos1])
            pos+=2
            pos1+=1
        return l1
        # for i in range(1,len(l2)):
            # l1.insert(i)