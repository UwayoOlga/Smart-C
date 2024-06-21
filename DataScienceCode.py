 import pandas as pd

# Sample data (replace with your dataset)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display basic statistics
print("Basic Statistics:")
print(df.describe())

# Group by City and calculate average age
print("\nAverage Age by City:")
avg_age = df.groupby('City')['Age'].mean()
print(avg_age)
