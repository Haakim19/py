'''
Question 01
Write a program in python to calculate the sum of the series (1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n).

Sample Output:
Input the value for nth term: 5
1*1 = 1
2*2 = 4
3*3 = 9
4*4 = 16
5*5 = 25
The sum of the above series is: 55

'''
'''number=int(input("Enter a number to be squar value:"))
total=0
for i in range(0,number+1):
    
    print(int(i)**2)
    total+=int(i)**2
print("Sum of the series:",total)'''





'''
Question 02
RTX Company decided to give awards to senior employees. Write a program to accept employee number,
designation and years of working of 50 employees. Display the employee number of employees who
have at least 10 years of working experience with RTX company.

'''


'''for i in range(1,51):
    employee_number=int(input("Employee Number:"))
    designation=(input("Designation:"))
    years_of_working=int(input("Years of working:"))
    
    if years_of_working>=10:
        print(f"Employee number {employee_number} is working {years_of_working} years with RTX company as a {designation}.")'''
   
   




'''
Question 03
A program is needed to compute the total sales at a supermarket during a specified hour. It will
account for an average of 20 customers visiting the supermarket and will offer discounts based
on the following criteria.
bill amount>=15000--->7%
bill amount>=10000--->5%
bill amount<5000--->nop
'''
net_bill=0
bill_amount=0
grand_bill=0

for i in range(1,3):
    bill_amount=int(input("your bill amount: "))
    if bill_amount>=15000:
        net_bill=bill_amount-bill_amount*0.07
    elif bill_amount>=10000:
        net_bill=bill_amount-bill_amount*0.05
    else:
        net_bill=bill_amount
    print(f'Your Bill Amount is: {net_bill}.')
    grand_bill+=net_bill
print(f'Total Sales at that time:{grand_bill}.')




'''
Question 4
A program is needed to read number of electricity units used by the customer. It's needed to
calculate and display the electricity bill based on following criteria.
Units used (u)Per unit Charge
u>=100 = 30
100>u>=50 = 20
u<50 = 10
*If the total bill is greater than 5000, 5% from the bill will be added to the bill as a tax.
*If the total bill is less than 500, 5% from the bill will be deducted as a discount.

'''
''''bill=0

Number_of_units=int(input("Number of units used: "))
if Number_of_units>=100:
    bill=Number_of_units*30
elif Number_of_units>=50 and Number_of_units<100:
    bill=Number_of_units*20
elif Number_of_units<50:
    bill=Number_of_units*10
if bill>5000:
    bill+=(bill*0.05)
elif bill<500:
    bill-=(bill*0.05)

print(f'Your Bill is:{bill}')'''