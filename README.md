## Table of Contents

- [217 - Contains Duplicate](#217---contains-duplicate)
- [242 - Valid Anagram](#242---valid-anagram)
- [1 - Two sum](#1---two-sum)
- [49 - Group Anagram](#49---group-anagram)
- [347 - Top K Frequent Element](#347---top-k-frequent-element)
- [659 - Encode and Decode Strings](#659---encode-and-decode-strings)
- [238 - Product of Array Itself](#238---product-of-array-itself)
- [36 - Valid Sudoku](#36---valid-sudoku)
- [128 - Longest Consecutive Sequence](#128---longest-consecutive-sequence)

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

## 347 - Top K Frequent Element
**brute force** :
- 計算每一個字母出現頻率存成list
- 對list進行排序
- 依照排序取出
⏳ **time complexity**: O(nlogn) </br>
**Solution**: </br> 
**解題思路** ：桶排序(bucket sort)
- 先loop through array 然後計算每個字母的次數存在hash map
- 把hash map的每一個pair取出來(.items())
- 根據freq的數字存進array，freq的index就是頻率，每一個item都是一個存放數字的array
- 從高到低依序取freq array裡的數字
⏳ **time complexity**: O(n * k) </br>
```python
count.get(num, 0) # count是一個hash map，如果沒有count[num]就自動建立count[num] = 0
freq = [[] for i in range(len(array))] # 在freq裡面建立數個array
```

## 659 - Encode and Decode Strings
**Solution**: </br> 
**解題思路** 
- encode就是把每個字串串起來，然後每個字串前面加上字串長度以及#
- decode就是以index i 為基準從0開始跑，index j每次迴圈都跟i一樣的地方開始
- 如果string[j]不是#就往前一格
- 這樣string[i:j]取出來的就是字串長度
- 再取出j後面長度為string[i:j]的單字並且append到答案裡
⏳ **time complexity**: O(n) </br>

## 238 - Product of Array Itself
**brute force** :
- 對於 nums 中的每一個元素，重新遍歷整個陣列，把除了自己以外的所有數字乘起來。
- 
⏳ **time complexity**: O(n^2) </br>
**Solution**: </br> 
**解題思路** 
- 有兩個array分別是prefix跟suffix
- index i 從 0 開始loop，分別把乘積存入array
- 把其中一個array倒過來
- 兩個array的值相乘得出結果
⏳ **time complexity**: O(n) </br>
```python
reversed_suffix = suffix[::-1] # 把suffix這個array倒過來排序
```

## 36 - Valid Sudoku
**brute force** :
- 先檢查rows在檢查cols最後檢查square
```python
def isValidSudoku(board):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == ".":
                continue
            
            # 檢查列
            for col in range(9):
                if col != j and board[i][col] == num:
                    return False

            # 檢查欄
            for row in range(9):
                if row != i and board[row][j] == num:
                    return False

            # 檢查 3x3 區塊
            box_row_start = 3 * (i // 3)
            box_col_start = 3 * (j // 3)
            for row in range(box_row_start, box_row_start + 3):
                for col in range(box_col_start, box_col_start + 3):
                    if (row != i or col != j) and board[row][col] == num:
                        return False
                        
    return True

```
⏳ **time complexity**: O(1)(因為永遠都是9x9)  </br>
**Solution**: </br> 
**解題思路** 
- 建立三個dict，其中每一個key都對應一個set
- squares的dict的key為(rows/3, cols/3)
- iterate through the board，檢查cols/rows/squares裡的set是否包含這個
⏳ **time complexity**: O(1)(因為永遠都是9x9) </br>
```python
cols = collections.defaultdict(set) # 創建一個默認字典，默認值為集合
cols[c].add(board[r][c]) # 在cols[c]這個集合裡新增一個值
```

## 128 - Longest Consecutive Sequence
**brute force** :
- 查找每一個num並檢查num+1是否存在array
```python
def longestConsecutive(nums):
    longest = 0
    for num in nums:
        current = num
        length = 1
        while current + 1 in nums:  # O(n) 查找
            current += 1
            length += 1
        longest = max(longest, length)
    return longest

```
⏳ **time complexity**: O(n²) </br>
**Solution**: </br> 
**解題思路** ：取set，因為查找set的時間複雜度是O(1) while 查找array的時間複雜度是O(n)
- 先把原本的array取set（這樣查找才是O(1))
- iterate原本的array
- 每一個array item先檢查是否是consequence的開頭
- 如果是的話依序往前加1，檢查其數是否在set裡
⏳ **time complexity**: O(n) </br>
```python
nums_set = set(nums) # no duplicate numbers
```

