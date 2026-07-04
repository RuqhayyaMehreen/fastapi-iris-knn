import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
from pathlib import Path

# Read the .data file
df = pd.read_csv("iris.data", header=None)

# Set column names
df.columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]

# Check first 5 rows
print(df.head())
# Separate features and target

X = df.drop("species", axis=1)
y = df["species"]

# Create models folder
MODEL_PATH = Path("models")
MODEL_PATH.mkdir(exist_ok=True)

MODEL_FILE = MODEL_PATH / "knn_model.joblib"

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create KNN model
knn = KNeighborsClassifier(n_neighbors=3)

# Train
knn.fit(X_train, y_train)

# Accuracy
accuracy = knn.score(X_test, y_test)
print("Accuracy:", accuracy)

# Save model
joblib.dump(
    {
        "model": knn,
        "feature_names": X.columns.tolist()
    },
    MODEL_FILE
)

print("Model saved successfully")