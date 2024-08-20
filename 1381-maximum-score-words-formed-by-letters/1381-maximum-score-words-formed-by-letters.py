class Solution(object): 
    def __init__(self):
        self.maxscore=float("-inf")
        self.dict1={}
    def solve(self,words,score,dict1,index,currentsum):
        self.maxscore=max(self.maxscore,currentsum)
        if(index>= len(words)):
            return
        dict2=dict1.copy()
        currentsum2=0
        j=0

        while j<len(words[index]):
            ch=words[index][j]
            if(dict2.get(ch,0)>0):
                dict2[ch]-=1
                currentsum2 +=score[ord(ch)-ord("a")]   
            else:

                break
            j+=1

        if(j==len(words[index])):
            self.solve(words,score,dict2,index+1,currentsum+currentsum2)
        self.solve(words,score,dict1,index+1,currentsum)

    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        self.dict1={}
        # self.sum=0
        for i in letters:
            if(i in self.dict1):
                self.dict1[i]+=1
            else:
                self.dict1[i]=1
        self.maxscore=float("-inf")
        self.solve(words,score,self.dict1,0,0)
        return self.maxscore
        