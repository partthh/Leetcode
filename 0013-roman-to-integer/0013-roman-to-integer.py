class Solution:
    def romanToInt(self, s: str) -> int:
        add1=0
        set1={"I":1,'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        for i,j in zip(s,s[1:]):
            if set1[i]<set1[j]:
                add1-=set1[i]
            # elif(set1[i]>set1[j]):
                # pass
            else:
                add1+=set1[i]
        return add1+set1[s[-1]]