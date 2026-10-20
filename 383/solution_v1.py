class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_set = set(ransomNote)
        freq_note = {}
        freq_mag = {}

        for c in ransomNote:
            freq_note[c] = freq_note.get(c, 0) + 1
        
        for c in magazine:
            freq_mag[c] = freq_mag.get(c, 0) + 1

        
        for c in ransom_set:
            if(freq_note.get(c,0) > freq_mag.get(c,0)):
                return False
        
        return True