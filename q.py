#question-1
#develop a cpp program to input item number,item price,discount,and quantity
#display the total amount


item_no=input("Enter the item number: ")
item_price=input("Enter the item price: ")
discount=input("Enter the dicount (0.10 for 10%): ")
quantity=input("Quantity: ")

total=float(item_price)*float(quantity)
net_total=total-total*float(discount)

print("Your Total is: "+str(net_total))

#question-2
#develop a py program to input the product code, product price and the quantity and output the total price
#if product code =1  --> 3% discount
#if product code =2 --> 5% discount

p_code=float(input("your product code: "))
p_price=float(input("your product price: "))
quantity=float(input("Quantity of the product: "))

total=p_price*quantity
if p_code==1:
    print(f'your total amount is: {total-total*3/100}')

elif p_code==2:
    print(f'your total amount is: {total-total*5/100}')
else:
    print("invalid product code!")

#question-3
#in an online ordering system , costomers have been catagorized into 'regular' and "non-regular" to allow the discount. 
#inputs==> customer no,password,and the order value
#if customer number
    #even number--> regular 10% discount
    #odd number --> non regular 5% discount
#display the customer number,customer type,net value of the order

password=input("Password: ")
customer_no=int(input("Customer Number: "))
order_value=float(input("order value: "))

mod=customer_no%2
if mod==0:
    customer_type="Regular"
    discount=0.1

elif mod==1:
    customer_type="NON-Regular"
    discount=0.05

else:
    print("invalid customer Number!")

print(f'customer Number: {customer_no}\ncustomer type: {customer_type}\nNet value: {order_value-order_value*discount}')


#question-4
#develop a programm to input a number and display its a positive or negative number or zero
num=float(input("Enter a number: "))

if num==0:
    print("its zero !")
elif num>0:
    print("its a positive number ")
else:
    print("its a negative number")

#print hello in count 1-5
i=1
while i<=5:
    print("hello")
    i+=1

#question-5
#input 10 numbers calculate the total and display the total
total=0
num=0
i=1
while i<=10:
    num=int(input("enter number:"))
    total=total+num
    i+=1
print(total)

#question-6
#input 10 numbers and list the positive,negative numbers separatly and display them 
pnums =[]
nnums=[]
for i in range(0,10):
    num=int(input(f'enter number {i+1}: '))
    if num>0:
        pnums.append(num)
    else:
        nnums.append(num)
        
print(f'entered posituve numbers:{pnums}')
print(f'entered negative numbers:{nnums}')