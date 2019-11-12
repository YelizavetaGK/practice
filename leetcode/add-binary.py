class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(i) for i in a]
        b = [int(i) for i in b]

        k = 0
        summ = [a.pop(), b.pop()]

        while k != len(summ) - 1:
            for i in range(len(summ)-1, k, -1):
                if (summ[i] + summ[i-1]) == 2:
                    del summ[i], summ[i-1]
                    summ += [0, 1]
                else:
                    tmp = summ[i] + summ[i-1]
                    del summ[i], summ[i-1]
                    summ.append(tmp)
            k += 1
            if a:
                summ.append(a.pop())
            if b:
                summ.append(b.pop())

        number = ''
        for i in summ[::-1]:
            number += str(i)

        return number