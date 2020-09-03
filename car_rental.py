print("Welcome to car rentals!")
menu_str = (input("Would you like to continue (y/n)? ")) 

b_base = 40 # price per day for budget
b_milage = 0.25 # price per mile for budget

d_base = 60 # price per day for daily
d_milage = 0.25 # price for each mile driven above 100 miles per day

while menu_str != "n": # while for menu_str and it will run as long as the input 'n'
    code = input("Customer code (b or d): ") 
    days = int(input("Number of days: "))
    start = int(input("Odometer reading at the start: "))
    end = int(input("Odometer reading at the end: "))

    miles = end - start  
    print("Miles driven:",miles)

    if code == "b":    
        amount = round( (days * b_base) + (miles * b_milage),1 ) # total amount for the days + total miles charges

    else :
        more_miles = miles - (days * 100) # calculates miles driven over 100 miles per day

        if more_miles > 0 : # if miles per day is over 0 then it will charge the amount 
            amount = round( (days * d_base) + (more_miles * d_milage),1 ) # total amount for the days + total amount for all miles driven above 100 miles per day

        else: # if miles per day is less then 0 is will only charge the days 
            amount = round( (days * d_base),1 ) # total amount for the days

    print("Amount due:", amount) 
    menu_str = (input("Would you like to continue (y/n)? "))   