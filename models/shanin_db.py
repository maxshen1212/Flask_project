import sqlite3
from sqlite3 import Error

class shaninDatabase:
    # 資料庫Connect
    def __init__(self):
        db_name = r"shanin.db"
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except Error as error:
            print("shanin資料庫連線失敗!",error)
            
    # 註冊帳號
    def user_register(self,user_name=None,user_mail=None,user_password=None,root=None):
        try:
            self.cursor.execute("INSERT INTO user_info(user_name,user_mail,user_password,root) VALUES (?,?,?,?)",
                               (user_name,user_mail,user_password,root))
            print(f"{user_name}註冊帳號已完成！")
            self.conn.commit()
        except Error as error:
            print(f"{user_name}註冊帳號發生錯誤，請重新註冊!", error)
            
    # 新增歌曲
    def insert_song(self,day=None,time=None,song=None,member1=None,member2=None,member3=None,member4=None,member5=None,mail1=None,mail2=None,mail3=None,mail4=None,mail5=None):
        self.cursor.execute("SELECT * FROM line WHERE day=? and time=?", (day,time,))
        data = self.cursor.fetchall()
        try:
            if data:
                print(f"此時間已有預約！")
            else:
                self.cursor.execute("INSERT INTO line (day,time,song,member1,member2,member3,member4,member5, \
                                mail1,mail2,mail3,mail4,mail5) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);",
                                (day,time,song,member1,member2,member3,member4,member5,mail1,mail2,mail3,mail4,mail5))
                print(f"新增{song}完成！")
                self.conn.commit()
        except Error as error:
            print(f"新增{song}發生錯誤，請重新登記!", error)

    # 刪除指定紀錄
    def delete_specified_record(self,day,time):
        try:
            self.cursor.execute("DELETE FROM line WHERE day=? and time=?", (day,time,))
            self.conn.commit()
            print("=> 刪除成功")
        except Error as error:
            print(f"刪除時發生錯誤",error)
    
    # 查詢指定天數所有隊伍資訊
    def search_team_Information(self,day):
        try:
            self.cursor.execute("SELECT * FROM line WHERE day=?",(day,))
            data = self.cursor.fetchall()
            self.conn.commit()
        except Error as error:
            print(f"查詢時發生錯誤：{error}")
            
    # 查詢指定紀錄       
    def search_record(self,name):
        try:
            self.cursor.execute("SELECT * FROM line WHERE member1=? or member2=? or member3=? or member4=? or member5=?",(name,name,name,name,name,))
            data = self.cursor.fetchall()
            print("查詢成功",data)
        except Error as error:
            print(f"執行 SELECT 操作時發生錯誤：{error}")
            
    # 查詢管理人        
    def search_root(self,user):
        try:
            self.cursor.execute("SELECT root FROM user_info WHERE user_name=?", (user,))
            data = self.cursor.fetchall()
            self.conn.commit()
            print("=> 查詢成功",data)
        except Error as error:
            print(f"執行 SELECT 操作時發生錯誤",error)
                
#data=shaninDatabase()
# data.search_root()
# data.user_register()
# data.insert_song()
# data.search_team_Information()
# data.search_record()
# data.delete_specified_record()