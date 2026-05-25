"""
This code demonstrates basic data analysis and visualization using pandas and matplotlib.

The code performs the following steps:
1. Creates a sample dataset with columns for Name, Age, Salary, and Experience.
2. Saves the dataset as a CSV file.
3. Loads the dataset from the CSV file.
4. Displays the first few rows of the dataset.
5. Provides summary information about the dataset.
6. Calculates descriptive statistics for the numerical columns.
7. Prints the count of each unique value in the 'Name' column.
8. Checks for missing values in the dataset.
9. Visualizes the distribution of ages using a histogram.
10. Visualizes the distribution of salaries using a histogram.

Note: The file path and file name used in the code are specific to the user's system and may need to be modified.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (create a sample dataset)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Eva", "Grace", "Helen", "Ivy"],
    "Age": [25, 30, 35, 40, 45, 50, 23, 30, 55],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000],
    "Experience": [2, 5, 7, 10, 15, 20, 15, 13, 5],
}

df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv("sample_data.csv", index=False)

# Load dataset for demonstration
df = pd.read_csv("sample_data.csv")

# Display first few rows
df.head()

# Get summary information
df.info()

# Descriptive statistics
print(df.describe())

# table of categorical variables
print(df['Name'].value_counts())

# Checking for missing values
print(df.isnull().sum())

# Visualizing Age Distribution
plt.hist(df['Age'], bins=4, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

# Visualizing Salary Distribution
plt.hist(df['Salary'], bins=4, color='skyblue')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Distribution')
plt.show()
