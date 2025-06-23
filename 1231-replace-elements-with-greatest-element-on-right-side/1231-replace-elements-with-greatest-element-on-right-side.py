class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # arr1=[-1]*len(arr)
        # curr=-1
        maxi=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            curr=arr[i]
            arr[i]=maxi
            if curr>maxi:
                maxi=curr
        arr[-1]=-1
        return arr

        # return arr1




        