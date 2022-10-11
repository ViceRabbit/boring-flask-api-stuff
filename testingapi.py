from flask import Flask, request

app = Flask(__name__)

class CalcClass():
    def __init__(self, vals):
        self.vals = vals
    def sumup(self):
        return sum(self.vals)
    def roundup(self, digits):
        return round(self.vals, digits)

@app.route('/')
def Index():
    return 'hi i guess'

@app.route('/calculator')
def CalculatorIndex():
    return {"Supported": ["/sum", "/round/<number of digits [OPTIONAL]>", "/multiplication", "/division"]}

@app.route('/calculator/sum', methods=['POST'])
def SumIndex():
    print(f'Called!; got response of {request.json["values"]}')
    answer = CalcClass(request.json["values"])
    return {"Ans": answer.sumup()}

@app.route('/calculator/round', methods=['POST'])
@app.route('/calculator/round/<digits>', methods=['POST'])
def RoundIndex(digits=2):
    print(f'Called!; got response of {request.json["values"]}')
    answer = CalcClass(request.json["values"])
    return {"Ans": answer.roundup(int(digits))}





