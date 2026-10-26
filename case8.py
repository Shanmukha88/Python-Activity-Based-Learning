shifts = [
    ("Emp101", 9, 13),
    ("Emp102", 12, 16),
    ("Emp103", 14, 18)
]

print("--- Employee Shift Conflict Audit ---")
conflict_found = False

for i in range(len(shifts)):
    for j in range(i + 1, len(shifts)):
        emp1, start1, end1 = shifts[i]
        emp2, start2, end2 = shifts[j]
        
        if (start1 < end2) and (start2 < end1):
            print(f"Conflict Detected: {emp1} ({start1}:00-{end1}:00) overlaps with {emp2} ({start2}:00-{end2}:00)")
            conflict_found = True

if not conflict_found:
    print("No shift conflicts detected across all scheduled employees.")