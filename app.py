# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:11:56 2021

@author: kartik.sharma10
"""

from flask import Flask, render_template, request
from model import Recommend

app = Flask(__name__)  # intitialize the flaks app
recommend = Recommend() # create object of the class

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        user = request.form["userid"]
        data=recommend.getTopProducts(user)
        error=False
        if len(data)==1:
            error = True
        return render_template('index.html', data=data, flag=True, errors=error)
    
    return render_template('index.html', flag=False)


if __name__ == '__main__' :
    app.run(debug=True )






