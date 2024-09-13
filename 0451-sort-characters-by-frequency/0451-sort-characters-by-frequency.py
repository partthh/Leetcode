class Solution(object):
    def frequencySort(self, str1):
        
        hashset={}
        for i in str1:
            if(i in hashset):
                hashset[i]+=1
            else:
                hashset[i]=1
        # return hashset
        # print(hashset)
        # print (len(hashset))
        str1=""
        count=0
        while len(hashset)>0:
            maxx1=max(hashset,key=hashset.get)
            count=hashset[maxx1]
            # for i in range(count):
            str1+=maxx1*count
            # count=0
            del hashset[maxx1]

        # count=0
        # print(max(hashset))
        # # while 
        # maxx1=max(hashset,key=hashset.get)
        return str1
        """
            :type s: str
            :rtype: str
        """

        