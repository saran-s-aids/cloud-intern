# Define display fallback for environments outside Jupyter/Colab
if 'display' not in globals():
    display = print

# 1.
import pandas as pd

# Load the California Housing training data
try:
    df = pd.read_csv('/content/sample_data/california_housing_train.csv')
except FileNotFoundError:
    # Fallback to standard online URL if running locally
    df = pd.read_csv('https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv')

# Display the first 5 rows of the DataFrame
display(df.head())

# 2.
import pandas as pd

# Load the student performance dataset
student_df = pd.read_csv('student_performance.csv')

# Display the first few rows to understand the data structure
display(student_df.head())

# 3.
student_df.info()

# 4.
# Filter for students with 'Math Score' less than or equal to 75
low_math_scores = student_df[student_df['math_score'] <= 75]

print(f"Number of students with a Math Score <= 75: {len(low_math_scores)}")
display(low_math_scores)

# 5.
students_chennai_mumbai = student_df[student_df['city'].isin(['Chennai', 'Mumbai'])]

print(f"Number of students from Chennai or Mumbai: {len(students_chennai_mumbai)}")

if not students_chennai_mumbai.empty:
    print("\nProgramming Scores for students from Chennai and Mumbai:")
    display(students_chennai_mumbai[['name', 'city', 'programming_score']])
else:
    print("No students found from Chennai or Mumbai in the dataset.")

# 6.
student_df['total_score'] = (student_df['math_score'] + student_df['science_score'] +
                             student_df['english_score'] + student_df['programming_score'])

top_performer = student_df.loc[student_df['total_score'].idxmax()]

print("Top Performer based on total scores:")
display(top_performer.to_frame().T)

# 7.
least_performer = student_df.loc[student_df['total_score'].idxmin()]

print("Least Performer based on total scores:")
display(least_performer.to_frame().T)