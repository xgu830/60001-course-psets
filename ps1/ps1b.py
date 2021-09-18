total_cost = float(input("Enter the total cost of your dream house: "))
portion_down_payment = 0.2
print("Down payment required:", portion_down_payment * total_cost)

current_savings = float(input("Enter your current savings: "))
invest_return = float(input("Enter your annual invest return, as a decimal(i.e. 0.1 for 10%): "))
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal(i.e. 0.1 for 10%): "))

semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal(i.e. 0.1 for 10%): "))
raising_month = 6

required_month = 0
while current_savings <= (total_cost * portion_down_payment):
    current_savings = ((annual_salary / 12) * portion_saved) + current_savings * (1 + invest_return / 12) 
    required_month += 1
    if required_month == raising_month:
        annual_salary += annual_salary * semi_annual_raise
        raising_month += 6

print("Total months required to saving for down payment:", required_month)