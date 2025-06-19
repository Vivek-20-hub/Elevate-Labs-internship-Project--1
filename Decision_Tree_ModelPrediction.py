

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

df_model = df.copy()
df_model.dropna(inplace=True)


cols_to_drop_model = ['SalarySlab', 'EmployeeCount', 'StandardHours', 'Over18', 'emp_id']
df_model = df_model.drop(columns=cols_to_drop_model, errors='ignore')

for col in df_model.select_dtypes(include=['object']).columns:
    if df_model[col].nunique() <= 2: 
        le = LabelEncoder()
        df_model[col] = le.fit_transform(df_model[col])
    else: 
        df_model = pd.get_dummies(df_model, columns=[col], drop_first=True)

X = df_model.drop('Attrition', axis=1)
y = df_model['Attrition'] 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


train_cols = set(X_train.columns)
test_cols = set(X_test.columns)

missing_in_test = list(train_cols - test_cols)
for c in missing_in_test:
    X_test[c] = 0

missing_in_train = list(test_cols - train_cols)
for c in missing_in_train:
    X_train[c] = 0

X_test = X_test[X_train.columns]

print("--- Logistic Regression Model ---")

log_reg_model = LogisticRegression(max_iter=1000, solver='liblinear', random_state=42)
log_reg_model.fit(X_train, y_train)

y_pred_lr = log_reg_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print("\nClassification Report:\n", classification_report(y_test, y_pred_lr))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred_lr))

print("\n--- Decision Tree Model ---")


dec_tree_model = DecisionTreeClassifier(random_state=42)
dec_tree_model.fit(X_train, y_train)

y_pred_dt = dec_tree_model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print("\nClassification Report:\n", classification_report(y_test, y_pred_dt))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred_dt))

plt.close('all') 
plt.figure(figsize=(20,10)) 
plot_tree(dec_tree_model, filled=True, feature_names=X_train.columns.tolist(), class_names=['No Attrition', 'Attrition'], rounded=True)
plt.title("Decision Tree Visualization")
plt.savefig("decision_tree.png", dpi=300) 
plt.show() 
