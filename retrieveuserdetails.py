import databaseconnection as data
import sys

class main:
    def __init__(self, id):
        self.id = id
        self.data = data.main()
        
        self.getInfo()
        
        if self.id == -1:
            print("Account not found")
        else:
            for counter in self.alldata:
                print(counter)
        
        
    def getInfo(self):
        query = "SELECT Forename, Surname, Committee, [Email Address], [Profile Picture] FROM Users WHERE ID == " + self.id
        
        try:
            self.data.execute(query)
            self.alldata = self.data.fetchOneRecord()
            
        except:
            self.id = -1
            
        self.data.closeConnection()


if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
            print("There was an unexpected error")
    else:
        try:
            ID = sys.argv[1]
            main(ID)
        except:
            print("Account not found")