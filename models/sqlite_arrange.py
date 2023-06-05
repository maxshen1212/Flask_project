import sqlite3
# 宣告使用 sqlite3 模組

# 排隊
def user_arrange(db_name, idno, password):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        data = (id, name, age)
        cursor.execute(
            "INSERT INTO users (id, name, age) VALUES (?, ?, ?)", data)
        results = cursor.fetchall()
        if results:
            if results[0][0] == password:
                return 'success'
            else:
                return 'fail'
        else:
            print(f"=> 找不到{idno}使用者！")
    except sqlite3.Error as error:
        print("=>登入時發生錯誤：", error)
    finally:
        conn.close()
