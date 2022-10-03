score = int(input("Enter score: "))

if 90 <= score:
    grade = "A"
elif 80 <= score:
    grade = "B"
elif 70 <= score:
    grade = "C"
else:
    grade = "F"

print("Your score is {}, Grade is {}".format(score, grade))