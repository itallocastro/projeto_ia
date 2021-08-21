from flask import Flask
from flask import request
from model import DecisionTreePhone
app = Flask(__name__)

@app.route("/", methods=['POST'])
def getDecision():
    data = request.json['data']
    decision = DecisionTreePhone()
    model = decision.fitModel()
    predict = model.predict([data])
    return f"O telefone indicado para você é o {predict[0]}"