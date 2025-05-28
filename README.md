## Table of Contents

- [217 - Contains Duplicate](#217---contains-duplicate)
- [242 - Valid Anagram](#242---valid-anagram)
- [1 - Two sum](#1---two-sum)
- [49 - Group Anagram](#49---group-anagram)
- [347 - Top K Frequent Element](#347---top-k-frequent-element)
- [659 - Encode and Decode Strings](#659---encode-and-decode-strings)
- [238 - Product of Array Itself](#238---product-of-array-itself)
- [36 - Valid Sudoku](#36---valid-sudoku)
- [128 - Longest Consecutive Sequence](#128---longest-consecutive-sequence) <br/>
    <br/>
  Two Pointers
- [125 - Valid Palindrome](#125---valid-palindrome)
- [167 - Two Integer Sum II](#167---two-integer-sum-ii)
- [15 - three Sum](#15---three-sum)
- [11 - Container With Most Water](#11---container-with-most-water)  <br/>
 <br/>
  Sliding Window
  
- [121 - Best time to sell and buy stocks](#121---best-time-to-sell-and-buy-stocks)
- [3 - Longest Substring Without Repeating Characters](#3---longest-substring-without-repeating-characters)
- [424 - Longest Repeating Character Replacement](#424---longest-repeating-character-replacement)
- [567 - Permutation in String](#567---permutation-in-string) <br/>
 <br/>
  Stack
  
- [20 - Valid Parentheses](#20---valid-parentheses)
- [155 - Min Stack](#155---min-stack)
- [150 - Evaluate Reverse Polish Calculation](#150---evaluate-reverse-polish-calculation)  <br/>
 <br/>
  Binary Search
  
- [704 - Binary Search](#704---binary-search)
- [153 - Find  Minimum in Sorted Array](#153---find -minimum-in-sorted-array)
- [33 - Search in Sorted Array](#33---search-in-sorted-array)  <br/>
<br/>
  Linked List
  
- [141 - Linked List Cycle](#141---linked-list-cycle)
- [206 - Reversed Linked List](#206---reversed-linked-list)
- [21 - Merge Two Sorted Lists](#21---merge-two-sorted-lists)
- [143 - Reorder List](#143---reorder-list)
- [19 - Remove nth node from the end of list](#19---remove-nth-node-from-the-end-of-list)   <br/>


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
# Two Pointers 
- 看到sorted -> 直覺反應two pointers指針法因為sorted讓排序變得有意義
- 只要你可以明確根據某個條件「排除掉某些不可能是最優解的情況」，就可以用 two pointers。
- 只要左右移動有“明確方向感”，且能剪掉不必要的組合，你就能用 Two Pointers！

## 125 - Valid Palindrome
**brute force** :
- 把array反轉然後比較
- 雖然反轉array的時間複雜度也是O(n)但卻要浪費空間
```python
def isPalindrome(s: str) -> bool:
    # Step 1: Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())

    # Step 2: Reverse the cleaned string
    reversed_str = cleaned[::-1]

    # Step 3: Compare original and reversed
    return cleaned == reversed_str
```
⏳ **time complexity**: O(n) </br>
**Solution**: </br> 
**解題思路** ：取set，因為查找set的時間複雜度是O(1) while 查找array的時間複雜度是O(n)
- 先清理原本的string，只留下數字跟英文字母
- 由兩個指針，一個從左往右移動，一個從右到左移動
⏳ **time complexity**: O(n) </br>
```python
s = "".join(c for c in s if c.isalnum()).lower() # only numbers and english letters will be included
```

## 167 - Two Integer Sum II
**brute force** :
- 跑兩次迴圈相加
⏳ **time complexity**: O(n^2) </br>
**Solution**: </br> 
**解題思路** ：
- 兩個指針，一個往左走一個往右走
- 由相加數跟target比大小去決定要往左走還是往右走
⏳ **time complexity**: O(n) </br>

## 15 - three Sum
**brute force** :
- 先loop外迴圈一次
- 然後裡面再迴圈一次
- 接著裡面再回圈一次
⏳ **time complexity**: O(n^3) </br>
**Solution**: </br> 
**解題思路** ：
- 先sort原本的array
- iterate array，先固定第一個元素，然後對剩下的元素進行指針法
⏳ **time complexity**: O(nlogn)+O(n^2)= O(n^2) </br>

## 11 - Container With Most Water
**brute force** :
- iterate 迴圈 然後裡面再迴圈一次
⏳ **time complexity**: O(n^2) </br>
**Solution**: </br> 
**解題思路** ：
- 由兩個指針，一個從左往右移動，一個從右到左移動
- 因為我們的目標是勁量找到最高的邊，所以比較左指針跟右指針
- 哪個指針指向的邊較短就移動一步，尋找更大的邊
⏳ **time complexity**: O(n) </br>

# Sliding Window
- ✨ Sliding Window 是 Two Pointers 的特化版本：專注在處理「一段連續區間的狀態」

## 121 - Best time to sell and buy stocks
**brute force** :
- 對於每一天 i：當作「買入」的那天
- 嘗試在之後的每一天 j 當作「賣出」的那天
- 計算 prices[j] - prices[i]
- 記錄最大利潤
⏳ **time complexity**: O(n^2) </br>
**Solution**: </br> 
**解題思路** ：
- 兩個指針分別從index = 0, 1開始移動
- 如果右邊的數比較小，就把那天當作left，買入的那一天
- right持續往右
⏳ **time complexity**: O(n) </br>

## 3 - Longest Substring Without Repeating Characters
**brute force** :
- 對於每個起點 i，從 i+1 到結尾的每個 j
- 檢查 s[i:j] 是否有重複字元
- 如果沒有，更新最大長度
```python
def lengthOfLongestSubstring(s):
    max_len = 0
    n = len(s)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len
```
⏳ **time complexity**: O(n^2) </br>
**Solution**: </br> 
**解題思路** ：
- 兩個指針分別從index = 0, 1開始移動
- 如果右指針指向的元素重複，就移動左指針直到沒有重複
- 不然就移動右指針並計算長度
⏳ **time complexity**: O(n) </br>
```python
char.add(s[r]) # add element to set
char.remove(s[l]) # remove element from set
```

## 424 - Longest Repeating Character Replacement
**brute force** :
- 枚舉所有子字串 s[i:j]
- 統計其中出現最多次的字母的次數 max_freq
- 看這段子字串是否能夠在 k 次 replace 內全變成同一個字母：
- (j - i + 1) - max_freq <= k
- 如果可以，更新最大長度
```python
def characterReplacement(s, k):
    max_len = 0
    n = len(s)
    for i in range(n):
        count = [0] * 26
        max_count = 0
        for j in range(i, n):
            idx = ord(s[j]) - ord('A')
            count[idx] += 1
            max_count = max(max_count, count[idx])
            window_len = j - i + 1
            if window_len - max_count <= k:
                max_len = max(max_len, window_len)
    return max_len
```
⏳ **time complexity**: O(n^2) </br>
**Solution**: </br> 
**解題思路** ：Sliding Window
- 兩個指針分別從index = 0, 0開始移動
- 如果不滿足條件，就縮小窗口
- 不然就移動右指針extend the window
⏳ **time complexity**: O(n) </br>
```python
max(item) # where item can be an array
```

## 567 - Permutation in String
**brute force** :
- 產生 s1 的所有 permutation（排列）
- 在 s2 中用 sliding window，逐格比對是否有出現過其中一個 permutation
```python
from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perms = set([''.join(p) for p in permutations(s1)])
        window_len = len(s1)
        for i in range(len(s2) - window_len + 1):
            if s2[i:i+window_len] in perms:
                return True
        return False

```
⏳ **time complexity**: O(n! + m * n) </br>
**Solution**: </br> 
**解題思路** ：Sliding Window
- 先set up 兩個array，array的index是字母的ASC碼，value是出現的次數
- 在比較兩個array，看有多少個match
- 開始兩個指針逐步移動，計算array之中元素的次數
- 同時間要更新是否matches
⏳ **time complexity**: O(m) where m is the bigger length </br>
```python
array2 = [0] * 26 # 一個array裡面26個元素都是0
ord(s1[i]) - ord("a") # 計算ASC碼
```

## 20 - Valid Parentheses
**brute force** :
- 每次都嘗試刪掉所有合法的 pair
- 如果最後整個字串都被「清空」→ 是有效的
- 否則 → 有多餘或錯配的括號
```python
def isValid(s: str) -> bool:
    prev = None
    while s != prev:
        prev = s
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""
```
⏳ **time complexity**: O(n^2) </br>
**Solution**: </br> 
**解題思路** ：使用stack資料結構，後進先出
- 如果屬於前一半的符號，就存進stack
- 如果碰到後一半的，就去比對stack的最後一個
⏳ **time complexity**: O(n) where n is the length </br>
```python
return True if not stack else False # 如果stack是負的，就return True
```

## 155 - Min Stack
**brute force** :
- 如果要查找最小值一定要loop全部
⏳ **time complexity**: O(n) </br>
**Solution**: </br> 
**解題思路** ：使用stack資料結構，後進先出
- 創造兩個stack，一個儲存原本的值，一個儲存到目前為止的最小值
⏳ **time complexity**: O(1) where n is the length </br>
```python
val = val if not self.minStack else min(self.minStack[-1], val) # A if condition else B 為python的三元運算子
```

## 150 - Evaluate Reverse Polish Calculation
**brute force** :
- 從左到右掃描 tokens
- 每當發現一個運算子 + - * /：取出它前面兩個操作數（index i-2, i-1）計算結果
- 將三個 token 位置：[a, b, op] 替換成 result
- 重新從頭開始（因為整個 tokens 變短了）
- 重複這過程直到只剩一個元素
⏳ **time complexity**: O(n^2) 因為每次都要重新建立一個n長度的陣列，建立n次</br>
**Solution**: </br> 
**解題思路** ：使用stack資料結構，後進先出
- 先把數字擺進去stack，碰到計算符號就依序拿出來計算
⏳ **time complexity**: O(n) where n is the length </br>
```python
int(num) # 把num變成integer which means rounded to zero
```

## 704 - Binary Search
**brute force** :
- 從左到右去檢查
⏳ **time complexity**: O(n) 因為每次都要重新建立一個n長度的陣列，建立n次</br>
**Solution**: </br> 
**解題思路** ：
- Binary Search
⏳ **time complexity**: O(logn) where n is the length </br>

## 153 - Find  Minimum in Sorted Array
**brute force** :
- 逐一檢查
⏳ **time complexity**: O(n)</br>
**Solution**: </br> 
**解題思路** ：
-用binary search去檢查中間值
⏳ **time complexity**: O(logn) where n is the length </br>

## 33 - Search in Sorted Array
**brute force** :
- 逐一檢查
⏳ **time complexity**: O(n)</br>
**Solution**: </br> 
**解題思路** ：
-用binary search去檢查中間值
⏳ **time complexity**: O(logn) where n is the length </br>

## 141 - Linked List Cycle
**Solution**: </br> 
**解題思路** ：Linked List
- 用快慢指針法，如果有cycle的話，兩個指針最終一定會重疊
⏳ **time complexity**: O(n) where n is the length 但最重要的是空間複雜度只有O(1)不需要額外的空間去儲存 </br>

## 206 - Reversed Linked List
**Solution**: </br> 
**解題思路** ：Linked List
- 從head開始出發，把head當成curr, 另外還有prev
- 把curr.next存在temp
- 把curr.next改成prev
- prev變成目前的curr
- curr則變成下一個，也就是temp
- 直到curr變成None(while curr:)
- return prev
⏳ **time complexity**: O(n) where n is the length 但最重要的是空間複雜度只有O(1)不需要額外的空間去儲存 </br>

## 21 - Merge Two Sorted Lists
**Solution**: </br> 
**解題思路** ：Linked List
- 先設立一個dummy linked list
- 然後依序比較list1跟list2的value
- 讓dummy接上比較小的
- 一直loop直到list1跟list2有一個變成空的
- 如果還有剩下的，直接接上全部
⏳ **time complexity**: O(n+m) where n, m are the lengths 但最重要的是空間複雜度只有O(1)不需要額外的空間去儲存 </br>
雖然產生了一個新的「合併後的 linked list」，但你並沒有創建任何新的節點，而是重用原本的節點
👉 所以額外空間使用是常數的 → 空間複雜度是 O(1) ✅
```python
dummy = ListNode() # 創造一個linked list叫做dummy
return dummy.next #回傳不能直接回傳dummy因為dummy本身是None，是dummy.next才是整個linked list的開頭
```

## 143 - Reorder List
**Solution**: </br> 
**解題思路** ：Linked List
- 分成三個部分：1) 用快慢指針法找出中間的node 2) 把後半部分的list reverse 3)把前後兩個list合併
```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle one using fast/slow pointers:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next
        slow.next = None # separate the first half from the second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
```
⏳ **time complexity**: O(n+m) where n, m are the lengths 但最重要的是空間複雜度只有O(1)不需要額外的空間去儲存 </br>
雖然產生了一個新的「合併後的 linked list」，但你並沒有創建任何新的節點，而是重用原本的節點
👉 所以額外空間使用是常數的 → 空間複雜度是 O(1) ✅

## 19 - Remove nth node from the end of list
**Solution**: </br> 
**解題思路** ：Linked List
- 分成三個部分：1) 先求出總共有多少個 2)走到那一步的時候就接上別的節點

⏳ **time complexity**: O(n) 但最重要的是空間複雜度只有O(1)不需要額外的空間去儲存 </br>
雖然產生了一個新的「合併後的 linked list」，但你並沒有創建任何新的節點，而是重用原本的節點
👉 所以額外空間使用是常數的 → 空間複雜度是 O(1) ✅
```python
curr = head # otherwise you will move head 要小心不要直接用head去移。不然你就會已經走完整條list
        while curr:
            index += 1
            curr = curr.next
```


