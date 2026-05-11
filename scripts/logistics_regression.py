import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("dataset/csv/dataset_all.csv")

X = df[["protocol", "packets", "bytes", "duration", "packets_per_sec"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42 
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n=== Logistic Regression Classification Report ===")
print(classification_report(y_test, y_pred, zero_division=0))

print("\n=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))
