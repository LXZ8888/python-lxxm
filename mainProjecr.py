from flask import Flask, render_template, jsonify
from flask import request

import testcase,user

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(user.bp)  # 注册用户蓝图
app.register_blueprint(testcase.bp)  #注册用户蓝图

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086, debug=True)
