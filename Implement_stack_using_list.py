'''
Steps:-
1. Declare stack variable to store 'list type' values.
2. Define push function.
    Take the user input from user to add element in stack
    and store it into 'element' variable.
    Use append method to add element in stack.
    Print stack
3. Define pop_element function.
    Check if stack is empty or not, using 'if not'.
    Else use pop method to pop element and store values into
    'e' variable.
    Print removed element i.e. 'e'.
    Print stack.
    
4. The "while true" loop in python runs without any
    conditions until the break statement executes inside the loop.
5. Construct switch case statement in which three options to be given
    first for push, second for pop, last for quit.
6. Get the user input converted to integer and store it into 'choice'
    variable.
7. If choice is 1, push fuction will be executed.
8. If choice is 2, pop fuction will be executed.
9. If choice is 3, break statement will be executed.

'''
stack=[]
def push():
    element=input("Enter the element :")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty!")
    else:
        e=stack.pop()
        print("removed element :", e)
        print(stack)

while True:
    print("Select the operation 1.push, 2.pop, 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct operations!")
