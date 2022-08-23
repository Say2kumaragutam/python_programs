num=int(input("Enter the number:"))
sum=0
n=len(str(num))
while num!=0:
    digit=num%10
    sum=sum+digit**n
    num=num//10
if num==sum:
    print(num,"is a armstrong number")
else:
    print("Not")
