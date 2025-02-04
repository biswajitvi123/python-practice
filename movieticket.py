
def singleTon(arg):
    l=[]
    def inner():
        if len(l)==0:
            obj=arg()
            l.append(obj)
        return l[0]
    return inner
@singleTon
class movie1():
    def __init__(self):
        self.total=200
    def Booking(self):
        requird=int(input("enter how many tickets to book"))
        if requird <= self.total:
            print("Booked tickets Successfully")
            self.total-=requird
            print(f' Available tickets is {self.total}')
        else:
            print("tickets are not allowed")
@singleTon
class movie2():
    def __init__(self):
        self.total=300
    def Booking(self):
        requird=int(input("enter how many tickets to book"))
        if requird <= self.total:
            print("Booked tickets Successfully")
            self.total-=requird
            print(f' Available tickets is {self.total}')
        else:
            print("tickets are not allowed")

@singleTon
def Bmyshow():
    print("1.paytm /n 2.amazonpay /n 3. googlepay")
    choice = int(input("book show"))
    if choice==1:
        print('1.paytm')
        user = movie1()
        user.Booking()
        print('paytm booked successfully')
        
    elif choice==2:
        print('2.amazonpay')
        user=movie1()
        user.Booking()
        print('amazonpay booked successfully')
        
    elif choice==3:
        print('3.googlepay')
        user=movie1()
        user.Booking()
        print('googlepay booked successfully')
    elif choice==4:
        print('phonepay')
        user=movie1()
        user.Booking()
        print('phonepay booked successfully')
    elif choice==5:
        print('offline')
        user=movie1()
        user.Booking()
        print('offline booked successfully')
    else:
        print("no shows are availble")
@singleTon
def amazonpay():
    print("1.paytm /n 2.amazonpay /n 3) googlepay")
    choice = int(input("book show"))
    if choice==1:
        print('1.paytm')
        user = movie2()
        user.Booking()
        print('paytm booked successfully')
        
    elif choice==2:
        print('2.amazonpay')
        user=movie2()
        user.Booking()
        print('amazonpay booked successfully')
        
    elif choice==3:
        print('3.googlepay')
        user=movie2()
        user.Booking()
        print('googlepay booked successfully')
    elif choice==4:
        print('phonepay')
        user=movie2()
        user.Booking()
        print('phonepay booked successfully')
    elif choice==5:
        print('offline')
        user=movie2()
        user.Booking()
        print('offline booked successfully')
    else:
        print("no shows are availble")

user1=Bmyshow()
user2=amazonpay()

