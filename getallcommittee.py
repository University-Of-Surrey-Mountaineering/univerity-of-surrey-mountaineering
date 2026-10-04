import databaseconnection as Data

class main:
    def __init__(self):
        out = self.getallcommittee()
        if out == False:
            print("There was an error")
        else:
            for counter in out:
                print(counter)
    
    
    def getallcommittee(self):
        query = ("SELECT Users.Forename, Users.Surname, Users.[Profile Picture], Committee.[Role Name], Committee.[About Me] From Users"
                 " INNER JOIN Committee ON Users.ID == Committee.[Current User];")
        try:
            data = Data.main()
            data.execute(query)
            out = data.fetchAllRecords()
            data.closeConnection()
            return out
        except:
            data.closeConnection()
            return False
    
    
if __name__ == "__main__":
    main()