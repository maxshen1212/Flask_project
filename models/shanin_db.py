import sqlite3
from sqlite3 import Error
DB_NAME = "shanin.db"

# 註冊帳號 ok
def user_register(user_name=None,user_mail=None,user_password=None,root=False):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO user_info(user_name,user_mail,user_password,root) VALUES (?,?,?,?)''',
                            (user_name,user_mail,user_password,root))
        print(f"{user_name}註冊帳號已完成！")
        conn.commit()
        return True
    except Error as error:
        print(f"{user_name}註冊帳號發生錯誤，請重新註冊!", error)
        return False
    finally:
        conn.close()
        
        
# 新增歌曲 ok
def insert_song(day=None,time=None,song=None,member1=None,mail1=None,member2=None,mail2=None,member3=None,mail3=None,member4=None,mail4=None,member5=None,mail5=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM line WHERE day=? and time=?", (day,time,))
    data = cursor.fetchall()
    try:
        if data:
            print(f"此時間已有預約！")
        else:
            cursor.execute('''INSERT INTO line (day,time,song,member1,member2,member3,member4,member5,
                            mail1,mail2,mail3,mail4,mail5) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);''',
                            (day,time,song,member1,member2,member3,member4,member5,mail1,mail2,mail3,mail4,mail5))
            print(f"新增{song}完成！")
            conn.commit()
    except Error as error:
        print(f"新增{song}發生錯誤，請重新登記!", error)
    finally:
        conn.close()
        
        
# 刪除指定紀錄
def delete_line(day,time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM line WHERE day=? and time=?", (day,time,))
        conn.commit()
        print(f"=> 刪除{day}的{time}歌曲成功")
        return "success"
    except Error as error:
        print(f"刪除時發生錯誤",error)
    finally:
        conn.close()
        
        
# 查詢指定天數所有隊伍資訊 ok
def get_line_info(day):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM line WHERE day=?",(day,))
        data = cursor.fetchall()
        print(f"查詢指定天數所有隊伍資訊成功{data}")
        if data:
            return data
        else:
            return []
    except Error as error:
        print(f"查詢時發生錯誤：{error}")
    finally:
        conn.close()
        
        
# 查詢指定紀錄   
def search_record(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM line WHERE member1=? or member2=? or member3=? or member4=? or member5=?",(name,name,name,name,name,))
        data = cursor.fetchall()
        print("查詢成功",data)
    except Error as error:
        print(f"執行 SELECT 操作時發生錯誤：{error}")
    finally:
        conn.close()
        
        
# 查詢使用者  ok     
def search_login_user(mail,password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user_info WHERE user_mail=? AND user_password=?", (mail,password))
        data = cursor.fetchall()
        print("=> 查詢成功",data)
        return data
    except Error as error:
        print(f"執行 SELECT 操作時發生錯誤",error)
    finally:
        conn.close()

# search_root()
# search_root("asd")
# user_register("MAX","maxshen1212@gmail.com","1212")
# insert_song("day0","23:00","stasdar","masdax","qwedqwe123@asdd")
# get_line_info()
# search_record()
# delete_specified_record()