first_name=input("enter your first name")
if first_name>"a" and  first_name<"z" or first_name>"A" and first_name>"Z":
    print("next")
    last_name=input("enter your last name")
    if last_name>"a" and  last_name<"z" or last_name>"A" and last_name>"Z":
        print("next")
        mob=input("enter your mobile number")
        if len(mob)>=10:
            print("next")
            age=input("enter your age")
            if age>="18":
                print("ok you can login!!!!")
                print("a OTP has been sent to you")
                otp=input("enter your otp")
                if len (otp)==6 or len (otp)==4:
                    print("correct!")
                    gender=input("enter your gender")
                    if gender=="female" or gender=="male":
                        print("ok thanks")
                        print("Login Succesful !!!!!")


                        print("  Welcome in google   ")
                    else:
                        print("choose between male or female")
                else: 
                    print("invaild otp!!")
            else:
                print("sorry you can't login!")        
        else:
            print("incorrect no.")
    else:
        print(" please enter vailed name")
else:
    print("enter your name")