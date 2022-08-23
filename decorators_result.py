def decor_result(result_function):
    def distinction(marks):
        for i in marks:
            if i>=80:
                print("Distinction")
        result_function(marks)
    return distinction

@decor_result
def result(marks):
    for m in marks:
        if m>=33:
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")

marks=[70,60,85,64,95]
result(marks)
print(result)

"""
Explanation of this program:-
1. create a function result with marks as an argument.
2. Use for loop to check in every value or traverse through each value of marks
3. apply if condition to check marks is greater than or equal to 33
4. if True, pass keyword is passed
5. if False, else block is checked and returns fail. Also break is passed to terminate the loop.
6. when for block is not satisfied then it will print pass
7. now pass value for marks in form of array
8. call function named result
9. print the result
10.Now we want to create a new function for adding functionality or new features which would not affect the result function
11.create a function named 'decor_result' and pass result_function as an argument
12.under decor_result function create one new function named 'distinction' and also return distinction 
13.pass marks as an argumnet to distinction function
14.for loop to iterate over every item in marks
15.if marks is greater then or equal to 80, print distinction
16.if for loop not satisfied, return result_function(marks)
17.
"""

        
