'''
Python Program To Find out Given String or Number is Palindrome or Not.
'''
string=input("Enter the string :") # to accept user input
if string==string[::-1]:           # if string and reverse of string is true 
    print("Palindrome")            # prints palindrome number
else:                              # else statement
    print("Not Palindrome")        # prints not palindrome
