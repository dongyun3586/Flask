from flask import Flask
from flask import abort, redirect, url_for
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sum.html')


@app.route('/sum')
@app.route('/sum/<int:num1>/<int:num2>')
def calc(num1=None, num2=None):
    if num1 and num2:
        print(f'num1={num1}, num2={num2}')
        return f'<h1>{num1}~{num2}의 합계 {sum([i for i in range(num1, num2+1)])}</h1>'
    else:
        return '<h1>매개변수 오류</h1>'

@app.route('/sum2/', methods=['POST', 'GET'])
def calc2():
    if request.method == "POST":
        if 'num1' in request.form and 'num2' in request.form:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            return f'<h1>{num1}~{num2}의 합계 {sum([i for i in range(num1, num2 + 1)])}</h1>'
        else:
            return '<h1>매개변수 오류</h1>'

    num1 = request.args.get('num1', '')
    num2 = request.args.get('num2', '')
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        return f'<h1>{num1}~{num2}의 합계 {sum([i for i in range(num1, num2 + 1)])}</h1>'
    else:
        return '<h1>매개변수 오류</h1>'




@app.route('/login')
def login():
    abort(401)
    return this_is_never_executed()

def this_is_never_executed():
    return 'this_is_executed'

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    print('name', name)
    return render_template('child.html')

