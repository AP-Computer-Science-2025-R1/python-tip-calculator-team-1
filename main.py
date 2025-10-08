restaurant_name = 'Gyu-Kaku'
restaurant_address = '44-45 21st St, Long Island City, NY 11101'


#GREETING USER
def greeting_user ():
    print("Welcome to the NYC Tip Calculator!")

#GETTING PRE-TAX TOTAL
def get_bill_total (subtotal):
    print ()

#CALCULATING TAX
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
    
#CALCULATING TIP 
def get_tip_percentage(total_with_tax):
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
    
    return round(floating_number * percent / 100, 2)



#PRINTING OUT THE RECIEPT
#funtions 1 & 2
greeting_user()
print("------------------------------------------------------")
#getting user input
subtotal= input("What was the total for your bill? $")
#to make sure the subtotal could be a float
floating_number= float(subtotal)
get_bill_total(floating_number)


#funtion 3
# rounding all numbers to the nearest hundreth for accuracy (,2) allows that to happen
tax = round(calculate_ny_tax(floating_number), 2)
total_with_tax= round (floating_number + tax, 2)

#funtion 4
tip_amount = get_tip_percentage(total_with_tax)
# rounding all numbers to the nearest hundreth for accuracy (,2) allows that to happen
total_with_tax= round (floating_number + tax, 2)
grand_total = round(total_with_tax + tip_amount, 2)

# PRINTING OUT MOST OF THE RECIEPT
print()
print("Calculating your total...")
print("------------------------------------------------------")
print("Here is your bill summary: ")
print(f"Subtotal: ${subtotal}")
print(f"NYC Tax : ${tax}")
print(f"Total with tax : ${total_with_tax}")
print(f"Tip : ${tip_amount}")
print("------------------------------------------------------")
print(f"Grand total ${grand_total}")
