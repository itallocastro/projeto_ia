from flask import Flask
from flask import request
from model import DecisionTreePhone
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
def formatData(data):
    for i in range(len(data)):
        data[i] = float(data[i])
    return data

@app.route("/", methods=['POST'])
def getDecision():
    data = formatData(request.json['data'])

    decision = DecisionTreePhone()
    model = decision.fitModel()
    with open('rules.txt', 'r') as file:
        print(data)
        decision = decision.predict(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], file)
        
    return f"O telefone indicado para você é o {decision}"