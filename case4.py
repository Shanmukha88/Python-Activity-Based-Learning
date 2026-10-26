marks = [65, 72, 80, 88, 92]

first_exam = marks[0]
last_exam = marks[-1]
overall_change = last_exam - first_exam

highest_score = max(marks)
lowest_score = min(marks)
average_score = sum(marks) / len(marks)

print("Assessment Scores:", marks)
print(f"Average Score: {average_score:.2f}")
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)

if overall_change > 0:
    print("Performance Trend: Improving (+", overall_change, "marks)")
elif overall_change < 0:
    print("Performance Trend: Declining (", overall_change, "marks)")
else:
    print("Performance Trend: Constant performance")