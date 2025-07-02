class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr=[]
        hashset={}
        for i,j in enumerate((nums)):
            hashset[j]=i
        print(hashset)
        for i in range(len(nums)):
            if target-nums[i] in hashset and hashset[target-nums[i]]!=i :
                # temp=hashset.get(target-i)
                # print(temp,"okay")
                # print(i)
                arr.append(i)
                arr.append(hashset[target-nums[i]])
                return arr
                # return ([i,hashset.get(target-nums[i])]
                # break
        # return arr
            