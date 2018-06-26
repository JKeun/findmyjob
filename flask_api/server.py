from flask import Flask, request, render_template, jsonify

import json
import pandas as pd
import numpy as np
from sklearn.externals import joblib


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    
    # user input
    user_input = request.form['description']

    # predict result
    pred_prob = clf.predict_proba([user_input])[0]
    sorted_list = sorted(list(zip(y_class, pred_prob)), key=lambda x: x[1], reverse=True)

    results = {'items': [],}
    rank_index = 0

    for job, prob in sorted_list:
        results['items'].append({
            'rank': rank_index+1,
            'job': job,
            'prob': prob,
        })
        rank_index += 1

    responses = json.dumps(results)

    return responses

if __name__=='__main__':
    clf = joblib.load("./models/pred-model.pkl")
    y_class = joblib.load("./models/y-class.pkl")
    app.run(host='0.0.0.0', port=8080, debug=True)
