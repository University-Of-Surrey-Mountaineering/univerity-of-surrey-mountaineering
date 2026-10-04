import databaseconnection as Data


class main:
    def __init__(self):
        self.getRequest()
        if self.out == None:
            print("There are no approval requests")
        else:
            for counter in self.out:
                print(counter)
    
    
    def getRequest(self):
        query = "SELECT * FROM Membership_Request WHERE Status == 0;"
        
        try:
            data = Data.main()
            data.establishConnection()
            data.execute(query)
            self.out = data.fetchOneRecord()
                        
        except:
            self.out = None
        data.closeConnection()
    
    
if __name__ == "__main__":
    main()