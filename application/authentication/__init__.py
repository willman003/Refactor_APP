from flask import Blueprint

auth_login = Blueprint('auth_login',__name__,template_folder="templates")
auth_token = Blueprint('auth_token',__name__,template_folder="templates")

from .views import *