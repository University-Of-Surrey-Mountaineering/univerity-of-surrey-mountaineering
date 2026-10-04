import databaseconnection as Data
import sys

class getroleids:
    def __init__(self, id):
        self.id = id
        roles = self.getroleids()
        print(roles)
    
    
    def getroleids(self):
        query = ("SELECT [Role ID], [About ME]" 
                "FROM Committee "
                "INNER JOIN Users "
                "ON Committee.[Current User] = Users.ID "
                "WHERE Users.ID == " + self.id + ";")
        try:
            data = Data.main()
            data.execute(query)
            allroles = data.fetchAllRecords()
            return allroles
        except:
            print("Unexpected error thrown")
        data.closeConnection()
    
class updateroles:
    def __init__(self, id, aboutme):
        self.id = id
        self.updateallroles(aboutme)
        
    def updateallroles(self, aboutme):
        query = "UPDATE Committee SET [About Me] = '" + aboutme + "' WHERE [Current User] == " + self.id + ";"
        try:
            data = Data.main()
            data.update(query)
            print("Correctly updated details")
        except:
            print("There was an unexpected error")
        data.closeConnection()
        
if __name__ == "__main__":
    if len(sys.argv) == 2:
        id = sys.argv[1]
        getroleids(id)
    elif len(sys.argv) == 3:
        id = sys.argv[1]
        aboutme = sys.argv[2]
        updateroles(id, aboutme)
    else:
        print("unexpected error")