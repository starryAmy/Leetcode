class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        array1 = [0] * 26
        array2 = [0] * 26
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            array1[ord(s1[i]) - ord("a")] += 1 # store value
            array2[ord(s2[i]) - ord("a")] += 1
        matches = 0
        for i in range(len(array1)): # check how many matches
            if array1[i] == array2[i]:
                matches += 1
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26: return True
            index = ord(s2[i]) - ord("a")
            array2[index] += 1
            if array1[index] == array2[index]: # included new word and it matches
                matches += 1
            elif array1[index] + 1 == array2[index]: # included new word but it doesnt match
                matches -= 1
            index = ord(s2[l]) - ord("a")
            array2[index] -= 1
            if array1[index] == array2[index]: # included new word and it matches
                matches += 1
            elif array1[index] - 1 == array2[index]: # included new word but it doesnt match
                matches -= 1
            l += 1
        return matches == 26 # haven't checked the last window
