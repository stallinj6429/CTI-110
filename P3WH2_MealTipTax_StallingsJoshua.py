#Tip calculator, will calculate the total amount of a meal purchased at a restaurant
#1AUG2020
#CTI-110 P4HW2 - Meal tax tip calculator
#Joshua Stallings
#

foodCost = int(input("Enter food cost: "))
print()
tipPercent = float(input("How much would you like to tip? (15%, 18%, 20%): "))
print()
if (tipPercent == 15.0) or (tipPercent == 18.0) or (tipPercent == 20.0): #compare input amount to allowed tip amounts
    tipPercent = tipPercent / 100 #move decimal to the hundereths place
    taxPercent = 0.06 # autmatically add a 6% sales tax
    tipTotalAmount = tipPercent * foodCost#calculate the tip amount
    taxTotalAmount = taxPercent * foodCost#calculate the tax amount
    totalCost = foodCost + taxTotalAmount + tipTotalAmount #add up all the totals
    print("Calculated tip:", tipTotalAmount) # display totals
    print("Calculated tax:", '{:.2f}'.format(taxTotalAmount))
    print("Total cost including tip and tax:", totalCost)
else:
    print('Error')