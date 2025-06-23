class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr1=[-1]*len(arr)
        maxi=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            
            arr1[i]=maxi
            if arr[i]>maxi:
                maxi=arr[i]

        return arr1




        