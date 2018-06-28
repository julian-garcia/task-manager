from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world again'

if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=int(os.getenv('PORT') or 8000),
            debug=True)
