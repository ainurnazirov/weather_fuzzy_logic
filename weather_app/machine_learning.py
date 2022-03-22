import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import os.path
from weather_fuzzy_logic.settings import BASE_DIR
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv(os.path.join(BASE_DIR) + '/weather_app/data/weather.csv')

feature_list = ['temperature', 'pressure', 'humidity']

X = df[feature_list]
y = df[['precipitation']]

logreg = LinearRegression()
logreg.fit(X, y)


def compute_machine_learning(temperature, pressure, humidity):
    params = [temperature, pressure, humidity]
    day = np.array(params).reshape(1, -1)

    prediction = float(logreg.predict(day))

    return prediction
