import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset/internship_data.csv")

# Convert text columns into numbers
le = LabelEncoder()

data["Department"] = le.fit_transform(data["Department"])
data["Python"] = le.fit_transform(data["Python"])
data["Java"] = le.fit_transform(data["Java"])
data["MachineLearning"] = le.fit_transform(data["MachineLearning"])
data["WebDevelopment"] = le.fit_transform(data["WebDevelopment"])
data["Communication"] = le.fit_transform(data["Communication"])
data["Interest"] = le.fit_transform(data["Interest"])
data["Location"] = le.fit_transform(data["Location"])
data["RecommendedInternship"] = le.fit_transform(data["RecommendedInternship"])

# Input features
X = data.drop("RecommendedInternship", axis=1)

# Output
y = data["RecommendedInternship"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model/recommendation_model.pkl")

print("Model trained successfully!")