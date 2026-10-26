borrow_records = [
    ("BK001", "26NR1A0501", 0),
    ("BK002", "26NR1A0502", 4),
    ("BK003", "26NR1A0503", 10)
]

fine_rate_per_day = 5.0
total_fine_collected = 0.0

print("--- Library Fine Reconciliation Summary ---")

for book_id, student_roll, days_overdue in borrow_records:
    if days_overdue > 0:
        fine_amount = days_overdue * fine_rate_per_day
        total_fine_collected += fine_amount
        print(f"Student: {student_roll} | Book: {book_id} | Overdue: {days_overdue} days | Fine Due: Rs.{fine_amount:.2f}")
    else:
        print(f"Student: {student_roll} | Book: {book_id} | Status: Returned on time (No Fine)")

print("-------------------------------------------")
print(f"Total Fine Amount to Collect: Rs.{total_fine_collected:.2f}")