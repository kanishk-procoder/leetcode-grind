class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_to_pattern = {}
        pattern_to_s = {}
        words = s.split()
        if len(words)!=len(pattern):
            return False

        for a , b in zip(pattern, words):
            if a in pattern_to_s and pattern_to_s[a]!=b:
                return False
            if b in s_to_pattern and s_to_pattern[b]!=a:
                return False

            s_to_pattern[b] = a
            pattern_to_s[a] = b

        return True