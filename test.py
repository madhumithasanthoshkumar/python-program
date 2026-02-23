#Fizz Buzz
num=int(input("Enter a number: "))
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#valid anagram
string_one=str(input("Enter word1:"))
string_two=str(input("Enter word2:"))
if len(string_one)==len(string_two):
    list1=list(string_one)
    list2=list(string_two)
    list1.sort()
    list2.sort()
    if list1==list2:
        print("It is valid anagram")
    else:
        print("Its not an anagram")
else:
    print("Its not an anagram")

#Best time to buy and sell stock

def majorityprofit(prices):
    majority_profit=0
    buy_day=0
    sell_day=0
    for i in range (len(prices)):
        for j in range(i+1,len(prices)):
            profit=prices[j]-prices[i]
            if profit>majority_profit:
                majority_profit=profit
                buy_day=i
                sell_day=j
    return majority_profit,buy_day,sell_day
prices=list(map(int,input("Enter the stock prices separated by space:").split()))
profit,buy_day,sell_day=majorityprofit(prices)
if profit>0:
    print("Buy on day:",buy_day+1,"at price",prices[buy_day])
    print("Sell on day:",sell_day+1,"at price",prices[sell_day])
    print("Maximum profit",profit)
else:
    print("No profit posiible")
