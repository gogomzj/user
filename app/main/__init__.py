from flask import Blueprint

# 创建一个蓝本 每一个蓝本可以管理一部分路由和视图
main = Blueprint('main', __name__)

# 导入视图
from . import views