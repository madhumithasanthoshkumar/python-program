'''def generate(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
if __name__ == "__main__":
    numRows = int(input("Enter number of rows: "))
    result = generate(numRows)
    print("Pascal's Triangle:")
    for row in result:
        print(row)
def getRow(rowIndex):
    row = [1] * (rowIndex + 1)
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
    return row
if __name__ == "__main__":
    rowIndex = int(input("Enter row index: "))
    result = getRow(rowIndex)
    print("Pascal Row:", result)
def addBinary(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result = str(total % 2) + result
        carry = total // 2
    return result
if __name__ == "__main__":
    a = input("Enter first binary number: ")
    b = input("Enter second binary number: ")
    print("Binary Sum:", addBinary(a, b))
def detectCapitalUse(word):
    if word.isupper():
        return True
    if word.islower():
        return True
    if word[0].isupper() and word[1:].islower():
        return True
    return False
if __name__ == "__main__":
    word = input("Enter a word: ")
    print("Correct Capital Usage:", detectCapitalUse(word))
def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total
if __name__ == "__main__":
    s = input("Enter Roman number: ")
    print("Integer value:", romanToInt(s))
def maximumProduct(nums):
    nums.sort()
    product1 = nums[-1] * nums[-2] * nums[-3]
    product2 = nums[0] * nums[1] * nums[-1] 
    return max(product1, product2)
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Maximum Product:", maximumProduct(nums))
def removeDuplicates(nums):
    nums.sort()  
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    k = removeDuplicates(nums)
    print("Number of unique elements:", k)
    print("Modified array:", nums[:k])
def removeDuplicates(nums):
    unique = []
    for num in nums:
        if nums.count(num) == 1:
            unique.append(num)
        elif num not in unique:
            unique.append(num)
    return unique
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    result = removeDuplicates(nums)
    print("After removing duplicates:", result)'''
word = input("Enter a word: ")
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
is_upper = True
for ch in word:
    if ch not in capital:
        is_upper = False
        break
if is_upper==True:
    print("UPPERCASE")
else:
    print("Not UPPERCASE")
    