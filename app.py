import pickle
from flask import Flask, request, app, jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

## Load the model
regmodel = pickle.load(open('RanF_reg.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

# A.P.I.
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']     #will make sure data given as i/p is in json format and stored inside 'data' key
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = np.array(list(data.values())).reshape(1, -1)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__=='__main__':
    app.run(debug=True)
