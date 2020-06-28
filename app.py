import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('lr_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('award_index.html')
@app.route('/predict', methods = ['POST'])
def predict():
    features = [int[x] for x in request.forms.values()]
    y_prediction = model.predict(features)    
    return render_template('index.html', prediction_text = y_prediction)   

if __name__=="__main__":
    app.run(debug=True)