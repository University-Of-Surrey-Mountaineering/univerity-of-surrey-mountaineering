import datetime as date
import sqlite3 as sql

class main:
    def __init__(self):
        self.establishConnection()
        self.getTrip()


    def establishConnection(self):
        try:
            self.connection = sql.connect("Data.db")
            self.Cursor = self.connection.cursor()
                    
        except sql.Error as error:
            print('Error occurred -', error)
    
    def getTrip(self):
        x = date.datetime.now()
        year = x.strftime("%Y")
        month = x.strftime("%m")
        day = x.strftime("%d")
        entiredate = year + "-" + month + "-" + day
        query = 'SELECT ID, "Trip Date", Photo FROM Trips WHERE "Trip Date" < "' + entiredate + '";'
        try:
            self.Cursor.execute(query)
            result = self.Cursor.fetchone()
            self.ID = result[0]
            self.date = result[1]
            self.photo = result[2]
                    
        except:
            self.ID = -1


if __name__ == "__main__":
    main()