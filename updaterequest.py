import databaseconnection as Data
import datetime as date
import sys

class main:
    def __init__(self, requestid, memberid, committeeid, type, status):
        self.requestid = requestid
        self.memberid = memberid
        self.committeeid = committeeid
        
        if (status == "-1"):
            self.denyRequest()
        elif (status == "1"):
            self.acceptRequest(type)
            
    def denyRequest(self):
        query = "UPDATE Membership_Request SET Status = -1 WHERE [Request ID] == " + self.requestid
        
        try:
            data = Data.main()
            data.establishConnection()
            data.update(query)
            
        except:
            print("There was an unexpected error")
            
        data.closeConnection()
        
    def acceptRequest(self, type):
        try:
            type, expdate = self.setDate(type)
        except:
            print("Date Error")
        datenow = date.datetime.now()
        year = datenow.strftime("%Y")
        month = datenow.strftime("%m")
        day = datenow.strftime("%d")
        datenow = year + "-" + month + "-" + day 
        query = ("INSERT INTO Memberships ([User ID], [Membership Type], Status, [Expiry Date]) "
                 "VALUES (" + self.memberid + ", '" + type + "', 1, '" + expdate + "');")

        query2 = ("INSERT INTO Approved (RequestID, [Approved By], [approved date]) "
                  "VALUES (" + self.requestid + ", " + self.committeeid + ", '" + datenow + "');")
        
        query3 = "UPDATE Membership_Request SET Status = 1 WHERE [Request ID] == " + self.requestid
        try:
            data = Data.main()
            data.establishConnection()
            data.update(query)
            data.update(query2)
            data.update(query3)
        except:
            print("Unexpected Error")
        print("Successfully approved")
        data.closeConnection()
        
    def setDate(self, type):
        datenow = date.datetime.now()
        monthnow = datenow.strftime("%m")
        yearnow = datenow.strftime("%Y")
        if type == "semester":
            if monthnow >= "06":
                yearnow = int(yearnow) + 1
                return ("Semester 1", str(yearnow) + "-02-08")
            elif monthnow < "03":
                return ("Semester 1", yearnow + "-02-08")
            else:
                return ("Semester 2", yearnow + "-07-31")
        elif type == "year":
            if monthnow >= "06":
                yearnow = int(yearnow) + 1
                return ("Year", str(yearnow) + "-07-31")
            elif monthnow < "06":
                return ("Year", str(yearnow) + "-07-31")
                
        
if __name__ == "__main__":
    if len(sys.argv) > 6:
        print("There was an unexpected error")
    else:
        try:
            requestid = sys.argv[1]
            committeeid = sys.argv[2]
            memberid = sys.argv[3]
            type = sys.argv[4]
            status = sys.argv[5]
            main(requestid, memberid, committeeid, type, status)
        except:
            print("There was an unexpected issue")