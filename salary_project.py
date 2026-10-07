# Import a immportant librarys
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np

# read data
df = pd.read_csv("salary_data_1000.csv")
# fill nan to None
df = df.fillna("None")

# set X and Y data
x = df.drop(columns=["id", "salary"])
X = pd.get_dummies(x, drop_first=True)
Y = df[["salary"]]

# train and test split data
train_x, test_x, train_y, test_y = train_test_split(X,Y)

# create a poly model
model = PolynomialFeatures(degree=3)
poly_train = model.fit_transform(train_x)

# creaate Regression model
regr = LinearRegression()
regr.fit(poly_train, train_y)
poly_test_x = model.fit_transform(test_x)
yhat = regr.predict(poly_test_x)

# get score model with R2Score
print("r2score =", r2_score(test_y, yhat))

# get a new x data
age = int(input("Enter age: "))
experience_years = int(input("enter experience_years: "))
education = input("Enter education: ")
job_level = input("Enter Job level: ")
weekly_hours = int(input("Enter weekly_hours: "))
city = input("Enter City: ")

# create DataFrame with new data x
new_data = pd.DataFrame([{
    "age": age,
    "experience_years":experience_years,
    "education":education,
    "job_level":job_level,
    "weekly_hours":weekly_hours,
    "city":city
}])

# set new x and predect data
new_x = pd.get_dummies(new_data, drop_first=True)
new_X = new_x.reindex(columns=X.columns, fill_value=0)
poly_new_data_x = model.transform(new_X)
predication = regr.predict(poly_new_data_x)

# print a model answer
print("model answer:", predication)
