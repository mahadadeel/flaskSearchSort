# app.py
from flask import Flask, render_template, request

def bubbleSort(input_data):
    numVals = len(input_data)
    for i in range(numVals):
        for x in range(0, numVals-i-1):
            if input_data[x] > input_data[x+1]:
                input_data[x], input_data[x+1] = input_data[x+1], input_data[x]
    return input_data

def mergeSort(input_data):
    if len(input_data) > 1:
        middle = len(input_data) // 2
        left = input_data[:middle]
        right = input_data[middle:]
        mergeSort(left)
        mergeSort(right)
        leftTrv = 0
        rightTrv = 0
        mainTrv = 0
        while leftTrv < len(left) and rightTrv < len(right):
            if left[leftTrv] < right[rightTrv]:
              input_data[mainTrv] = left[leftTrv]
              leftTrv += 1
            else:
                input_data[mainTrv] = right[rightTrv]
                rightTrv += 1
            mainTrv += 1
        while leftTrv < len(left):
            input_data[mainTrv] = left[leftTrv]
            leftTrv += 1
            mainTrv += 1
        while rightTrv < len(right):
            input_data[mainTrv] = right[rightTrv]
            rightTrv += 1
            mainTrv += 1
        return input_data

def linearSearch(input_list, criteria):
    for i in input_list:
        if i == criteria:
            return input_list.index(i)

app = Flask(__name__)

@app.route('/home')
def home():
  return render_template('index.html')

@app.route('/bubble', methods=["GET","POST"])
def bubble():
    if request.method == "GET":
        return render_template('bubble.html')
    elif request.method == "POST" and "the_list" in request.form:
        _list = request.form["the_list"]

        if _list:
            _list = list(_list.split(','))
            while "" in _list:
                _list.remove("")
            _list = [int(x) for x in _list]
            _list = bubbleSort(_list)

    return render_template("bubble.html", _list = _list)

@app.route('/merge', methods=["GET","POST"])
def merge():
    if request.method == "GET":
        return render_template('merge.html')
    elif request.method == "POST" and "the_list" in request.form:
        _list = request.form["the_list"]

        if _list:
            _list = list(_list.split(','))
            while "" in _list:
                _list.remove("")
            _list = [int(x) for x in _list]
            _list = mergeSort(_list)

    return render_template("merge.html", _list = _list)

@app.route('/linear', methods=["GET","POST"])
def linear():
    if request.method == "GET":
        return render_template('linear.html')
    elif request.method == "POST" and "the_list" in request.form:
        return render_template("linear.html")

@app.route('/binary', methods=["GET","POST"])
def binary():
    return render_template('binary.html')

if __name__ == '__main__':
  app.run()
