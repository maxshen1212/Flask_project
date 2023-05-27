from flask import Flask
from flask import request
from flask import url_for, redirect
from flask import render_template

from google.oauth2 import id_token
from google.auth.transport import requests

app=Flask(__name__) # __name__ 代表目前執行的模組
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

@app.route("/index5")
def index5():
    return render_template("index5.html")


if __name__=="__main__":  # 若直接執行本程式才啟動伺服器，若僅被呼叫則不啟動
   app.run(debug=True, port=5251)