from . import auth_login,auth_token
from .forms import *
from ..api_handler.handler import *

from flask import render_template, redirect, url_for, session,g

from werkzeug.security import generate_password_hash, check_password_hash

import base64

@auth_login.route('/login',methods=['GET','POST'])
def login():
    form = Form_dang_nhap()
    thong_bao = ''
    if form.validate_on_submit():
        ten_dang_nhap = form.ten_dang_nhap.data
        mat_khau = base64.b64encode((form.mat_khau.data).encode(encoding='ascii'))
        check = check_customer(session['token'],ten_dang_nhap,mat_khau)
        if check:            
            session['customer'] = check
            return redirect(url_for('main.index'))
        else:
            thong_bao = 'Tên đăng nhập hoặc Mật khẩu không chính xác!'
                           

    return render_template('login.html', form = form,thong_bao=thong_bao)

@auth_login.route('/register',methods=['GET','POST'])
def register():
    form = Form_dang_ky()
    status = ''
    if form.validate_on_submit():
        status = api_create_customer(session['token'],form.ten_khach_hang.data,
            form.email.data,
            form.dia_chi.data,
            form.dien_thoai.data,
            form.ten_dang_nhap.data,
            form.mat_khau.data)
        
    return render_template('register.html', form = form, status = status)

@auth_login.route('/logout',methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@auth_login.route('/account',methods=['GET','POST'])
def account_information():
    customer = api_get_customer(session['token'],session['customer']['customer_id'])
    form = Form_cap_nhat()

    return render_template('account_info.html',form=form,customer=customer)

@auth_token.route('/login',methods=['GET','POST'])
def login_for_token():
    form = Form_token()
    if form.validate_on_submit():
        user_name = form.ten_dang_nhap.data + ":"
        password = form.mat_khau.data
        expire = form.expiration.data
        encode = base64.b64encode((user_name+password).encode(encoding='ascii'))
        token = api_authentication(basic_auth=encode.decode('utf-8'),expiration=expire)
        session['token'] = token
        redirect(url_for('main.index'))
    return render_template('token.html',form=form)