'''def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=10
for i in range(n):
        print(fib(i))
def trib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return trib(n-1) + trib(n-2) + trib(n-3)
n = 10
for i in range(n):
    print(trib(i))
#list
list=[1,2,3,4,5]
#index
print(list[2])
#slicing
print(list[:])
#list operators
#concatenation
list2=[2,5,5,6,7,8,9]
print(list+list2)
#repetition
a=['hi']
print(a*3)
#membership
print(10 in list)
print(1 not in list)
print(2 in list)
#comparison
print(list<list2)
print(list>list)
print(list==list2)
print(list!=list2)
#list methods
list3=[3,4,1,5,2,7,4,8,4]
print(list)
list.append(21)
print(list)
list.pop
print(list)
list.insert(1,5)
print(list)
list.remove(5)
print(list)
list.reverse()
print(list)
list.extend(list2)
print(list)
list2.count(5)
print(list2)
list.index(4)
print(list)
list3.sort()
print(list3)
list.clear()
print(list)
list=[1,2,3,4,5]
for i in range(len(list)):
        print(list[i]*2,end=" ")
#lambda
num=[1,2,3,4,5]
multi=list(map(lambda x:x*2,num))
print(multi)
def func(x):
    return x*2
result=list(map(func,num))
print(result)
num=[1,2,3,4,5,6,7,8,8,5,4,66,44,79]
multi=list(filter(lambda x:x%2==0,num))
print(multi)
num=[1,2,3,4,5,6,7,8,8,5,4,66,44,79]
def func(x):
    if x%2==0:
     return x
result=list(filter(func,num))
print(result)
from functools import reduce
num=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,num))
odd=list(filter(lambda x:x%2!=0,num))
add_even=reduce(lambda x,y:x+y,even)
add_odd=reduce(lambda x,y:x+y,odd)
print(add_even)
print(add_odd)
word=str(input("Enter word:"))
if word==word[::-1]:
    print("Its palindrome")
else:
    print("Its not palindrome")
word=str(input("Enter word:"))
rev=""
for i in word:
    rev=i+rev
if word==rev:
    print("Its palindrome")
else:
    print("Its not palindrome")
num=int(input("Enter number:"))
original=num
res=0
while num>0:
    digit=num%10
    res=res*10+digit
    num=num//10
if original==res:
    print("Its palindrome")
else:
    print("Its not palindrome")'''


