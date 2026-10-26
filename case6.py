answer_key = "ABCDABCDAB"
student_answers = "ABCDCBCDAB"

correct_count = 0
incorrect_count = 0
unanswered_count = 0

for i in range(len(answer_key)):
    if student_answers[i] == 'X':
        unanswered_count += 1
    elif student_answers[i] == answer_key[i]:
        correct_count += 1
    else:
        incorrect_count += 1

total_score = (correct_count * 4) - (incorrect_count * 1)

print("--- Answer Evaluation Result ---")
print("Total Questions:", len(answer_key))
print("Correct Answers (+4 each):", correct_count)
print("Incorrect Answers (-1 each):", incorrect_count)
print("Unanswered Questions (0 each):", unanswered_count)
print("Final Score:", total_score)