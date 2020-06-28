import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
lrs = pickle.load(open('lr_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('award_index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    features = np.array([[int(x) for x in request.forms.values()]])
    #features = [np.array(features)]
    y_prediction = lrs.predict(features)[0]  
    return render_template('award_index.html', prediction_text='Employee Salary should be $ {}'.format(y_prediction))   

if __name__=="__main__":
    app.run(debug=True)
