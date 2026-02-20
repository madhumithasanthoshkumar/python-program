'''class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
print("Are trees same?", isSameTree(p, q))
n=4
if n%2 == 0:
    print("Alice wins")
else:
    print("Alice loses")
arr = [1,2,3,1,2,4,5]
duplicate = False
for i in arr:
    if arr.count(i) > 1:
        duplicate = True
        break
print(duplicate)
n = 4
k = 2
result = []
def backtrack(start, path):
    if len(path) == k:
        result.append(path[:])
        return   
    for i in range(start, n + 1):
        path.append(i)
        backtrack(i + 1, path)
        path.pop()
backtrack(1, [])
print(result)
n=int(input("Enter a number:"))
for i in range(1,n):
    sqrt=i*i
    if sqrt==n:
        print(i)
n = int(input("Enter number: "))
if n <= 0:
    print(False)
else:
    while n % 3 == 0:
        n = n // 3 
    print(n == 1)
n = int(input("Enter number: "))
if n <= 0:
    print(False)
else:
    while n % 2== 0:
        n = n // 2
    print(n == 1)
n = int(input("Enter number: "))
if n <= 0:
    print(False)
else:
    while n % 4== 0:
        n = n // 4
    print(n == 1)
class gobika:
    def clg(self,mark):
        if mark>35:
            print("Pass")
        else:
            print("Fail")
result=gobika()
result.clg(70)'''
class Student:
    def __init__(self, temperature):
        self.temperature = temperature
    def convert(self):
        fahrenheit = (self.temperature * 9/5) + 32
        print("Celsius", self.temperature, "to Fahrenheit", fahrenheit)
s = Student(50)
s.convert()        

