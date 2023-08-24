
import random

class Account():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def checkpassword(self,password):
         return self.password==password
class train_info():
    def __init__(self,train_number,source,destination,available_seats):
        self.train_number=train_number
        self.source=source
        self.destination=destination
        self.available_seats=available_seats   
    def display_info(self):
        print("----------\n")
        print("train_number:",self.train_number)
        print("source:",self.source)
        print("destination:",self.destination)
        print("available_seats:",self.available_seats)
        print("------------\n")    
    def book_tickets(self,num_tickets):
        if num_tickets>self.available_seats:
            return "not sufficient tickets"  
        else:
            pnr_list=[]
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000,999999))
            self.available_seats-=num_tickets
            return pnr_list
class passenger:
    def __init__(self,name,age,gender,phone):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone
    def display_info(self):
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender)
        print("phone:",self.phone) 
class ticket:
    def __init__(self,train,source,destination,passengers,pnr):
        self.train=train
        self.source=source
        self.destination=destination
        self.pnr=pnr
    def display_info(self):
        print("train:",self.train.train_number)
        print("source:",self.source)
        print("destination:",self.destination)
        print("pnr:",self.pnr)
        for passenger in self.passengers:
            passenger.display_info()
        print("------")    
    
accounts=[]  
loginaccount=None
while True:      
    print("1.create your account\n2.login")
    choice=int(input("enter your choice:"))
    if choice==1:
      username=input("enter username:")
      password=input("enter password:")
      accounts.append(Account(username,password))
      print("account created succesfully")
    elif choice==2:
        username=input("enter username:")
        password=input("enter password:")
        for account in accounts:
            if account.username==username and account.checkpassword(password):
              loginaccount=account
              print(username,"logged in")
              
        if loginaccount is None:    
           print("invalid username and password")
        else:
           print("login successful") 
           break
    else:
        print("enter valid details")
print("welcome to ticket booking\nAvailable train detaails")

if loginaccount is not None:
    trains=[train_info(12345,"hyd","bng",150),
            train_info(45678,"chennai","tpt",120),train_info(91011,"kadapa","antpr",20)] 
for train in trains:
    train.display_info()
while True:
    try:
        train_number=input("enter train number")
        num_tickets=int(input("enter number of tickets:"))
        if num_tickets<=0:
            raise ValueError("number of tickets should be greater than 0")
        for train in trains:
            if train.train_number==train_number:
                if num_tickets>train.seats:
                    raise ValueError("selected more than available tickets")
                break
        else:
            raise ValueError("incorrect train number")
        break
    except ValueError as e:
        print("invalid input",e)
train = None
for t in trains:
    if t.train_number == train_number:
        train = t
        break

if train is None:
    print("Invalid Train Number.")

else:
    passengers = []
    for i in range(num_tickets):
        print(f"\nEnter details for Passenger {i + 1}:")
        while True:
            try:
                name = input("Name: ")
                if not name:
                    raise ValueError("Name cannot be empty")
                age = int(input("Age: "))
                if age <= 0 or age > 120:
                    raise ValueError("Invalid Age")
                gender = input("Gender: ")
                phone = input("Phone Number: ")
                if not phone or len(phone) != 10 or not phone.isdigit():
                    raise ValueError("Invalid Phone Number")
                passenger = passenger(name, age, gender, phone)
                passengers.append(passenger)
                break
            except ValueError as e:
                print(f"Invalid Input: {e}")


    pnr_list = train.book_tickets(num_tickets)
    if pnr_list is None:
        print("Tickets not available.")
    else:
        print("\n--------------Booking Successful!------------\n\nYour Ticket Details: \n")

        for i in range(num_tickets):
            ticket = ticket(train, train.source, train.destination, [
                            passengers[i]], pnr_list[i])
            ticket.display_info()
            print("\n--------Thank You------- \n-------Safe Journey------")





    

