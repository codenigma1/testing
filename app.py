from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>🚀 Hello from Flask App deployed via GitHub on Azure but on staging slot!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
