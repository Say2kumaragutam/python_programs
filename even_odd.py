n=int(input("Enter the number :"))
result = "Leap year" if n%400==0 else "Leap year" if n%4==0 and n%100==100 else "Not a leap year"
print(result)
