# Case Study 8: Student Marks Matrix Analysis
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

student_count = int(input("Number of students: "))
subject_count = int(input("Number of subjects: "))
students = input("Student names: ").split()
subjects = input("Subject names: ").split()
marks = []
for i in range(student_count):
    row = [float(x) for x in input(f"Marks for {students[i]}: ").split()]
    if len(row) != subject_count or any(x < 0 or x > 100 for x in row):
        print("Invalid marks row")
        raise SystemExit
    marks.append(row)
totals = [sum(row) for row in marks]
print("\nStudent results:")
for i in range(student_count):
    print(f"{students[i]}: total={totals[i]:.1f}, average={totals[i]/subject_count:.2f}")
print("Subject averages:")
for j in range(subject_count):
    average = sum(marks[i][j] for i in range(student_count)) / student_count
    print(f"{subjects[j]}: {average:.2f}")
top = max(totals)
print("Top performer(s): " + ", ".join(students[i] for i in range(student_count) if totals[i] == top))
