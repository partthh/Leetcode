class Solution(object):
    def __init__(self):
        self.result=[]
    def solve(self,nums,current,used):
        if(len(current)==len(nums)):
            self.result.append(current[:])
            return
        for i in range(len(nums)):
            if(nums[i] not in current):
                current.append(nums[i])
                used[i]=True
                self.solve(nums,current,used)
                used[i]=False
                current.pop()
                # break
        
        
        # current.append(nums[index])
        
        # current.pop()
        # self.solve(nums,current,index+1)
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result=[]
        used=[False]*len(nums)
        self.solve(nums,[],used)
        return self.result
        