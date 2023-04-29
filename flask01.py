'''
总结:flask基础应用，返回的3种类型处理，需要注意的点
flask是一款非常流行的Python Web框架。还有另外一款djago。
优点：
1.微框架、简洁、只做他需要做的，给开发者提供了很大的扩展性。
2.Flask和相应的插件写得很好，用起来很爽。
3.开发效率非常高，(比如使用SQLAlchemy的ORM操作数据库可以节省开发者大量书写sql时间)
4.Flask的灵活度非常之高，他不会帮你做太多的决策，一些你都可以按照自己的意愿进行更改。
安装：pip install flask



flask配套的JinJa模板。前后端不分离
Flask渲染Jinja模板：要渲染一个模板，通过render_template方法即可，
    @app.route('/about/')
    def about():
        return render_template('about.html')
当访问/about/的时候，about()函数会在当前目录下的templates文件夹下寻找about.html模板文件。如果想更改模板文件地址，应该在创建app的时候，给Flask传递一个关键字参数template_folder，指定具体的路径，


测试开发重点在测试，不是在开发。重点在自动化的落实，把这些自动化展示的方式到页面，而不是代码和工具


'''

'''
flask步骤:1、导入2、实例化3、装饰器4定义函数5、运行run
'''
'''
JinJa模板步骤：1、创建文件templates、html 2、导入render_template 3、return render_template('路径lxz.html')
json格式转换：1、导入JSON然后2、 d = json.dumps(d)3、返回格式是text.html，所以又需要jsonify。于是不用json.dumps这方法
jsonify方法：python第三方库方法。Content-Type: application/json  。接口返回格式text转换成json

'''
from flask import Flask, render_template,jsonify

# 传入__name__初始化一个Flask实例
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# 处理视图函数，必须有返回值，1返回文本 2返回html 3JSON数据(不能返回字典，导入json模块，转换数据。d=json.dumps(d))
# app.route装饰器映射URL和执行的函数。这个设置将根URL映射到hello_world函数上
@app.route('/')  # 装饰器：映射hello_world函数,默认是根路径。底层调用这个函数
def hello_world():
    return 'hello Wor21l1d!'
    print('1')  # 没返回值就报错


# 另外一个页面。视图函数名称一定不能重复
@app.route('/test')
def test():
    return render_template('lxz.html')
    # return 'new page'
    #  ‘’‘三个引号返回html内容,这种就是前后端没有分离，前端后端都写在一起了
    # Flask渲染这么多网页内容太繁琐，所以JinJa模板解决这个问题


#     return '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <button>
# 按钮
# </button>
# </body>
# </html>
#
#      '''


'''
接口：获取所有的用户的接口,get
{
data:[
     {
     "name":"test1"
     },
      {
     "name":"test2"
     }
     
   ],
   "code":200
}

'''

import json


# 写完，通过postman都可以请求我们写的接口了
@app.route('/users', methods=['GET'])
def users():
    d = {
        "code": 200,
        "data": [
            {
                "name": "test1"
            },
            {
                "name": "清风"   #页面会出现乱码  name": "\u6e05\u98ce"，postman可以正常显示。所以需要使用jsonify方法是需要添加一句 app.config['JSON_AS_ASCII'] = False


            }
        ],
    }
    # d = json.dumps(d)
    d=jsonify(d)
    return d



if __name__ == '__main__':
    # 运行本项目,host=0.0.0.0可以让其他电脑访问到该网站。
    # port指定访问的端口。默认的host是127.0.0.1。port为5000
    # debug=True表示不重启app，可以正常调试。  修改实时监控，页面更新. 默认为false
    app.run(host='0.0.0.0', port=9000, debug=True)
