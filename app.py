# https://maxcnunes.com/post/2012/12/24/desenvolvendo-pequena-aplicacao-web-python-flask/

# Created by:  Alexsandro Monteiro
# Date:        19/02/2019
# Site for Tests Python / Flask

# Python any Where
# https://www.pythonanywhere.com/user/AlexsandroMO/
# pip install flask

from flask import Flask, render_template, url_for, request, redirect, send_file, send_from_directory
import db as db_ncr
import os
import lxml
import json
import requests
from datetime import date, datetime
from tinydb import TinyDB, Query, where
import random


# ==================================
app = Flask(__name__)

class Var_State():
    def __init__(self, login_acess):
        self.login_acess = login_acess

Var_State.login_acess = False

@app.route("/")
@app.route("/home_ncr")
def home_ncr():
    status = Var_State.login_acess
    title_status = 'Home | NCR'
    pasta = './static'
    for diretorio in os.walk(pasta):
        for arquivo in diretorio[2]:
            if arquivo == 'INT_DELNT_CRTL_META_REV.xlsx':
                os.remove('static/INT_DELNT_CRTL_META_REV.xlsx')
            elif arquivo == 'rai.xlsx':
                os.remove("static/rai.xlsx")

    return render_template('ncr/home-ncr.html', status=status, title_status=title_status)

@app.route("/create")
def create():
    return render_template('ncr/create.html')

@app.route("/userarea_loged")
def userarea_loged():
    status = Var_State.login_acess
    title_status = 'Home | NCR'
    return render_template('ncr/userarea_loged.html', status=status, title_status=title_status)

@app.route("/fileform")
def fileform():
    status = Var_State.login_acess
    title_status = 'Upload | NCR'
    return render_template('ncr/fileform.html', status=status, title_status=title_status)


@app.route("/login")
def login():
    title_status = 'Login | NCR'
    return render_template('ncr/login.html', title_status=title_status)

@app.route("/create_table")
def create_table():
    status = Var_State.login_acess
    pasta = './static'
    status_files, status_files1, status_files2 = [],[],[]
    for diretorio in os.walk(pasta):
        for arquivo in diretorio[2]:
            #print('-----',arquivo)
            if arquivo == 'INT_DELNT_CRTL_META_REV.xlsx':
                status_files1.append('-')
            elif arquivo == 'rai.xlsx':
                status_files2.append('-')

    if len(status_files1) != 1:
        status_files.append('INT_DELNT_CRTL_META_REV.xlsx')

    if len(status_files2) != 1:
        status_files.append('rai.xlsx')

    status_files_len = len(status_files)
    if status_files_len > 0:
        return render_template('ncr/message-erro-file.html', status_files=status_files, status_files_len=status_files_len, status=status)

    else:
        df = db_ncr.create_list()
        return render_template('ncr/upload.html', msg_df=df[1], status=status, df=df[0], tables=[df[0].to_html(classes='data')], titles=df[0].columns.values)

@app.route("/logout")
def logout():
    Var_State.login_acess = False
    return render_template('ncr/home-ncr.html')

@app.route("/download")
def download():
    status = Var_State.login_acess
    return redirect(url_for('static', filename='NCR_RAI_LIBERAR.xlsx'))

@app.route('/userarea', methods=['POST', 'GET'])
def userarea():

    title_status = 'Home | NCR'

    if request.method == 'POST':
        resultuserarea = request.form
        email = resultuserarea['email']
        password = resultuserarea['password']

        read_register = db_ncr.readDB(email, password)

        if email == '' or password == '':
            return f"""
            <h2>Atenção, Todos os campos precisam ser preenchidos... :( </h2><br><br><br>
            <p><a href="/login"><img src="https://image.flaticon.com/icons/png/512/54/54906.png" alt="some text" width=40 height=40></p>

            """
        if read_register[0] == True:
            Var_State.login_acess = True

            status = Var_State.login_acess

            if status == True:
                return render_template("ncr/userarea.html", title_status=title_status, title='Python_Flask', status=status,name_user=read_register[1].lower().capitalize())
                

            else:
                return render_template("ncr/login.html", title_status=title_status, email=email)

        else:
            return render_template("ncr/message.html", title_status=title_status, email=email)

@app.route('/delite_arq')
def delite_arq():
    pasta = './static'
    for diretorio in os.walk(pasta):
        for arquivo in diretorio[2]:
            if arquivo == 'INT_DELNT_CRTL_META_REV.xlsx':
                os.remove('static/INT_DELNT_CRTL_META_REV.xlsx')
            elif arquivo == 'rai.xlsx':
                os.remove("static/rai.xlsx")
                
    return render_template('ncr/home-ncr.html') 


@app.route('/register')
def register():
    status = Var_State.login_acess
    return render_template('ncr/register.html', status=status)


@app.route('/erro')
def erro():
    return render_template('ncr/erro.html')


@app.route('/dbname', methods=['POST', 'GET'])
def dbname():
    if request.method == 'POST':
        resultdbname = request.form
        firstname = resultdbname['firstname']
        lastname = resultdbname['lastname']
        email1 = resultdbname['email1']
        email2 = resultdbname['email2']
        password1 = resultdbname['password1']
        password2 = resultdbname['password2']

        if firstname and lastname and email1 and email2 and password1 and password2 != '':
            if email1 != email2:
                return f"""
          <h2>Atenção! Senhas não São Identicas... :( </h2><br><br><br>
          <p><a href="/register"><img src="https://image.flaticon.com/icons/png/512/54/54906.png" alt="some text" width=40 height=40></p>

          """
            if password1 != password2:
                return f"""
          <h2>Atenção! Senhas não São Identicas... :( </h2><br><br><br>
          <p><a href="/register"><img src="https://image.flaticon.com/icons/png/512/54/54906.png" alt="some text" width=40 height=40></p>

          """
            else:
                db_ncr.registerDB(firstname.upper(), lastname.upper(), email1.upper(), password1)
                return render_template('ncr/dbname.html', firstname=firstname)
        else:
            return f"""
          <h2>Atenção, Todos os campos precisam ser preenchidos... :( </h2><br><br><br>
          <p><a href="/register"><img src="https://image.flaticon.com/icons/png/512/54/54906.png" alt="some text" width=40 height=40></p>

          """

@app.route('/handleUpload', methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        print('---------', photo)
        if photo.filename != '':
            print('foi')
            photo.save(os.path.join('static/', photo.filename))
    return redirect(url_for('userarea_loged'))


if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8000, debug=True)
    app.run(debug=True)














        # pasta = './static'
        # arquivo_meta = 'INT_DELNT_CRTL_META_REV.xlsx'
        # #arquivo_rai = 'rai.xlsx'
        # diretorio = os.listdir(pasta)
        # if arquivo in diretorio:
        #     print('---removendo arquivo----')
        #     os.remove('{}/{}'.format(pasta, arquivo_meta))
        #     print('>>>>>> {} removido da pasta {}'.format(pasta, arquivo_meta))
        # else:
        #     print('|||||||||||||||||| este arquivo nao existe')