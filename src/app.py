from flask import Flask, render_template
from flask import request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'a и b - не числа'
    #return str(a - b)
    return str(a**2 + 4*a*b - b**2)  

if __name__ == '__main__':
     app.run()