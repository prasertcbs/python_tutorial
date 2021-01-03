def grade_point(grade_letter):
    grade_letter = grade_letter.upper()
    # if grade_letter == "A":
    #     return 4
    # elif grade_letter == "B+":
    #     return 3.5
    # elif grade_letter == "B":
    #     return 3
    # elif grade_letter == "C+":
    #     return 2.5
    # elif grade_letter == "C":
    #     return 2
    # elif grade_letter == "D+":
    #     return 1.5
    # elif grade_letter == "D":
    #     return 1
    # elif grade_letter == "F":
    #     return 0
    gdict = {"A": 4, "B+": 3.5, "B": 3, "C+": 2.5, "C": 2, "D+": 1.5, "D": 1, "F": 0}
    return gdict[grade_letter]


subjects = int(input("total subjects: "))
total_credits = 0
total_points = 0
for i in range(subjects):
    credit, grade_letter = input("enter credit grade (ex. 3 B): ").split(" ")
    credit = float(credit)
    total_credits += credit
    total_points += credit * grade_point(grade_letter)
print("total credits = ", total_credits)
print("total points  = ", total_points)
print("GPA           = ", total_points / total_credits)
