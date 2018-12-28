num_quizzes = float(input("How many quizzes have you had in total? "))
current_quiz = 0
marks = []
quiz_full = float(input("How much was each quiz out of? "))
while num_quizzes > current_quiz:
    current_quiz = current_quiz + 1
    quiz_mark = float(input("How much did you get in quiz no " + str(current_quiz) + ": "))
    marks.append(quiz_mark)
total_quiz = sum(marks)
mt_total = float(input("How much was your mid-term out of? "))
mt_gotten = float(input("How much did you get on your mid-term? "))
mt_percentage = (mt_gotten / mt_total) * 100
grade_numbers = [86, 73, 67, 60]
grade_letters = ["A", "B", "C+", "C"]
for a, b in zip(grade_numbers, grade_letters):
    sum_two = total_quiz + mt_gotten
    sum_two_total = (num_quizzes * quiz_full) + mt_total
    required = (a - sum_two) / (100.0 - sum_two_total)
    required = required * 100.0
    print("To get " + str(b) + ", which is " + str(a) + "%, you need to get " + str(required) + "% on your final.")
# for i in range(0, len(grade_numbers)):
#     sum_two = total_quiz + mt_gotten
#     sum_two_total = (num_quizzes * quiz_full) + mt_total
#     required = (grade_numbers[i] - sum_two) / (100.0 - sum_two_total)
#     required = required * 100.0
#     print("To get " + str(grade_letters[i]) + ", which is " + str(grade_numbers[i]) + "%, you need to get a " + str(required) + "% on your final.")