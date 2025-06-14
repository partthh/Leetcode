class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1={}
        for i in nums:
            # if i in dict1:
            dict1[i]=dict1.get(i,0)+1
            # else:
            #     dict1[i]=1
        print (dict1)
        for i,value in dict1.items():
            if value==1:
                return i