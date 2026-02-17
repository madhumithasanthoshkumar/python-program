'''apple_fruit=10
print(apple_fruit)
# Data type
int float str bool
birthyear=int(input("Birth year"))
now=2026
age=now-birthyear
print("Age",age)
current_age=int(input("current age"))
maximum_age=int(input("maximum age"))
Lifetime_Total_days=(maximum_age-current_age)*365
one_day=int(input("Food cost per day"))
print("Lifetime expence",Lifetime_Total_days*one_day)
current_age=int(input("current age"))
maximum_age=int(input("maximum age"))
Lifetime_Total_days=(maximum_age-current_age)*365
one_day=int(input("Water consumption in litre"))
living_days=Lifetime_Total_days*one_day
print("You will drink",living_days,"litres of water by age",maximum_age)
total_trip_distance=int(input("Total_trip_distance in km:"))
mileage=int(input("Your car mileage per litre:"))
petrol_price=int(input("Petrol price:"))
needed_fuel=(total_trip_distance/mileage)
fuel_cost=needed_fuel*petrol_price
print("Total fuel cost of your trip is",fuel_cost)
daily_data_usage=int(input("Enter your daily data usage in GB:"))
number_days_in_month=30
total_amount_of_data_usage=daily_data_usage*number_days_in_month
print("you used ",total_amount_of_data_usage,"GB data per month")
current_age=int(input("current age"))
life_days=current_age*365
print("You lived",life_days,"days")
original_price_of_product=int(input("Original price of product"))
discount_percentage=int(input("Discount Percentage"))
discount_amount=(original_price_of_product/discount_percentage)
after_discount=original_price_of_product-discount_amount
print("Final price After discount",after_discount)
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
if num1==num2:
    print(num1,"is equal to",num2)
elif num1>num2:
    print(num1,"is greater than",num2)
else:
    print(num1,"is less than",num2)
mark=int(input("Enter your mark:"))
if mark==100:
    print("O Grade")
elif mark>90:
    print("A Grade")
elif mark>80 and mark<90:
    print("B Grade")
elif mark>70 and mark<80:
    print("C Grade")
elif mark<60 and mark>35:
    print("D Grade")
else:
    print("Fail")
product_purchased_price=int(input("Product purchased price"))
product_sell_price=int(input("Product selled price"))
profit=product_sell_price-product_purchased_price
loss=product_purchased_price-product_sell_price
if product_purchased_price>product_sell_price:
    print("Loss",loss)
elif product_purchased_price==product_sell_price:
    print("No profit,No loss")
else:
    print("Profit",profit)
letter=input("Enter letter:")
type_of_letter=letter.isdigit()
if type_of_letter==True:
    print("It is not an alphabet")
vowels=['A','E','I','O','U','a','e','i','o','u']
consonant=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for j in range(len(consonant)):
    if letter==consonant[j]:
        print("Consonant")
for i in range (len(vowels)):
    if letter==vowels[i]:
        print("It is vowel")'''
