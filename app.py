# app.py
# Implement:
# CSV Import

from flask import Flask, render_template, request
from time import *

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
    for i in range(len(input_list)):
        if input_list[i] == criteria:
            return str(i)
    return None

def binarySearch(input_list, criteria, start, end):
    if criteria in input_list:
        if start > end:
            return -1
        middle = (start + end)//2
        if criteria == input_list[middle]:
            return str(middle)
        elif criteria < input_list[middle]:
            return str(binarySearch(input_list, criteria, start, middle-1))
        else:
            return str(binarySearch(input_list, criteria, middle+1, end))
    else:
        return None

def formatList(input_list):
    input_list = list(input_list.split(','))
    while "" in input_list:
        input_list.remove("")
    input_list = [int(x) for x in input_list]
    return input_list

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
            _list = formatList(_list)
            _startTime = time_ns()
            _list = bubbleSort(_list)
            _endTime = time_ns()
            _timeTaken = _endTime - _startTime
            if _timeTaken < 1000000000:
                _timeDisplay = str(_timeTaken)+" nanoseconds"
            else:
                _timeDisplay = str(_timeTaken/1000000000)+" seconds"
        else:
            return render_template("bubble.html", _error = True)

    return render_template("bubble.html", _list = _list, _time = _timeDisplay)

@app.route('/merge', methods=["GET","POST"])
def merge():
    if request.method == "GET":
        return render_template('merge.html')
    elif request.method == "POST" and "the_list" in request.form:
        _list = request.form["the_list"]

        if _list:
            _list = formatList(_list)
            _startTime = time_ns()
            _list = mergeSort(_list)
            _endTime = time_ns()
            _timeTaken = _endTime - _startTime
            if _timeTaken < 1000000000:
                _timeDisplay = str(_timeTaken)+" nanoseconds"
            else:
                _timeDisplay = str(_timeTaken/1000000000)+" seconds"
        else:
            return render_template("merge.html", _error = True)

    return render_template("merge.html", _list = _list, _time = _timeDisplay)

@app.route('/linear', methods=["GET","POST"])
def linear():
    if request.method == "GET":
        return render_template('linear.html')
    elif request.method == "POST" and "the_list" in request.form and "the_criteria" in request.form:
        _list = request.form["the_list"]
        _criteria = request.form["the_criteria"]

        if _list and _criteria:
            _list = formatList(_list)
            _criteria = int(_criteria)
            _startTime = time_ns()
            _position = linearSearch(_list, _criteria)
            _endTime = time_ns()
            if _position == None:
                _position = "This item is not in the list"
            _timeTaken = _endTime - _startTime
            if _timeTaken < 1000000000:
                _timeDisplay = str(_timeTaken)+" nanoseconds"
            else:
                _timeDisplay = str(_timeTaken/1000000000)+" seconds"
        else:
            return render_template("linear.html", _error = True)

    return render_template("linear.html", _position = _position, _time = _timeDisplay)

@app.route('/binary', methods=["GET","POST"])
def binary():
    if request.method == "GET":
        return render_template('binary.html')
    elif request.method == "POST" and "the_list" in request.form and "the_criteria" in request.form:
        _list = request.form["the_list"]
        _criteria = request.form["the_criteria"]

        if _list and _criteria:
            _list = formatList(_list)
            _startTime = time_ns()
            _list = mergeSort(_list)
            _endTime = time_ns()
            _criteria = int(_criteria)
            _position = binarySearch(_list, _criteria, 0, len(_list))
            if _position == None:
                _position = "This item is not in the list"
            _timeTaken = _endTime - _startTime
            if _timeTaken < 1000000000:
                _timeDisplay = str(_timeTaken)+" nanoseconds"
            else:
                _timeDisplay = str(_timeTaken/1000000000)+" seconds"
        else:
            return render_template("binary.html", _error = True)

    return render_template("binary.html", _position = _position, _list = _list, _time = _timeDisplay)

if __name__ == '__main__':
  app.run()
