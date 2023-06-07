import sqlite3
# 宣告使用 sqlite3 模組

# 加入排隊
def user_queue(db_name,member1,member2,member3,member4,date,time,email):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        # 人員只有一個時
        if not member2 and not member3 and not member4:
            cursor.execute(
                "INSERT INTO user (member1,date,time,)email) VALUES(?,?,?,?)",(member1,date,time,email)
            )
        # 人員有二個時
        elif not member3 and not member4:
            cursor.execute(
                "INSERT INTO user (member1,member2,date,time,email) VALUES(?,?,?,?,?)",(member1,member2,date,time,email)
                )
        # 人員有三個時
        elif not member4:
            cursor.execute(
                "INSERT INTO user (member1,member2,member3,date,time,email) VALUES(?,?,?,?,?,?)",(member1,member2,member3,date,time,email)
                )
        # 人員有四個時
        else:
            cursor.execute(
                "INSERT INTO user (member1,member2,member3,member4,date,time,email) VALUES(?,?,?,?,?,?,?)",(member1,member2,member3,member4,date,time,email)
                )
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        return "排隊資料已存在"


# index5-查詢該時段有沒有被預約
def search_time(db_name,date,time):
    try:
        #判斷有無資料，沒有的話回傳布林值判斷是否前往下一個網頁
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE date = ? AND time = ?,VALUES(?,?)",(date,time)
        )
        rsv = cursor.fetchall()
        conn.close()
        # 有的話回傳布林值False
        if rsv:
            return False,"此時段已被預約"
        #沒有的話回傳布林值True
        else:
            return True
    except sqlite3.Error as error:
        return "資料發生錯誤"

# 刪除日期時間資料
def delete_data(db_name,date):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE date = ? ,VALUES(?) ",(date)
    )
    rsv = cursor.fetchall()
    if rsv:
        cursor.execute("DELETE FROM user WHERE date = ?,VALUES(?)",(date,))
    conn.commit()
    conn.close()

def cancel_rsv(db_name,date,time,email):
    try:
        # 提供日期時間來和email取消預約
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        # 查詢有無此預約
        cursor.execute("SELECT * FROM user WHERE date = ? AND time = ? AND email = ?,VALUES(?,?,?)",(date,time,email))
        rsv = cursor.fetchone()
        # 有的話刪除沒有就回傳文字
        if rsv:
            cursor.execute("DELETE FROM user WHERE date = ? AND time = ? AND email = ?,VALUES(?,?,?)",(date,time,email))
            conn.commit()
            conn.close()
            return "已成功取消預約"
        else:
            conn.commit()
            conn.close()
            return "查無此預約"

    except sqlite3.Error as error:
        return"資料發生錯誤"
