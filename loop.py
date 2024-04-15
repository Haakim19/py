#creat a program prints 1-100 exlude number that devided by 3 and 5

#for only single devistion to exclude
for a in range(1, 101):
    if a % 5 != 0:
        print(a)
for i in range(1,101):
    if i%3 !=0:
       if i%5 !=0:
            print(i)
#or we can use like this       
for i in range(1, 101):
    if not (i % 3 == 0 or i % 5 == 0):
        print(i)      
# in while loop like this
i = 1

while i <= 100:
    if not(i % 3 == 0 or i % 5 == 0):
        print(i)
    i += 1
