from ast import Store
from re import A
# carlos neyoy
#c129 
#2-27-2024

#part 1 of the lab
myAge = 32
yourAge = 18
myNumber = 81 
yourNumber = 17
votingAge = 18
# first set of conditions given
if myAge == 31 and yourAge < myAge :
    print("my age is 31 and your age is less than that")
elif myAge <= 35 and myAge >= 32 :
    print("my age is between 32 and 35")
elif yourAge == votingAge or yourAge > votingAge:
    print("you can vote")

# second set of conditions given 
if myAge == 31 and yourAge < myAge :
    print("my age is 31 and your age is less than that")
else :
    print("our ages do not qualify")
if myAge <= 35 and myAge >= 32 :
    print("my age is between 32 and 35")
else :
    print("our ages do not qualify")
if yourAge == votingAge or yourAge > votingAge:
    print("you can vote")
else :
    print("you cannot vote")
if myNumber == 83 or yourNumber == 83 :
    print("one of our numbers is 83")
else :
    print("83 is not our numbers")

#part 2 of the lab
print("this is part 2 of the lab")

monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 #percent of sales increase 
prompt = "what was the sales total" # prompt will be a string literal

#this code gets the monthly sales 
print("what was the monthly sale total")
monthlySales =float(input(prompt))

#this block of code determines the storeAmount bonus 
if monthlySales >= 110000 :
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
     storeAmount = 4000 
elif monthlySales >= 80000:
    storeAmount = 3000
else :
    storeAmount = 0

print("what was the sales increase")
salesIncrease = float(input())
salesIncrease = salesIncrease/100
# this block of code determines employee bonus amount 
if salesIncrease >= 0.05:  
    empAmount = 75 
elif salesIncrease >= 0.04 :
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0
# this block of code prints out to the user the store bonus and employee bonus after calculation
if storeAmount == 6000 and empAmount == 75:
    print("the store bonus is ", "$",storeAmount)
    print("the employee bonus amount is", "$",empAmount)
    print("Congrats! You have reached the highest bonus amounts possible!")
else :
     print("the store bonus is ", "$",storeAmount)
     print("the employee bonus amount is", "$",empAmount)

