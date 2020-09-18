''' Type your code here. '''
milesPerGallon = float(input())
dollarsPerGallon = float(input())
gasCost20 = (20 / milesPerGallon) * dollarsPerGallon
gasCost75 = (75 / milesPerGallon) * dollarsPerGallon
gasCost500 = (500 / milesPerGallon) * dollarsPerGallon


print('{:.2f} {:.2f} {:.2f}'.format(gasCost20, gasCost75, gasCost500))