import databaseconnection as data
import sys
import base64


class main:
    def __init__(self, Uname, Pword):
        self.ID = 0
        self.Uname = Uname
        self.Pword = Pword
        
        
        
        self.login()
        
        if self.ID == -1:
            print("Incorrect username or password")
        else:
            print(self.ID)
            print(self.Uname)
            
            
    def login(self):
        Data = data.main()
        query = "SELECT ID FROM Users WHERE UserName == '" + self.Uname + "' AND Password == '" + Data.encodestring(self.Pword) + "'"
        
        try:
            Data.execute(query)
            self.ID = Data.fetchOneRecord()[0]
            
        except:
            
            self.ID = -1
            
        Data.closeConnection()
        

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("There was an unexpected error")
    else:
        try:
            Uname = sys.argv[1]
            Pword = sys.argv[2]
            main(Uname, Pword)
        except:
            print("Please enter your username and password")
        
        
    
    