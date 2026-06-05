import pandas as pd

print("EMPLOYEE SALARY ETL PROJECT")

data = {
    "employee_id": [101, 102, 103, 104, 105, 102, 106, 107],
    "employee_name": ["Arun", "Bala", "Chitra", "Divya", "Ezhil", "Bala", "Farhan", "Gokul"],
    "department": ["HR", "IT", "Finance", "IT", "Sales", "IT", "HR", "Finance"],
    "monthly_salary": [30000, 45000, 50000, 60000, 35000, 45000, 32000, 55000]
}

df = pd.DataFrame(data)

df.to_excel("employee_salary_data.xlsx", index=False)

df = pd.read_excel("employee_salary_data.xlsx")

print("\nOriginal Dataset:")
print(df)

df = df.drop_duplicates()

df["yearly_salary"] = df["monthly_salary"] * 12

print("\nCleaned Dataset:")
print(df)

df.to_csv("cleaned_employee_salary.csv", index=False)

print("\nCleaned dataset saved as cleaned_employee_salary.csv")
