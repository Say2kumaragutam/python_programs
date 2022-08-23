''' Queue implementation using list
'''
queue=[]
def enqueue():
    element=input("Enter the element :")
    queue.append(element)
    print(element,"is added to queue")

def dequeue():
    if not queue:
        print("Queue is empty !")
    else:
        e=queue.pop(0)
        print("Reversed element :",e)

def display():
    print(queue)

while True:
    print("Select the operation 1.enquque 2,dequeue 3.display 4.quit")
    choice=int(input("Enter the operation :"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("ENter the valid choice")
