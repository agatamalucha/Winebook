from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    digit =5*5
    return str(digit)

@app.route('/home', methods=['GET', 'POST'] )
def name(place):
    return '<h1> You are on the home page </h1>'

if __name__ == '__main__':
    app.run(debug=True)
