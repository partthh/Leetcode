class Solution(object):
    def __init__(self):
        self.result=[]
        self.set1=set()
    def solve(self,nums,current):
        if(len(current)==len(nums)):
            self.result.append(current[:])
            return
        for i in range(len(nums)):
            if(nums[i] not in self.set1):
                current.append(nums[i])
                self.set1.add(nums[i])
                # used[i]=True
                self.solve(nums,current)
                # used[i]=False
                self.set1.remove(nums[i])
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
        self.set1=set()
        # used=[False]*len(nums)
        self.solve(nums,[])
        return self.result
        