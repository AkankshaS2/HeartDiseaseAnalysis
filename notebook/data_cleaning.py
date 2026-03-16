import pandas as pd


df = pd.read_csv("notebook/Heart_new2.csv")


print(df.isnull().sum())


binary_cols = [
"Smoking","AlcoholDrinking","Stroke","DiffWalking",
"PhysicalActivity","Asthma","KidneyDisease","SkinCancer","HeartDisease"
]

for col in binary_cols:
    df[col] = df[col].map({"Yes":1,"No":0})


df.to_csv("heart_new.csv",index=False)

print("Data cleaned successfully")..