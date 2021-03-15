from flask import Flask,jsonify
from flask import request
import pandas as pd
import urllib,json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

f= urllib.request.urlopen('http://www.health-ok.in/restsql/res/healthok.MemberMedicalConditionFull?_output=application/json&_limit=10000&_offset=0') 
patient=json.load(f)
edu_mat=pd.read_csv('education material.csv',encoding="Latin1")

@app.route('/EducationalMaterial/<int:member_id>')
def EducationalMaterial(member_id):
    result={}
    

    for i in patient['Members']:
        if i['MemberId']==member_id:
            for medcon in i["MemberMedicalConditions"]:
                temp=medcon["MedicalConditionTypeId"]
                result[medcon['MedicalConditionDescription']]=edu_mat['EducationMaterial'][temp-1]
   
    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True,use_reloader=False)  


