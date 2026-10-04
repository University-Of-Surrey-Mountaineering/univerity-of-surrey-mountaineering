import sys
import databaseconnection as Data


class main:
    def __init__(self, username, password, forename, surname, email):
        self.username = username
        self.password = password
        self.forename = forename
        self.surname = surname
        self.email = email
        
        out = self.checkUsername()
        if out == True:
            print(self.createprofile())
        else:
            print(out)
        
    def checkUsername(self):
        query = "SELECT ID FROM Users WHERE UserName == '" + self.username + "' OR [Email Address] == '" + self.email + "';"
        try:
            data = Data.main()
            data.execute(query)
            out = data.fetchOneRecord()
            data.closeConnection()
            
            if out != None:
                return "Username or email is already in use"
            else:
                return True
        except:
            data.closeConnection()
            return "Unexpected Error was thrown"
    
    
    def createprofile(self):
        data = Data.main()
        query = ("INSERT INTO Users (UserName, Password, Forename, Surname, [Email Address]) "
        "VALUES ('" + self.username + "', '" + data.encodestring(self.password) + "', '" + self.forename + "', '" + self.surname + "', '" + self.email + "');")
        try:
            data.update(query)
            data.closeConnection()
            return "Account added"
        except:
            return "Unexpected error occured"
    
if __name__ == "__main__":
    try:
        if len(sys.argv) == 6:
            username = sys.argv[1]
            password = sys.argv[2]
            forename = sys.argv[3]
            surname = sys.argv[4]
            email = sys.argv[5]
            
            main(username, password, forename, surname, email)
    except:
        print("Please enter your details")