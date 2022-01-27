from flask import Flask, render_template, request
from src.factorial import factorial

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def index():
    result = 0
    if request.method == 'POST':
        number = request.form['number']
        result = factorial(int(number))
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
