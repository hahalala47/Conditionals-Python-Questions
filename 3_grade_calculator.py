Score = input("Please enter your score to calculate grade: ")
score = int(Score)


if score >= 90:
        grade = "A"
if score >= 80:
        grade = "B"
if score >= 70:
        grade = "C"
if score >= 60:
        grade = "D"
else:
        grade = "F"
print("grade",grade )
exit()

if score >= 101:
        print("Enter the score again")
        exit()
