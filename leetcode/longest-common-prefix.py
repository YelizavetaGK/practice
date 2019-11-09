class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        elif len(strs) == 1:
            return strs[0]

        length = max([len(i) for i in strs])
        first_word = strs[0]
        j = length
        prefix = ''
        flag = False

        while j >= 0:

            for i in range(1, len(strs)):
                if first_word[0:j] == strs[i][0:j]:
                    flag = True
                else:
                    flag = False
                    break
            if flag == True and len(prefix) < len(first_word[0:j]):
                prefix = first_word[0:j]
            j -= 1

        return prefix
        