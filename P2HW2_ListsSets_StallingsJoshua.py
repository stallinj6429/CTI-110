#CTI-110
#P2HW2 - Lists and sets
#Joshua Stallings
#9/18/2020
#
numList = [] #intiate an emty list
firstNum = int(input('Enter number:' )) #add number to list
numList.append(firstNum)

secondNum = int(input('Enter number:' ))
numList.append(secondNum)

thirdNum = int(input('Enter number:' ))
numList.append(thirdNum)

fourthNum = int(input('Enter number:' ))
numList.append(fourthNum)

fifthNum = int(input('Enter number:' ))
numList.append(fifthNum)

sixthNum = int(input('Enter number:' ))
numList.append(sixthNum)

seventhNum = int(input('Enter number:' ))
numList.append(seventhNum)

eigthNum = int(input('Enter number:' ))
numList.append(eigthNum)

ninthNum = int(input('Enter number:' ))
numList.append(ninthNum)

tenthNum = int(input('Enter number:' ))
numList.append(tenthNum)


print('Min:',min(numList))#print min number
print('Max:',max(numList))#print max number
print('Sum:',sum(numList))#print the sum of the list
print('Average:', sum(numList) / len(numList))#print the average of the list
numSet = set(numList)# convert to set, getting rid of duplicates
print('Set:', sorted(numSet))





    
