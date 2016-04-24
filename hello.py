import os

from flask import Flask

# name is __main__ if from terminal
# or __hello__ if called from python terminal??
app = Flask(__name__)

@app.route('/')
def hello_world():
    # n: next, c: continue
    #import pdb; pdb.set_trace()
    i = 3
    i += 1
    visited = i
    return "You've visited {} times".format(str(visited))
    
if __name__ == '__main__':
    host = os.getenv('IP', '0,0,0,0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)