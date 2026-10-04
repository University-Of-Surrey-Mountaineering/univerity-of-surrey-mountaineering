import databaseconnection as Data
import datetime as date
import sys


class main:
    def __init__(self, id):
        if id == None:
            result = self.getalltrips()
            accept = 0
        else:
            accept, result = self.getonetrip(id)
            
        if result == None:
            print("None")
        elif accept == 1 and result != None:
            for counter in result:
                print(counter)
        else:
            for counter in result:
                print(counter)
    
    def getalltrips(self):
        x = date.datetime.now()
        year = x.strftime("%Y")
        month = x.strftime("%m")
        day = x.strftime("%d")
        entiredate = year + "-" + month + "-" + day
        query = "SELECT ID, [Trip Name], [Trip Date] FROM Trips WHERE [Trip Date] > '" + entiredate + "';"
        try:
            data = Data.main()
            data.execute(query)
            result = data.fetchAllRecords()
            if len(result) == 0:
                return None
            else:
                return result
        except:
            return None
        
    def getonetrip(self, id):
        query = "SELECT [Trip Name], [Trip Date], Details FROM Trips WHERE ID == " + id + ";"
        try:
            data = Data.main()
            data.execute(query)
            result = data.fetchOneRecord()
            if len(result) == 0:
                return 0, None
            else: 
                return 1, result
        except:
            return 0, None
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        id = None
        main(id)
    elif len(sys.argv) == 2:
        id = sys.argv[1]
        main(id)
    else:
        print("None")