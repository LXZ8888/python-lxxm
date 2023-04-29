from flask import Flask, render_template, jsonify
from flask import request


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False





if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8086,debug=True)