from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

cols_to_drop_model = ['SalarySlab', 'EmployeeCount', 'StandardHours', 'Over18', 'emp_id']
df_model = df_model.drop(columns=cols_to_drop_model, errors='ignore')

X_train = pd.get_dummies(X_train, drop_first=True)
X_test = pd.get_dummies(X_test, drop_first=True)
y_train = pd.get_dummies(y_train, drop_first=True)
y_test = pd.get_dummies(y_test, drop_first=True)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

model = LogisticRegression(class_weight="balanced")
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

confusion = confusion_matrix(y_test, y_pred)
print("Confusion Matrix: \n", confusion)

report = classification_report(y_test, y_pred)
print("Classification Report: \n", report)

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.show()

import shap
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)
shap.initjs()
shap.summary_plot(shap_values, X_test)

