units = float(input("Enter total electricity units consumed: "))
fixed_charge = 50.0

if units <= 100:
    energy_charge = units * 1.50
elif units <= 300:
    energy_charge = (100 * 1.50) + ((units - 100) * 2.50)
else:
    energy_charge = (100 * 1.50) + (200 * 2.50) + ((units - 300) * 4.00)

total_bill = fixed_charge + energy_charge

print("--- Electricity Bill Statement ---")
print("Units Consumed:", units)
print("Fixed Charge: Rs.", fixed_charge)
print("Energy Charge: Rs.", energy_charge)
print("Total Bill Payable: Rs.", total_bill)