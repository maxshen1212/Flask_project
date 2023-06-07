import sqlite3
db_name = "shanin.db"

'''建立資料庫及資料表，若資料庫已存在則不執行任何操作'''
try:
    conn = sqlite3.connect(db_name)
    conn.execute('''CREATE TABLE IF NOT EXISTS day1 (
                        iid INTEGER PRIMARY KEY AUTOINCREMENT,
                        time TEXT NOT NULL UNIQUE,
                        song TEXT NOT NULL,
                        member1 TEXT NOT NULL,
                        mail1 TEXT NOT NULL,
                        member2 TEXT,
                        mail2 TEXT,
                        member3 TEXT,
                        mail3 TEXT,
                        member4 TEXT,
                        mail4 TEXT,
                        member5 TEXT,
                        mail5 TEXT)
                    ''')
    print("=> 資料庫建立完成！")
except sqlite3.Error as error:
    print("=> 建立資料庫時發生錯誤：", error)
finally:
    conn.close()


'''建立資料庫及資料表，若資料庫已存在則不執行任何操作'''
try:
    conn = sqlite3.connect(db_name)
    conn.execute('''CREATE TABLE IF NOT EXISTS user_info (
                        iid INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_name TEXT UNIQUE NOT NULL,
                        user_mail TEXT UNIQUE NOT NULL,
                        user_password TEXT NOT NULL,
                        root Bool NOT NULL)
                    ''')
    print("=> 資料庫建立完成！")
except sqlite3.Error as error:
    print("=> 建立資料庫時發生錯誤：", error)
finally:
    conn.close()

# 註冊帳號
# try:
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO user_info ("user_name", "user_mail", "user_password", "root") VALUES ('沈治翰', 'maxshen1212@gmail.com', 'MAXMAX1212', 'true');
#                     ''')
#     print("=> 建立使用者完成！")
#     conn.commit()
# except sqlite3.Error as error:
#     print("=> 建立資料庫時發生錯誤：", error)
# finally:
#     conn.close()
    
# 新增歌曲
# try:
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO day1 ("time", "song", "member1", "mail1") VALUES ('12:00', '麥田捕手', '沈治翰', 'maxshen1212@gmail.com');
#                     ''')
#     print("=> 建立使用者完成！")
#     conn.commit()
# except sqlite3.Error as error:
#     print("=> 建立資料庫時發生錯誤：", error)
# finally:
#     conn.close()
    
# 刪除指定紀錄
# try:
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM day1 WHERE song=?", ('討厭',))
#     conn.commit()
#     print("刪除成功")
# except sqlite3.Error as error:
#     print(f"執行 DELETE 操作時發生錯誤：{error}")

# 查詢指定天數所有隊伍資訊
# try:
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM day1")
#     conn.commit()
#     print("刪除成功")
# except sqlite3.Error as error:
#     print(f"執行 SELECT 操作時發生錯誤：{error}")
    
# 查詢指定紀錄
# try:
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM member WHERE mname LIKE '沈'")
#     data = cursor.fetchall()
# except sqlite3.Error as error:
#     print(f"執行 SELECT 操作時發生錯誤：{error}")
# if len(data) > 0:
#     for record in data:
#         print(f"Id：{record[0]}, Name：{record[1]}, Pwd：{record[2]}")
# else:
#     print("查無資料")
    
# try:
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM students")
#     results = cursor.fetchall()
#     if not results:
#         print("=> 沒有學生資料！")
#     else:
#         print("\n所有學生資料：")
#         print("學號\t姓名\t手機\t\t成績")
#         for result in results:
#             print(f"{result[1]}\t{result[2]}\t{result[3]}\t{result[4]}")
# except sqlite3.Error as error:
#     print("=> 顯示所有記錄時發生錯誤：", error)
# finally:
#     conn.close()