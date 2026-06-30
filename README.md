# 🏠 House Price Prediction using Multiple Linear Regression

This project demonstrates how to build a Multiple Linear Regression model using Scikit-Learn to predict house prices based on multiple features.

## Objective

Predict the price of a house using:

- Area (square feet)
- Number of bedrooms
- Age of the house

## Dataset

| Feature | Description |
|----------|-------------|
| area_sqft | Size of the house |
| bedrooms | Number of bedrooms |
| age | Age of the house in years |
| price | House price (Target Variable) |

Example dataset:

```csv
area_sqft,bedrooms,age,price
1000,2,15,120000
1200,3,10,150000
1500,3,5,200000
1800,4,8,250000
2000,4,2,300000
2200,5,1,350000
2500,5,3,400000
```

## Technologies Used

- Python
- Pandas
- Scikit-Learn

## Machine Learning Workflow

1. Load dataset
2. Select features (`X`)
3. Select target (`y`)
4. Split dataset into training and testing sets
5. Train a Linear Regression model
6. Predict house prices
7. Evaluate using R² Score
8. Interpret feature coefficients

## Features Used

```python
X = df[["area_sqft", "bedrooms", "age"]]
```

Target:

```python
y = df["price"]
```

## Model Evaluation

The model is evaluated using:

- R² Score

Higher R² values indicate better predictive performance.

## Feature Importance

After training, the coefficients show how each feature affects the predicted price.

Example:

```text
Area        +150
Bedrooms +22000
Age       -1800
```

Interpretation:

- Larger houses generally cost more.
- More bedrooms increase the price.
- Older houses decrease the price.

## Sample Prediction

Example input:

```python
1700 sqft
3 bedrooms
6 years old
```

The trained model predicts the estimated selling price.

## Project Structure

```
house-price-prediction/
│
├── houses.csv
├── main.py
├── README.md
├── requirements.txt
└── venv/
```

## Concepts Learned

- Multiple Linear Regression
- Feature Selection
- Train/Test Split
- Model Training
- Predictions
- R² Score
- Feature Coefficients
- Comparing Actual vs Predicted Values

## Future Improvements

- Add more training data
- Perform feature scaling
- Handle missing values
- Try Random Forest Regression
- Hyperparameter tuning
- Save the trained model using joblib

