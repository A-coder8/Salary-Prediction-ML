# 使用机器学习进行薪资预测 💰🤖

[🇬🇧 English](README.md) | [🇮🇷 فارسی](README.fa.md)

这是一个使用机器学习根据员工的个人信息和工作相关特征预测薪资的回归项目。

## 📌 特征

模型使用以下特征：

- 年龄（Age）
- 工作经验年数（Experience Years）
- 教育程度（Education）
- 职位级别（Job Level）
- 每周工作时间（Weekly Hours）
- 城市（City）

目标变量：

- 薪资（Salary）

## 🧠 使用的模型与工具

本项目使用：

- `Pandas` —— 数据处理
- `Scikit-learn` —— 机器学习
- `Linear Regression` —— 线性回归
- `PolynomialFeatures` —— 创建多项式特征
- `pd.get_dummies()` —— 对分类数据进行编码

## 📊 数据集

该数据集包含 **1000 条模拟员工数据**。

数据列：

```text
age
experience_years
education
job_level
weekly_hours
city
salary
```

## 🔮 手动预测

该项目还支持手动输入员工信息，并预测其薪资。

例如：

```text
Enter age: 25
Enter experience_years: 3
Enter education: Bachelor
Enter Job level: Junior
Enter weekly_hours: 40
Enter City: Tabriz

Model answer: ...
```

## ⚠️ 注意

本项目中的数据集是**模拟数据**，仅用于机器学习练习。

其中的薪资数据并不代表真实世界的薪资统计数据。
