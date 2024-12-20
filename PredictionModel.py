import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
df = pd.read_csv('sickle_cell_disease_data.csv')

# Step 2: Preprocess the data
# Selecting features (X) and target variable (y)
X = df[['Gender', 'Pain_Episodes', 'Jaundice', 'Fatigue', 
        'Hemoglobin_Level', 'Reticulocyte_Count', 'Bilirubin_Level', 'Family_History']]
y = df['Has_SCD']

# Step 3: Normalize the numerical features (Hemoglobin_Level, Reticulocyte_Count, Bilirubin_Level)
scaler = StandardScaler()
X[['Hemoglobin_Level', 'Reticulocyte_Count', 'Bilirubin_Level']] = scaler.fit_transform(X[['Hemoglobin_Level', 'Reticulocyte_Count', 'Bilirubin_Level']])

# Step 4: Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the logistic regression model
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Step 6: Make predictions (probabilities)
probabilities = logreg.predict_proba(X_test)[:, 1]  # Probabilities for class 1 (Has SCD)

# Convert probabilities to percentage
probabilities_percentage = probabilities * 100

# Step 7: Print the predicted probabilities (as percentage)
for i, prob in enumerate(probabilities_percentage[:10]):  # Display the first 10 predictions
    print(f"Patient {i+1}: {prob:.2f}% chance of having SCD")

# Optional: Evaluate the model's performance (accuracy, confusion matrix, etc.)
accuracy = accuracy_score(y_test, logreg.predict(X_test))
print(f'Accuracy: {accuracy * 100:.2f}%')

# Print confusion matrix
print('Confusion Matrix:')
print(confusion_matrix(y_test, logreg.predict(X_test)))

# Print classification report (precision, recall, f1-score)
print('Classification Report:')
print(classification_report(y_test, logreg.predict(X_test)))
