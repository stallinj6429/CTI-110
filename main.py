current_price = int(input())
last_months_price = int(input())
differenceInPrice = current_price - last_months_price
mortgage = (current_price * 0.051) / 12
''' Type your code here. '''
print("This house is $",current_price,". The change is $",differenceInPrice,"since last month.")
print("The estimated monthly mortgage is $",'{:.2f}'.format(mortgage),'.')