basic_pay = float(input("Enter Basic Pay: "))
overtime_hours = float(input("Enter Overtime Hours worked: "))

hra = basic_pay * 0.20
da = basic_pay * 0.10
overtime_pay = overtime_hours * 150.0
gross_salary = basic_pay + hra + da + overtime_pay

if gross_salary > 50000:
    tax = gross_salary * 0.10
else:
    tax = gross_salary * 0.05

pf = basic_pay * 0.12
total_deductions = tax + pf
net_salary = gross_salary - total_deductions

print("--- Employee Pay Slip ---")
print("Gross Salary: Rs.", gross_salary)
print("Tax Deduction: Rs.", tax)
print("PF Deduction: Rs.", pf)
print("Total Deductions: Rs.", total_deductions)
print("Net Payable Salary: Rs.", net_salary)