class SBI:
    ROI = 0.07

    def __init__(self, name, Mobno, aadhar, pan, gender, bal, pin):
        self.name = name
        self.Mobno = Mobno
        self.aadhar = aadhar
        self.pan = pan
        self.Gender = gender
        self.bal = bal
        self.pin = pin

    def Details(self):
        print(f'name    : {self.name}')
        print(f'mobno   : {self.Mobno}')  # Fixed case here
        print(f'aadhar  : {self.aadhar}')
        print(f'pan     : {self.pan}')
        print(f'Gender  : {self.Gender}')
        print(f'bal     : {self.bal}')

    def withdraw(self):
        if self.checkpin() == self.pin:
            amount = int(input('Enter the amount to withdraw: '))
            if self.bal >= amount:
                self.bal -= amount
                print('Amount debited successfully.')
                print(f'Available balance is {self.bal}')
            else:
                print('Insufficient funds.')
        else:
            print('Invalid pin.')

    @staticmethod
    def checkpin():
        return int(input('Enter the 4-digit pin: '))

    def doposite(self):
        amount = int(input('Enter the amount to deposit: '))
        self.bal += amount
        print('Amount credited successfully.')
        print(f'Available balance is {self.bal}')

    def checkbal(self):
        if self.checkpin() == self.pin:
            print(f'Available balance is {self.bal}')
        else:
            print('Invalid pin.')

    @classmethod
    def change(cls):
        var = float(input('Enter the new ROI: '))
        cls.ROI = var

    def changepin(self):
        oldpin = int(input('Enter the old pin: '))  # Converted input to integer
        if self.pin == oldpin:
            newpin = int(input('Enter the new pin: '))  # Converted input to integer
            self.pin = newpin
            print('Pin changed successfully!')
        else:
            print('Invalid old pin.')

# Testing
cust1 = SBI('vicky', 8594951164, 12345678, 'abcd212', 'male', 10000, 1234)
cust2 = SBI('ASHA', 8594958794, 45245678, 'bdt212', 'female', 8000, 4567)

# Uncomment the lines below to test the functionalities
# cust1.checkbal()
cust1.withdraw()
cust1.doposite()
# print(SBI.ROI)
