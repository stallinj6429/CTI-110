inputMonth = input()
inputDay = int(input())
if (inputMonth == 'March') or (inputMonth == 'April') or (inputMonth == 'May') or(inputMonth == 'June'):
    if (inputMonth == 'March') and ((inputDay >= 1) and (inputDay <= 19)):
        print('Winter')
    elif (inputMonth == 'March') and ((inputDay >= 20) and (inputDay <= 30)):
        print('Spring')
    elif (inputMonth == 'April') and ((inputDay >= 1) and (inputDay <= 31)):
          print('Spring')
    elif (inputMonth == 'May') and ((inputDay >= 1) and (inputDay <= 31)):
        print('Spring')
    elif (inputMonth == 'June') and ((inputDay >= 1) and (inputDay <= 20)):
        print('Spring')
    elif (inputMonth == 'June') and ((inputDay >= 21) and (inputDay <= 30)):
        print('Summer')
    else:
        print('Invalid')
elif (inputMonth == 'July') or (inputMonth == 'August') or (inputMonth == 'September'):
    if (inputMonth == 'July') and ((inputDay >= 1) and (inputDay <= 31)):
        print('Summer')
    elif (inputMonth == 'August') and ((inputDay >= 1) and (inputDay <= 31)):
        print('Summer')
    elif (inputMonth == 'September') and ((inputDay >= 1) and (inputDay <= 21)):
        print('Summer')
    elif (inputMonth == 'September') and ((inputDay >= 22) and (inputDay <= 30)):
        print('Autumn')
    else:
        print('Invalid')
elif (inputMonth == 'October') or (inputMonth == 'November') or (inputMonth == 'December'):
    if (inputMonth == 'October') and ((inputDay >= 1) and (inputDay <= 31)):
        print('Autumn')
    elif (inputMonth == 'November') and ((inputDay >= 1) and (inputDay <= 30)):
        print('Autumn')
    elif (inputMonth == 'December') and ((inputDay >= 1) and (inputDay <= 20)):
        print('Autumn')
    elif (inputMonth == 'December') and ((inputDay >= 21) and (inputDay <= 31)):
        print('Winter')
    else:
        print('Invalid')
elif (inputMonth == 'January') or (inputMonth == 'Febuary'):
    if (inputMonth == 'January') and ((inputDay >= 1) and (inputDay <= 31)):
        print('Winter')
    elif (inputMonth == 'Febuary') and ((inputDay >= 1) and (inputDay <= 28)):
        print('Winter')
    else:
        print('Invalid')
else:
    print('Invalid')


    
