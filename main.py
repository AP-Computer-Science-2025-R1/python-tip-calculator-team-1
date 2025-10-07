restaurant_name = 'Gyu-Kaku'
restaurant_address = '44-45 21st St, Long Island City, NY 11101'


#GREETING USER
def greeting_user ():
    print("Welcome to the NYC Tip Calculator!")

#GETTING PRE-TAX TOTAL
def get_bill_total (pre_tax):
    print (f"Your total before tax is {pre_tax}")


def calculate_ny_tax(subtotal: float) -> float:
    """
    Calculates the sales tax based on the subtotal provided.

    Parameters:
    subtotal (float): The subtotal amount before tax.

    Returns:
    float: The calculated tax amount.
    """
    tax_rate = 0.08875
    tax = subtotal * tax_rate
    return tax

def get_tip_percentage(subtotal):
    print("Tip options: 1) 15%  2) 18%  3) 20%  4) Custom")
    option = input("Choose (1-4): ")
    if option == "1":
        percent = 15
    elif option == "2":
        percent = 18
    elif option == "3":
        percent = 20
    elif option == "4":
        percent = float(input("Enter your tip %: "))
    else:
        percent = 15
    return round(subtotal * percent / 100, 2)








#PRINTING OUT THE RECIEPT
greeting_user()
print("------------------------------------------------------")
pre_tax= input("Please input your total before tax: ")
#to make sure the number could be a float
floating_number= float(pre_tax)

get_bill_total(floating_number)
