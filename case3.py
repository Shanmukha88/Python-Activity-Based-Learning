items = [
    ("Notebook", 50.0, 4),
    ("Pen", 10.0, 10),
    ("Bag", 500.0, 1)
]

subtotal = 0.0

print("--- Itemized Invoice ---")
for item_name, price, qty in items:
    item_total = price * qty
    subtotal += item_total
    print(f"{item_name} x {qty} @ Rs.{price} = Rs.{item_total}")

# Discount slabs
if subtotal > 1000:
    discount = subtotal * 0.15
elif subtotal > 500:
    discount = subtotal * 0.10
else:
    discount = 0.0

final_total = subtotal - discount

print("------------------------")
print("Subtotal: Rs.", subtotal)
print("Discount Applied: Rs.", discount)
print("Final Payable Amount: Rs.", final_total)