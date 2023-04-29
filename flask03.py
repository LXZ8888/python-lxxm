from flask import Flask, render_template, jsonify
from flask import request
# import requests
from flask import request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

'''
request.args请求参数,get类型，获取某一个参数的值，用get方法取具体的值
request.get_json() :post类型，入参为json字符串，
request.form：post类型，入参为表单类型，用get方法取具体的值
request.get_data():post类型，入参为text文件类型，默认的值是字节类型，
request.path请求路径
request.method请求方法
request.headers.get() 请求头信息,拿到token，token到底正不正确，然后再去数据库比较
    print(request.headers.get('token'))
    print(request.headers.get('cookie'))
    print(request.headers.get('Authorization'))
    print(request.headers.get('User-Agent'))
'''


'''
导入要放到最前面，不然报错
flask模块中的request:请求上下文，客户端发送了请求给服务端，就发送了一个request对象
通过一系列的方法读取这个request对象中的内容（请求方法request.method，请求路径request.path,请求参数request.args,请求头信息）
'''
'''用户相关的接口  '''


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
    '''获取所有的用户'''
    d = {
        "code": 200,
        "data": [
            {
                "name1": "test1",
                "rank": "putong"
            },
            {
                "name2": "test2",
                "rank": "vip"

            },
            {
                "name3": "test3",
                "rank": "vvip"
            }
        ],
    }
    # d=json.dumps(d)
    canshu = request.args    #request.args参数
    # print(canshu)
    # print(request.path)
    # print(request.method)
    limit = canshu.get('limit')
    tab = canshu.get('tab')
    d = jsonify(d)
    # print(request.headers.get('token'))
    # print(request.headers.get('cookie'))
    print(request.headers.get('User-Agent'))


    return d


@app.route('/users/<int:id>', methods=['get'])
def user(id):
    '''
    获取单个用户
    id:通过用户请求传过去的id，传入视图函数
    '''
    print(id)
    res = {"code": 200, id: id}
    return jsonify(res)

@app.route('/addUser',methods=['POST'])
def addUser():
    '''新增用户'''
    canshu=request.get_json()  #返回响应值
    #print(type(canshu),canshu)
    res={"code":200,"msg":"{}用户新增成功".format(canshu['username'])}
    return jsonify(res)



@app.route('/editUser',methods=['POST'])
def editUser():
    '''编辑用户'''
    canshu=request.form
    id=canshu.get('id')
    phone=canshu.get('phone')
    print(id,phone)
    res={"code":200,"msg":"用户编辑成功"}
    return jsonify(res)

@app.route('/deleteUser',methods=['POST'])
def deletUser():
    '''删除用户'''
    canshu=request.get_data()
    print(type(canshu),canshu)
    print(type(str(canshu)))
    res={"code":200,"msg":"用户删除成功"}
    return jsonify(res)

if __name__ == '__main__':
    # 运行本项目,host=0.0.0.0可以让其他电脑访问到该网站。
    # port指定访问的端口。默认的host是127.0.0.1。port为5000
    # debug=True表示不重启app，可以正常调试。  修改实时监控，页面更新. 默认为false
    app.run(host='0.0.0.0', port=9000, debug=True)
