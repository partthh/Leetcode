class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dictu = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        a = 0
        b = a + 1
        while b <= n - 1:
            if s[a] == 'X' and (s[b] == 'L' or s[b] == 'C'):
                result += dictu[s[b]] - dictu[s[a]]
                a += 2
            elif s[a] == 'C' and (s[b] == 'D' or s[b] == 'M'):
                result += dictu[s[b]] - dictu[s[a]]
                a += 2
            elif s[a] == 'I' and (s[b] == 'V' or s[b] == 'X'):
                result += dictu[s[b]] - dictu[s[a]]
                a += 2
            else:
                result += dictu[s[a]]
                a += 1
            b = a + 1
        if a == n - 1:
            result += dictu[s[n-1]]
        return result