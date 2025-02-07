import pandas as pd
import json
import pickle
import os

path = os.path.dirname(os.path.abspath(__file__))


df = pd.read_csv(os.path.join(path, "dataset", 'churn_train.csv'))

with open(os.path.join(path, "features.json"), "r") as json_file:
    important_features = json.load(json_file)['features']

lr_model = pickle.load(open(os.path.join(path, "models", "Random Forest.pkl"), 'rb'))


X = df[important_features].values
y = df["churn"]

y_pred = lr_model.predict(X)
df['predictions'] =  y_pred
df.to_csv(os.path.join(path, "dataset", "churn_predictions.csv"), index=False)


print("Predictions: ", y_pred)