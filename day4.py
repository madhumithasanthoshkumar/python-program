'''
def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    list1=list(s).sort()
    list2=list(t).sort()
    if list1==list2:
        return True
    else:
        return False
s = input("Enter first string: ")
t = input("Enter second string: ")
print(isAnagram(s, t))
def climbStairs(n):
    if n<=2:
        return n  
    first=1
    second=2
    for i in range(3,n+1):
        third=first+second
        first=second
        second=third
    return second
n=int(input("Enter number of stairs: "))
result=climbStairs(n)
print("Number of ways to climb", n, "stairs is:", result)
n=int(input("Enter number:"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("Fizz and Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
n=int(input("Enter a number :"))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")
def majorityElement(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for key in count:
        if count[key] > len(nums) // 2:
            return key
nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = majorityElement(nums)
print("Majority Element is:", result)
nums1=[1,2,3,4,5]
nums2=[4,6,7,9,2,5]
result=list(set(nums1) & set(nums2))
print("Intersection:", result)
list1 = [1, 2, 4, 5, 7]
list2 = [1, 6, 7, 9, 3]
res = []
for num in list1:
    if num not in res:
        res.append(num)
for num in list2:
    if num not in res:
        res.append(num)
print("Union:", res)
list1 = list(map(int, input("Enter first sorted list: ").split()))
list2 = list(map(int, input("Enter second sorted list: ").split()))
merged = []
i = 0
j = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1
while i < len(list1):
    merged.append(list1[i])
    i += 1
while j < len(list2):
    merged.append(list2[j])
    j += 1
print("Merged List:", merged)
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
i = m - 1
j = n - 1
k = m + n - 1
while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1
print("Merged Array:", nums1)
strs = ["flower", "flow", "flight"]
if len(strs) == 0:
    print("Longest Common Prefix:", "")
else:
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                break
    print("Longest Common Prefix:", prefix)
arr=['h','e','l','l','o']
print(arr[::-1])
arr = ['h','e','l','l','o']
print(reversed(arr))
arr = ['h','e','l','l','o']
i = 0
j = len(arr) - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
print("Reversed list:", arr)
nums = [4, 1, 2, 1, 2]
for num in nums:
    if nums.count(num) == 1:
        print("Single number is:", num)
arr = [1,2,3,0,2,0,3,0]
index = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[index], arr[i] = arr[i], arr[index]
        index += 1
print("After moving zeros:", arr)'''







def maxprofit(prices):
    max_profit=0
    buy_day=0
    sell_day=0
    for i in range (len(prices)):
        for j in range(i+1,len(prices)):
            profit=prices[j]-prices[i]
            if profit>max_profit:
                max_profit=profit
                buy_day=i
                sell_day=j
    return max_profit,buy_day,sell_day
prices=list(map(int,input("Enter the stock prices separated by space:").split()))
profit,buy_day,sell_day=maxprofit(prices)
if profit>0:
    print("Buy on day:",buy_day+1,"at price",prices[buy_day])
    print("Sell on day:",sell_day+1,"at price",prices[sell_day])
    print("Maximum profit",profit)
else:
    print("No profit posiible")



        