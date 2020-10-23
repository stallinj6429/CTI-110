def miles_to_laps(miles):
    laps = miles * 4
    return laps

if __name__ == '__main__':
    userMiles = float(input())
    print('{:.2f}'.format(miles_to_laps(userMiles)))