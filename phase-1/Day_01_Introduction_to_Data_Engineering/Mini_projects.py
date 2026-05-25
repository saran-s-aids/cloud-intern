import pandas as pd

df = pd.read_csv('student_performance.csv')

df['total_score'] = df['math_score'] + df['science_score'] + df['english_score'] + df['programming_score']

columns_to_keep = ['name', 'gender', 'department', 'math_score', 'programming_score', 'attendance_percentage', 'total_score']
df = df[columns_to_keep]

# ---------------------------------------------------------
# TASK 1: Display Project Title
# ---------------------------------------------------------
print("="*50)
print("          STUDENT PERFORMANCE EXPLORER")
print("="*50)
print()

# ---------------------------------------------------------
# TASK 2: Dataset Overview
# ---------------------------------------------------------
print("--- 2. Dataset Overview ---")
print(f"Total number of students: {len(df)}")
print(f"Total number of columns: {len(df.columns)}")
print(f"Number of unique departments: {df['department'].nunique()}\n")

# ---------------------------------------------------------
# TASK 3: Department-wise Analysis
# ---------------------------------------------------------
print("--- 3. Department-wise Analysis ---")
dept_counts = df['department'].value_counts()
print("Count of students in each department:")
print(dept_counts.to_string())
print()

# ---------------------------------------------------------
# TASK 4: Score Analysis
# ---------------------------------------------------------
print("--- 4. Score Analysis ---")
print(f"Highest Math Score: {df['math_score'].max()}")
print(f"Lowest Math Score: {df['math_score'].min()}")
print(f"Average Math Score: {df['math_score'].mean():.2f}")
print(f"Average Programming Score: {df['programming_score'].mean():.2f}")
print(f"Average Attendance Percentage: {df['attendance_percentage'].mean():.2f}%\n")

# ---------------------------------------------------------
# TASK 5: Gender-wise Analysis
# ---------------------------------------------------------
print("--- 5. Gender-wise Analysis ---")
gender_avg = df.groupby('gender')['total_score'].mean()
print("Average Total Score by Gender:")
print(gender_avg.to_string())
print()

# ---------------------------------------------------------
# TASK 6: Top Performers
# ---------------------------------------------------------
print("--- 6. Top 5 Performers ---")
# Sort values descending and take the top 5
top_students = df.sort_values(by='total_score', ascending=False).head(5)

# Using iterrows() as per the project requirements
for index, row in top_students.iterrows():
    print(f"Name: {row['name']} | Dept: {row['department']} | Total Score: {row['total_score']}")
print()

# ---------------------------------------------------------
# TASK 7: Attendance Analysis
# ---------------------------------------------------------
print("--- 7. Attendance Analysis (Below 75%) ---")
low_attendance = df[df['attendance_percentage'] < 75]

if low_attendance.empty:
    print("Great! All students have an attendance above 75%.")
else:
    for index, row in low_attendance.iterrows():
        print(f"Name: {row['name']} | Dept: {row['department']} | Attendance: {row['attendance_percentage']}%")
