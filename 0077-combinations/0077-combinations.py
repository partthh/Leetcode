class Solution(object):
    def __init__(self):
        # self.arr=[]
        self.result=[]
    def solve(self,n,index,k,current):
        if(len(current)==k):
            self.result.append(current[:])
            return
        if index>n:
            return
        current.append(index)
        self.solve(n,index+1,k,current)
        current.pop()
        self.solve(n,index+1,k,current)
        

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # arr=[0]*k
        self.solve(n,1,k,[])
        return self.result


        