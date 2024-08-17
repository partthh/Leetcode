class Solution(object):
    def __init__(self):
        self.count1=0
        self.arr=[]
        self.result=float("-inf")

    def solve(self,requests,count1,arr,index):
        if(index==self.count1):
            if all(x==0 for x in arr):
                self.result=max(count1,self.result)
            return
        arr[requests[index][0]]-=1
        arr[requests[index][1]]+=1

        # count1+=1
        # arr[]
        self.solve(requests,count1+1,arr,index+1)
        arr[requests[index][0]]+=1
        arr[requests[index][1]]-=1
        # count1-=1
        self.solve(requests,count1,arr,index+1)
        

    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        self.count1=len(requests)
        arr=[0]*n
        # self.count=0
        self.solve(requests,0,arr,0)
        return self.result
        