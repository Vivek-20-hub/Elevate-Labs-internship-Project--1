import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('HR_Analytics.csv') 


attrition_counts = df.groupby(['Department', 'Attrition']).size().unstack(fill_value=0)
attrition_summary = attrition_counts.copy()
attrition_summary['TotalEmployees'] = attrition_summary.sum(axis=1)
attrition_summary['AttritionRate_%'] = (attrition_summary['Yes'] / attrition_summary['TotalEmployees'] * 100).round(2)

plt.figure()
attrition_summary['AttritionRate_%'].plot(kind='bar', color='salmon')
plt.title("Attrition Rate by Department")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Department")
plt.tight_layout()

plt.savefig('attrition_rate_by_department.png', dpi=100)
plt.clf()

salary_dept = df.pivot_table(index='Department', columns='SalarySlab', aggfunc='size', fill_value=0)


plt.figure()
df['SalarySlab'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title("Overall Salary Band Distribution")
plt.ylabel("Number of Employees")
plt.xlabel("Salary Band")
plt.tight_layout()

plt.savefig('salary_band_distribution.png', dpi=100)
plt.clf()

promotion_summary = df.groupby('Department')['YearsSinceLastPromotion'].agg(['mean', 'median']).round(2)


plt.figure()
df['YearsSinceLastPromotion'].plot(kind='hist', bins=15, color='purple', edgecolor='black')
plt.title("Distribution of Years Since Last Promotion")
plt.xlabel("Years Since Last Promotion")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig('years_since_last_promotion_hist.png', dpi=100)
plt.clf()

plt.figure()
promotion_summary['mean'].plot(kind='bar', color='limegreen')
plt.title("Average Years Since Last Promotion by Department")
plt.ylabel("Average Years")
plt.xlabel("Department")
plt.tight_layout()

plt.savefig('avg_years_since_last_promotion_by_dept.png', dpi=100)
plt.clf()

print("\n=== Attrition Summary ===")
print(attrition_summary)

print("\n=== Salary Band Distribution by Department ===")
print(salary_dept)

print("\n=== Promotion Summary ===")
print(promotion_summary)


temp_df = df.copy()

for col in temp_df.select_dtypes(include=["object"]).columns:
    temp_df[col] = temp_df[col].astype("category").cat.codes

temp_df = temp_df.drop(columns=["emp_id","employee_count", "over_18", "standard_hours"], errors='ignore')

plt.figure(figsize=(16, 14))
sns.heatmap(temp_df.corr(), annot=True, fmt=".2f", cmap="coolwarm", annot_kws={"size": 8})

plt.savefig("heatmap.png", bbox_inches='tight', dpi=100)
plt.clf()
