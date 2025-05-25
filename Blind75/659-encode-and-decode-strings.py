class Solution:
    def encode(self, strs: List[str]) -> str:
        # we want to turn all strings in this array into a single array
        # before each word we have to add the number of length and delimiter
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s): # use i to run through
            j = i # j always starts at the same place
            while j < len(s) and s[j] != "#":
                j += 1
            else:
                length = int(s[i:j])
                word = s[j + 1: j + 1 + length]
                res.append(word)
                i += j + length + 1
        return res
