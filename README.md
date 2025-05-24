## 217 - Contains Duplicate
**brute force** : run each nums in num and then run through the rest nums and compare </br>
⏳ ** time complexity**: O(n^2) </br>
**Solution**: set up a new empty hash table -> run through each num -> if num is already in hash table, return True -> else, add the number to hash table</br>
⏳** time complexity**: O(n)
