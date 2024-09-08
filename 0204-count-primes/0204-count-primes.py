class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0

        # ans1=
        ans=[1]*(n)
        ans[0]=0

        ans[1]=0
        for i in range(2,int(n**0.5)+1):
            for j in range(i*i,n,i):
                ans[j]=0

        return sum(ans)