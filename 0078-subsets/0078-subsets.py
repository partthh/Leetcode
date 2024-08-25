class Solution(object):
    def __init__(self):
        self.result = []
    
    def solve(self, nums, index, curr):
        if index == len(nums):
            self.result.append(curr[:]) 
            return
        
        curr.append(nums[index])
        self.solve(nums, index + 1, curr)
        
        curr.pop()
        self.solve(nums, index + 1, curr)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.solve(nums, 0, [])
        return self.result
        