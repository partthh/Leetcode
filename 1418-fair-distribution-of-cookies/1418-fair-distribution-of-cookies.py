class Solution(object):
    def __init__(self):
        self.result=float('inf')

    def solve(self,index,cookies,children,k):
        if index==len(cookies):
            self.result=min(self.result,max(children))
            return
            
        candy=cookies[index]
        for i in range(k):
            children[i]+=candy
            self.solve(index+1,cookies,children,k)
            children[i]-=candy
            if(children[i]==0):
                break


    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        children=[0]*k
        self.solve(0,cookies,children,k)
        return self.result
        