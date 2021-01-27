import sqlite3

# DBに接続する。なければDBを作成する。
conn = sqlite3.connect('example.db')

# カーソルを取得する
c = conn.cursor()

# テーブルを作成
#c.execute('CREATE TABLE articles  (id int, title varchar(1024), body text, created datetime)')

# レコード（項目）の追加。Insert実行
c.execute(
    "INSERT INTO articles VALUES (1,'今朝のおかず','魚を食べました','2020-02-01 00:00:00')")
c.execute(
    "INSERT INTO articles VALUES (2,'今日のお昼ごはん','カレーを食べました','2020-02-02 00:00:00')"
)
c.execute(
    "INSERT INTO articles VALUES (3,'今夜の夕食','夕食はハンバーグでした','2020-02-03 00:00:00')"
)

# コミット
conn.commit()

#  fetchallで結果リストを取得する
print("変更前")
c.execute('SELECT * FROM articles')
for row in c.fetchall():
    print(row)

#  レコード（項目）の削除。DELETEの実行。
c.execute('DELETE FROM articles WHERE id=?', (2, ))

# コミット
conn.commit()

#  fetchallで結果リストを取得する
print("変更前")
c.execute('SELECT * FROM articles')
for row in c.fetchall():
    print(row)

#  レコード（項目）の削除。DELETEの実行。
c.execute('DELETE FROM articles WHERE id=?', (1, ))
c.execute('DELETE FROM articles WHERE id=?', (3, ))

# コミット
conn.commit()

# コネクションをクローズする
conn.close()
