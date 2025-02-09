# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report

# Load the training and test datasets using absolute paths
train_data = pd.read_csv(r"C:\Users\admin\Downloads\digit-recognizer\train.csv")
test_data = pd.read_csv(r"C:\Users\admin\Downloads\digit-recognizer\test.csv")

# Assuming the label column is named 'label' and the rest are pixel columns
# Adjust according to your actual dataset structure
X_train = train_data.drop(columns='label').values
y_train = train_data['label'].values

# Since the test data does not have labels, we will split train_data for this example
# In a real scenario, you would need the test labels to evaluate the model
X_train_split, X_test_split = X_train[:33600], X_train[33600:]
y_train_split, y_test_split = y_train[:33600], y_train[33600:]

# Standardize the data
scaler = StandardScaler()
X_train_split = scaler.fit_transform(X_train_split)
X_test_split = scaler.transform(X_test_split)

# Build the model
model = svm.SVC(kernel='linear', C=2, random_state=42)

# Train the model
model.fit(X_train_split, y_train_split)

# Make predictions
y_pred = model.predict(X_test_split)

# Compute confusion matrix
cm = confusion_matrix(y_test_split, y_pred)

# Plot confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.arange(10), yticklabels=np.arange(10))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Print classification report
print("Classification Report:")
print(classification_report(y_test_split, y_pred))

# Plot some predictions
def plot_predictions(data, target, predictions):
    fig, axes = plt.subplots(2, 5, figsize=(10, 5))
    for i, ax in enumerate(axes.flat):
        ax.imshow(data[i].reshape(28, 28), cmap='gray')  # Adjust the reshape size if needed
        ax.set_title(f'Pred: {predictions[i]}\nTrue: {target[i]}')
        ax.axis('off')
    plt.show()

# Plot predictions on the test set
plot_predictions(X_test_split, y_test_split, y_pred)
