class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        result = (a | b) ^ c
        flips = bin(result).count('1')

        flips += bin((a & b) & result).count('1')
        return flips
