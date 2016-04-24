import os

from flask import Flask

# name is __main__ if from terminal
# or __hello__ if called from python terminal??
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"
    
if __name__ == '__main__':
    host = os.getenv('IP', '0,0,0,0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port)