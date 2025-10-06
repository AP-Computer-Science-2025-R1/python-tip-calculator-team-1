restaurant_name = 'Gyu-Kaku'
restaurant_address = '44-45 21st St, Long Island City, NY 11101'
bill_subtotal = 148.58
floating_number= float(bill_subtotal)
#to make sure the number could be a float


#GREETING USER
def greeting_user ():
    print("Welcome to the NYC Tip Calculator!")

#GETTING PRE-TAX TOTAL
def get_bill_total (bill_subtotal):
    print (f"Your total before tax is {bill_subtotal}")

#PRINTING OUT THE RECIEPT
greeting_user()
print("------------------------------------------------------")
get_bill_total(bill_subtotal)