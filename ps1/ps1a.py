total_cost = float(input("Enter the total cost of your dream house: "))
portion_down_payment = 0.2
print("Down payment required:", portion_down_payment * total_cost)

current_savings = float(input("Enter your current savings: "))
invest_return = 0.1
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion saved every month from saraly in decimal form(i.e. 0.1 for 10%): "))

required_month = 0
while current_savings <= (total_cost * portion_down_payment):
    current_savings = ((annual_salary / 12) * portion_saved) + current_savings * (1 + invest_return / 12) 
    required_month += 1

print("Total months required to saving for down payment:", required_month)