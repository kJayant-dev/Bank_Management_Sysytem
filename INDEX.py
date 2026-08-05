import json 
from pathlib import Path 
import string 
import random


class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exist ")
    except Exception as err:
        print(f"An exception occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)



    def Createaccount(self):
        info = {
            "name": input("Enter your name :- "),
            "age" : int(input("Enter your age :- ")),
            "email": input("Enter your email :- "),
            "pin": int(input("Enter your 4 number pin :- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18  :
            print("Sorry you cannot create your account because your age is less than 18 ")
        if len(str(info['pin'])) != 4 :
            print("Your PIN is not Valid ")
        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number for Further purpose...")

            Bank.data.append(info)

            Bank.__update()
        
    def depositmoney(self):
        accnumber = input("Enter your account number : ")
        pin = int(input("Enter your PIN :  "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Data Not exist in Database...")
        
        else:
            amount = int(input("How much you want to depoit : "))
            if amount  > 10000 or amount < 0:
                print("Sorry the amount is too much you can deposit below 10000 and above 0")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully ")
    

    def withdrawmoney(self):
        accnumber = input("Enter your account number : ")
        pin = int(input("Enter your PIN :  "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Data Not exist in Database...")
        
        else:
            amount = int(input("How much you want to withdraw : "))
            if userdata[0]['balance']  < amount:
                print("Soory you dont have that much money")
              
            else:
                
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully ")


    def showdetails(self):

        accnumber = input("Enter your account number ")
        pin = int(input("Enter your PIN : "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("Your information are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")



    def updatedetails(self):
        accnumber = input("Enter your account number : ")
        pin = int(input("Enter your PIN :  "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Data Not exist in Database...")
        
        else:
            print("You cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("please tell new name : "),
                "email":input("please tell your new Email  :"),
                "pin": input("enter new PIN : ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details updated successfully")


    def Delete(self):
        accnumber = input("Enter your account number :  ")
        pin = int(input("Enter tell your PIN :  "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Data Not exist in Database... ")
        else:
            check = input("Press (y) if you actually want to delete the account or press (n)")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully ")
                Bank.__update()

            

user = Bank()

while True:

    print("1  Creating an Account")
    print("2  Deposititing the money in the bank Account ")
    print("3  Withdrawing the money ")
    print("4  Display Your Details  ")
    print("5  Updating the details")
    print("6  Deleting your account")
    print("7 Exit")

    check = int(input("Enter your Choice :  :- "))

    if check == 1:
        user.Createaccount()

    elif check == 2:
        user.depositmoney()

    elif check == 3:
        user.withdrawmoney()

    elif check == 4:
        user.showdetails()

    elif check == 5:
        user.updatedetails()

    elif check == 6:
        user.Delete()
    elif check == 7:
        print("Thank You...")
        break
    else:
        print("Invalid Choice ")