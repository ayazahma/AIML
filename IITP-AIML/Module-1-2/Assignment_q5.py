import pandas as pd
import numpy as np

data = {
    'Name': ['Rohan', 'Shreya', 'Kavya', 'Vansh', 'Kushal'],
    'Age': [25, 30, 35, np.nan, 40],
    'Salary': [50000, 60000, np.nan, 80000, 90000],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Fill missing values in 'Age' and 'Salary' columns with their respective mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Add a new column "Experience" with random values between 1 and 10
df['Experience'] = np.random.randint(1, 11, size=len(df))

# Sort the DataFrame by "Salary" in descending order
df = df.sort_values(by='Salary', ascending=False)
# Display the updated DataFrame
print("\nDataFrame after filling missing values, adding 'Experience' column, sorting by 'Salary' ")
print(df)
# Select only the 'Name' and 'Salary' columns
selected_columns = ['Name', 'Salary']
print("\nSelected Columns (Name and Salary):")
print(df[selected_columns])
# Check for duplicate rows in the DataFrame
duplicates = df.duplicated()
if duplicates.any():
    print("\nDuplicate rows found:")
    print(df[duplicates])
else:
    print("\nNo duplicate rows found.")