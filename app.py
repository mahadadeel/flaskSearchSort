# app.py
from flask import Flask, render_template

def bubbleSort(input_data):
    numVals = len(input_data)
    for i in range(numVals):
        for x in range(0, numVals-i-1):
            if input_data[x] > input_data[x+1]:
                input_data[x], input_data[x+1] = input_data[x+1], input_data[x]
    return input_data

app = Flask(__name__)

@app.route('/home')
def home():
  return render_template('index.html')

@app.route('/test',methods=["GET","POST"])
def test():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST" and "myList" in request.form:
        _list = request.form["myList"]
        return render_template("index.html", _response = _list)

if __name__ == '__main__':
  app.run()
