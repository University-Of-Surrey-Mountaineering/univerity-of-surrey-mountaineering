import sqlite3 as sql
import base64

class main:
    def __init__(self):
        self.establishConnection()
        
    def establishConnection(self):
                try:
                    self.connection = sql.connect("Data.db")
                    self.Cursor = self.connection.cursor()
                    
                except sql.Error as error:
                    print('Error occurred -', error)
                
    def execute(self, query):
        try:
            self.Cursor.execute(query)
        except:
            raise Exception()
        
    def update(self, query):
        try:
            self.Cursor.execute(query)
            self.connection.commit()
        except:
            raise Exception()
        
    def fetchOneRecord(self):
        try:
            return self.Cursor.fetchone()
        except:
            raise Exception()
            
    def fetchAllRecords(self):
        try:
            return self.Cursor.fetchall()
        except:
            raise Exception()
    
    def encodestring(self, string):
        enc_pass = base64.b64encode(string.encode('utf-8')).decode('utf-8')
        return enc_pass

    def decodestring(self, string):
        dec_pass = base64.b64decode(string).decode('utf-8')
        return dec_pass
        
    def getCursor(self):
        return self.Cursor
    
    def getConnection(self):
        return self.connection
    
    def closeConnection(self):
        self.connection.close()
    
    