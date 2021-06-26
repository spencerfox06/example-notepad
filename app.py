from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Spencer says Hello World'

if __name__ == '__main__':
    app.run(debug=True)

