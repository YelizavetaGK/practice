class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_d = []
        a = 0
        while a == 0:
            if digits:
                a = (digits.pop()+1) % 10
            else:
                digits.append(1)
                break
            new_d.append(a)
        return digits + new_d[::-1]