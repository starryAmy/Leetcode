class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # handle all strings to make sure only alpha
        # create two hash tables
        # put two strings into hash table
        hashTable1 = {}
        for i in s:
            if i in hashTable1:
                hashTable1[i] += 1
            else:
                hashTable1[i] = 0
        hashTable2 = {}
        for i in t:
            if i in hashTable2:
                hashTable2[i] += 1
            else:
                hashTable2[i] = 0
        if hashTable1 == hashTable2:
            return True
        return False
