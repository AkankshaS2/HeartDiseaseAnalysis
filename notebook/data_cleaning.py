import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/Heart_new2.csv")

# Check missing values
print(df.isnull().sum())

# Convert Yes/No to 1/0
binary_cols = [
"Smoking","AlcoholDrinking","Stroke","DiffWalking",
"PhysicalActivity","Asthma","KidneyDisease","SkinCancer","HeartDisease"
]

for col in binary_cols:
    df[col] = df[col].map({"Yes":1,"No":0})

# Save cleaned dataset
df.to_csv("../data/processed/cleaned_heart_data.csv",index=False)

print("Data cleaned successfully")