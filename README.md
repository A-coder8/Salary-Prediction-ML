# Salary Prediction 💰🤖

**Language:** [🇮🇷 فارسی](README.fa.md)

A Machine Learning regression project that predicts an employee's salary based on personal and job-related features.

## 📌 Features

The model uses these features:

- Age
- Years of experience
- Education
- Job level
- Weekly working hours
- City

Target:

- Salary

## 🧠 Model

The project uses:

- `Pandas` for data processing
- `Scikit-learn` for Machine Learning
- `Linear Regression` for salary prediction
- `PolynomialFeatures` for creating polynomial features
- `pd.get_dummies()` for categorical data encoding

## 📊 Dataset

The dataset contains 1000 synthetic employee records.

Columns:

```text
age
experience_years
education
job_level
weekly_hours
city
salary
```

## 🔮 Manual Prediction

The project also allows entering employee information manually and predicting the expected salary.

Example:

```text
Enter age: 25
Enter experience_years: 3
Enter education: Bachelor
Enter Job level: Junior
Enter weekly_hours: 40
Enter City: Tabriz

Model answer: ...
```

## ⚠️ Note

This dataset is synthetic and was created for Machine Learning practice. The salary values are not real-world salary statistics.
