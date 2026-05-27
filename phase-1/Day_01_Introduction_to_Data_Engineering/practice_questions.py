import pandas as pd

# Load the dataset
df = pd.read_csv('student_performance.csv')

# Calculate total_score
df['total_score'] = df['math_score'] + df['science_score'] + df['english_score'] + df['programming_score']

# ---------------------------------------------------------
# PRACTICE QUESTIONS SOLUTIONS
# ---------------------------------------------------------

print("="*60)
print("             PRACTICE QUESTIONS SOLUTIONS")
print("="*60)
print()

# Question 1: How many students are from the Electronics Department?
electronics_count = len(df[df['department'] == 'Electronics'])
print("1. How many students are from the Electronics Department?")
print(f"   Answer: {electronics_count} students")
print(f"   Code: len(df[df['department'] == 'Electronics'])")
print("-" * 60)

# Question 2: What is the average attendance of female students?
avg_attendance_female = df[df['gender'] == 'Female']['attendance_percentage'].mean()
print("2. What is the average attendance of female students?")
print(f"   Answer: {avg_attendance_female:.2f}%")
print(f"   Code: df[df['gender'] == 'Female']['attendance_percentage'].mean()")
print("-" * 60)

# Question 3: Who is the student with the lowest programming score?
lowest_prog_idx = df['programming_score'].idxmin()
lowest_prog_student = df.loc[lowest_prog_idx, 'name']
lowest_prog_score = df.loc[lowest_prog_idx, 'programming_score']
print("3. Who is the student with the lowest programming score?")
print(f"   Answer: {lowest_prog_student} (Score: {lowest_prog_score})")
print(f"   Code: df.loc[df['programming_score'].idxmin()]['name']")
print("-" * 60)

# Question 4: How many students scored above 80 in math?
math_above_80_count = len(df[df['math_score'] > 80])
print("4. How many students scored above 80 in math?")
print(f"   Answer: {math_above_80_count} students")
print(f"   Code: len(df[df['math_score'] > 80])")
print("-" * 60)

# Question 5: What is the average total_score for students with attendance above 90%?
avg_total_high_attendance = df[df['attendance_percentage'] > 90]['total_score'].mean()
print("5. What is the average total_score for students with attendance above 90%?")
print(f"   Answer: {avg_total_high_attendance:.2f}")
print(f"   Code: df[df['attendance_percentage'] > 90]['total_score'].mean()")
print("="*60)


