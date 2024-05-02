def Start_Menu():
    print("*****MENU*****")
    print("1. Check Ballance.")
    print("2. Deposit Money.")
    print("3. Withdraw Money.")
    print("4. Transfer Money.")
    print("5. Logout.")

    option=int(input("Option(1-5):"))
    return 5

def check_ballance(ballance):
    print(f"Your Ballance:{ballance}")


def deposit_money(ballance):
    deposit_amount=float(input("Deposit Amount: "))
    ballance+=deposit_amount
    return ballance
    

def withdraw_money(ballance):
    withdraw_money=float(input("Withdraw Amount: "))
    ballance-=withdraw_money
    return ballance

def transfer_money(ballance):
    transfer_money=float(input("Transfer Amount: "))
    if transfer_money<ballance:
        ballance-=transfer_money
    else:
        print("Not Enough Money.")
    return ballance

def main():
    option = Start_Menu()

    if option==1:
        check_ballance()
    if option==2:
        deposit_money()
    if option==3:
        withdraw_money()
    if option==4:
        transfer_money()
    if option==5:
        print("****THANKYOU FOR BANKING WITH US*****")
        
if __name__ == 'main':
    main()


