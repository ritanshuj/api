from flask import Flask,jsonify,render_template
from flask import request
import pandas as pd
import urllib,json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

f= urllib.request.urlopen('http://www.health-ok.in/restsql/res/healthok.MemberMedicalConditionFull?_output=application/json&_limit=10000&_offset=0') 
patient=json.load(f)
edu_mat=pd.read_csv('education material.csv',encoding="Latin1")

@app.route('/EducationalMaterial',methods=['POST'])

def EducationalMaterial():
    result={}
    x=[int(n) for n in request.form.values()]
    member_id=x[0]
    for i in patient['Members']:
        if i['MemberId']==member_id:
            for medcon in i["MemberMedicalConditions"]:
                temp=medcon["MedicalConditionTypeId"]
                result[medcon['MedicalConditionDescription']]=edu_mat['EducationMaterial'][temp-1]
                
   
    return render_template("index.html", output = result)

if __name__=="__main__":
    app.run(debug=True,use_reloader=False)  


