# 宣告使用 sqlite3 模組
import sqlite3

# 設定常數
DB_NAME = 'mydb.db'

# 建立對檔案型資料庫 mydb.db 的物件參考
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()