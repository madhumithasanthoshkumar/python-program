'''student_type=int(input("Enter 1 for hostellar Enter 2 for Dayscholar"))
if student_type==1:
    hostel_fee=float(input("Enter your hostel fees"))
    tuition_fee=float(input("Enter your tuition fees"))
    print("Total amount you want to pay",hostel_fee+tuition_fee)
elif student_type==2:
    tuition_fee=float(input("Enter your tuition fees"))
    bus_fee=float(input("Enter your bus fees"))
    print("Total amount you want to pay",bus_fee+tuition_fee)
else:
    print("Invalid input")
bank_balance=5054
withdrawal=int(input("WITHDRAWAL AMOUNT:"))
limit=10000
if withdrawal>bank_balance:
    print("INSUFFICIENT BANK BALANCE")
elif withdrawal>limit:
    print("LIMIT EXCEED")
else:
    print("BALANCE :",bank_balance-withdrawal)
bank_balance=15000
pin=2345
user_pin=int(input("Enter pin:"))
limit=10000
if pin==user_pin:
    withdrawal=int(input("Enter withdrawal amount:"))
    if withdrawal>bank_balance:
      print("INSUFFICIENT BANK BALANCE")
    elif withdrawal<=0 :
      print("Invalid amount")
    elif withdrawal>limit:
      print("LIMIT EXCEED")
    else:
      print("BALANCE :",bank_balance-withdrawal)
      print("WITHDRAWAL SUCCESSFULL")
else:
    print("Wrong pin")
age=int(input("Enter your age:"))
morning_discount=50
show_time=int(input("Enter 1 for morning,Enter 2 for evening:"))
senior_ticket=200
child_ticket=150
adult_ticket=250
if show_time==1:
    if age<5:
      print("Free entry")
    elif age>=5 and age<=17:
      print("Child ticket")
      print("Your ticket price is",child_ticket-morning_discount)
    elif age>17 and age<=50:
      print("Adult ticket")
      print("Your ticket price is",adult_ticket-morning_discount)
    elif age>50 and age<60:
      print("Senior citizon")
      print("Your ticket price is",senior_ticket-morning_discount)
    else:
       print("You won 30% discount")
       print("Your ticket price is",adult_ticket-75-50)

else:
  if age<5:
      print("Free entry")
  elif age>=5 and age<=17:
      print("Child ticket")
      print("Your ticket price is",child_ticket)
  elif age>17 and age<=50:
      print("Adult ticket")
      print("Your ticket price is",adult_ticket)
  elif age>50 and age<60:
      print("Senior citizon")
      print("Your ticket price is",senior_ticket)
  else:
       print("You won 30% discount")
       print("Your ticket price is",adult_ticket-75)
 #loop
sum=0
for i in range(1,101):
    if i%2==1:
        print(i)
        sum=sum+i
print("SUM:",sum)
sum=0
for i in range(1,101):
    if i%2==0:
        print(i)
        sum=sum+i
print("SUM:",sum)
for i in range (1,11):
        print(i,"*5=",i*5)
total=0
for i in range (5):
    mark=int(input("Enter your mark:"))
    total=total+mark
print("Total mark:",total)
print("Average mark:",total/5)
for i in range(6):
      print("*"*i)
s=6
for i in range(5):
      s=s-1
      print(s*"*")
sum=0
i=1
while i<101:
        print(i)
        sum=sum+i
        i+=2
print("SUM:",sum)
sum=0
i=2
while i<101:
            print(i)
            sum=sum+i
            i+=2
print("SUM:",sum)
i=1
while i<11:
    print(i,"*5=",i*5)
    i+=1
total=0
i=1
while i<6:
    mark=int(input("Enter your mark:"))
    total=total+mark
    i+=1
print("Total mark:",total)
print("Average mark:",total/5)
i=1
while i<6:
      print("*"*i)
s=6
i=1
while i<6:
      s=s-1
      print(s*"*")
      i+=1'''
total_seat=52
available_seat=10
passenger_need=int(input("How many seats you want:"))
remaining_seat=0
if passenger_need>available_seat:
    print("Only",available_seat,"available")
else:
    for i in range(1,passenger_need+1):
        passenger=str(input("Enter you name:"))
        print("Seat",i,"Booked for",passenger)
        if i==available_seat:
          print("All seats are booked")
        else:
          remaining_seat=available_seat-i
if remaining_seat<available_seat:
    print("Few seats are available also",available_seat-i)








