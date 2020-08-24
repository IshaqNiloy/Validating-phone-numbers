# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def validating_phone_number(user_input):
    #Checks if all the characters are digits and the string starts with 7, 8 or 9
    if len(re.findall("[0-9]",user_input)) == 10 and re.search("^[789]", user_input):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    for _ in range(int(input())):
        #Calls the function
        validating_phone_number(input())