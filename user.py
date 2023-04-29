'''用户相关的接口'''
from flask import Blueprint
bp= Blueprint('user',__name__,url_prefix='/user/')

@bp.route('/',)
def index():
    return '用户相关'

@bp.route('detail/')
def profile():
    return '个人简介'