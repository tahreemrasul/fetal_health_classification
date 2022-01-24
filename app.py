from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_classification_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        accelerations = float(request.form['accelerations'])
        uterine_contractions=float(request.form['uterine_contractions'])
        prolongued_decelerations=float(request.form['prolongued_decelerations'])
        mean_value_of_short_term_variability=float(request.form['mean_value_of_short_term_variability'])
        abnormal_short_term_variability = float (request.form['abnormal_short_term_variability'])
        percentage_of_time_with_abnormal_long_term_variability=\
            float(request.form['percentage_of_time_with_abnormal_long_term_variability'])
        histogram_mean = float (request.form['histogram_mean'])

        prediction=model.predict([[percentage_of_time_with_abnormal_long_term_variability,
        abnormal_short_term_variability, histogram_mean,
        mean_value_of_short_term_variability, prolongued_decelerations,
        accelerations, uterine_contractions]])
        output=round(prediction[0],2)
        if output==1:
            return render_template('index.html', prediction_text="Fetal Health: Normal")
        elif output==2:
            return render_template('index.html', prediction_text="Fetal Health: Suspect")
        elif output==3:
            return render_template('index.html', prediction_text="Fetal Health: Pathological")
        else:
            return render_template('index.html',prediction_text="Fetal Health could not be accurately predicted")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

