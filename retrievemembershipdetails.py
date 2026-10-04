import databaseconnection as Data
import datetime as date
import sys

class main:
    def __init__(self, id):
        self.id = id
        self.getmembership()
        self.checkRecords()
        if len(self.memberships) > 1:
            print("There was an unexpected error")
        else:
            print(self.memberships[0].getMemberId())
            print(self.memberships[0].getExpiryDate())
            
        
        
    def getmembership(self):
        data = Data.main()
        query = ("SELECT Memberships.[Membership ID], Memberships.[Membership Type], Memberships.[Expiry Date] "
        "FROM Memberships "
        "INNER JOIN Users ON Memberships.[User ID] = Users.ID "
        "WHERE Memberships.Status == 1 AND Users.ID == " + self.id + ";")
        try:
            data.execute(query)
            self.out = data.fetchAllRecords()
        except:
            self.id = -1
        data.closeConnection()
        
    def checkRecords(self):
        membershipids = []
        self.memberships = []
        i = 0
        if len(self.out) == 0:
            print("You dont have a membership")
            print("None")
        else:
            for counter in self.out:
                self.memberships.append(Membership(counter))
                if not self.memberships[i].checkExpiry():
                    membershipids.append(self.memberships[i].getMemberId())
                    self.memberships.pop()
                i += 1
            
            self.updateMembership(membershipids)
            
    def updateMembership(self, memberids):
        if (len(memberids) != 0):
            data = Data.main()
            query = "UPDATE Memberships SET Status = 0 WHERE [Membership ID] IN ("
            for counter in memberids:
                query += str(counter) + ", "
            query = query[:-2]
            query += ");"
            
            try:
                data.update(query)
            except:
                print("Unexpected sql error")
            data.closeConnection()
        
        
class Membership:
    def __init__(self, data):
        self.memberid = data[0]
        self.type = data[1]
        self.expirydate = data[2]
        
    def checkExpiry(self):
        x = date.datetime.now()
        year = x.strftime("%Y")
        month = x.strftime("%m")
        day = x.strftime("%d")
        expyear = self.expirydate[0:4]
        expmonth = self.expirydate[5:7]
        expday = self.expirydate[8:10]
        
        if year == expyear:
            if month == expmonth:
                if day == expday:
                    return True
                elif day > expday:
                    return False
                elif day < expday:
                    return True
            elif month > expmonth:
                return False
            elif month < expmonth:
                return True
        elif year > expyear:
            return False
        elif year < expyear:
            return True        
        
    def getMemberId(self):
        return self.memberid
    def getType(self):
        return self.type
    def getExpiryDate(self):
        return self.expirydate

if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
            print("There was an unexpected error")
    else:
        try:
            ID = sys.argv[1]
            main(ID)
        except:
            print("There was an unexpected issue")