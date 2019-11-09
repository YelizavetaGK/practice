class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0

        while(x > revertedNumber):
            revertedNumber = revertedNumber* 10 + x % 10
            x //= 10

        if x == revertedNumber//10 or x == revertedNumber:
            return True
        else:
            return False