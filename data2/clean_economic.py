import pandas as pd

# Load CSV
df = pd.read_csv(r"C:\Users\HP\Credtech-Hackathon\data2\economic.csv")

print("Original Data:")
print(df.head())

# --- Cleaning Steps ---

# 1. Convert 'value' to numeric (sometimes it’s string)
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# 2. Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 3. Drop rows with missing values (if any)
df = df.dropna()

# 4. Optional: sort by date
df = df.sort_values(by='date')

# Save cleaned data
df.to_csv(r"C:\Users\HP\Credtech-Hackathon\data2\economic_cleaned.csv", index=False)

print("\nCleaned Data:")
print(df.head())
print("\nCleaned CSV saved as economic_cleaned.csv")
