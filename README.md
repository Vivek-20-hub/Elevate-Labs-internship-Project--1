# Elevate-Labs-internship-Project--1

---
## Introduction
Employee attrition is one of the most significant challenges faced by organizations today. High turnover not only disrupts operational continuity but also results in substantial costs related to hiring, onboarding, and training new staff. Moreover, the loss of experienced employees impacts team productivity and organizational knowledge. This project aims to address this issue by leveraging data analytics and machine learning to understand the underlying causes of attrition and predict which employees are most at risk of leaving. By doing so, HR teams and management can take timely actions to improve retention, enhance employee satisfaction, and make data-informed strategic decisions.

---

---

## Abstract

The goal of this project is to predict employee attrition using historical HR data and provide actionable insights through data visualization and machine learning. We analyze multiple factors such as work environment, job role, salary, tenure, satisfaction levels, and performance metrics to uncover patterns that influence attrition. By building a logistic regression model and interpreting its output using SHAP, we gain a clear understanding of which features drive employee turnover. Furthermore, a Power BI dashboard is developed to visually communicate key trends and department-wise breakdowns. The outcome of this project serves not just as a predictive tool, but also as a strategic guide for implementing effective employee retention policies.

---
---

## Tools and Technologies Used

---
---

## Python:
Python was the primary programming language used throughout the project. It was chosen for its simplicity, rich ecosystem of data science libraries, and versatility in handling data analysis, machine learning, and automation tasks.

## Pandas:
Pandas was used extensively for data loading, cleaning, manipulation, and transformation. It provided powerful data structures such as DataFrames, making it easy to filter, aggregate, and preprocess employee records from the CSV file.

## NumPy:
NumPy complemented Pandas by offering high-performance numerical operations. It was particularly helpful during data standardization and when working with large arrays or matrix transformations.

## Matplotlib:
Matplotlib was used to create static, customizable plots and charts. It played a crucial role in generating visual outputs such as bar charts, line graphs, and histograms that helped identify trends related to attrition.

## Seaborn:
Built on top of Matplotlib, Seaborn allowed for easier and more aesthetic statistical visualizations. It was particularly effective in creating heatmaps, count plots, and distribution plots to uncover hidden relationships within the data.

## Scikit-learn:
Scikit-learn was the core library for building and evaluating machine learning models. It was used to perform tasks such as splitting the dataset, training the logistic regression model, and calculating performance metrics like accuracy, precision, recall, and the confusion matrix.

## SHAP (SHapley Additive exPlanations):
SHAP was used to interpret the machine learning model by explaining the impact of each feature on predictions. It provided global and individual-level explanations, which helped identify critical factors leading to employee attrition.

## Power BI:
Power BI was used to build an interactive and professional dashboard for visualizing attrition insights. It allowed end-users (such as HR teams) to filter by department, age, salary, and other variables to explore trends and support data-driven decision-making.

---
---

## Programming Language & Modules
---
---

Python was used as the primary programming language for its ease of use and strong data science ecosystem.

Pandas helped manipulate and filter data, especially for analyzing factors like department-wise attrition.

NumPy supported numerical operations required during data normalization and model input preparation.

Matplotlib & Seaborn were used to create visualizations that revealed trends such as higher attrition in Sales and among employees with low job satisfaction.

Scikit-learn enabled the building and evaluation of the Logistic Regression model using metrics like accuracy, precision, and recall.

SHAP was used for interpreting model predictions and understanding feature importance related to attrition.

Jupyter Notebook served as the interactive development environment, combining code, output, and commentary in one place.

---
## Machine Learning Model

---
---

Model Used: Logistic Regression, a binary classifier ideal for predicting "Yes" or "No" outcomes (i.e., whether an employee will leave).

Input Features: Included age, monthly income, overtime status, job level, years at company, and job satisfaction.

Key Insight: Employees with overtime, lower income, and low job satisfaction had 20–30% higher attrition probability on average.

Evaluation Metrics: Used accuracy, precision, recall, and F1-score to ensure balanced performance.

Confusion Matrix: Helped identify how often the model predicted attrition correctly vs. where it failed (e.g., false negatives).

---
---


## Model Interpretability (SHAP Analysis)

Purpose: SHAP was used to understand why the model predicted attrition for certain employees.

---
## Top Influencing Features:
---

OverTime — increased attrition risk by approx. 25–35%.

Low Job Satisfaction — added to a 20% increase in attrition likelihood.

Years with Current Manager — longer relationships correlated with lower attrition.

Work-Life Balance — poor balance led to higher attrition risks.

SHAP Summary Plot: Visually showed feature importance and the direction of influence (positive or negative) on attrition.

----
