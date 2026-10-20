
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #this is a second approach
        # isme ham total count of the characters check krte rhenge ydi koi ransom wala char h mag m to ek count kam kr denge 
        # ydi hme koi element ki jrurat h but uska count zero reh gya to smjho False return krna h
        freq = {}

        for c in magazine:
            freq[c] = freq.get(c, 0) + 1

        for c in ransomNote:
            if freq.get(c, 0) == 0:
                return False

            freq[c] -= 1

        return True
