from flask import Flask, request, session, url_for, redirect, make_response, render_template

app = Flask(__name__)  # __name__ 代表目前執行的模組
# 環境設定
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


@app.route("/index4")
def index4():
    return render_template("index4.html")


@app.route('/line_form/<timeValue>', methods=['GET', 'POST'])
def line_form(timeValue):
    if request.method == 'GET':  # 輸入網址會進到這裡
        print("get")
        response = make_response(
            render_template("line_form.html", time=timeValue))
    elif request.method == 'POST':  # 表單送出後會到這裡
        print("post")
        song = request.values.get('song')
        time = request.values.get('time')
        member_num = int(request.values.get('member_num'))
        member = []
        email = []
        for i in range(1, member_num+1):
            member.append(request.values.get(f'member{i}'))
            email.append(request.values.get(f'mail{i}'))
        print(member)
        print(email)
        # 更新是否成功，回傳驗證結果 update_result
        update_result = "success"
        ''' 建立回應 '''
        if update_result == 'success':  # 如果都正確
            response = make_response(redirect(url_for('index1')))
        else:  # 如果錯誤
            response = make_response(redirect(url_for('index1')))
        print(update_result)
    else:
        response = make_response(redirect(url_for('index')))

    return response


if __name__ == "__main__":  # 若直接執行本程式才啟動伺服器，若僅被呼叫則不啟動
    app.run(debug=True, port=5251)
