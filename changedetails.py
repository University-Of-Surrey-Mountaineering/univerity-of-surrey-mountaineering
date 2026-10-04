import databaseconnection as Data
import sys



class main:
    def __init__(self, id, username, password, email):
        self.id = id
        self.query = "UPDATE Users SET "
        self.testInputs(username, "UserName")
        self.testInputs(password, "Password")
        self.testInputs(email, "[Email Address]")
        self.query = self.query[:-2]
        self.query += " WHERE ID == '" + self.id + "';"
        self.updatetable(username)
        
        
        
    def testInputs(self, input, rowname):
        if input != "ifyouarereadingthisgoandfuckyourself,thereisnothingtoseehere.thislongassstringisheretoavoidnullerrors":
            self.query += rowname + " = '" + input +"', "
    
    def updatetable(self, username):
        query1 = "SELECT ID FROM Users WHERE UserName == '" + username + "';"
        try:
            data = Data.main()
            data.execute(query1)
            data.fetchOneRecord()[0]
            print("Username is already in use")
        except:
            data.update(self.query)
            print("Your details have been updated")
        data.closeConnection
    
if __name__ == "__main__":
    if len(sys.argv) == 5:
        id = sys.argv[1]
        username = sys.argv[2]
        password = sys.argv[3]
        email = sys.argv[4]
        main(id, username, password, email)
    else:
        print("unexpected error")