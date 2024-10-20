from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/')
def this():
    return 'this is a protfolio project'

if __name__ == '__main__':
    app.run(debug=True)
