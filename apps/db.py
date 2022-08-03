import sqlite3


class BotDB:
    def __init__(self):
        self.con = sqlite3.connect('botbase.db')
        self.cur = self.con.cursor()

    def setup(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS users (
            id        INTEGER  PRIMARY KEY AUTOINCREMENT,
            userid    INT      UNIQUE       NOT NULL,     
            join_date DATETIME DEFAULT ( (DATETIME('now') ) )   NOT NULL        
            )"""
        )
        self.con.commit()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS dictionary (
            id        INTEGER  PRIMARY KEY AUTOINCREMENT,
            userid    INT      REFERENCES users (userid) ON DELETE CASCADE  NOT NULL,     
            word      TEXT     NOT NULL,    
            trans     TEXT     NOT NULL        
            )"""
        )
        self.con.commit()

    def add_user(self, user):
        self.cur.execute(f"""INSERT INTO users(userid, join_date) VALUES(?,?)""", (user,'now'))
        self.con.commit()

    def check_user(self, user):
        self.cur.execute(f"""SELECT userid FROM users WHERE userid = {user}""")
        if self.cur.fetchone() is None:
            return False
        return True

    def check_word(self, user, word):
        self.cur.execute(f"""SELECT * FROM  dictionary WHERE userid = {user} AND word = {word} """)
        if self.cur.fetchall() is None:
            return False
        return True

    def add_word(self, user, word, trans):
        self.cur.execute(f""" INSERT INTO dictionary(userid, word, trans) VALUES(?,?,?)""",(user, word, trans))
        self.con.commit()

    def close(self):
        self.con.close()