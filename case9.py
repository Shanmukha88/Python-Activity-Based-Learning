prepared_qty = [100, 120, 110, 130, 105]  # in kg
served_qty   = [85,  95,  105, 110, 100]  # in kg

total_prepared = sum(prepared_qty)
total_leftovers = 0

print("--- Daily Food Wastage Report ---")
for i in range(len(prepared_qty)):
    leftover = prepared_qty[i] - served_qty[i]
    total_leftovers += leftover
    waste_percentage = (leftover / prepared_qty[i]) * 100
    print(f"Day {i+1}: Prepared = {prepared_qty[i]}kg | Served = {served_qty[i]}kg | Leftover = {leftover}kg ({waste_percentage:.1f}%)")

overall_waste_percentage = (total_leftovers / total_prepared) * 100

print("---------------------------------")
print("Total Food Prepared:", total_prepared, "kg")
print("Total Food Wasted:", total_leftovers, "kg")
print(f"Overall Wastage Rate: {overall_waste_percentage:.2f}%")