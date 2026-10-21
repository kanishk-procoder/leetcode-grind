
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        available = {}

        for c in chars:
            available[c] = available.get(c, 0) + 1

        res = 0

        for word in words:
            needed = {}

            for c in word:
                needed[c] = needed.get(c, 0) + 1

            good = True

            for c, count in needed.items():
                if count > available.get(c, 0):
                    good = False
                    break

            if good:
                res += len(word)

        return res
