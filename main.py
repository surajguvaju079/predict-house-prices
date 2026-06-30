import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv("houses.csv")

X = df[["area_sqft", "bedrooms", "age"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predicted = model.predict(X_test)

score = r2_score(y_test, predicted)

new_house = pd.DataFrame({
    "area_sqft": [1700],
    "bedrooms": [3],
    "age": [6]
})

prediction = model.predict(new_house)

comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": predicted
})

print("Prediction:", prediction)
print("\nR² Score:", score)
print("\nCoefficients:")
print(pd.Series(model.coef_, index=X.columns))
print("\nIntercept:", model.intercept_)
print("\nComparison:")
print(comparison)
