total_cost = float(input("Enter the total cost of your dream house: "))
portion_down_payment = 0.2
down_payment = total_cost * portion_down_payment
print("Down payment required:", down_payment)


start_savings = float(input("Enter your current savings: "))
current_savings = start_savings
invest_return = float(input("Enter your annual invest return, as a decimal(i.e. 0.1 for 10%): "))

start_salary = float(input("Enter your starting annual salary: "))
annual_salary = start_salary
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal(i.e. 0.1 for 10%): "))
raising_month = 6

guess_low = 0
guess_high = 10000
guess = int((guess_low + guess_high) / 2)
portion_saved = guess / 10000
epsilon = 100
guess_steps = 1

while (down_payment - current_savings) >= epsilon and (guess_high - guess_low) >= 4:
    for required_month in range(36):
        current_savings = ((annual_salary / 12) * portion_saved) + current_savings * (1 + invest_return / 12)
        if required_month == raising_month:
                annual_salary += annual_salary * semi_annual_raise
                raising_month += 6
    print("Portion_saved", portion_saved, "Guess_steps", guess_steps, "Difference", down_payment - current_savings)

    if (current_savings + 100) < down_payment:
        guess_low = guess
    else: 
        guess_high = guess

    if abs(down_payment - current_savings) >= epsilon:
        current_savings = start_savings
        raising_month = 6
        annual_salary = start_salary
        guess = int((guess_low + guess_high) / 2)
        portion_saved = guess / 10000
        guess_steps += 1
        
    else:
        print("Total_savings: ", current_savings, "annual_salary", annual_salary)
        print("Best savings rate: ", portion_saved)
        print("Steps in bisection search:", guess_steps)

if (down_payment - current_savings) >= epsilon:
    print("It is not possible to pay the down payment in three years.")