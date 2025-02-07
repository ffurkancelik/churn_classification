# Churn Prediction Project

## Overview

This project focuses on predicting customer churn using machine learning models. The dataset used for training is located in `dataset/churn_train.csv`. The project includes data preprocessing, feature importance analysis, model training, and evaluation. The trained models are stored in `models/`.

## Project Structure

```
churn/
│-- Churn.ipynb                      # Jupyter Notebook with analysis and modeling
│-- dataset/
│   └── churn_train.csv               # Training dataset
│-- models/
│   ├── Logistic Regression.pkl       # Trained Logistic Regression model
│   ├── Random Forest.pkl             # Trained Random Forest model
│   ├── XGBoost.pkl                   # Trained XGBoost model
│-- Additional Images/                # Feature importance and PCA visualization
│-- features.json                      # JSON file describing the features
│-- test_with_csv_file.py              # Python script for testing models
```

## Data Exploration

- The dataset consists of various customer attributes, including demographic, usage, and service-related features.
- Key missing values were handled using imputation techniques.
- Outliers were identified and managed using standard deviation thresholds.
- Jupyter Notebook (`Churn.ipynb`) contains outputs and visualizations illustrating these findings.

### Churn_CLV.ipynb

This notebook is used to understand and analyze the dataset in depth:

- **Historical Analysis:** Extracts first and last observed transaction dates using `user_lifetime`.
- **Understanding User Lifetime:** Provides insights into how long customers stay engaged before churning.
- **Data Preprocessing:** Filters out invalid or redundant transaction records.
- **Exploratory Data Analysis (EDA):** Uses visualization techniques to analyze data trends.
- **Feature Selection:** Identifies key variables affecting churn prediction.


## Feature Importance

- **Correlation Analysis:** Identified highly correlated features to avoid redundancy.
- **Mutual Information:** Selected top informative features.
- **PCA (Principal Component Analysis):** Used for dimensionality reduction and optimizing feature selection.
- **Random Forest Feature Importance:** Ranked feature significance using a tree-based model.
- **Top 10 Most Important Features:** Extracted using feature importance methods.
- Some feature importance plots are saved in `Additional Images/` and are also present in `Churn.ipynb`.

## Assumptions

- Customers with long inactivity are more likely to churn.
- High service usage variability may indicate potential churn risk.
- Certain demographic attributes influence churn probability.

## Model Training

- **Logistic Regression:** Baseline model for churn prediction.
- **Random Forest:** Improved performance using an ensemble learning approach.
- **XGBoost:** Optimized gradient boosting model for high accuracy.

## Conclusion

- The Random Forest and XGBoost models performed significantly better than Logistic Regression.
- Feature selection played a crucial role in improving model performance.
- Customers with irregular service usage patterns were more likely to churn.
- Certain features such as tenure and monthly charges had significant importance in predicting churn.
- Visualizations from `Churn.ipynb` provided insights into key customer behaviors.
- The dataset and models could be further improved with additional external features or real-time customer feedback data.

## Testing the Model

- The models (Logistic Regression, Random Forest, XGBoost) can be used for predictions.
- Use `test_with_csv_file.py` to input new data and predict churn probabilities using these models.
- Before running unzip the models.zip
