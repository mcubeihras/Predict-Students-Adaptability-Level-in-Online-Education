from flask import Flask, render_template, request

import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open("df1.pkl", 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form['Gender']
        if Gender == "Boy":
            Gender = 0
        else:
            Gender = 1 

        Age = request.form.get('Age')
        if Age == "1-5":
            Age = 0
        elif Age == "6-10":
            Age = 5
        elif Age == "11-15":
            Age = 1
        elif Age == "16-20":
            Age = 2
        elif Age == "21-25":
            Age = 3
        else:
            Age = 4
        
        Education_Level = request.form.get('Education Level')
        if Education_Level == "University":
            Education_Level = 2
        elif Education_Level =="College":
            Education_Level =0
        else :
            Education_Level = 1 
        
        Institution_Type = request.form.get('Institution Type')
        if Institution_Type == "Non Government":
            Institution_Type = 1
        else:
            Institution_Type = 0
        
        IT_Student = request.form.get('IT Student')
        if IT_Student == "No":
            IT_Student = 0
        else:
            IT_Student = 1
            
        Load_shedding = request.form.get('Load shedding')
        if Load_shedding == "Low":
            Load_shedding = 1
        else:
            Load_shedding = 0
        
        Financial_Condition = request.form.get('Financial Condition')
        if Financial_Condition == "Poor":
            Financial_Condition = 1
        elif Financial_Condition =="Mid":
            Financial_Condition =0
        else:
            Financial_Condition = 2
            
        Internet_Type = request.form.get('Internet Type')
        if Internet_Type == "Wifi":
            Internet_Type = 1
        else:
            Internet_Type = 0
            
        Network_Type = request.form.get('Network Type')
        if Network_Type == "2G":
            Network_Type = 0
        elif Network_Type =="3G":
            Network_Type =1
        else:
            Network_Type = 2
            
        Class_Duration = request.form.get('Class Duration')
        if Class_Duration == "0":
            Class_Duration = 0
        elif Class_Duration =="1-3":
            Class_Duration =1
        else:
            Class_Duration = 2
            
        Self_Lms = request.form.get('Self Lms')
        if Self_Lms == "No":
            Self_Lms = 0
        else:
            Self_Lms = 1
            
        Device = request.form.get('Device')
        if Device == "Tab":
            Device = 2
        elif Device =="Mobile":
            Device =1
        else:
            Device = 0
              
        prediction=model.predict([[Gender, Age, Education_Level, Institution_Type, IT_Student, Load_shedding, Financial_Condition, Internet_Type, Network_Type, Class_Duration, Self_Lms, Device]])
        print(prediction)
        prediction=np.round(prediction[0],2)
        if prediction == 0:
            return render_template('index.html',prediction="High")
        elif prediction == 1:
            return render_template('index.html',prediction="Low")
        else:
            return render_template('index.html',prediction="Moderate")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)