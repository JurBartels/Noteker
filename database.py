import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("database.db")
        self.db = self.con.cursor()
        if(self.check(tableName="data") == None):
            self.db.execute("CREATE TABLE data (sdesc, fnr, knr, ka, desc)")
            print("created new")
        else:
            print("table exists")
        self.con.commit()
        self.con.close()

    #return tuple with table name if table exists, None if not
    def check(self, tableName):
        return self.db.execute('''
                        SELECT name
                        FROM sqlite_master
                        WHERE type = 'table' AND name =?
                        ''', (tableName,)).fetchone()

    def insert(self, sdesc, fnr, knr, ka, desc):
        self.con = sqlite3.connect("database.db")
        self.db = self.con.cursor()
        self.db.execute('''
                        INSERT INTO data
                        VALUES (?,?,?,?,?)
                        ''', (sdesc, fnr, knr, ka, desc))
        self.con.commit()
        self.con.close()

    def read(self):
        self.con = sqlite3.connect("database.db")
        self.db = self.con.cursor()
        result = self.db.execute('''
                        SELECT sdesc, fnr, knr, ka, desc
                        FROM data
                        ''').fetchall()
        print(result)
        self.con.commit()
        self.con.close()

    def searchOne(self, term):
        self.con = sqlite3.connect("database.db")
        self.db = self.con.cursor()
        result = self.db.execute('''
                                 SELECT *
                                 FROM data
                                 WHERE sdesc = ?
                                 OR fnr = ?
                                 OR knr = ?
                                 OR ka = ?
                                 OR desc = ?

                                 ''', (term,term,term,term,term)).fetchall()
        print(result)
        self.con.commit()
        self.con.close()












        
