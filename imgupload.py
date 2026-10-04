import databaseconnection as Data
import sys


class main:
    def __init__(self, request, id, filelocation):
        
        if request == "1":
            state = self.uploadpfp(id, filelocation)
        elif request == "2":
            state = self.uploadrequest(id, filelocation)
        else:
            state = False
        
        if state:
            print("Success")
        else:
            print("Fail")
    
    def uploadpfp(self, id, filelocation):
        query = "UPDATE Users SET [Profile Picture] = '" + filelocation + "' WHERE ID = " + id
        
        try:
            data = Data.main()
            data.update(query)
            data.closeConnection()
            return True
        except:
            data.closeConnection()
            return False
        
    def uploadrequest(self, id, filelocation):
        query = "INSERT INTO Membership_Request ([Member ID], [Request Photo]) VALUES (" + id + ", '" + filelocation + "');"
        
        try: 
            data = Data.main()
            data.update(query)
            data.closeConnection()
            return True
        except:
            data.closeConnection()
            return False
    

    
if __name__ == "__main__":
    if len(sys.argv) == 4:
        request = sys.argv[1]
        id = sys.argv[2]
        filelocation = sys.argv[3]
        main(request, id, filelocation)
    else:
        print("Fail")