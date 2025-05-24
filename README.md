## Table of Contents

- [217 - Contains Duplicate](#217---contains-duplicate)
- [242 - Valid Anagram](#242---valid-anagram)
- [1 - Two sum](#1---two-sum)
- [49 - Group Anagram](#49---group-anagram)

## 217 - Contains Duplicate
**brute force** : run each nums in num and then run through the rest nums and compare </br>
⏳ **time complexity**: O(n^2) </br>
**Solution**: </br> 
set up a new empty hash table -> run through each num -> if num is already in hash table, return True -> else, add the number to hash table</br>
⏳ **time complexity**: O(n)

```python
# 取得所有 keys
print(person.keys())
# 取得所有 values
print(person.values())
# 取得所有項目 (key, value) 組
print(person.items())
# 清空字典
person.clear()
# 用 pop 同時拿到被刪的值
removed_value = person.pop("city")
# 增加 city
person["city"] = "Tokyo"
```

## 242 - Valid Anagram
**brute force** : sorted out two arrays and compare </br>
⏳ **time complexity**: O(nlogn) </br>
```python
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```
**Solution**: </br> 
- **Check length:** If the lengths of `s` and `t` are different, return `False` immediately.
- **Count characters in `s`:** Create a hash map (dictionary) to count how many times each character appears in `s`.
- **Subtract counts using `t`:** Loop through each character in `t` and subtract 1 from the corresponding count in the hash map.
- **Final check:** If any value in the hash map is not zero, return `False`. Otherwise, return `True`.
  
⏳ **time complexity**: O(n)

```python
sorted(array) # return a new sorted array or string
sorted(nums, reverse=True)  # 👉 [9, 5, 2, 1]
nums.sort() # 會直接修改原本的陣列，不會回傳任何陣列
```
## 1 - Two sum
**brute force** : run through the array and check the sum </br>
⏳ **time complexity**: O(n^2) </br>
**Solution**: </br> 
- **Check the difference**: run through the array and check the difference
- **Store in the table**: if the diff in hash table, return the indices. Else, store the diff in the hash table

## 49 - Group Anagram
**brute force** :
- 建立一個 groups 陣列，每一組是 anagram 群。
- 遍歷每個字 word，檢查是否能放進某一組（比對是否為 anagram）。
- 如果找不到，就新開一組。
⏳ **time complexity**: O(n²·klogk) </br>
**Solution**: </br> 
**解題思路** ：對參數進行迴圈，每一個字的array index當成字母的順序
- 先loop through array
- 每一個string在loop through，然後計算每一個字母的數量存成array
- 把array轉換成tuple存到result hash map
- return hash map中的values
⏳ **time complexity**: O(n * k) </br>
```python
ord(s) - ord("a") # ord()是轉換字母到ASCII碼
tuple(word) # 可以把array轉化成tuple，就可以當成hash map裡的key
```
