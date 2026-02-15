Salary=int(input("ENTER YOUR SALARY"))
if Salary>=100000:
    print("Your Salary is",Salary)
    print("TAX is ",Salary*5/100)
    print("NET SALARY IS ",Salary-Salary*5/100)
    
elif 100000>Salary>=80000:
    print("Your Salary is",Salary)
    print("TAX is ",Salary*3/100)
    print("NET SALARY IS ",Salary-Salary*3/100)
    
else:
    print("NO TAX ")
    print("YOUR SALARY",Salary)