class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first_ele = strs[0]
        last_ele = strs[-1]
        common_word = []
        for i in range(len(first_ele)):
            if(first_ele[i] == last_ele[i]):
                common_word.append(first_ele[i])
            else:
                break
        result = "".join(common_word)
        return result

