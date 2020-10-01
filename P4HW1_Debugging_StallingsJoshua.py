# Student Grade program
# 1OCT2020
# P4HW1_Debugging
#Stallings, Joshua


def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70

    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score < A_score:
            print('Your grade is: B')
    elif score >= C_score < B_score:
        print('Your grade is: C')
    else:
        print('Your grade is: F') 







# program start
main()
