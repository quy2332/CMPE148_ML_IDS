import pandas as pd

files = [
    "dataset/csv/dataset_benign.csv",
    "dataset/csv/dataset_scan.csv",
    "dataset/csv/dataset_syn_flood.csv",
    "dataset/csv/dataset_icmp_flood.csv"
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
df.to_csv("dataset/csv/dataset_all.csv", index=False)

print(df)
print("\nSaved to dataset_all.csv")
