'''用户相关的接口  '''
from flask import Flask, render_template, jsonify
from flask import request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 数据写死
datas = [
    {'name': 'test1', 'from': '长沙', 'id': 1, "gender": "boy"},
    {'name': 'test2', 'from': '上海', 'id': 2, "gender": "boy"},
    {'name': 'test3', 'from': '深圳', 'id': 3, "gender": "girl"},
    {'name': 'test4', 'from': '深圳', 'id': 4, "gender": "girl"},
    {'name': 'test5', 'from': '深圳', 'id': 5, "gender": "boy"},
]


@app.route('/')
def test():
    return 'Hello qingfeng，test!'


import json


@app.route('/users', methods=['GET'])
def users():
    '''获取所有的用户
   limit:表示限制数量， 1 返回一条数据   非必填
    tab：表示类型， tab：boy 返回用户里面所有性别为男的用户信息   非必填
    参数异常的情况，添加各种返回提示信息
    '''
    canshu = request.args

    # 我想在tab为girl的情况下，再返回限制条数
    # 我想在前10条数据，返回这10条数据里面tab为girl
    # 如果用户传了limit参数，而且传了tab
    # 多个参数都传了，需要放到第一个进行判断
    if 'tab' in canshu and 'limit' in canshu:
        limit = canshu.get('limit')
        tab = canshu.get('tab')
        d = [data for data in datas if data['gender'] == tab]
        d = d[:int(limit)]
        return jsonify({'code': 200, 'users': d})

    if 'limit' in canshu:  # 如果用户传了limit参数
        limit = canshu.get('limit')
        d = datas[:int(limit)]  # 切片L【：1】   #如果读取数据库语句，select * from 表 limit2
        return jsonify({'code': 200, 'users': d})

    if 'tab' in canshu:  # 如果用户传了tab参数
        tab = canshu.get('limit')
        # d = []
        # # d = jsonify({'name': 'test5', 'from': '深圳'})  #返回的必须是一个json字符串，json对象 {}
        # for data in datas:
        #     if data['gender'] == tab:
        #         d.append(data)
        # 1循环一个列表，2再加一个if判断，获取列表满足条件的值，3再添加到一个新的列表
        d = [data for data in datas if data['gender'] == tab]
        return jsonify({'code': 200, 'users': d})



    else:  # 没有传任何参数，默认返回所有的用户
        d = jsonify({'code': 200, 'users': datas})
    return d



if __name__ == '__main__':
    # 运行本项目,host=0.0.0.0可以让其他电脑访问到该网站。
    # port指定访问的端口。默认的host是127.0.0.1。port为5000
    # debug=True表示不重启app，可以正常调试。  修改实时监控，页面更新. 默认为false
    app.run(host='0.0.0.0', port=9000, debug=True)
