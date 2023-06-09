from flask import Flask, request, session, url_for, redirect, make_response, render_template
from models.shanin_db import *

app = Flask(__name__)  # __name__ 代表目前執行的模組
# 環境設定
app.config['SECRET_KEY'] = 'MAXSHEN'
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/index1")
def index1():
    return render_template("index1.html")


@app.route("/index2")
def index2():
    return render_template("index2.html")


@app.route("/index3")
def index3():
    return render_template("index3.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':  # 輸入網址會進到這裡
        response = make_response(render_template('login.html'))
    elif request.method == 'POST':  # 表單送出後會到這裡
        mail = request.values.get('mail')
        password = request.values.get('password')
        # 驗證是否有這個使用者以及密碼是否正確，生出驗證結果 auth_result
        data = search_login_user(mail,password)  # 假設成功
        print(data)
        ''' 建立回應 '''
        if data:  # 如果都正確
            name = data[0][1]
            root = data[0][4]
            print(name)
            print(root)
            ''' 設定 Session '''
            session['username'] =name
            if root==1:
                session['root'] = "true"
                print("使用者為管理員")
            else:
                print("使用者不是管理員")
            response = make_response(redirect(url_for('index')))
        else:  # 如果錯誤
            response = make_response(redirect(url_for('login')))
            
    else:
        response = make_response(redirect(url_for('index')))

    return response


@app.route('/logout')
def logout():
    session.pop('username', None) # None是為了避免找不到對應的key產生錯誤
    return make_response(redirect(url_for('login')))


@app.route('/check_login', methods=['GET'])
def check_login():
    username = session.get('username', None) # None是為了避免找不到對應的key產生錯誤
    # print(username)
    if username:
        return "True"
    else:
        return "False"
    
    
@app.route('/check_root', methods=['GET'])
def check_root():
    root = session.get('root', None) # None是為了避免找不到對應的key產生錯誤
    # print(root)
    if root:
        return "True"
    else:
        return "False"
    
    
@app.route('/line_form/<day>/<timeValue>', methods=['GET', 'POST'])
def line_form(day,timeValue):
    if request.method == 'GET':  # 輸入網址會進到這裡
        print("get")
        response = make_response(
            render_template("line_form.html", time=timeValue, day=day))
    elif request.method == 'POST':  # 表單送出後會到這裡
        print("post")
        song = request.values.get('song')
        time = request.values.get('time')
        member_num = int(request.values.get('member_num'))
        member = [None,None,None,None,None]
        email = [None,None,None,None,None]
        for i in range(1, member_num+1):
            member[i-1]=request.values.get(f'member{i}')
            email[i-1]=request.values.get(f'mail{i}')
        # 更新是否成功，回傳驗證結果 update_result
        update_result = insert_song(day,time,song,member[0],email[0],member[1],email[1],member[2],email[2],member[3],email[3],member[4],email[4])
        ''' 建立回應 '''
        response = make_response(redirect(url_for('index2')))
        print(update_result)
    else:
        response = make_response(redirect(url_for('index')))

    return response


@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'GET':  # 輸入網址會進到這裡
        print("get_sign")
        response = make_response(render_template("sign.html"))
    elif request.method == 'POST':  # 表單送出後會到這裡
        print("post_sign")
        name = request.values.get('name')
        mail = request.values.get('mail')
        password = request.values.get('password')
        sign_result = user_register(name,mail,password)
        # 更新是否成功，回傳驗證結果 update_result
        ''' 建立回應 '''
        if sign_result:  # 如果都正確
            response = make_response(redirect(url_for('login')))
        else:  # 如果錯誤
            response = make_response(redirect(url_for('sign')))
        print(sign_result)
    else:
        response = make_response(redirect(url_for('sign')))

    return response


@app.route('/cancel_line', methods=['POST'])
def cancel_line():
    day = request.form.get('day')
    time = request.form.get('time')
    print(day)
    print(time)
    delete_result = delete_line(day,time)
    if delete_result =="success":
        return {"code":200}
    
    
@app.route('/get_line/<day>', methods=['GET'])
def get_line(day):
    time_line=get_line_info(day)
    return {"code":200,"data":time_line}
    

@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('page_not_found.html', error=error),404)

if __name__ == "__main__":  # 若直接執行本程式才啟動伺服器，若僅被呼叫則不啟動
    app.run(debug=True, port=5251,host="0.0.0.0")
