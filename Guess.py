import time
flag = 1
while True and flag!=0:
        print("\n\t\t------------------ Guess Game ------------------ \n")
        time.sleep(1)
        print("\n Think of a Number !\n")
        time.sleep(2)
        print("\n Multiply the result by 2\n")
        time.sleep(2)
        print("\n Add the number with 2\n")
        time.sleep(2)
        print("\n Multiply the result by 5\n")
        time.sleep(2)
        print("\n Add the result with 5\n")
        time.sleep(2)
        print("\n Multiply the result by 10\n")
        time.sleep(2)
        print("\n Add the result with 10\n")
        time.sleep(5)
        a = int(input("\n Tell me the final Result...I'll tell you the numbr you thought: "))
        res = int((a/100)-1)
        num = res
        num = (((((num*2)+2)*5)+5)*10)+10
        if num == a:
            print("\n\n\t\t\tYou thought the number "+str(res)+" !\n")
            time.sleep(1)
            print("\n Thank you for playing :)")
        else:
            print("\n\n Wrong Result...Try next time !\n")
        time.sleep(2)
        opt = input("\n Do you want to play again? y/n \n")
        if opt.lower()=="y":
            continue
        else:
            print("\n\t\t\t\tGood Bye !\n\n")
            flag = 0
