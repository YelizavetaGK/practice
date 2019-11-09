class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = []
        current = s[0]

        for i in range(1, len(s)):
            if roman[current] < roman[s[i]]:
                number.append(-roman[current])
            else:
                number.append(roman[current])
            current = s[i]
        number.append(roman[s[-1:]])       
        
        return sum(number)