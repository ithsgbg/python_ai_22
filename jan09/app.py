import pickle
import pandas as pd
from flask import Flask
from flask_cors import CORS


knn_model = pickle.load(open('knn_model.pkl', 'rb'))


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.get('/api/predict/<measurement>')
    def predict(measurement):
        weight, height = measurement.split(',')
        weight = float(weight) * 10
        height = float(height) * 10
        df = pd.DataFrame([[weight, height]], columns=['weightkg', 'stature'])
        knn_prediction = knn_model.predict(df)
        return {'prediction': knn_prediction[0]}
    
    return app