'''用例相关的接口'''
from flask import Blueprint
bp= Blueprint('testcase',__name__,url_prefix='/testcase/')

@bp.route('/',)
def index():
    return '用例首页'

@bp.route('detail/')
def profile():
    return '用例详情'