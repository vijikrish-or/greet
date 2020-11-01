from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
def_name="jojo"

@app.route('/')
def index():
    return render_template('index.html',name=def_name)

@app.route('/greetsp',methods = ['POST'])
def greetsp():
    inputent=request.form['messagename']
    return render_template('index.html',name=inputent)