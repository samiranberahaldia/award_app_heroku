import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
lrs = pickle.load(open('lr_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('award_index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    return render_template('award_index.html', prediction_text='Employee Salary should be $ {}'.format(prediction[0]))   

if __name__=="__main__":
    app.run(debug=True)
