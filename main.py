restaurant_name = 'Gyu-Kaku'
restaurant_address = '44-45 21st St, Long Island City, NY 11101'


#GREETING USER
def greeting_user ():
    print("Welcome to the NYC Tip Calculator!")

#GETTING PRE-TAX TOTAL
def get_bill_total (pre_tax):
    print (f"Your total before tax is {pre_tax}")



#PRINTING OUT THE RECIEPT
greeting_user()
print("------------------------------------------------------")
pre_tax= input("Please input your total before tax: ")
#to make sure the number could be a float
floating_number= float(pre_tax)

get_bill_total(floating_number)
