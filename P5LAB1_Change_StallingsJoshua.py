'''
Created on Oct 22, 2020

@author: jdsta
'''
def exactChange(total):
    #calculates the exact change for a user entered amount of dollars, value is a float
    
    
    if total <= 0: # if total is 0 then say no change
        print('No change.')
    else:
        dollars = total // 1 # gets the dollar amount
        dollars = int(dollars) # converts float to int
        total = total - dollars # substract dollars from the total amount
        total = round(total, 2) # round up to the nearest whole cent (i dont know why its off by a fraction)
        total = total * 100 # move two decimal places
        totalWithNoDollars = int(total) # convert float to int
        quarters = totalWithNoDollars // 25 # gets the amount of quarters
        quarterTotal = quarters * 25 # get to total amount quarters are worth
        totalWithNoDollars = totalWithNoDollars - quarterTotal # subtract the amount in quarters from total
        dimes = totalWithNoDollars // 10 # gets the amount of dimes
        dimesTotal = dimes * 10 # gets the total amount dimes are worth
        totalWithNoDollars = totalWithNoDollars - dimesTotal # subtract dimes worth from total
        nickles = totalWithNoDollars // 5 # get the number of nickels
        nicklesTotal = nickles * 5 # get the total amount of nickel worth
        totalWithNoDollars = totalWithNoDollars - nicklesTotal # substract nickel worth from total
        pennies = totalWithNoDollars // 1 # get the amount of pennies
        return dollars, quarters, dimes, nickles, pennies # put values into a tuple
def printDollars(dollars): # print dollars
    if dollars > 1:
        print(dollars, 'dollars')
    elif dollars == 0:
        pass
    else:
        print(dollars, 'dollar')   
def printQuarters(quarters): # print quarters
    if quarters > 1:
        print(quarters, 'quarters')
    elif quarters == 0:
        pass
    else:
        print(quarters, 'quarter')
def printDimes(dimes): # print dimes
    if dimes > 1:
        print(dimes, 'dimes')
    elif dimes == 0:
        pass
    else:
        print(dimes, 'dime')
def printNickles(nickles): # print nickels
    if nickles > 1:
        print(nickles, 'nickels')
    elif nickles == 0:
        pass
    else:
        print(nickles, 'nickel')
def printPennies(pennies): # print pennies
    if pennies > 1:
        print(pennies, 'pennies')
    elif pennies == 0:
        pass
    else:
        print(pennies, 'penny')
input_val = float(input())   # get user input  
dollars, quarters, dimes, nickles, pennies = exactChange(input_val)   # pass values from exact change fucntion to local variables
printDollars(dollars) # passing local variables to print functions
printQuarters(quarters)
printDimes(dimes)
printNickles(nickles)
printPennies(pennies)


        