from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    digit =5*5
    return str(digit)

@app.route('/home', methods=['GET', 'POST'] )
def home():
    links=['https://www.youtube.com', 'https://www.bing.com','https://www.python.org','https://www.enkato.com' ]
    return render_template('example.html', myvar='flask example', links=links)

if __name__ == '__main__':
    app.run(debug=True)
