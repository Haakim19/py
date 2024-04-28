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
number=int(input("Enter a number to be squar value:"))
total=0
for i in range(0,number+1):
    
    print(int(i)**2)
    total+=int(i)**2
print("Sum of the series:",total)
