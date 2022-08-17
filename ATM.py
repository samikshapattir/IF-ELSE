print("         WELCOME TO PNB BANK    ")
print("         insert your card       ")
language=input ("enter your language")
if language=="hindi" or language=="english":
    print("ok next")
    pin=int(input("enter your pin"))
    if pin>=1000 and pin<9999:
        print("ok next")
        account=input("enter your account")
        if account=="saving"  or account=="current":
            print("ok next")
            transtion=input("which type of transtion you want")
            total=100
            if transtion=="debit":
                debit=int(input("how many"))
                print("your account balance left=",total-debit)
            else:
                if transtion=="credit":
                 credit=int(input("how many"))
                 print("your account balance is=",total+credit)
            recipt=input("do you want recipt<yes/no")
            if recipt=="yes":
                print("wait processing....")
                print("THANKES FOR VISITING...!!")
            else:
                print("OK THANKES FOR VISITING")
                print("select correct language")
        else:
          print("sorry incorrect!!!")
    else:
        print("incorrect pin!!")
else:
    print("select=hindi/english")
            